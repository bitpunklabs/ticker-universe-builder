"""Reviewed presentation layouts for qualified Global/Core; no membership changes."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

import global_core as full
import global_core_view as core
from coverage_core import need
from universe_core import UniverseError, _write_atomic, read_json
from watchlist_core import check_watchlist, render_watchlist


def render(composition, layout, universe_sha256):
    """Require a complete, exact-once presentation assignment bound to original JSON bytes."""
    need(isinstance(layout, dict) and set(layout) == {
        "schema_version", "kind", "universe_sha256", "sections"
    }, "layout: unexpected or missing fields")
    need(type(layout["schema_version"]) is int and layout["schema_version"] == 1
         and layout["kind"] == "global_watchlist_layout", "layout: unsupported schema/kind")
    need(layout["universe_sha256"] == universe_sha256, "layout: universe hash changed")
    sections = layout["sections"]
    need(isinstance(sections, list) and sections, "layout: nonempty sections required")
    rows, groups, ids = [], [], set()
    for section in sections:
        need(isinstance(section, dict) and set(section) == {"id", "name", "tickers"},
             "layout section: expected id, name and tickers")
        code, name, tickers = section["id"], section["name"], section["tickers"]
        need(isinstance(code, str) and full.SAFE_ID.fullmatch(code), "layout: unsafe section id")
        need(code not in ids, "layout: duplicate section id")
        ids.add(code)
        need(isinstance(name, str) and name and name == name.strip(),
             "layout: nonempty section name required")
        need(isinstance(tickers, list) and tickers and all(isinstance(t, str) for t in tickers),
             "layout: each section needs ticker strings")
        groups.append({"id": code, "name": name})
        rows.extend({"ticker": ticker, "section": code} for ticker in tickers)
    need(Counter(row["ticker"] for row in rows)
         == Counter(row["ticker"] for row in composition["members"]),
         "layout: must assign every member exactly once, without additions")
    return render_watchlist(rows, groups, "section")


def checked_view(universe_path, contract_path, layout_path, policy=None):
    path = Path(universe_path)
    composition = read_json(path)
    validator = {"global_composition": full.validate,
                 "global_core_composition": core.validate}.get(composition.get("kind"))
    need(validator is not None, "layout: qualified Global or Global Core required")
    checked = validator(path, contract_path, policy)
    need(checked["passed"] and checked.get("qualified"),
         "layout: source validation failed: " + "; ".join(checked.get("errors", [])))
    text = render(composition, read_json(layout_path), full.file_hash(path))
    return text, {
        **check_watchlist(text),
        "qualified": True,
        "universe_sha256": full.file_hash(path),
        "contract_sha256": full.file_hash(Path(contract_path)),
        "layout_sha256": full.file_hash(Path(layout_path)),
        "source_cutoffs": composition["source_cutoffs"],
        "warnings": checked["warnings"],
    }


def export(universe_path, contract_path, layout_path, output, policy=None):
    text, checked = checked_view(universe_path, contract_path, layout_path, policy)
    stem = Path(universe_path).stem + "-by-observation"
    files = {
        stem + ".txt": text,
        "layout.json": Path(layout_path).read_bytes().decode("utf-8"),
        stem + ".validation.json": json.dumps(checked, ensure_ascii=False, indent=2) + "\n",
    }
    destination = _write_atomic(output, files)
    return {"status": "complete", "validation_passed": True, "artifacts": {
        "watchlist": str(destination / (stem + ".txt")),
        "layout": str(destination / "layout.json"),
        "validation": str(destination / (stem + ".validation.json")),
    }, "artifact_sha256": {name: full.file_hash(destination / name) for name in files}}


def validate(watchlist_path, universe_path, contract_path, layout_path, policy=None):
    try:
        path = Path(watchlist_path)
        need(path.suffix == ".txt", "layout: .txt watchlist required")
        text, checked = checked_view(universe_path, contract_path, layout_path, policy)
        need(path.read_bytes() == text.encode("utf-8"),
             "layout: published TXT differs from exact reviewed layout")
        return checked
    except (UniverseError, OSError, ValueError, TypeError, KeyError, AttributeError) as exc:
        return {"passed": False, "qualified": False, "errors": [str(exc)], "warnings": []}
