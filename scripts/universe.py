#!/usr/bin/env python3
"""Build, maintain and validate one ticker universe.

    python scripts/universe.py measure  --prices P --benchmark B --source URL --output M
    python scripts/universe.py build    --spec S --snapshot N --output DIR [--seed universe.json]
    python scripts/universe.py maintain --universe U --changes C --output DIR
    python scripts/universe.py validate universe.json

Exit code 0 means the artifacts were written and validation passed. Exit code 2 means nothing was
written: a universe that fails its own checks is never produced.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import measure_core  # noqa: E402
from universe_core import (  # noqa: E402
    UniverseError,
    apply_change_set,
    build_universe,
    load_policy,
    read_json,
    validate_universe,
    write_artifacts,
)


def measure(args: argparse.Namespace) -> int:
    bundle = measure_core.measure(
        prices=args.prices,
        benchmarks=args.benchmark,
        source=args.source,
        window=args.window,
        liquidity_window=args.liquidity_window,
        as_of=args.as_of,
    )
    payload = bundle
    if args.into:
        payload = measure_core.merge_into_snapshot(read_json(args.into), bundle)
    Path(args.output).write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "status": "measured",
        "output": args.output,
        "as_of": bundle["as_of"],
        "tickers": len(bundle["metrics"]),
        "notes": bundle["notes"],
    }, ensure_ascii=False))
    return 0


def build(args: argparse.Namespace) -> int:
    universe, report = build_universe(
        read_json(args.spec),
        read_json(args.snapshot),
        load_policy(args.policy),
        read_json(args.seed) if args.seed else None,
    )
    artifacts = write_artifacts(universe, report, args.output)
    return _ok(universe, report, artifacts, report["stats"])


def maintain(args: argparse.Namespace) -> int:
    universe, report = apply_change_set(
        read_json(args.universe), read_json(args.changes), load_policy(args.policy)
    )
    artifacts = write_artifacts(universe, report, args.output)
    return _ok(universe, report, artifacts, report["maintenance"])


def validate(args: argparse.Namespace) -> int:
    report = validate_universe(read_json(args.universe), load_policy(args.policy))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["passed"] else 2


def _ok(universe: dict, report: dict, artifacts: dict[str, Path], detail: dict) -> int:
    print(json.dumps({
        "status": "passed",
        "output": str(artifacts["directory"]),
        "artifacts": {name: str(path) for name, path in artifacts.items() if name != "directory"},
        "version_hash": universe["version_hash"],
        "warnings": report["warnings"],
        **detail,
    }, ensure_ascii=False))
    return 0


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser(prog="universe.py", description=__doc__)
    value.add_argument(
        "--policy", help="policy JSON override (default: assets/default-policy.json)"
    )
    sub = value.add_subparsers(dest="command", required=True)

    stats = sub.add_parser("measure", help="compute the window statistics from a price table")
    stats.add_argument("--prices", required=True, help="CSV of date,ticker,close[,volume|turnover]")
    stats.add_argument(
        "--benchmark", required=True, action="append",
        help="factor leg; repeat for an equal-weighted basket",
    )
    stats.add_argument("--source", required=True, help="http(s) URL the price table came from")
    stats.add_argument("--window", type=int, default=180, help="factor window in sessions")
    stats.add_argument(
        "--liquidity-window", type=int, default=30, help="turnover window in sessions"
    )
    stats.add_argument("--as-of", help="defaults to the last date in the table")
    stats.add_argument("--into", help="snapshot.json to fold the metrics into")
    stats.add_argument("--output", required=True, help="file to write")
    stats.set_defaults(handler=measure)

    new = sub.add_parser("build", help="build a universe from a researched snapshot")
    new.add_argument("--spec", required=True, help="build-spec.json")
    new.add_argument("--snapshot", required=True, help="researched snapshot.json")
    new.add_argument("--output", required=True, help="new, empty output directory")
    new.add_argument(
        "--seed",
        help="existing universe to widen or narrow to this profile instead of rebuilding",
    )
    new.set_defaults(handler=build)

    review = sub.add_parser("maintain", help="apply an evidence-backed change set")
    review.add_argument("--universe", required=True, help="existing universe.json")
    review.add_argument("--changes", required=True, help="changes.json")
    review.add_argument("--output", required=True, help="new, empty output directory")
    review.set_defaults(handler=maintain)

    check = sub.add_parser("validate", help="validate a standalone universe.json")
    check.add_argument("universe", help="universe.json")
    check.set_defaults(handler=validate)
    return value


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        return args.handler(args)
    except (UniverseError, measure_core.MeasureError) as exc:
        print(f"{args.command} failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
