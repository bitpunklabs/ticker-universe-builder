"""Resumable local build receipts; research and network retries remain agent-owned."""

from __future__ import annotations

import hashlib
import json
import shlex
from datetime import datetime, timezone
from pathlib import Path

from universe_core import (
    PROFILES,
    UniverseError,
    build_universe,
    load_policy,
    market_guidance,
    normalize_snapshot,
    read_json,
    write_artifacts,
)


def save(path: Path, value: dict) -> None:
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def diagnostics(spec: dict, snapshot: dict, policy: dict, seed: dict | None = None) -> dict:
    """Admission checks are the core's; these counts never authorize a build."""
    try:
        normalized = normalize_snapshot(snapshot)
        if policy.get("selection_model") == "coverage_first":
            result = {
                "selection_model": "coverage_first",
                "coverage_plan_present": bool(snapshot.get("coverage_plan")),
                "admissions": sum(bool(c.get("admission")) for c in normalized["candidates"]),
                "candidates": len(normalized["candidates"]),
                "note": "Research necessary representatives and unresolved Core decisions "
                        "first; do not pad capacity.",
            }
            if spec.get("profile") == "extreme" and seed and seed.get("profile") == "heavy":
                from coverage_core import expansion_minimum

                held = {c["asset_id"] for c in seed["members"]}
                minimum = expansion_minimum(len(held), policy)
                maximum = spec.get("target_count") or snapshot["coverage_plan"]["budgets"]["extreme"]
                proposed = {
                    c["asset_id"] for c in normalized["candidates"]
                    if c["eligible"] and c["asset_id"] not in held
                    and (c.get("admission") or {}).get("kind") == "satellite"
                }
                result["expansion"] = {
                    "heavy_entities": len(held), "min_entities": minimum,
                    "max_entities": maximum, "eligible_proposed_additions": len(proposed),
                    "minimum_candidate_gap": max(0, minimum - len(held) - len(proposed)),
                    "note": "Snapshot capacity only; evidence, sector, satellite and export "
                            "gates still apply.",
                }
            return result
        guide = market_guidance(spec["market"], policy, normalized["market_spec"])
        stages = {}
        for profile in PROFILES[: PROFILES.index(spec["profile"]) + 1]:
            level = policy["profiles"][profile]["coverage_level"]
            themes = {
                t["theme_code"] for t in normalized["taxonomy"] if t["coverage_level"] <= level
            }
            bench = [
                c for c in normalized["candidates"] if c["eligible"] and c["theme_code"] in themes
            ]
            target = (
                spec.get("target_count") or guide[profile]["target"]
                if profile == spec["profile"]
                else guide[profile]["target"]
            )
            count = len({c["asset_id"] for c in bench})
            stages[profile] = {
                "target": target,
                "eligible_unique_assets": count,
                "capacity_shortfall": max(0, target - count),
                "missing_themes": sorted(themes - {c["theme_code"] for c in bench}),
                "unrepresented_duties": sorted(
                    t["theme_code"] for t in normalized["taxonomy"]
                    if t["theme_code"] in themes and t.get("representative_roles") and not any(
                        c["theme_code"] == t["theme_code"] and
                        c["role"] in t["representative_roles"] for c in bench)
                ),
                "qualified_beta_candidates": sum(c["role"] == "BETA_SATELLITE" for c in bench),
            }
        return {
            "stages": stages,
            "note": (
                "Capacity describes only the supplied research snapshot, not the whole market. "
                "Research unmapped inventory before declaring a source capacity ceiling; "
                "seed and token limits still apply."
            ),
        }
    except (UniverseError, KeyError, ValueError, TypeError) as exc:
        return {"input_error": str(exc)}


