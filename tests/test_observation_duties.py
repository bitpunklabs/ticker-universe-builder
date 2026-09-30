"""Economic coverage must survive selection and maintenance, not just a section header."""

import sys
from copy import deepcopy
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from build_run import diagnostics  # noqa: E402
from test_universe_core import (  # noqa: E402
    candidate,
    change_set,
    evidence,
    small_policy,
    snapshot,
    spec,
)
from universe_core import (  # noqa: E402
    MARKETS,
    UniverseError,
    apply_change_set,
    build_universe,
    content_hash,
    normalize_taxonomy,
    render_markdown,
    starter_taxonomy,
    universe_hash,
    validate_universe,
)


def researched():
    raw = snapshot()
    for theme in raw["taxonomy"]:
        if theme["theme_code"] in {"00_A", "10_A"}:
            theme.update(
                purpose="Observe the declared structural function.",
                representative_roles=["BENCHMARK", "THEME_LEADER"],
            )
    return raw


def test_satellite_presence_cannot_replace_a_core_duty():
    raw = researched()
    raw["candidates"][1]["role"] = "BREADTH_PROXY"
    with pytest.raises(UniverseError, match="no qualified representative.*10_A"):
        build_universe(spec(), raw, small_policy())
    assert diagnostics(spec(), raw, small_policy())["stages"]["light"]["unrepresented_duties"] == [
        "10_A"
    ]


def test_seed_satellite_does_not_hide_a_new_representative_requirement():
    raw = snapshot()
    raw["candidates"][1]["role"] = "BREADTH_PROXY"
    seed, _ = build_universe(spec(), raw, small_policy())
    for theme in raw["taxonomy"][:2]:
        theme.update(
            purpose="Retain the market and business duty.",
            representative_roles=["BENCHMARK", "THEME_LEADER"],
        )
    raw["candidates"].append(candidate("BINANCE:ETHUSDT.P", "ETH", "10_A", "THEME_LEADER"))
    policy = small_policy()
    policy["tiers"]["medium"] = 4
    built, report = build_universe(spec("medium"), raw, policy, seed)
    assert {"BTC", "SOL", "ETH", "LINK"} == {c["asset_id"] for c in built["members"]}
    assert report["stats"]["duties"]["represented"] == 2


def test_validator_rechecks_roles_even_when_hashes_are_recomputed():
    built, _ = build_universe(spec(), researched(), small_policy())
    built["members"][1]["role"] = "BREADTH_PROXY"
    built["version_hash"] = universe_hash(built)
    built["content_hash"] = content_hash(built)
    assert (
        "unrepresented observation duty: 10_A" in validate_universe(built, small_policy())["errors"]
    )


def test_removal_leaving_satellites_still_fails():
    raw = researched()
    raw["candidates"].append(candidate("BINANCE:ETHUSDT.P", "ETH", "10_A", "BREADTH_PROXY"))
    policy = small_policy()
    policy["tiers"]["light"] = 3
    built, _ = build_universe(spec(), raw, policy)
    changes = change_set(
        built,
        [
            {
                "op": "REMOVE",
                "ticker": "BINANCE:SOLUSDT.P",
                "reason": "Test loss of a structural duty.",
                "evidence": evidence(),
            }
        ],
        review_depth="deep",
    )
    with pytest.raises(UniverseError, match="unrepresented observation duty: 10_A"):
        apply_change_set(built, changes, policy)


@pytest.mark.parametrize("roles", [[], ["BREADTH_PROXY"], ["UNKNOWN"], "ANCHOR", [True]])
def test_empty_or_noncore_representative_contract_is_rejected(roles):
    themes = researched()["taxonomy"]
    themes[0]["representative_roles"] = roles
    with pytest.raises(UniverseError, match="representative_roles"):
        normalize_taxonomy(themes)


def test_duties_are_hashed_rendered_and_legacy_is_explicit():
    built, report = build_universe(spec(), researched(), small_policy())
    assert "Observe the declared structural function." in render_markdown(built, report)
    changed = deepcopy(built)
    changed["taxonomy"][0]["purpose"] = "A different duty."
    assert universe_hash(changed) != built["version_hash"]
    _, legacy = build_universe(spec(), snapshot(), small_policy())
    assert legacy["stats"]["duties"]["undeclared"] == ["00_A", "10_A"]


