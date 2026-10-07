"""Recovery must preserve gates, prior artifacts and exact attempt inputs."""

import json
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from build_run import run_build  # noqa: E402
from test_universe_core import candidate, small_policy, snapshot, spec  # noqa: E402


def write(path, data):
    path.write_text(json.dumps(data))
    return str(path)


def start(tmp_path, data=None, profile="heavy"):
    build_spec = dict(
        spec(profile), target_count=4 if profile == "heavy" else 5, allow_outside_guidance=True
    )
    return dict(
        spec=write(tmp_path / "spec.json", build_spec),
        snapshot=write(tmp_path / "snapshot.json", data or snapshot()),
        policy=write(tmp_path / "policy.json", small_policy()),
        output=str(tmp_path / "output"),
    )


def resume(result, **changes):
    return run_build(
        spec=None,
        snapshot=None,
        output=None,
        resume=str(Path(result["checkpoint"]).parent),
        **changes,
    )


def test_missing_theme_repair_and_unchanged_retry(tmp_path):
    data = snapshot()
    data["candidates"].pop()
    args = start(tmp_path, data)
    first, code = run_build(**args)
    assert code == 2 and first["status"] == "needs_research"
    assert first["diagnostics"]["stages"]["heavy"]["missing_themes"] == ["12_A"]
    assert not Path(args["output"]).exists()
    again, code = resume(first)
    assert code == 2 and again["number"] == 1 and again["retry_skipped"]
    write(Path(args["snapshot"]), snapshot())
    repaired, code = resume(first)
    assert code == 0 and repaired["number"] == 2
    archive = json.loads(Path(first["inputs_archive"]).read_text())
    assert len(archive["snapshot"]["candidates"]) == 3
    state = json.loads(Path(first["checkpoint"]).read_text())
    assert [a["status"] for a in state["attempts"]] == ["needs_research", "complete"]


def test_partial_can_resume_without_overwriting_valid_subset(tmp_path):
    args = start(tmp_path, profile="max")
    first, code = run_build(**args)
    assert code == 3 and first["shortfall"] > 0
    old_path = Path(first["artifacts"]["universe"])
    old_bytes = old_path.read_bytes()
    report = Path(first["artifacts"]["reports"]["en"]).read_text()
    assert "PARTIAL:" in report
    data = snapshot()
    data["candidates"].append(candidate("BINANCE:AVAXUSDT.P", "AVAX", "12_A", "BETA_SATELLITE"))
    write(Path(args["snapshot"]), data)
    final, code = resume(first)
    assert code == 0 and final["filled"] == final["target"]
    assert old_path.read_bytes() == old_bytes
    assert final["artifacts"]["universe"] != str(old_path)


def test_invalid_facts_still_fail_after_resume(tmp_path):
    args = start(tmp_path)
    first, _ = run_build(**args)
    data = snapshot()
    del data["candidates"][0]["listing"]
    write(Path(args["snapshot"]), data)
    invalid, code = resume(first)
    assert code == 2 and not invalid["validation_passed"]
    assert "artifacts" not in invalid


def test_success_is_idempotent(tmp_path):
    first, code = run_build(**start(tmp_path))
    assert code == 0
    second, code = resume(first)
    assert code == 0 and second["number"] == 1
    assert second["artifacts"] == first["artifacts"]


def test_seeded_expansion_reports_zero_then_researched_additions(tmp_path):
    args = start(tmp_path)
    heavy, code = run_build(**args)
    assert code == 0
    write(Path(args["spec"]), dict(spec("max"), target_count=5, allow_outside_guidance=True))
    args.update(seed=heavy["artifacts"]["universe"], output=str(tmp_path / "max"))
    first, code = run_build(**args)
    assert code == 3
    assert first["expansion"] == {
        "from_profile": "heavy", "seed_members": 4, "retained": 4, "added": 0, "removed": 0,
    }
    assert "not the whole market" in first["diagnostics"]["note"]
    data = snapshot()
    data["candidates"].append(candidate("BINANCE:AVAXUSDT.P", "AVAX", "12_A", "BETA_SATELLITE"))
    write(Path(args["snapshot"]), data)
    final, code = resume(first)
    assert code == 0 and final["filled"] == 5
    assert final["expansion"] == dict(first["expansion"], added=1)


