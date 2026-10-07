"""Regression cases for observed failure modes, never fabricated market research."""

from __future__ import annotations

import copy
import hashlib
import json
import random
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

import evaluate_core
import measure_core as m
import provider_core as p
import pytest
import theme_metrics as t
from test_measure_core import BENCHMARK, price_table
from test_universe_core import candidate, change_set, evidence, small_policy, snapshot, spec
from universe_core import (
    PROFILES,
    UniverseError,
    apply_change_set,
    build_universe,
    content_hash,
    market_guidance,
    normalize_snapshot,
    read_json,
    universe_hash,
    validate_ticker,
    validate_universe,
)
from universe_core import (
    load_policy as current_policy,
)


def load_policy():
    """Historical 0.4/0.5 fixtures explicitly replay their archived selection policy."""
    return current_policy(Path(__file__).resolve().parents[1] / "examples/legacy-policy.json")


@pytest.mark.parametrize("ticker", ["SSE:300308", "SZSE:600519", "BSE:000001"])
def test_cn_wrong_venue_is_rejected(ticker):
    assert validate_ticker("cn", ticker)


@pytest.mark.parametrize("ticker", ["SZSE:300308", "SSE:600519", "BSE:920001"])
def test_cn_reviewed_prefixes_are_accepted(ticker):
    assert not validate_ticker("cn", ticker)


@pytest.mark.parametrize(
    "mutation, error",
    [
        (lambda c: c.update(reason=""), "requires a reason"),
        (lambda c: c.update(reason=None), "requires a reason"),
        (lambda c: c.update(evidence=evidence(3)), "tier 1 or tier 2"),
        (lambda c: c.update(listing=None), "active listing"),
        (lambda c: c["listing"].update(as_of="2026-08-01"), "older than 30"),
        (lambda c: c["listing"].update(as_of="2026-09-10"), "future-dated"),
        (lambda c: c.update(measurement_record=None), "measurement_record"),
        (lambda c: c["measurement_record"].update(last_session="2026-09-10"), "after as_of"),
        (lambda c: c["measurement_record"].update(data_sha256="abc"), "SHA-256"),
        (lambda c: c["measurement_record"].update(observations=10), "30 observations"),
        (lambda c: c.update(eligible="false"), "boolean"),
    ],
)
def test_admission_requires_current_traceable_facts(mutation, error):
    raw = snapshot()
    mutation(raw["candidates"][1])
    with pytest.raises(UniverseError, match=error):
        normalize_snapshot(raw)


def test_independence_cannot_be_a_judged_bypass():
    raw = snapshot()
    raw["measurement"]["independence"] = {"basis": "judged", "method": "looks independent"}
    with pytest.raises(UniverseError, match="cannot be judged"):
        normalize_snapshot(raw)
    raw = snapshot()
    raw["candidates"][1]["metrics"]["factor_r2"] = None
    with pytest.raises(UniverseError, match="factor_r2"):
        normalize_snapshot(raw)


@pytest.mark.parametrize(
    "field,value", [("factor_r2", 29), ("beta_strength", 54), ("beta_stability", 49)]
)
def test_beta_label_requires_all_three_gates(field, value):
    raw = snapshot()
    beta = raw["candidates"][-1]
    beta["metrics"][field] = value
    beta["metrics"].pop("independence")
    with pytest.raises(UniverseError, match="BETA_SATELLITE requires"):
        normalize_snapshot(raw)


def test_hash_catches_fact_edits_without_membership_change():
    universe, _ = build_universe(spec(), snapshot(), small_policy())
    modified = copy.deepcopy(universe)
    modified["members"][0]["reason"] = "silently edited reason"
    assert universe_hash(modified) == universe["version_hash"]
    assert content_hash(modified) != universe["content_hash"]
    report = validate_universe(modified, small_policy())
    assert not report["passed"]
    assert any("content_hash" in e for e in report["errors"])


