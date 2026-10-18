"""Synthetic adversarial Global contracts; none of these fixtures is market research."""

import hashlib
import json
import shutil
import subprocess
import sys
from copy import deepcopy
from datetime import date, timedelta
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from global_core import compose, digest, evaluate, validate
from test_coverage_core import build
from universe_core import UniverseError
from watchlist_core import check_watchlist, render_watchlist

ROOT = Path(__file__).resolve().parents[1]
AS_OF = "2026-09-09"


def ev():
    return [{"url": "https://example.com/synthetic", "as_of": AS_OF, "tier": 1}]


def group(key):
    return {"id": key, "name": key, "purpose": "Synthetic observation purpose"}


def identity(ticker, entity, coverage="entity"):
    return dict(
        ticker=ticker,
        entity_id=entity,
        name=entity,
        economic_market="US",
        coverage_type=coverage,
        legal_ids=["SYNTHETIC:" + entity],
        evidence=ev(),
    )


def selection(ticker, source, theme, duties):
    return dict(
        ticker=ticker,
        source=source,
        theme=theme,
        market="US",
        duties=duties,
        reason="Synthetic distinct business observation",
        evidence=ev(),
    )


def fixture():
    universe, _ = build(profile="light")
    catalog = dict(
        schema_version=1,
        kind="global_reference_catalog",
        as_of=AS_OF,
        references=[
            dict(
                ticker="SP:FIX",
                name="INDEX",
                kind="index",
                observes="Synthetic US breadth",
                verified_ticker="SP:FIX",
                verified_as_of=AS_OF,
                evidence=ev(),
            )
        ],
    )
    sources = {"us": universe, "refs": catalog}
    contract = dict(
        schema_version=1,
        kind="global_coverage_contract",
        scope_level="synthetic",
        scope="Synthetic regression only",
        markets=[group("US")],
        themes=[group(t) for t in ("BANK", "TECH", "GAUGE")],
        duties=[
            dict(
                id=k,
                dimension=dimension,
                group=g,
                purpose="Synthetic duty",
                minimum=1,
                leader_minimum=leaders,
                allowed_kinds=kinds,
            )
            for k, dimension, g, leaders, kinds in [
                ("US_BROAD", "market", "US", 0, ["index", "etf"]),
                ("BANK", "theme", "BANK", 1, ["equity"]),
                ("TECH", "theme", "TECH", 1, ["equity"]),
                ("GAUGE", "theme", "GAUGE", 0, ["index", "etf"]),
            ]
        ],
    )
    spec = dict(
        schema_version=1,
        kind="global_spec",
        as_of=AS_OF,
        sources=[
            dict(
                id=key, kind="universe" if key == "us" else "catalog", file=key + ".json", sha256=""
            )
            for key in sources
        ],
        identities=[
            identity("NYSE:CORE0", "BANK"),
            identity("NYSE:CORE6", "TECH"),
            identity("SP:FIX", "INDEX", "market"),
        ],
        selections=[
            selection("NYSE:CORE0", "us", "BANK", ["BANK"]),
            selection("NYSE:CORE6", "us", "TECH", ["TECH"]),
            selection("SP:FIX", "refs", "GAUGE", ["US_BROAD", "GAUGE"]),
        ],
    )
    contract["source_themes"] = [
        dict(
            id="us:" + theme["theme_code"],
            disposition="mapped",
            reason="Synthetic mapping",
            themes=["BANK" if theme["theme_code"] == "10_A" else "TECH"],
        )
        for theme in universe["taxonomy"]
    ]
    return spec, contract, sources