def run_build(
    *,
    spec: str | None,
    snapshot: str | None,
    output: str | None,
    policy: str | None = None,
    seed: str | None = None,
    language: str | None = None,
    run_dir: str | None = None,
    resume: str | None = None,
) -> tuple[dict, int]:
    if resume and run_dir:
        raise UniverseError("choose --resume or --run-dir")
    if not resume and not all((spec, snapshot, output)):
        raise UniverseError("build needs --spec, --snapshot and --output, or --resume RUN_DIR")
    root = Path(resume or run_dir or (str(output) + ".run")).resolve()
    state_path = root / "run.json"
    if resume:
        state = read_json(state_path)
        if state.get("schema_version") != 1 or state.get("kind") != "build_run":
            raise UniverseError("unsupported build run checkpoint")
        paths = dict(state["inputs"])
    else:
        if root.exists() and any(root.iterdir()):
            raise UniverseError(f"run directory is not empty; continue with --resume {root}")
        root.mkdir(parents=True, exist_ok=True)
        state = {"schema_version": 1, "kind": "build_run", "attempts": []}
        paths = {}
    for key, value in (
        ("spec", spec),
        ("snapshot", snapshot),
        ("policy", policy),
        ("seed", seed),
        ("output", output),
    ):
        if value is not None:
            paths[key] = str(Path(value).resolve())
    if language is not None:
        paths["language"] = language
    next_command = f"python scripts/universe.py build --resume {shlex.quote(str(root))}"
    # Read before starting an attempt; a missing file can be repaired at the saved input path.
    payload = {
        "spec": read_json(paths["spec"]),
        "snapshot": read_json(paths["snapshot"]),
        "policy": load_policy(paths.get("policy")),
        "seed": read_json(paths["seed"]) if paths.get("seed") else None,
        "language": paths.get("language"),
    }
    digest = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    previous = state["attempts"][-1] if state["attempts"] else None
    changed_destination = (
        output is not None and previous and str(Path(output).resolve()) != previous["output"]
    )
    if (
        previous
        and previous["input_sha256"] == digest
        and previous["status"] != "running"
        and not changed_destination
    ):
        result = {
            **previous,
            "checkpoint": str(state_path),
            "resume_command": next_command,
            "retry_skipped": "Inputs unchanged; repair or expand the saved inputs before resuming.",
        }
        return result, (
            0 if previous["status"] == "complete" else 3 if previous["status"] == "partial" else 2
        )
    number = len(state["attempts"]) + 1
    attempt_dir = root / f"attempt-{number:03d}"
    attempt_dir.mkdir()
    save(attempt_dir / "inputs.json", payload)
    destination = Path(paths["output"]) if not previous or output else attempt_dir / "artifacts"
    attempt = {
        "number": number,
        "input_sha256": digest,
        "status": "running",
        "started_at": datetime.now(timezone.utc).isoformat(),
        "output": str(destination),
        "inputs_archive": str(attempt_dir / "inputs.json"),
    }
    state.update(inputs=paths, status="running", resume_command=next_command)
    state["attempts"].append(attempt)
    save(state_path, state)
    try:
        universe, report = build_universe(
            payload["spec"], payload["snapshot"], payload["policy"], payload["seed"]
        )
        artifacts = write_artifacts(universe, report, destination, paths.get("language"))
        filled, target = len(universe["members"]), universe["limits"]["target_count"]
        attempt.update(
            status=("complete" if universe.get("selection_model") == "coverage_first"
                    or filled >= target else "partial"),
            validation_passed=True,
            target=target,
            filled=filled,
            shortfall=(0 if universe.get("selection_model") == "coverage_first"
                       else max(0, target - filled)),
            unused_capacity=max(0, target - filled),
            version_hash=universe["version_hash"],
            warnings=report["warnings"],
            **report["stats"],
        )
        attempt["artifacts"] = {
            k: {lang: str(p) for lang, p in v.items()} if isinstance(v, dict) else str(v)
            for k, v in artifacts.items()
            if k != "directory"
        }
        if payload["seed"]:
            held = {c["asset_id"] for c in payload["seed"]["members"]}
            chosen = {c["asset_id"] for c in universe["members"]}
            attempt["expansion"] = {
                "from_profile": payload["seed"]["profile"],
                "seed_members": len(held),
                "retained": len(held & chosen),
                "added": len(chosen - held),
                "removed": len(held - chosen),
            }
        code = 0 if attempt["status"] == "complete" else 3
    except (UniverseError, OSError) as exc:
        attempt.update(status="needs_research", validation_passed=False, error=str(exc))
        code = 2
    if code:
        attempt["diagnostics"] = diagnostics(
            payload["spec"], payload["snapshot"], payload["policy"], payload["seed"]
        )
        attempt["next_actions"] = [
            "Repair invalid facts or missing themes; expand the verified bench for capacity gaps.",
            "Recompute affected measurements, then resume with the corrected input paths.",
            "Keep eligibility and depth unchanged; do not spend retries on identical inputs.",
        ]
    attempt["finished_at"] = datetime.now(timezone.utc).isoformat()
    state["status"] = attempt["status"]
    save(attempt_dir / "result.json", attempt)
    save(state_path, state)
    return {**attempt, "checkpoint": str(state_path), "resume_command": next_command}, code