def test_refresh_and_theme_update_are_audited_without_churn():
    universe, _ = build_universe(spec(), snapshot(), small_policy())
    fresh = copy.deepcopy(universe["members"][1])
    fresh["metrics"]["liquidity"] = 80
    fresh["listing"]["as_of"] = "2026-09-10"
    operations = [
        {
            "op": "REFRESH",
            "ticker": fresh["ticker"],
            "candidate": fresh,
            "reason": "Fresh measured observation",
            "evidence": evidence(),
        },
        {
            "op": "UPDATE_THEME",
            "theme": fresh["theme_code"],
            "weight": 2.5,
            "reason": "Reassessed research coverage",
            "evidence": evidence(),
        },
    ]
    changes = change_set(universe, operations, base_content_hash=universe["content_hash"])
    updated, report = apply_change_set(universe, changes, small_policy())
    assert report["passed"]
    assert report["maintenance"]["added"] == report["maintenance"]["removed"] == []
    assert updated["members"][1]["metrics"]["liquidity"] == 80
    assert updated["content_hash"] != universe["content_hash"]
    with pytest.raises(UniverseError, match="base_content_hash"):
        apply_change_set(
            updated, dict(changes, base_version_hash=updated["version_hash"]), small_policy()
        )
    operations[0]["candidate"]["role"] = "QUALITY_LEADER"
    with pytest.raises(UniverseError, match="preserve membership"):
        apply_change_set(universe, changes, small_policy())


def test_refresh_clears_uncovered_or_unmeasurable_old_fields():
    raw = snapshot()
    bundle = {
        "metrics": {"BINANCE:BTCUSDT.P": {"liquidity": 80}},
        "measurement": {},
        "records": {},
        "notes": ["provider outage"],
    }
    merged = m.merge_into_snapshot(raw, bundle)
    assert merged["complete"] is False
    for item in merged["candidates"]:
        assert "factor_r2" not in item["metrics"]
        assert "independence" not in item["metrics"]
    assert "provider outage" in merged["notes"]
    assert raw["candidates"][0]["metrics"]["factor_r2"] == 40


def test_cutoff_and_signed_beta(tmp_path):
    prices = tmp_path / "prices.csv"
    price_table(prices, {BENCHMARK: (1, 0, 100), "BINANCE:INVUSDT.P": (-2, 0, 200)})
    bundle = m.measure(
        prices=prices, benchmarks=[BENCHMARK], source="https://example.com/data", as_of="2026-03-28"
    )
    assert bundle["metrics"]["BINANCE:INVUSDT.P"]["beta_strength"] == 0
    assert all(r["last_session"] <= "2026-03-28" for r in bundle["records"].values())
    assert (
        bundle["records"][BENCHMARK]["data_sha256"]
        == hashlib.sha256(prices.read_bytes()).hexdigest()
    )


@pytest.mark.parametrize(
    "body",
    [
        "2026-01-01,X,100,1\n2026-01-01,X,101,2\n",
        "2026-01-01,X,nan,1\n",
        "2026-01-01,X,100,-1\n",
        "2026-99-01,X,100,1\n",
        "2026-01-01,X,100,not-a-number\n",
    ],
)
def test_malformed_bars_do_not_become_measurements(tmp_path, body):
    path = tmp_path / "bad.csv"
    path.write_text("date,ticker,close,turnover\n" + body)
    with pytest.raises(m.MeasureError):
        m.read_bars(path)


def test_peer_gauge_excludes_self_and_refuses_ambiguous_assignment(tmp_path):
    path = tmp_path / "bars.csv"
    price_table(path, {"A": (1, 0, 100), "B": (1, 0, 200), "C": (2, 0, 300)})
    mapping = {
        "schema_version": 1,
        "themes": {"10_A": {"members": ["A", "B", "C"], "mode": "peer_basket"}},
    }
    gauges, _ = t.resolve_gauges(m.read_bars(path), mapping)
    assert gauges["A"]["legs"] == ["B", "C"]
    assert gauges["C"]["legs"] == ["A", "B"]
    mapping["themes"]["10_B"] = {"members": ["A"], "benchmarks": ["B"]}
    with pytest.raises(m.MeasureError, match="only one"):
        t.resolve_gauges(m.read_bars(path), mapping)


