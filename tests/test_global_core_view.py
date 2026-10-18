"""Synthetic failure probes for reviewed Global-to-Core derivation, not market research."""

import json
import shutil
import subprocess
import sys
from copy import deepcopy
from pathlib import Path

import pytest
from test_global_core import ev, with_fund, write_inputs

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import global_core as full  # noqa: E402
import global_core_view as core  # noqa: E402
from universe_core import UniverseError  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]


def inputs(tmp_path):
    spec, contract, sources = with_fund()
    spec_path, contract_path = write_inputs(tmp_path / "inputs", spec, contract, sources)
    receipt = full.compose(spec_path, contract_path, tmp_path / "parent")
    parent_path = Path(receipt["artifacts"]["universe"])
    review = dict(
        schema_version=1,
        kind="global_core_review",
        parent_sha256=full.file_hash(parent_path),
        parent_contract_sha256=full.file_hash(contract_path),
        scope="Synthetic Core review; all parent duties retained",
        protected_tickers=["SP:FIX"],
        decisions=[
            dict(
                ticker=r["ticker"],
                action="omit" if r["ticker"] == "AMEX:FIXETF" else "retain",
                reason="Synthetic reviewed priority",
                evidence=ev(),
                covered_by=["NYSE:CORE6"] if r["ticker"] == "AMEX:FIXETF" else [],
            )
            for r in spec["selections"]
        ],
        theme_reviews=[
            dict(id=t["id"], emphasis="leaders", reason="Synthetic theme review", evidence=ev())
            for t in contract["themes"]
        ],
    )
    review_path = tmp_path / "review.json"
    review_path.write_text(json.dumps(review))
    return parent_path, contract_path, review_path, review