def write_inputs(tmp_path, spec, contract, sources):
    tmp_path.mkdir(parents=True, exist_ok=True)
    for entry in spec["sources"]:
        path = tmp_path / entry["file"]
        path.write_text(json.dumps(sources[entry["id"]], indent=2))
        entry["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    (tmp_path / "spec.json").write_text(json.dumps(spec))
    (tmp_path / "contract.json").write_text(json.dumps(contract))
    return tmp_path / "spec.json", tmp_path / "contract.json"


def fund(ticker):
    sessions, day = [], date.fromisoformat(AS_OF)
    while len(sessions) < 30:
        if day.weekday() < 5:
            sessions.append(dict(date=day.isoformat(), notional_usd=2e7))
        day -= timedelta(days=1)
    sessions.reverse()
    measurement = dict(value=2e9, as_of=AS_OF, source=ev()[0]["url"])
    return dict(
        ticker=ticker,
        category="theme",
        benchmark_id="SYNTHETIC_INDEX",
        exposure_group="SYNTHETIC_TECH",
        structure="unlevered_equity",
        inception="2020-01-01",
        assets_usd=measurement,
        gross_fee_pct={**measurement, "value": 0.4},
        spread_pct={**measurement, "value": 0.05},
        holdings_as_of=AS_OF,
        holdings_source=ev()[0]["url"],
        holdings=[dict(entity_id="BANK", weight=0.5), dict(entity_id="TECH", weight=0.5)],
        activity=dict(
            source=ev()[0]["url"],
            as_of=AS_OF,
            currency="USD",
            method="source_reported_notional",
            data_sha256=digest(sessions),
            observations=sessions,
        ),
    )


def with_fund():
    spec, contract, sources = fixture()
    ticker = "AMEX:FIXETF"
    sources["refs"]["references"].append(
        dict(
            ticker=ticker,
            name="FUND",
            kind="etf",
            observes="Synthetic technology basket",
            verified_ticker=ticker,
            verified_as_of=AS_OF,
            evidence=ev(),
            fund=fund(ticker),
        )
    )
    spec["identities"].append(identity(ticker, "FUND", "theme"))
    spec["selections"].append(selection(ticker, "refs", "TECH", ["TECH"]))
    contract["duties"][2]["allowed_kinds"].append("etf")
    return spec, contract, sources


def test_portable_atomic_bundle_and_independent_cli(tmp_path):
    spec, contract, sources = fixture()
    s, c = write_inputs(tmp_path / "inputs", spec, contract, sources)
    receipt = compose(s, c, tmp_path / "out")
    path = Path(receipt["artifacts"]["universe"])
    assert validate(path, c)["qualified"]
    assert Path(receipt["artifacts"]["watchlist"]).read_text() == ("NYSE:CORE0,NYSE:CORE6,SP:FIX\n")
    shutil.move(tmp_path / "out", tmp_path / "moved")
    shutil.rmtree(tmp_path / "inputs")
    copied_contract = tmp_path / "moved/global-contract.json"
    moved = tmp_path / "moved" / path.name
    result = subprocess.run(
        [
            sys.executable,
            "scripts/universe.py",
            "validate-global",
            str(moved),
            "--contract",
            str(copied_contract),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stderr
    assert json.loads(result.stdout)["symbols"] == 3
    assert "synthetic" in (moved.with_suffix(".en.html")).read_text()


@pytest.mark.parametrize(
    "mutation,match",
    [
        (lambda s, c, u: s["identities"][1].update(entity_id="BANK"), "duplicate global"),
        (
            lambda s, c, u: s["identities"][1].update(legal_ids=["SYNTHETIC:BANK"]),
            "duplicate legal",
        ),
        (lambda s, c, u: s["selections"].pop(0), "missing mandatory"),
        (lambda s, c, u: s["selections"][0].update(ticker="NYSE:UNKNOWN"), "absent"),
        (lambda s, c, u: s["selections"][0].update(market="JP"), "economic mix-up"),
        (lambda s, c, u: s["selections"][0].update(duties=["US_BROAD"]), "conflicts"),
        (lambda s, c, u: s["selections"][0].update(duties=["INVENTED"]), "coverage claims"),
        (lambda s, c, u: c.update(required_tickers=["AMEX:DIA"]), "required ticker"),
        (lambda s, c, u: c.update(excluded_tickers=["NYSE:CORE0"]), "excluded ticker"),
        (lambda s, c, u: c.update(etf_rules={"min_aum_usd": 1}), "weaken"),
        (lambda s, c, u: c["themes"].append(group("EMPTY")), "frozen duty"),
        (lambda s, c, u: s["identities"][2].update(coverage_type="theme"), "broad-market"),
        (lambda s, c, u: s["identities"][2]["evidence"][0].update(as_of="2027-01-01"), "180 days"),
        (lambda s, c, u: u["refs"]["references"][0].update(verified_ticker="SP:OTHER"), "mismatch"),
        (lambda s, c, u: u["refs"]["references"][0].update(verified_as_of="2026-01-01"), "30 days"),
    ],
)
def test_unqualified_research_blocks_composition(mutation, match):
    spec, contract, sources = fixture()
    mutation(spec, contract, sources)
    with pytest.raises(UniverseError, match=match):
        evaluate(spec, contract, sources)


@pytest.mark.parametrize(
    "mutation,match",
    [
        (lambda f: f["assets_usd"].update(value=1e6), "assets below"),
        (lambda f: f["gross_fee_pct"].update(value=0.95), "fee above"),
        (lambda f: f["spread_pct"].update(value=0.3), "spread above"),
        (lambda f: f.update(structure="bond"), "unlevered equity"),
        (lambda f: f.update(ticker="AMEX:DIFFERENT"), "mismatch"),
        (lambda f: f.update(inception="2026-09-01"), "12 months"),
        (lambda f: f.update(holdings_as_of="2026-01-01"), "30 days"),
        (lambda f: f["holdings"].pop(), "full holdings"),
        (lambda f: f["activity"]["observations"].pop(), "30 completed"),
        (lambda f: f["activity"].update(currency="JPY"), "USD notional"),
        (lambda f: f["activity"]["observations"][0].update(notional_usd=1), "input hash"),
        (lambda f: f["gross_fee_pct"].update(value=True), "finite number"),
        (lambda f: f["assets_usd"].update(as_of="2027-01-01"), "30 days"),
    ],
)
def test_etf_quality_cannot_be_waived_for_coverage(mutation, match):
    spec, contract, sources = with_fund()
    mutation(sources["refs"]["references"][-1]["fund"])
    with pytest.raises(UniverseError, match=match):
        evaluate(spec, contract, sources)


def test_turnover_is_recomputed_and_not_an_author_supplied_mean():
    spec, contract, sources = with_fund()
    f = sources["refs"]["references"][-1]["fund"]
    for row in f["activity"]["observations"]:
        row["notional_usd"] = 1
    f["activity"]["data_sha256"] = digest(f["activity"]["observations"])
    with pytest.raises(UniverseError, match="turnover below"):
        evaluate(spec, contract, sources)


def test_source_validation_and_hashes_are_independent(tmp_path):
    spec, contract, sources = fixture()
    s, c = write_inputs(tmp_path, spec, contract, sources)
    (tmp_path / "us.json").write_text("{}")
    with pytest.raises(UniverseError, match="source hash changed"):
        compose(s, c, tmp_path / "out")
    assert not (tmp_path / "out").exists()
    sources["us"]["members"].pop()
    s, c = write_inputs(tmp_path, spec, contract, sources)
    with pytest.raises(UniverseError, match="independently qualify"):
        compose(s, c, tmp_path / "out")


def test_overlapping_etfs_require_real_distinct_duties_and_review():
    spec, contract, sources = with_fund()
    other = deepcopy(sources["refs"]["references"][-1])
    other.update(ticker="AMEX:SECOND", name="SECOND", verified_ticker="AMEX:SECOND")
    other["fund"]["ticker"] = "AMEX:SECOND"
    other["fund"]["benchmark_id"] = "SYNTHETIC_EQUAL_WEIGHT"
    sources["refs"]["references"].append(other)
    spec["identities"].append(identity("AMEX:SECOND", "SECOND", "theme"))
    spec["selections"].append(selection("AMEX:SECOND", "refs", "TECH", ["TECH"]))
    with pytest.raises(UniverseError, match="overlapping ETF"):
        evaluate(spec, contract, sources)
    spec["coexistence_reviews"] = [
        dict(pair=["AMEX:FIXETF", "AMEX:SECOND"], reason="Synthetic explanation", evidence=ev())
    ]
    with pytest.raises(UniverseError, match="distinct observation"):
        evaluate(spec, contract, sources)
    contract["duties"].append(
        dict(
            id="SECOND_JOB",
            dimension="theme",
            group="TECH",
            purpose="Synthetic distinct weighting job",
            allowed_kinds=["etf"],
            minimum=1,
        )
    )
    spec["selections"][-1]["duties"] = ["SECOND_JOB"]
    composed = evaluate(spec, contract, sources)
    assert composed["fund_overlap"][0]["holdings_overlap"] == 1
    assert composed["fund_overlap"][0]["reviewed"]


@pytest.mark.parametrize("tamper", ["member", "txt", "source", "denominator", "path"])
def test_independent_validator_rejects_published_tampering(tmp_path, tamper):
    spec, contract, sources = fixture()
    s, c = write_inputs(tmp_path / "in", spec, contract, sources)
    receipt = compose(s, c, tmp_path / "out")
    path = Path(receipt["artifacts"]["universe"])
    value = json.loads(path.read_text())
    if tamper == "member":
        value["members"].pop()
    elif tamper == "txt":
        Path(receipt["artifacts"]["watchlist"]).write_text("NYSE:CORE0\n")
    elif tamper == "source":
        (path.parent / "source-us.json").write_text("{}")
    elif tamper == "denominator":
        smaller = deepcopy(contract)
        smaller["duties"].pop()
        value["contract_sha256"] = digest(smaller)
    else:
        value["spec"]["sources"][0]["file"] = "../in/us.json"
    value["content_sha256"] = digest({k: v for k, v in value.items() if k != "content_sha256"})
    path.write_text(json.dumps(value))
    assert not validate(path, c)["passed"]


def test_output_collision_does_not_modify_existing_files(tmp_path):
    spec, contract, sources = fixture()
    s, c = write_inputs(tmp_path / "in", spec, contract, sources)
    compose(s, c, tmp_path / "out")
    before = {p.name: p.read_bytes() for p in (tmp_path / "out").iterdir()}
    with pytest.raises(UniverseError, match="not empty"):
        compose(s, c, tmp_path / "out")
    assert before == {p.name: p.read_bytes() for p in (tmp_path / "out").iterdir()}


@pytest.mark.parametrize(
    "text",
    [
        "NVDA",
        "NASDAQ:nvda",
        "NASDAQ:NVDA,",
        " NASDAQ:NVDA",
        "NASDAQ:NVDA\nNYSE:TSM",
        "NASDAQ:NVDA，NYSE:TSM",
        "NASDAQ:NVDA,NASDAQ:NVDA",
        "\ufeffNASDAQ:NVDA",
        "###EMPTY",
        "###ONE,###TWO,NASDAQ:NVDA",
        "###ONE,NASDAQ:NVDA,###ONE,NYSE:TSM",
        "###ONE,NYSE:TSM,###EMPTY",
        "###BAD:NAME,NYSE:TSM",
        "NASDAQ:NVDA\t",
    ],
)
def test_strict_txt_rejects_lossy_or_invalid_exports(text):
    assert not check_watchlist(text)["passed"]


def test_txt_header_capacity_and_ticker_only_rules():
    rows = [dict(ticker=f"NYSE:FIX{i}", theme="T") for i in range(1000)]
    assert check_watchlist(render_watchlist(rows), ticker_only=True)["symbols"] == 1000
    with pytest.raises(UniverseError, match="1001 tokens"):
        render_watchlist(rows, [dict(id="T", name="THEME")], "theme")
    assert not check_watchlist("###T,NYSE:FIX0\n", ticker_only=True)["passed"]
    assert check_watchlist("KRX:005930,HKEX:700,TSE:285A,BINANCE:BTCUSDT.P\n")["passed"]


def test_crlf_tampering_is_not_normalized_away_by_file_read(tmp_path):
    spec, contract, sources = fixture()
    s, c = write_inputs(tmp_path / "in", spec, contract, sources)
    receipt = compose(s, c, tmp_path / "out")
    txt = Path(receipt["artifacts"]["watchlist"])
    txt.write_bytes(txt.read_bytes().replace(b"\n", b"\r\n"))
    assert not validate(receipt["artifacts"]["universe"], c)["passed"]
    result = subprocess.run(
        [sys.executable, "scripts/universe.py", "check-watchlist", str(txt)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 2


@pytest.mark.parametrize(
    "mutation",
    [
        lambda s, c, u: c["source_themes"].pop(),
        lambda s, c, u: c["source_themes"][0].update(disposition="out_of_scope", themes=[]),
        lambda s, c, u: c["source_themes"][0].update(themes=["TECH"]),
        lambda s, c, u: s["identities"][0].update(entity_id=" bank "),
        lambda s, c, u: s.update(schema_version=True),
        lambda s, c, u: c.update(schema_version=True),
    ],
)
def test_followup_review_rejects_lost_lineage_and_noncanonical_identity(mutation):
    spec, contract, sources = fixture()
    mutation(spec, contract, sources)
    with pytest.raises(UniverseError):
        evaluate(spec, contract, sources)


def test_identical_etf_benchmark_cannot_be_excused_by_a_new_duty():
    spec, contract, sources = with_fund()
    other = deepcopy(sources["refs"]["references"][-1])
    other.update(ticker="AMEX:SECOND", name="SECOND", verified_ticker="AMEX:SECOND")
    other["fund"]["ticker"] = "AMEX:SECOND"
    sources["refs"]["references"].append(other)
    spec["identities"].append(identity("AMEX:SECOND", "SECOND", "theme"))
    spec["selections"].append(selection("AMEX:SECOND", "refs", "TECH", ["TECH"]))
    with pytest.raises(UniverseError, match="duplicate benchmark"):
        evaluate(spec, contract, sources)