def test_unfit_theme_does_not_fall_back_to_broad_index(tmp_path):
    path = tmp_path / "bars.csv"
    price_table(path, {"A": (1, 0, 100), "B": (1, 0, 200), "BAD": (-1, 0, 300)})
    mapping = {
        "schema_version": 1,
        "themes": {"10_A": {"members": ["A", "B"], "benchmarks": ["BAD"]}},
    }
    result = m.measure(
        prices=path, benchmarks=["A"], source="https://example.com/data", benchmark_map=mapping
    )
    assert result["theme_checks"]["10_A"]["usable"] is False
    assert "factor_r2" not in result["metrics"]["A"]
    assert "liquidity" in result["metrics"]["A"]


def test_multivariate_factors_capture_offsets_a_basket_hides():
    rng = random.Random(10)
    x = [rng.gauss(0, 0.02) for _ in range(180)]
    z = [rng.gauss(0, 0.02) for _ in range(180)]
    y = [2 * a - b + 0.001 for a, b in zip(x, z, strict=True)]
    coefficients, r2 = t.multi_fit(y, [x, z])
    assert coefficients == pytest.approx([2, -1], abs=1e-8)
    assert r2 == pytest.approx(1)
    assert t.multi_fit(y, [x, x]) is None


def test_fund_reproduction_is_not_robust_when_one_winner_does_all_the_work():
    days = [(date(2024, 1, 1) + timedelta(days=i)).isoformat() for i in range(520)]
    rng = random.Random(12)
    factor = [rng.gauss(0, 0.008) for _ in days]
    series = {}
    for ticker, drift in [("FUND", 0), ("WINNER", 0.002), ("LAG1", -0.0003), ("LAG2", -0.0003)]:
        close, rows = 100, []
        for day, move in zip(days, factor, strict=True):
            close *= 1 + move + drift
            rows.append((day, close, 1000))
        series[ticker] = rows
    mapping = {
        "themes": {"10_A": {"members": ["WINNER", "LAG1", "LAG2"]}},
        "funds": [{"ticker": "FUND", "themes": ["10_A"]}],
    }
    result = t.fund_comparisons(series, mapping)[0]
    assert result["reproduced"] is True
    assert result["robust"] is False
    assert result["windows"]["495"]["dropped"] == "WINNER"
    result = t.fund_comparisons({k: v[-300:] for k, v in series.items()}, mapping)[0]
    assert result["windows"]["495"]["measured"] is False
    assert result["reproduced"] is False


def test_forward_evaluation_rejects_in_sample_only(tmp_path):
    path = tmp_path / "bars.csv"
    price_table(path, {BENCHMARK: (1, 0, 100)})
    universe = {"as_of": "2026-10-01", "members": [{"ticker": BENCHMARK}]}
    with pytest.raises(evaluate_core.EvaluateError, match="forward"):
        evaluate_core.evaluate(universe=universe, prices=path)


def test_all_markets_max_increment_is_40_to_50_percent():
    policy = load_policy()
    assert PROFILES[-1] == "max"
    for market in policy["markets"]:
        bands = market_guidance(market, policy, None)
        ratio = bands["max"]["target"] / bands["heavy"]["target"]
        assert 1.4 <= ratio <= 1.5, market


def test_cn_real_max_retains_heavy_and_adds_qualified_beta():
    root = Path(__file__).resolve().parents[1]
    raw = read_json(root / "examples/cn-medium/snapshot.json")
    policy = load_policy()
    heavy, _ = build_universe(dict(spec("heavy"), market="cn"), raw, policy)
    max, report = build_universe(dict(spec("max"), market="cn"), raw, policy, heavy)
    held = {m["ticker"] for m in heavy["members"]}
    additions = [m for m in max["members"] if m["ticker"] not in held]
    assert held <= {m["ticker"] for m in max["members"]}
    assert len(heavy["members"]) == 520 and len(max["members"]) == 755
    assert sum(m["role"] == "BETA_SATELLITE" for m in additions) >= 165
    assert report["passed"] and report["stats"]["tradingview_tokens"] <= 1000
    medium, _ = build_universe(dict(spec("medium"), market="cn"), raw, policy)
    jumped, _ = build_universe(dict(spec("max"), market="cn"), raw, policy, medium)
    assert {m["ticker"] for m in jumped["members"]} == {
        m["ticker"] for m in max["members"]
    }
    direct, _ = build_universe(dict(spec("max"), market="cn"), raw, policy)
    assert {m["ticker"] for m in direct["members"]} == {m["ticker"] for m in max["members"]}


