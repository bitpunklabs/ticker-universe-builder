"""Synthetic regression contracts, not researched ticker recommendations."""

import hashlib
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from build_run import run_build
from coverage_core import audit_core
from test_universe_core import candidate, change_set, evidence, measurement
from universe_core import (
    UniverseError,
    apply_change_set,
    build_universe,
    content_hash,
    load_policy,
    render_txt,
    universe_hash,
    validate_universe,
)


def researched():
    """Ten necessary leaders, two peers, many attractive Beta alternatives."""
    profiles = ("light", "medium", "heavy", "extreme")
    plan = dict(
        schema_version=1,
        origin="new",
        scope="Synthetic US fixture only",
        evidence=evidence(),
        budgets=dict(zip(profiles, (4, 8, 20, 30), strict=True)),
        sectors=[
            dict(
                id=k,
                weight=1,
                rationale="Independent economic sector",
                caps=dict(zip(profiles, (4, 8, 10, 12), strict=True)),
            )
            for k in ("banking", "technology")
        ],
        branches=[],
        roster=[],
        references=[],
    )
    candidates = []
    for i in range(12):
        asset = f"CORE{i}"
        sector = "banking" if i < 6 else "technology"
        kind = "leader" if i not in (5, 11) else "peer"
        depth = "light" if i in (0, 1, 6, 7) else "medium" if i in (2, 3, 8, 9) else "heavy"
        c = candidate(f"NYSE:{asset}", asset, "10_A" if i < 6 else "11_A", "THEME_LEADER")
        c["admission"] = dict(
            kind=kind,
            branch=sector,
            min_profile=depth,
            business="Fixture leadership evidence",
            quality="Fixture quality evidence",
            evidence=evidence(),
            instrument=dict(kind="equity", quote_currency="USD", units=1),
        )
        candidates.append(c)
        plan["roster"].append(dict(asset_id=asset, kind=kind, min_profile=depth))
    for sector in ("banking", "technology"):
        plan["branches"].append(
            dict(
                id=sector,
                sector=sector,
                purpose="Differentiated business roles",
                min_profile="light",
                representatives=[
                    c["asset_id"] for c in candidates if c["admission"]["branch"] == sector
                ],
            )
        )
    for i in range(30):
        asset = f"BETA{i}"
        c = candidate(f"NYSE:{asset}", asset, "11_A", "BETA_SATELLITE")
        c["admission"] = dict(
            kind="satellite",
            branch="technology",
            min_profile="heavy",
            business="Verified supply-chain exposure",
            quality="Fixture quality evidence",
            evidence=evidence(),
            incremental_value=f"Distinct fixture business {i}",
            distinct_from=["CORE6"],
            instrument=dict(kind="equity", quote_currency="USD", units=1),
        )
        candidates.append(c)
    return dict(
        schema_version=1,
        market="us",
        as_of="2026-09-09",
        complete=True,
        sources=evidence(),
        measurement=measurement(),
        candidates=candidates,
        taxonomy=[
            dict(l1_code=k, l1_name=n, theme_code=k + "_A", theme_name=n, coverage_level=1)
            for k, n in [("10", "BANKS"), ("11", "TECH")]
        ],
        coverage_plan=plan,
    )


def build(data=None, profile="heavy", seed=None, **kwargs):
    return build_universe(
        dict(schema_version=1, market="us", profile=profile, **kwargs),
        data or researched(),
        load_policy(),
        seed,
    )


def resign(u):
    u["version_hash"] = universe_hash(u)
    u["content_hash"] = content_hash(u)
    return u


def test_default_requires_plan_and_does_not_certify_legacy_anchors():
    data = researched()
    del data["coverage_plan"]
    with pytest.raises(UniverseError, match="coverage_plan"):
        build(data)
    data = researched()
    del data["candidates"][2]["admission"]
    with pytest.raises(UniverseError, match="CORE2"):
        build(data)


def test_depth_roles_budgets_and_true_extreme_increment():
    light, _ = build(profile="light")
    medium, _ = build(profile="medium")
    heavy, report = build()
    extreme, final = build(profile="extreme", seed=heavy)
    assert [len(u["members"]) for u in (light, medium, heavy, extreme)] == [4, 8, 15, 18]
    assert {c["admission"]["kind"] for c in medium["members"]} == {"leader"}
    assert report["stats"]["quality"]["leader_coverage"] == 1
    assert final["stats"]["quality"]["unused_capacity"] == 12
    old = {c["asset_id"] for c in heavy["members"]}
    assert all(
        c["admission"]["kind"] == "satellite"
        for c in extreme["members"]
        if c["asset_id"] not in old
    )
    assert (
        len([c for c in extreme["members"] if c["admission"]["kind"] == "satellite"]) / 18 <= 0.35
    )


def test_bank_representatives_cannot_be_displaced_by_hot_candidates():
    data = researched()
    data["candidates"][3]["eligible"] = False
    data["candidates"][3]["exclusion_reasons"] = ["unverifiable_fact: missing leadership check"]
    with pytest.raises(UniverseError, match="CORE3"):
        build(data)
    with pytest.raises(UniverseError, match="budget"):
        build(target_count=10)


