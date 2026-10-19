"""Presentation cannot change qualified membership or conceal failed source validation."""

import json
import subprocess
import sys
from copy import deepcopy
from pathlib import Path

import pytest
from test_global_core import fixture, write_inputs
from test_global_core_view import inputs

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import global_core as full  # noqa: E402
import global_core_view as core  # noqa: E402
import global_watchlist as view  # noqa: E402
from universe_core import UniverseError, parse_watchlist  # noqa: E402


def layout_for(path):
    members = json.loads(path.read_text())["members"]
    return dict(schema_version=1, kind="global_watchlist_layout",
                universe_sha256=full.file_hash(path), sections=[
                    dict(id="INDEX", name="CORE_INDICES",
                         tickers=[r["ticker"] for r in members if r["kind"] == "index"]),
                    dict(id="LEADERS", name="COMPANIES",
                         tickers=[r["ticker"] for r in members if r["kind"] != "index"]),
                ])


@pytest.fixture
def qualified(tmp_path):
    spec, contract, sources = fixture()
    spec_path, contract_path = write_inputs(tmp_path / "inputs", spec, contract, sources)
    receipt = full.compose(spec_path, contract_path, tmp_path / "global")
    path = Path(receipt["artifacts"]["universe"])
    return path, contract_path


def test_export_preserves_facts_and_exact_order_and_detects_txt_changes(qualified, tmp_path):
    path, contract = qualified
    original = {p.name: p.read_bytes() for p in path.parent.iterdir()}
    layout = tmp_path / "layout.json"
    layout.write_text(json.dumps(layout_for(path)))
    receipt = view.export(path, contract, layout, tmp_path / "view")
    txt = Path(receipt["artifacts"]["watchlist"])
    assert [name for name, _ in parse_watchlist(txt.read_text())] == [
        "INDEX_CORE_INDICES", "LEADERS_COMPANIES"]
    assert view.validate(txt, path, contract, layout)["qualified"]
    assert original == {p.name: p.read_bytes() for p in path.parent.iterdir()}
    # Same ticker set, different order is still a changed reviewed view.
    tokens = txt.read_text().strip().split(",")
    tokens[-1], tokens[-2] = tokens[-2], tokens[-1]
    txt.write_text(",".join(tokens) + "\n")
    assert not view.validate(txt, path, contract, layout)["passed"]


@pytest.mark.parametrize("mutation", ["missing", "extra", "duplicate", "empty", "unsafe",
                                    "same_id", "wrong_hash", "unknown_field", "schema_bool"])
def test_layout_rejects_membership_and_structure_errors(qualified, mutation):
    path, _ = qualified
    layout = layout_for(path)
    if mutation == "missing":
        layout["sections"][1]["tickers"].pop()
    elif mutation == "extra":
        layout["sections"][1]["tickers"].append("NYSE:UNKNOWN")
    elif mutation == "duplicate":
        layout["sections"][1]["tickers"].append(layout["sections"][0]["tickers"][0])
    elif mutation == "empty":
        layout["sections"].append(dict(id="EMPTY", name="EMPTY", tickers=[]))
    elif mutation == "unsafe":
        layout["sections"][0]["name"] = "BAD,HEADER"
    elif mutation == "same_id":
        layout["sections"][1]["id"] = layout["sections"][0]["id"]
    elif mutation == "wrong_hash":
        layout["universe_sha256"] = "0" * 64
    elif mutation == "unknown_field":
        layout["extra"] = "ignored?"
    else:
        layout["schema_version"] = True
    with pytest.raises(UniverseError):
        view.render(json.loads(path.read_text()), layout, full.file_hash(path))


def test_layout_cannot_bypass_broken_source_or_write_failed_export(qualified, tmp_path):
    path, contract = qualified
    layout = tmp_path / "layout.json"
    layout.write_text(json.dumps(layout_for(path)))
    # The presentation still matches the parent, but a source has been changed.
    source = next(path.parent.glob("source-*.json"))
    source.write_text(source.read_text() + " ")
    with pytest.raises(UniverseError, match="source validation failed"):
        view.export(path, contract, layout, tmp_path / "failed")
    assert not (tmp_path / "failed").exists()


def test_core_layout_requires_its_own_binding_and_cli_revalidates_parent(tmp_path):
    parent, contract, review_path, _ = inputs(tmp_path)
    receipt = core.compose(parent, contract, review_path, tmp_path / "core")
    path = Path(receipt["artifacts"]["universe"])
    bad = deepcopy(layout_for(parent))
    with pytest.raises(UniverseError, match="universe hash"):
        view.render(json.loads(path.read_text()), bad, full.file_hash(path))
    layout = tmp_path / "layout.json"
    layout.write_text(json.dumps(layout_for(path)))
    command = [sys.executable, "scripts/universe.py", "export-global-watchlist",
               "--universe", str(path), "--contract", str(review_path), "--layout", str(layout),
               "--output", str(tmp_path / "view")]
    result = subprocess.run(command, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    txt = json.loads(result.stdout)["artifacts"]["watchlist"]
    check = [sys.executable, "scripts/universe.py", "validate-global-watchlist", txt,
             "--universe", str(path), "--contract", str(review_path), "--layout", str(layout)]
    assert subprocess.run(check, capture_output=True).returncode == 0
    source = next(path.parent.glob("source-*.json"))
    source.write_text(source.read_text() + " ")
    result = subprocess.run(check, capture_output=True, text=True)
    assert result.returncode == 2
    assert not json.loads(result.stdout)["qualified"]