def test_insufficient_beta_is_disclosed_without_relabelling():
    raw = snapshot()
    raw["taxonomy"] = raw["taxonomy"][:2]
    raw["candidates"] = [
        candidate(f"BINANCE:T{i}USDT.P", f"T{i}", "10_A" if i else "00_A", "THEME_LEADER")
        for i in range(10)
    ]
    policy = small_policy()
    policy["tiers"]["max"] = 10
    heavy, _ = build_universe(spec("heavy"), raw, policy)
    max, report = build_universe(spec("max"), raw, policy, heavy)
    assert len(max["members"]) == 10
    assert all(m["role"] == "THEME_LEADER" for m in max["members"])
    assert any("qualified beta additions filled 0" in w for w in report["warnings"])


def test_old_receipts_cannot_be_relabelled_fresh(tmp_path):
    path = tmp_path / "cache.json"
    url = "https://example.com/price"
    key = hashlib.sha256(json.dumps([url, None], sort_keys=True).encode()).hexdigest()
    record = {
        "request_hash": key,
        "retrieved_at": "2020-01-01T00:00:00+00:00",
        "response": {"old": True},
    }
    path.write_text(json.dumps(record))
    with (
        patch.object(p.urllib.request, "urlopen", side_effect=OSError("offline")),
        patch.object(p.time, "sleep"),
    ):
        with pytest.raises(p.ProviderError, match="offline"):
            p.request_json(url, path)
    assert json.loads(path.read_text()) == record
    record["retrieved_at"] = datetime.now(timezone.utc).isoformat()
    path.write_text(json.dumps(record))
    with patch.object(p.urllib.request, "urlopen", side_effect=AssertionError("must use cache")):
        assert p.request_json(url, path) == {"old": True}


def test_provider_partial_requests_remain_partial(tmp_path):
    rows = [
        {
            "ticker": "NASDAQ:A",
            "description": "A",
            "active_symbol": True,
            "is_primary": True,
            "typespecs": ["common"],
            "currency": "USD",
            "volume": 10,
            "close": 5,
            "market_cap_basic": 100,
            "industry": "X",
            "sector": "Y",
        }
    ]
    with (
        patch.object(p, "scan_equities", return_value=(rows, {"observed": 1})),
        patch.object(p, "fetch_equity_bars", side_effect=p.ProviderError("no data")),
    ):
        result = p.fetch_equities("us", tmp_path, "2026-09-28", 1, 1, set())
    assert result["complete"] is False
    assert result["received"] == 0
    assert result["failures"] == [{"ticker": "NASDAQ:A", "reason": "no data"}]
    assert (tmp_path / "prices.csv").read_text().splitlines() == ["date,ticker,close,turnover"]


def test_yahoo_adjustment_and_gbp_units():
    days = [
        int(datetime(2026, 8, 1, tzinfo=timezone.utc).timestamp()) + i * 86400 for i in range(35)
    ]
    payload = {
        "chart": {
            "result": [
                {
                    "timestamp": days,
                    "meta": {"currency": "GBp", "symbol": "TEST.L"},
                    "indicators": {
                        "quote": [{"close": [200 + i for i in range(35)], "volume": [100] * 35}],
                        "adjclose": [{"adjclose": [100 + i for i in range(35)]}],
                    },
                }
            ]
        }
    }
    rows, receipt = p.parse_yahoo(payload, "LSE:TEST", "2026-09-04")
    assert rows[0][2:] == (100, 200)
    assert receipt["turnover_currency"] == "GBP"
    assert receipt["observations"] == 35


