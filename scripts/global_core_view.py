"""Reviewed, coverage-preserving Core subsets of independently qualified Global compositions."""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

import global_core as full
from coverage_core import evidence, keyed, need, sentence
from universe_core import UniverseError, _write_atomic, read_json

PARENT_FILE = "parent-global.json"
PARENT_CONTRACT = "parent-contract.json"
CORE_CONTRACT = "global-core-contract.json"


def derive(parent, parent_contract, review, sources, policy=None):
    """Apply a complete authored review; inherit the parent's entire coverage denominator."""
    full.fields(
        review,
        {
            "schema_version",
            "kind",
            "parent_sha256",
            "parent_contract_sha256",
            "scope",
            "protected_tickers",
            "decisions",
            "theme_reviews",
        },
        {"basket_exposures"},
        "Global Core review",
    )
    need(
        type(review["schema_version"]) is int
        and review["schema_version"] == 1
        and review["kind"] == "global_core_review",
        "invalid Global Core review",
    )
    need(parent["kind"] == "global_composition", "Core requires a full Global parent")
    need(sentence(review["scope"]), "Core scope required")
    rows = keyed(parent["members"], "ticker", "parent members")
    decisions = keyed(review["decisions"], "ticker", "Core decisions")
    need(set(decisions) == set(rows), "every parent ticker needs exactly one Core decision")
    retained = set()
    for ticker, decision in decisions.items():
        full.fields(
            decision,
            {"ticker", "action", "reason", "evidence", "covered_by"},
            set(),
            ticker + " Core decision",
        )
        need(
            decision["action"] in {"retain", "omit"} and sentence(decision["reason"]),
            ticker + ": resolved Core action and reason required",
        )
        evidence(decision["evidence"], ticker + " Core decision", parent["as_of"])
        targets = decision["covered_by"]
        need(
            isinstance(targets, list)
            and all(isinstance(t, str) for t in targets)
            and len(targets) == len(set(targets)),
            ticker + ": invalid surviving coverage",
        )
        if decision["action"] == "retain":
            need(not targets, ticker + ": retained ticker cannot name replacement coverage")
            if rows[ticker]["kind"] in {"equity", "spot", "perpetual"}:
                need(rows[ticker]["leader"], ticker + ": Core entities must be researched leaders")
            retained.add(ticker)
    need(0 < len(retained) < len(rows), "Core must be a nonempty strict subset of Global")
    protected = review["protected_tickers"]
    need(
        isinstance(protected, list)
        and all(isinstance(t, str) for t in protected)
        and len(protected) == len(set(protected))
        and set(parent_contract.get("required_tickers", [])) <= set(protected)
        and set(protected) <= retained,
        "protected/parent-required tickers must survive Core",
    )
    for ticker, decision in decisions.items():
        if decision["action"] == "omit":
            targets = decision["covered_by"]
            need(
                bool(targets) and set(targets) <= retained,
                ticker + ": omitted ticker needs retained coverage targets",
            )
            duties = {d for target in targets for d in rows[target]["duties"]}
            need(
                set(rows[ticker]["duties"]) <= duties,
                ticker + ": surviving targets lose declared observation duties",
            )
    themes = keyed(review["theme_reviews"], "id", "Core theme reviews")
    need(
        set(themes) == {t["id"] for t in parent_contract["themes"]},
        "every original Global theme needs a Core review",
    )
    for theme in themes.values():
        full.fields(theme, {"id", "emphasis", "reason", "evidence"}, set(), "Core theme review")
        need(
            theme["emphasis"] in {"leaders", "basket", "mixed", "gauge", "context"}
            and sentence(theme["reason"]),
            "Core theme needs observation emphasis and reason",
        )
        evidence(theme["evidence"], theme["id"] + " Core theme", parent["as_of"])

    exposures = keyed(review.get("basket_exposures", []), "ticker", "Core basket exposures")
    exposure_rows = []
    for ticker, item in exposures.items():
        full.fields(
            item,
            {"ticker", "fund", "holding_entity_id", "reason", "evidence"},
            set(),
            "Core basket exposure",
        )
        fund = item["fund"]
        need(
            ticker in decisions
            and decisions[ticker]["action"] == "omit"
            and rows[ticker]["kind"] == "equity"
            and fund in retained
            and fund in decisions[ticker]["covered_by"]
            and fund in parent["fund_reviews"],
            "basket exposure must bind an omitted company to its retained coverage fund",
        )
        weight = parent["fund_reviews"][fund]["holdings"].get(item["holding_entity_id"])
        need(
            weight is not None and weight > 0 and sentence(item["reason"]),
            ticker + ": evidenced basket holding identity absent from parent holdings",
        )
        evidence(item["evidence"], ticker + " basket identity", parent["as_of"])
        exposure_rows.append({**deepcopy(item), "weight": weight})

    spec = deepcopy(parent["spec"])
    spec["selections"] = [r for r in spec["selections"] if r["ticker"] in retained]
    if "coexistence_reviews" in spec:
        spec["coexistence_reviews"] = [
            r for r in spec["coexistence_reviews"] if set(r["pair"]) <= retained
        ]
    contract = deepcopy(parent_contract)
    contract["scope"] = review["scope"]
    lookups = {
        key: {
            r["ticker"]: r
            for r in source.get("members", [])
            + source.get("coverage_plan", {}).get("references", [])
        }
        for key, source in sources.items()
        if "taxonomy" in source
    }
    for lineage in contract["source_themes"]:
        source_id, code = lineage["id"].split(":", 1)
        mapped = sorted(
            {
                r["theme"]
                for r in spec["selections"]
                if r["source"] == source_id
                and lookups[source_id][r["ticker"]]["theme_code"] == code
            }
        )
        lineage.update(
            disposition="mapped" if mapped else "out_of_scope",
            themes=mapped,
            reason="Core retains representatives from this original native source theme."
            if mapped
            else "No Core representative from this native source slice; all Global "
            "duties remain mandatory. See the complete parent-ticker decision ledger.",
        )
    composition = full.evaluate(spec, contract, sources, policy)
    need(
        composition["members"] == [r for r in parent["members"] if r["ticker"] in retained],
        "Core cannot alter parent members, roles, identities or duties",
    )
    composition.update(
        kind="global_core_composition",
        review_sha256=full.digest(review),
        parent={
            "file": PARENT_FILE,
            "sha256": review["parent_sha256"],
            "contract_file": PARENT_CONTRACT,
            "contract_sha256": review["parent_contract_sha256"],
        },
        parent_symbols=len(rows),
        basket_exposures=exposure_rows,
    )
    return composition, contract