def test_narrowing_reports_removed_members(tmp_path):
    args = start(tmp_path)
    heavy, _ = run_build(**args)
    write(Path(args["spec"]), dict(spec("light"), target_count=2, allow_outside_guidance=True))
    final, code = run_build(
        **dict(args, seed=heavy["artifacts"]["universe"], output=str(tmp_path / "light"))
    )
    assert code == 0
    assert final["expansion"] == {
        "from_profile": "heavy", "seed_members": 4, "retained": 2, "added": 0, "removed": 2,
    }


def test_output_conflict_can_use_new_destination(tmp_path):
    args = start(tmp_path)
    dest = Path(args["output"])
    dest.mkdir()
    (dest / "keep.txt").write_text("user data")
    first, code = run_build(**args)
    assert code == 2
    final, code = run_build(
        spec=None,
        snapshot=None,
        output=str(tmp_path / "new-output"),
        resume=str(Path(first["checkpoint"]).parent),
    )
    assert code == 0
    assert (dest / "keep.txt").read_text() == "user data"
    assert final["number"] == 2


def test_interrupted_attempt_can_retry_same_inputs(tmp_path):
    args = start(tmp_path)
    with patch("build_run.build_universe", side_effect=KeyboardInterrupt):
        with pytest.raises(KeyboardInterrupt):
            run_build(**args)
    state_path = Path(args["output"] + ".run/run.json")
    state = json.loads(state_path.read_text())
    assert state["status"] == "running"
    final, code = resume({"checkpoint": str(state_path)})
    assert code == 0 and final["number"] == 2


def coverage_gap_args(tmp_path, beta_count=5):
    from test_coverage_core import expansion_fixture, build
    data = expansion_fixture()
    heavy, _ = build(data, target_count=20)
    data['candidates'] = [c for c in data['candidates']
                          if c['admission']['kind'] != 'satellite'
                          or c['asset_id'] in {f'BETA{i}' for i in range(beta_count)}]
    return dict(spec=write(tmp_path/'spec.json', dict(schema_version=1, market='us', profile='max')),
                snapshot=write(tmp_path/'snapshot.json', data),
                seed=write(tmp_path/'heavy.json', heavy), output=str(tmp_path/'out'))


def test_small_max_gap_delivers_partial_and_can_retry_to_complete(tmp_path):
    from universe_core import validate_universe
    from test_coverage_core import expansion_fixture
    args = coverage_gap_args(tmp_path)
    first, code = run_build(**args)
    assert code == 3 and first['status'] == 'partial' and first['shortfall'] == 1
    assert first['validation_passed'] and not first['qualified']
    assert first['handler']['action'] == 'deliver'
    assert first['diagnostics']['recovery']['cause'] == 'candidate_supply'
    assert first['diagnostics']['recovery']['price_diagnostics']['beta_strength']['required'] is False
    path = Path(first['artifacts']['universe']);before = path.read_bytes()
    assert '-partial.json' in path.name
    u = json.loads(before)
    assert u['delivery']['required_entities'] == 26
    checked = validate_universe(u)
    assert checked['passed'] and not checked['qualified']
    report = Path(first['artifacts']['reports']['en']).read_text()
    assert 'PARTIAL: 25 / 26' in report and '25.0%' in report
    assert '-partial.txt' in first['artifacts']['watchlist']
    again, code = resume(first)
    assert code == 3 and again['retry_skipped'] and again['artifacts'] == first['artifacts']
    strict, code = resume(first, shortfall_action='retry')
    assert code == 2 and strict['handler']['action'] == 'retry' and 'artifacts' not in strict
    write(Path(args['snapshot']), expansion_fixture())
    repaired, code = resume(strict)
    assert code == 0 and repaired['status'] == 'complete' and repaired['filled'] == 26
    assert path.read_bytes() == before
    assert '-partial' not in Path(repaired['artifacts']['universe']).name


def test_large_max_gap_and_invalid_facts_cannot_be_delivered(tmp_path):
    args = coverage_gap_args(tmp_path, beta_count=4)
    result, code = run_build(**args, shortfall_action='deliver')
    assert code == 2 and result['handler']['action'] == 'retry'
    assert 'artifacts' not in result
    data = json.loads(Path(args['snapshot']).read_text())
    del data['candidates'][0]['listing']
    write(Path(args['snapshot']), data)
    again, code = resume(result)
    assert code == 2 and 'artifacts' not in again
    assert 'listing' in again['error']