def test_active_a_share_is_not_removed_by_global_primary_flag():
    row = {"description": "Synthetic A/H issuer", "active_symbol": True, "is_primary": False,
           "typespecs": ["common"], "currency": "CNY", "volume": 10, "close": 5,
           "market_cap_basic": 100, "industry": "Semiconductors", "sector": "Technology"}
    assert p.admissible_equity(row, "cn")
    row["currency"] = "USD"
    assert not p.admissible_equity(row, "cn")


def test_missing_output_hash_cannot_disable_integrity_check():
    universe, _ = build_universe(spec(), snapshot(), small_policy())
    universe.pop("content_hash")
    assert not validate_universe(universe, small_policy())["passed"]


@pytest.mark.parametrize(
    "field,value", [("as_of", "unknown"), ("as_of", "20260909"), ("tier", True)]
)
def test_evidence_has_typed_tier_and_iso_date(field, value):
    raw = snapshot()
    raw["sources"][0][field] = value
    with pytest.raises(UniverseError):
        normalize_snapshot(raw)


def test_measurement_diagnostics_survive_merge_and_build():
    raw = snapshot()
    bundle = {"as_of": raw["as_of"], "measurement": raw["measurement"],
              "metrics": {c["ticker"]: c["metrics"] for c in raw["candidates"]},
              "records": {c["ticker"]: c["measurement_record"] for c in raw["candidates"]},
              "theme_checks": {"10_A": {"usable": False, "fit": -.1}},
              "fund_comparisons": [{"ticker": "fixture", "robust": False}]}
    merged = m.merge_into_snapshot(raw, bundle)
    universe, _ = build_universe(spec(), merged, small_policy())
    assert universe["measurement_audit"]["theme_checks"] == bundle["theme_checks"]
    assert universe["measurement_audit"]["fund_comparisons"] == bundle["fund_comparisons"]


@pytest.mark.parametrize('ticker', ['BINANCE:WUSDT.P', 'BINANCE:SUSDT.P', 'BINANCE:TUSDT'])
def test_crypto_single_character_base_is_valid(ticker):
    # Binance inventory and TradingView both carry these shapes; listing evidence is still required.
    assert not validate_ticker('crypto', ticker)


def test_perpetual_scope_keeps_source_exclusions_and_identity_boundary(tmp_path):
    """Synthetic provider fixture, never reused as market evidence."""
    def contract(base, tags, kind='COIN'):
        return dict(baseAsset=base, quoteAsset='USDT', status='TRADING', symbol=base+'USDT',
                    contractType='PERPETUAL', underlyingType=kind, underlyingSubType=tags)

    products = [dict(b='AAA', q='USDT', st='TRADING', tags=['defi'], qv=100),
                dict(b='BAD', q='USDT', st='TRADING', tags=['Monitoring'])]
    perps = [contract('AAA', ['DeFi', 'Crypto']), contract('W', ['Infrastructure', 'Crypto']),
             contract('BAD', ['DeFi', 'Crypto']), contract('1000AAA', ['DeFi', 'Crypto']),
             contract('MACRO', ['TradFi']), contract('NOVEL', ['Alpha', 'Crypto'])]
    calls = []

    def request(url, cache, payload=None):
        if 'get-products' in url:
            return {'data': products}
        if 'exchangeInfo' in url:
            return {'symbols': perps if 'fapi' in url else perps[:1]}
        calls.append(url)
        end = datetime(2026, 9, 28, tzinfo=timezone.utc)
        bars = []
        for i in range(180):
            stamp = int((end - timedelta(days=179-i)).timestamp() * 1000)
            bars.append([stamp, 0, 0, 0, 100+i, 0, stamp+86399999, 2_000_000])
        return bars

    with patch.object(p, 'request_json', side_effect=request):
        result = p.fetch_crypto(tmp_path, '2026-09-28', 1000, 1, 'all-perpetuals')
    assert result['received'] == 2
    rows = json.loads((tmp_path / 'listings.json').read_text())['rows']
    assert {r['asset_id'] for r in rows} == {'AAA', 'W'}
    new = next(r for r in rows if r['asset_id'] == 'W')
    assert new['theme_source'] == 'https://fapi.binance.com/fapi/v1/exchangeInfo'
    assert new['tags'] == ['Infrastructure']
    assert len(calls) == 2