def _load_parent(path, contract_path, review, policy):
    path, contract_path = Path(path).resolve(), Path(contract_path).resolve()
    need(full.file_hash(path) == review["parent_sha256"], "pinned Global parent bytes changed")
    need(
        full.file_hash(contract_path) == review["parent_contract_sha256"],
        "pinned parent coverage contract bytes changed",
    )
    checked = full.validate(path, contract_path, policy)
    need(
        checked["passed"] and checked.get("qualified"),
        "Global parent must independently qualify: " + str(checked.get("errors")),
    )
    parent, parent_contract = read_json(path), read_json(contract_path)
    sources, texts = full._load_sources(parent["spec"], path.parent)
    return parent, parent_contract, sources, texts


def report(composition, contract):
    checked = full.report(composition, contract)
    checked.update(
        parent_symbols=composition["parent_symbols"],
        omitted_symbols=composition["parent_symbols"] - len(composition["members"]),
        strict_subset_verified=True,
        parent_coverage_preserved=True,
        basket_exposure_reviews=len(composition["basket_exposures"]),
        review_sha256=composition["review_sha256"],
    )
    return checked


def compose(parent_path, parent_contract_path, review_path, output, policy=None):
    parent_path, parent_contract_path = Path(parent_path), Path(parent_contract_path)
    review_path = Path(review_path)
    review = read_json(review_path)
    parent, parent_contract, sources, texts = _load_parent(
        parent_path, parent_contract_path, review, policy
    )
    composition, contract = derive(parent, parent_contract, review, sources, policy)
    composition["content_sha256"] = full.digest(composition)
    checked = report(composition, contract)
    stem = "global-core-" + composition["as_of"]

    def dump(value):
        return json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n"

    files = {
        stem + ".json": dump(composition),
        stem + ".validation.json": dump(checked),
        CORE_CONTRACT: review_path.read_bytes().decode("utf-8"),
        "global-contract.json": dump(contract),
        PARENT_FILE: parent_path.read_bytes().decode("utf-8"),
        PARENT_CONTRACT: parent_contract_path.read_bytes().decode("utf-8"),
    }
    suffixes = {"watchlist": "", "by_theme": "-by-theme", "by_market": "-by-market"}
    for key, text in full.exports(composition, contract).items():
        files[stem + suffixes[key] + ".txt"] = text
    for suffix in suffixes.values():
        files["parent-global" + suffix + ".txt"] = (
            (parent_path.parent / (parent_path.stem + suffix + ".txt")).read_bytes().decode("utf-8")
        )
    files[stem + ".en.md"], files[stem + ".en.html"] = full._readable(composition, checked, stem)
    files.update({f"source-{key}.json": text for key, text in texts.items()})
    destination = _write_atomic(output, files)
    return {
        "status": "complete",
        "validation_passed": True,
        "symbols": checked["symbols"],
        "parent_symbols": checked["parent_symbols"],
        "artifacts": {
            "universe": str(destination / (stem + ".json")),
            "watchlist": str(destination / (stem + ".txt")),
            "by_theme": str(destination / (stem + "-by-theme.txt")),
            "by_market": str(destination / (stem + "-by-market.txt")),
            "validation": str(destination / (stem + ".validation.json")),
            "report": str(destination / (stem + ".en.md")),
            "html": str(destination / (stem + ".en.html")),
            "contract": str(destination / CORE_CONTRACT),
        },
        "artifact_sha256": {name: full.file_hash(destination / name) for name in files},
        "warnings": checked["warnings"],
    }


