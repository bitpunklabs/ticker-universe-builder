#!/usr/bin/env python3
"""Rebuild the seven researched Medium examples, offline, without changing their inputs.

Snapshots contain dated observed facts and measured statistics, not synthetic seed scores.
Raw provider receipts and the research constructor for this release live in the local test
result directory. To refresh, fetch new evidence and research a new snapshot first.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from universe_core import (  # noqa: E402
    apply_change_set,
    build_universe,
    load_policy,
    read_json,
    render_markdown,
    render_txt,
    report_languages,
)

MARKET_ORDER = ("us", "jp", "cn", "kr", "hk", "uk", "crypto")


def write(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    for market in MARKET_ORDER:
        folder = ROOT / "examples" / f"{market}-medium"
        universe, report = build_universe(
            read_json(folder / "build-spec.json"),
            read_json(folder / "snapshot.json"),
            load_policy(),
        )
        write(folder / "universe.json", universe)
        write(folder / "validation.json", report)
        (folder / "watchlist.txt").write_text(render_txt(universe), encoding="utf-8")
        for language in report_languages(market):
            (folder / f"universe.{language}.md").write_text(
                render_markdown(universe, report, language=language), encoding="utf-8"
            )
        if market == "crypto":
            changes = {
                "schema_version": 1,
                "market": market,
                "as_of": universe["as_of"],
                "complete": True,
                "base_version_hash": universe["version_hash"],
                "base_content_hash": universe["content_hash"],
                "review_depth": "routine",
                "sources": universe["sources"],
                "ops": [
                    {
                        "op": "NO_CHANGE",
                        "reason": (
                            "Same-date review demonstration; no new evidence justifies churn."
                        ),
                    }
                ],
            }
            write(folder / "changes.json", changes)
            updated, review = apply_change_set(universe, changes, load_policy())
            write(folder / "maintained.json", updated)
            for language in report_languages(market):
                (folder / f"maintenance.{language}.md").write_text(
                    render_markdown(updated, review, language=language), encoding="utf-8"
                )
        print(f"{market}: {len(universe['members'])} members; {len(report['warnings'])} warnings")


if __name__ == "__main__":
    main()