def test_every_reviewed_market_starter_declares_duties():
    for market in MARKETS:
        for theme in starter_taxonomy(market):
            assert theme["purpose"] and theme["representative_roles"], (market, theme)


def test_replacement_needs_a_successor_for_the_same_duty():
    policy = small_policy()
    # Isolate successor coverage from the production turnover cap on this two-member fixture.
    policy["maintenance"]["deep"]["turnover_warning"] = 0.5
    built, _ = build_universe(spec(), researched(), policy)
    successor = candidate("BINANCE:ETHUSDT.P", "ETH", "10_A", "BREADTH_PROXY")
    op = {
        "op": "REPLACE",
        "ticker": "BINANCE:SOLUSDT.P",
        "candidate": successor,
        "reason": "Test replacing the last business representative.",
        "evidence": evidence(),
    }
    changes = change_set(built, [op], review_depth="deep")
    with pytest.raises(UniverseError, match="unrepresented observation duty: 10_A"):
        apply_change_set(built, changes, policy)
    successor["role"] = "THEME_LEADER"
    updated, report = apply_change_set(built, changes, policy)
    assert report["passed"] and any(c["asset_id"] == "ETH" for c in updated["members"])


def test_duty_updates_are_explicit_and_cannot_erase_the_requirement():
    built, _ = build_universe(spec(), researched(), small_policy())
    op = {
        "op": "UPDATE_THEME",
        "theme": "10_A",
        "purpose": "Observe an updated business duty.",
        "reason": "Business research updated the observation purpose.",
        "evidence": evidence(),
    }
    updated, report = apply_change_set(built, change_set(built, [op]), small_policy())
    assert report["passed"]
    assert updated["taxonomy"][1]["purpose"] == op["purpose"]
    assert updated["taxonomy"][1]["representative_roles"] == ["BENCHMARK", "THEME_LEADER"]
    op["representative_roles"] = []
    with pytest.raises(UniverseError, match="representative_roles"):
        apply_change_set(built, change_set(built, [op]), small_policy())


def test_recovery_can_repair_facts_then_duties_without_losing_attempts(tmp_path):
    import json

    from build_run import run_build

    raw = researched()
    raw["candidates"][1]["role"] = "BREADTH_PROXY"
    raw["candidates"][1]["listing"]["as_of"] = "2026-01-01"
    paths = {name: tmp_path / (name + ".json") for name in ["spec", "snapshot", "policy"]}
    for name, value in [
        ("spec", dict(spec(), target_count=2, allow_outside_guidance=True)),
        ("snapshot", raw),
        ("policy", small_policy()),
    ]:
        paths[name].write_text(json.dumps(value))
    options = dict(
        spec=str(paths["spec"]),
        snapshot=str(paths["snapshot"]),
        policy=str(paths["policy"]),
        output=str(tmp_path / "output"),
        seed=None,
        language=None,
        run_dir=str(tmp_path / "run"),
        resume=None,
    )
    first, code = run_build(**options)
    assert code == 2 and first["number"] == 1
    options.update(
        spec=None,
        snapshot=None,
        policy=None,
        output=None,
        run_dir=None,
        resume=str(tmp_path / "run"),
    )
    unchanged, code = run_build(**options)
    assert code == 2 and unchanged["number"] == 1 and unchanged["retry_skipped"]
    raw["candidates"][1]["listing"]["as_of"] = "2026-09-09"
    paths["snapshot"].write_text(json.dumps(raw))
    second, code = run_build(**options)
    assert code == 2 and second["number"] == 2
    assert second["diagnostics"]["stages"]["light"]["unrepresented_duties"] == ["10_A"]
    raw["candidates"][1]["role"] = "THEME_LEADER"
    paths["snapshot"].write_text(json.dumps(raw))
    third, code = run_build(**options)
    assert code == 0 and third["number"] == 3
    state = json.loads(Path(third["checkpoint"]).read_text())
    assert [a["status"] for a in state["attempts"]] == [
        "needs_research",
        "needs_research",
        "complete",
    ]