def test_portable_core_revalidates_parent_and_preserves_original_rows(tmp_path):
    parent, contract, review_path, review = inputs(tmp_path)
    before = {p.name: p.read_bytes() for p in parent.parent.iterdir()}
    result = core.compose(parent, contract, review_path, tmp_path / "core")
    path = Path(result["artifacts"]["universe"])
    stored = json.loads(path.read_text())
    assert stored["members"] == json.loads(parent.read_text())["members"][:3]
    checked = core.validate(path, review_path)
    assert checked["qualified"] and checked["symbols"] == 3
    assert checked["parent_symbols"] == 4 and checked["omitted_symbols"] == 1
    assert checked["duties"] == 4 and checked["parent_coverage_preserved"]
    assert before == {p.name: p.read_bytes() for p in parent.parent.iterdir()}
    assert "Global Core" in path.with_suffix(".en.html").read_text()
    shutil.move(path.parent, tmp_path / "relocated")
    shutil.rmtree(parent.parent)
    shutil.rmtree(tmp_path / "inputs")
    review_path.unlink()
    relocated = tmp_path / "relocated" / path.name
    result = subprocess.run(
        [
            sys.executable,
            "scripts/universe.py",
            "validate-global-core",
            str(relocated),
            "--contract",
            str(relocated.parent / core.CORE_CONTRACT),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert json.loads(result.stdout)["strict_subset_verified"]
    assert review == json.loads((relocated.parent / core.CORE_CONTRACT).read_text())


@pytest.mark.parametrize(
    "mutation,match",
    [
        (lambda r: r["decisions"].pop(), "every parent ticker"),
        (lambda r: r["decisions"].append(deepcopy(r["decisions"][0])), "duplicate Core decisions"),
        (lambda r: r["decisions"][-1].update(ticker="NYSE:INVENTED"), "every parent ticker"),
        (lambda r: r["decisions"][-1].update(covered_by=[]), "retained coverage targets"),
        (lambda r: r["decisions"][-1].update(covered_by=["NYSE:CORE0"]), "lose declared"),
        (lambda r: r["decisions"][-1].update(action="retain", covered_by=[]), "strict subset"),
        (lambda r: r["protected_tickers"].append("AMEX:FIXETF"), "protected/parent-required"),
        (lambda r: r["theme_reviews"].pop(), "every original Global theme"),
        (lambda r: r["theme_reviews"][0].update(reason=""), "observation emphasis"),
        (lambda r: r["decisions"][0]["evidence"][0].update(as_of="2027-01-01"), "180 days"),
        (lambda r: r.update(parent_sha256="0" * 64), "parent bytes changed"),
        (lambda r: r.update(parent_contract_sha256="0" * 64), "contract bytes changed"),
        (lambda r: r.update(schema_version=True), "invalid Global Core review"),
    ],
)
def test_incomplete_or_unjustified_reviews_do_not_publish(tmp_path, mutation, match):
    parent, contract, review_path, review = inputs(tmp_path)
    mutation(review)
    review_path.write_text(json.dumps(review))
    with pytest.raises(UniverseError, match=match):
        core.compose(parent, contract, review_path, tmp_path / "core")
    assert not (tmp_path / "core").exists()


@pytest.mark.parametrize(
    "tamper",
    [
        "parent",
        "parent_txt",
        "source",
        "member",
        "path",
        "coverage",
        "review",
        "txt",
        "expected_review",
    ],
)
def test_standalone_core_rejects_parent_and_core_tampering(tmp_path, tamper):
    parent, contract, review_path, review = inputs(tmp_path)
    receipt = core.compose(parent, contract, review_path, tmp_path / "core")
    path = Path(receipt["artifacts"]["universe"])
    stored = json.loads(path.read_text())
    if tamper == "parent":
        (path.parent / core.PARENT_FILE).write_text("{}")
    elif tamper == "parent_txt":
        (path.parent / "parent-global.txt").write_text("NYSE:CORE0\n")
    elif tamper == "source":
        (path.parent / "source-us.json").write_text("{}")
    elif tamper == "member":
        stored["members"][0]["name"] = "Promoted or substituted company"
    elif tamper == "path":
        stored["parent"]["file"] = "../parent/parent-global.json"
    elif tamper == "coverage":
        reduced = json.loads((path.parent / "global-contract.json").read_text())
        reduced["duties"].pop()
        (path.parent / "global-contract.json").write_text(json.dumps(reduced))
    elif tamper == "review":
        review["decisions"][0]["reason"] = "Changed after review"
        (path.parent / core.CORE_CONTRACT).write_text(json.dumps(review))
    elif tamper == "txt":
        path.with_suffix(".txt").write_text("NYSE:CORE0\n")
    else:
        review["decisions"][0]["reason"] = "Changed independent denominator"
        review_path.write_text(json.dumps(review))
    stored["content_sha256"] = full.digest(
        {k: v for k, v in stored.items() if k != "content_sha256"}
    )
    path.write_text(json.dumps(stored))
    assert not core.validate(path, review_path)["passed"]


def test_parent_required_ticker_and_qualified_source_cannot_be_bypassed(tmp_path):
    parent, contract, review_path, review = inputs(tmp_path)
    parent_contract = json.loads(contract.read_text())
    parent_contract["required_tickers"] = ["AMEX:FIXETF"]
    parent_data = json.loads(parent.read_text())
    sources, _ = full._load_sources(parent_data["spec"], parent.parent)
    review["protected_tickers"].append("AMEX:FIXETF")
    with pytest.raises(UniverseError, match="protected/parent-required"):
        core.derive(parent_data, parent_contract, review, sources)
    # Re-hashing a changed native source does not make the parent independently qualified.
    (parent.parent / "source-us.json").write_text("{}")
    with pytest.raises(UniverseError, match="independently qualify"):
        core.compose(parent, contract, review_path, tmp_path / "core")


def test_core_output_collision_preserves_existing_bundle(tmp_path):
    parent, contract, review_path, _ = inputs(tmp_path)
    core.compose(parent, contract, review_path, tmp_path / "core")
    before = {p.name: p.read_bytes() for p in (tmp_path / "core").iterdir()}
    with pytest.raises(UniverseError, match="not empty"):
        core.compose(parent, contract, review_path, tmp_path / "core")
    assert before == {p.name: p.read_bytes() for p in (tmp_path / "core").iterdir()}


def test_basket_substitution_requires_the_reviewed_issuer_in_actual_holdings(tmp_path):
    spec, contract, sources = with_fund()
    # This synthetic contract deliberately permits the retained basket for the technology duty.
    contract["duties"][2]["leader_minimum"] = 0
    spec_path, contract_path = write_inputs(tmp_path / "inputs", spec, contract, sources)
    receipt = full.compose(spec_path, contract_path, tmp_path / "parent")
    parent_path = Path(receipt["artifacts"]["universe"])
    parent = json.loads(parent_path.read_text())
    review = dict(
        schema_version=1,
        kind="global_core_review",
        parent_sha256=full.file_hash(parent_path),
        parent_contract_sha256=full.file_hash(contract_path),
        scope="Synthetic basket exposure proof",
        protected_tickers=["SP:FIX"],
        decisions=[
            dict(
                ticker=r["ticker"],
                action="omit" if r["ticker"] == "NYSE:CORE6" else "retain",
                reason="Synthetic observation review",
                evidence=ev(),
                covered_by=["AMEX:FIXETF"] if r["ticker"] == "NYSE:CORE6" else [],
            )
            for r in parent["members"]
        ],
        theme_reviews=[
            dict(id=t["id"], emphasis="mixed", reason="Synthetic scope", evidence=ev())
            for t in contract["themes"]
        ],
        basket_exposures=[
            dict(
                ticker="NYSE:CORE6",
                fund="AMEX:FIXETF",
                holding_entity_id="TECH",
                reason="Reviewed synthetic issuer",
                evidence=ev(),
            )
        ],
    )
    value, _ = core.derive(parent, contract, review, sources)
    assert value["basket_exposures"][0]["weight"] == 0.5
    review["basket_exposures"][0]["holding_entity_id"] = "ABSENT_ISSUER"
    with pytest.raises(UniverseError, match="absent from parent holdings"):
        core.derive(parent, contract, review, sources)


def focused_inputs(tmp_path):
    spec, contract, sources = with_fund()
    contract["duties"].append(dict(
        id="TECH_DETAIL", dimension="theme", group="TECH", purpose="Synthetic optional depth",
        allowed_kinds=["equity", "etf"], minimum=1,
    ))
    for row in spec["selections"]:
        if row["theme"] == "TECH":
            row["duties"].append("TECH_DETAIL")
    sp, cp = write_inputs(tmp_path / "inputs", spec, contract, sources)
    receipt = full.compose(sp, cp, tmp_path / "parent")
    pp = Path(receipt["artifacts"]["universe"])
    review = dict(
        schema_version=1, kind="global_core_review", scope="Synthetic focused Core",
        parent_sha256=full.file_hash(pp), parent_contract_sha256=full.file_hash(cp),
        protected_tickers=["SP:FIX"],
        decisions=[dict(
            ticker=r["ticker"], action="omit" if r["ticker"] == "AMEX:FIXETF" else "retain",
            reason="Synthetic Core priority", evidence=ev(),
            covered_by=["NYSE:CORE6"] if r["ticker"] == "AMEX:FIXETF" else [],
        ) for r in spec["selections"]],
        theme_reviews=[dict(
            id=t["id"], emphasis="leaders", reason="Synthetic reviewed theme", evidence=ev(),
        ) for t in contract["themes"]],
        coverage_decisions=[dict(
            id=d["id"], action="full_only" if d["id"] == "TECH_DETAIL" else "retain",
            reason="Retain the theme leader; detailed function remains in qualified Global.",
            evidence=ev(),
        ) for d in contract["duties"]],
    )
    rp = tmp_path / "review.json"
    rp.write_text(json.dumps(review))
    return pp, cp, rp, review


def test_focused_scope_is_explicit_and_keeps_parent_facts_and_groups(tmp_path):
    pp, cp, rp, _ = focused_inputs(tmp_path)
    receipt = core.compose(pp, cp, rp, tmp_path / "focused")
    path = Path(receipt["artifacts"]["universe"])
    stored = json.loads(path.read_text())
    checked = core.validate(path, rp)
    assert checked["qualified"] and not checked["parent_coverage_preserved"]
    assert checked["parent_markets_and_themes_preserved"]
    assert checked["parent_duties"] == 5 and checked["duties"] == 4
    assert checked["full_only_duties"] == ["TECH_DETAIL"]
    parent = json.loads(pp.read_text())
    before = {r["ticker"]: r for r in parent["members"]}
    for row in stored["members"]:
        expected = deepcopy(before[row["ticker"]])
        expected["duties"] = [d for d in expected["duties"] if d != "TECH_DETAIL"]
        assert row == expected
    assert "TECH_DETAIL" in parent["coverage"]
    derived = json.loads((path.parent / "global-contract.json").read_text())
    original = json.loads(cp.read_text())
    for key in ("markets", "themes", "required_tickers", "etf_rules"):
        assert derived.get(key) == original.get(key)
    assert "TECH_DETAIL" in path.with_suffix(".en.html").read_text()
    shutil.move(path.parent, tmp_path / "moved")
    shutil.rmtree(pp.parent)
    shutil.rmtree(tmp_path / "inputs")
    moved = tmp_path / "moved" / path.name
    assert core.validate(moved, moved.parent / core.CORE_CONTRACT)["qualified"]


@pytest.mark.parametrize("key", ["US_BROAD", "BANK", "TECH", "GAUGE"])
def test_focused_scope_cannot_retire_market_leader_or_index_duties(tmp_path, key):
    pp, cp, rp, review = focused_inputs(tmp_path)
    next(r for r in review["coverage_decisions"] if r["id"] == key)["action"] = "full_only"
    rp.write_text(json.dumps(review))
    with pytest.raises(UniverseError, match="cannot become full-only"):
        core.compose(pp, cp, rp, tmp_path / "core")
    assert not (tmp_path / "core").exists()


@pytest.mark.parametrize("mutation,match", [
    (lambda r: r["coverage_decisions"].pop(), "every parent duty"),
    (lambda r: r["coverage_decisions"].append(r["coverage_decisions"][0]), "duplicate"),
    (lambda r: r["coverage_decisions"][-1].update(action="waive"), "resolved action"),
    (lambda r: r["coverage_decisions"][-1].update(reason=""), "resolved action"),
    (lambda r: r["coverage_decisions"][-1].update(evidence=[]), "evidence"),
    (lambda r: r["coverage_decisions"][-1].update(action="retain"), "explicit full-only"),
    (lambda r: r.update(coverage_decisions=None), "must be a list"),
])
def test_focused_scope_needs_a_complete_evidenced_resolved_ledger(tmp_path, mutation, match):
    pp, cp, rp, review = focused_inputs(tmp_path)
    mutation(review)
    rp.write_text(json.dumps(review))
    with pytest.raises(UniverseError, match=match):
        core.compose(pp, cp, rp, tmp_path / "core")


def test_focused_scope_cannot_erase_an_entire_theme(tmp_path):
    pp, cp, _, review = focused_inputs(tmp_path)
    parent, original = json.loads(pp.read_text()), json.loads(cp.read_text())
    # Even a basket-only theme must retain an original duty; no empty category is permitted.
    next(d for d in original["duties"] if d["id"] == "TECH")["leader_minimum"] = 0
    next(d for d in review["coverage_decisions"] if d["id"] == "TECH")["action"] = "full_only"
    sources, _ = full._load_sources(parent["spec"], pp.parent)
    with pytest.raises(UniverseError, match="erase an original theme"):
        core.derive(parent, original, review, sources)


@pytest.mark.parametrize("tamper", ["member_claim", "derived_minimum", "scope_ledger"])
def test_focused_review_does_not_permit_unreviewed_changes(tmp_path, tamper):
    pp, cp, rp, _ = focused_inputs(tmp_path)
    receipt = core.compose(pp, cp, rp, tmp_path / "core")
    path = Path(receipt["artifacts"]["universe"])
    stored = json.loads(path.read_text())
    if tamper == "member_claim":
        stored["members"][0]["duties"] = []
    elif tamper == "derived_minimum":
        derived_path = path.parent / "global-contract.json"
        derived = json.loads(derived_path.read_text())
        derived["duties"][0]["minimum"] = 0
        derived_path.write_text(json.dumps(derived))
    else:
        stored["coverage_scope"]["full_only"].append("BANK")
    stored["content_sha256"] = full.digest(
        {k: v for k, v in stored.items() if k != "content_sha256"}
    )
    path.write_text(json.dumps(stored))
    assert not core.validate(path, rp)["passed"]


@pytest.mark.parametrize("kind", ["index", "yield", "commodity", "perpetual", "spot"])
def test_context_and_protocol_functions_cannot_be_retired_in_focused_scope(tmp_path, kind):
    _, cp, _, review = focused_inputs(tmp_path)
    contract = json.loads(cp.read_text())
    contract["duties"][-1]["allowed_kinds"] = [kind]
    with pytest.raises(UniverseError, match="cannot become full-only"):
        core.coverage_scope(contract, review, "2026-09-09")