def test_display_split_order_and_heat_do_not_change_selected_entities():
    original, _ = build()
    data = researched()
    data["taxonomy"].append(
        dict(
            l1_code="11",
            l1_name="TECH",
            theme_code="11_B",
            theme_name="MORE_CHIPS",
            coverage_level=3,
            weight=4,
        )
    )
    for i, c in enumerate(data["candidates"]):
        if c["theme_code"] == "11_A" and i % 2:
            c["theme_code"] = "11_B"
        c["metrics"]["heat"] = 100 if i % 2 else 0
    data["candidates"].reverse()
    data["taxonomy"].reverse()
    changed, _ = build(data)
    assert {c["asset_id"] for c in original["members"]} == {
        c["asset_id"] for c in changed["members"]
    }


@pytest.mark.parametrize(
    "mutation, error",
    [
        (
            lambda d: d["coverage_plan"]["sectors"][0]["caps"].update(medium=5, heavy=5),
            "sector cap",
        ),
        (lambda d: d["candidates"][3]["admission"].update(min_profile="extreme"), "delayed"),
        (lambda d: d["candidates"][12]["admission"].update(incremental_value=""), "incremental"),
        (lambda d: d["candidates"][0]["admission"].update(evidence=evidence(3)), "tier 1"),
        (lambda d: d["candidates"][0]["admission"]["instrument"].update(units=0), "contract units"),
    ],
)
def test_quality_failures(mutation, error):
    data = researched()
    mutation(data)
    with pytest.raises(UniverseError, match=error):
        build(data)


def test_extreme_requires_qualified_same_version_heavy():
    with pytest.raises(UniverseError, match="--seed"):
        build(profile="extreme")
    medium, _ = build(profile="medium")
    with pytest.raises(UniverseError, match="Heavy"):
        build(profile="extreme", seed=medium)
    heavy, _ = build()
    changed = researched()
    changed["coverage_plan"]["scope"] = "Different scope"
    with pytest.raises(UniverseError, match="coverage plan"):
        build(changed, profile="extreme", seed=heavy)
    heavy["members"].pop(0)
    resign(heavy)
    with pytest.raises(UniverseError):
        build(profile="extreme", seed=heavy)


def test_revalidate_rejects_missing_backbone_even_after_resigning():
    heavy, _ = build()
    heavy["members"] = [c for c in heavy["members"] if c["asset_id"] != "CORE4"]
    report = validate_universe(resign(heavy))
    assert not report["passed"]
    assert any("CORE4" in e for e in report["errors"])


def test_reference_layer_is_exported_without_consuming_entity_budget():
    data = researched()
    data["coverage_plan"]["references"] = [
        dict(
            id="rate10",
            ticker="TVC:US10Y",
            theme_code="10_A",
            kind="yield",
            observes="US ten-year Treasury yield",
            evidence=evidence(),
        )
    ]
    heavy, report = build(data)
    assert len(heavy["members"]) == 15
    assert report["stats"]["exported_tickers"] == 16
    assert "TVC:US10Y" in render_txt(heavy)
    with pytest.raises(UniverseError, match="TradingView"):
        build(data, tradingview_token_cap=14)
    data["coverage_plan"]["references"][0]["proxy_for"] = "Another yield"
    with pytest.raises(UniverseError, match="limitation"):
        build(data)


def baseline(data, action="retain", ticker="NYSE:CORE0"):
    text = "###10_A_BANKS," + ticker
    data["coverage_plan"].update(
        origin="migration",
        baseline=dict(
            watchlist=text,
            sha256=hashlib.sha256(text.encode()).hexdigest(),
            decisions=[
                dict(
                    ticker=ticker,
                    action=action,
                    asset_id="CORE0",
                    reason="Researched binding",
                    evidence=evidence(),
                )
            ],
        ),
    )


def test_core_decisions_and_instrument_conversion_are_explicit():
    data = researched()
    baseline(data, "pending")
    with pytest.raises(UniverseError, match="unresolved Core"):
        build(data)
    baseline(data, ticker="NASDAQ:CORE0")
    with pytest.raises(UniverseError, match="requires replace"):
        build(data)
    data["coverage_plan"]["baseline"]["decisions"][0]["action"] = "replace"
    build(data)
    data["coverage_plan"]["baseline"]["decisions"] = []
    with pytest.raises(UniverseError, match="every original Core"):
        build(data)


def test_maintenance_cannot_remove_a_necessary_leader():
    heavy, _ = build()
    changes = change_set(
        heavy, [dict(op="REMOVE", ticker="NYSE:CORE4", reason="fixture", evidence=evidence())]
    )
    changes["market"] = "us"
    with pytest.raises(UniverseError, match="CORE4"):
        apply_change_set(heavy, changes, load_policy())