def validate(path, review_path, policy=None):
    """Recompute parent, complete decisions, coverage, original rows and exact TXT views."""
    try:
        path = Path(path).resolve()
        stored, review = read_json(path), read_json(review_path)
        need(stored.get("kind") == "global_core_composition", "expected a Global Core composition")
        need(stored.get("review_sha256") == full.digest(review), "expected Core review changed")
        need(read_json(path.parent / CORE_CONTRACT) == review, "published Core review changed")
        unsigned = {k: v for k, v in stored.items() if k != "content_sha256"}
        need(stored.get("content_sha256") == full.digest(unsigned), "Core content hash mismatch")
        parent_ref = stored["parent"]
        need(
            parent_ref
            == {
                "file": PARENT_FILE,
                "sha256": review["parent_sha256"],
                "contract_file": PARENT_CONTRACT,
                "contract_sha256": review["parent_contract_sha256"],
            },
            "Core parent paths/hashes must be pinned portable copies",
        )
        parent, parent_contract, sources, _ = _load_parent(
            path.parent / PARENT_FILE, path.parent / PARENT_CONTRACT, review, policy
        )
        recomputed, contract = derive(parent, parent_contract, review, sources, policy)
        need(recomputed == unsigned, "Core differs from independently recomputed parent subset")
        need(
            read_json(path.parent / "global-contract.json") == contract,
            "Core changed the inherited coverage contract",
        )
        for key, text in full.exports(recomputed, contract).items():
            suffix = {"watchlist": "", "by_theme": "-by-theme", "by_market": "-by-market"}[key]
            need(
                (path.parent / (path.stem + suffix + ".txt")).read_bytes().decode("utf-8") == text,
                key + ": Core TXT differs from exact validated subset",
            )
        return report(recomputed, contract)
    except (UniverseError, OSError, ValueError, TypeError, KeyError, AttributeError) as exc:
        return {"passed": False, "qualified": False, "errors": [str(exc)], "warnings": []}