def test_failed_research_resumes_and_unused_capacity_is_success(tmp_path):
    data = researched()
    del data["candidates"][0]["admission"]
    sp, sn = tmp_path / "spec.json", tmp_path / "snapshot.json"
    sp.write_text(json.dumps(dict(schema_version=1, market="us", profile="heavy")))
    sn.write_text(json.dumps(data))
    result, code = run_build(spec=str(sp), snapshot=str(sn), output=str(tmp_path / "out"))
    assert code == 2 and not (tmp_path / "out").exists()
    sn.write_text(json.dumps(researched()))
    fixed, code = run_build(
        spec=None, snapshot=None, output=None, resume=str(Path(result["checkpoint"]).parent)
    )
    assert code == 0 and fixed["status"] == "complete" and fixed["unused_capacity"] == 5
    assert fixed["shortfall"] == 0 and fixed["quality"]["status"] == "qualified"
    assert json.loads(Path(result["inputs_archive"]).read_text())["snapshot"] == data


def test_audit_preserves_original_text_and_never_guesses_aliases():
    text = "###00_A_INDEX,TVC:VIX,###10_A_BANKS,NASDAQ:KHC"
    heavy, _ = build()
    audit = audit_core(text, heavy)
    assert audit["baseline"]["watchlist"] == text
    assert audit["missing_exact"] == ["NASDAQ:KHC", "TVC:VIX"]
    assert all(d["action"] == "pending" for d in audit["decisions"])


def test_policy_cannot_weaken_satellite_ceiling():
    policy = load_policy()
    policy["coverage"]["satellite_max"]["heavy"] = 0.5
    with pytest.raises(UniverseError, match="tighten"):
        build_universe(dict(schema_version=1, market="us", profile="heavy"), researched(), policy)


def test_unreviewed_candidates_are_deferred_without_padding():
    data = researched()
    for c in data["candidates"][12:]:
        del c["admission"]
    heavy, report = build(data)
    assert len(heavy["members"]) == 12
    assert report["stats"]["rejections"]["unverifiable_fact"] == 30


def test_export_cap_stops_optional_tail_without_discarding_backbone():
    heavy, report = build(tradingview_token_cap=16)
    assert report["passed"] and len(heavy["members"]) == 14


def test_crypto_needs_ecosystem_and_token_identity():
    data = researched()
    data["market"] = "crypto"
    for c in data["candidates"]:
        c["ticker"] = "BINANCE:" + c["asset_id"] + "USDT.P"
    spec = dict(schema_version=1, market="crypto", profile="heavy")
    with pytest.raises(UniverseError, match="ecosystem_id"):
        build_universe(spec, data, load_policy())
    for c in data["candidates"]:
        c["admission"].update(ecosystem_id=c["asset_id"], token_role="Fixture network token")
        c["admission"]["instrument"] = dict(kind="perpetual", quote_currency="USDT", units=1)
    universe, report = build_universe(spec, data, load_policy())
    assert report["passed"] and len(universe["members"]) == 15


def test_cli_build_validate_roundtrip(tmp_path):
    import subprocess

    root = Path(__file__).resolve().parents[1]
    data = researched()
    snapshot_path = tmp_path / "snapshot.json"
    snapshot_path.write_text(json.dumps(data))
    spec_path = tmp_path / "spec.json"
    spec_path.write_text(json.dumps(dict(schema_version=1, market="us", profile="heavy")))
    result = subprocess.run(
        [
            sys.executable,
            str(root / "scripts/universe.py"),
            "build",
            "--spec",
            str(spec_path),
            "--snapshot",
            str(snapshot_path),
            "--output",
            str(tmp_path / "output"),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    receipt = json.loads(result.stdout)
    assert receipt["status"] == "complete" and receipt["unused_capacity"] == 5
    validated = subprocess.run(
        [
            sys.executable,
            str(root / "scripts/universe.py"),
            "validate",
            receipt["artifacts"]["universe"],
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert json.loads(validated.stdout)["stats"]["quality"]["status"] == "qualified"


def test_core_audit_includes_exported_reference_layer():
    data = researched()
    data["coverage_plan"]["references"] = [
        dict(
            id="vix",
            ticker="TVC:VIX",
            theme_code="10_A",
            kind="index",
            observes="Direct volatility index",
            evidence=evidence(),
        )
    ]
    heavy, _ = build(data)
    assert audit_core("###10_A_REFERENCE,TVC:VIX", heavy)["exact_retained"] == 1


def test_diff_exposes_economic_plan_changes():
    from universe_core import diff_universes

    heavy, _ = build()
    data = researched()
    data["coverage_plan"]["scope"] += "; clarified scope"
    revised, _ = build(data)
    result = diff_universes(heavy, revised)
    assert not result["identical"] and result["coverage_plan"]["changed"]
    assert not result["added"] and not result["removed"]


@pytest.mark.parametrize("field,value", [("budgets", []), ("roster", None)])
def test_malformed_plan_returns_actionable_contract_error(field, value):
    data = researched()
    data["coverage_plan"][field] = value
    with pytest.raises(UniverseError, match="coverage:"):
        build(data)
