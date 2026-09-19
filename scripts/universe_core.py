#!/usr/bin/env python3
"""Deterministic build, validation, rendering and maintenance primitives.

The agent supplies researched facts and proposed operations. This module owns every mutation and
output invariant. It intentionally uses only the Python standard library.
"""

from __future__ import annotations

import hashlib
import json
import math
import os
import re
import shutil
import tempfile
from collections import Counter, defaultdict
from copy import deepcopy
from datetime import date
from pathlib import Path
from typing import Any

MARKETS = {"cn", "us", "crypto"}
PROFILES = ("light", "medium", "heavy")
PROFILE_INDEX = {name: index for index, name in enumerate(PROFILES)}
ROLES = {
    "BENCHMARK",
    "ANCHOR",
    "THEME_LEADER",
    "QUALITY_LEADER",
    "BETA_SATELLITE",
    "INDEPENDENT_SENSOR",
    "BREADTH_PROXY",
    "LIQUIDITY_SENSOR",
    "NEW_LISTING",
}
BUCKET_BY_ROLE = {
    "BENCHMARK": "core",
    "ANCHOR": "core",
    "THEME_LEADER": "core",
    "QUALITY_LEADER": "core",
    "BETA_SATELLITE": "satellite",
    "INDEPENDENT_SENSOR": "satellite",
    "BREADTH_PROXY": "satellite",
    "LIQUIDITY_SENSOR": "tactical",
    "NEW_LISTING": "tactical",
}
ROLE_ORDER = {
    "BENCHMARK": 1100,
    "ANCHOR": 1000,
    "THEME_LEADER": 900,
    "QUALITY_LEADER": 800,
    "INDEPENDENT_SENSOR": 700,
    "BETA_SATELLITE": 600,
    "BREADTH_PROXY": 500,
    "LIQUIDITY_SENSOR": 400,
    "NEW_LISTING": 300,
}
SCORE_WEIGHTS = {
    "core": {"liquidity": 0.35, "quality": 0.4, "independence": 0.15, "heat": 0.1},
    "satellite": {"liquidity": 0.25, "quality": 0.2, "independence": 0.4, "heat": 0.15},
    "tactical": {"liquidity": 0.45, "independence": 0.15, "heat": 0.4},
}
BETA_SCORE_WEIGHTS = {
    "liquidity": 0.25,
    "beta_strength": 0.35,
    "beta_stability": 0.25,
    "heat": 0.15,
}
US_VENUES = {"NASDAQ", "NYSE", "AMEX", "NYSEARCA", "ARCA", "CBOE", "IEX", "OTC"}
CN_VENUES = {"SSE", "SZSE", "BSE"}

METRIC_FIELDS = (
    "liquidity",
    "quality",
    "independence",
    "heat",
    "factor_r2",
    "beta_strength",
    "beta_stability",
)
# Window-dependent statistics. A model cannot know these without computing them, so the snapshot
# has to say which window and which source produced them; declaring them as judgement is refused.
MEASURED_ONLY_METRICS = {"liquidity", "factor_r2", "beta_strength", "beta_stability"}
MEASUREMENT_BASES = {"measured", "judged"}

# Closed vocabulary. Free text hides the reason a candidate lost its slot inside prose nobody
# aggregates; a code can be counted across rounds.
EXCLUSION_CODES = {
    "not_listed",
    "delisted_or_halted",
    "risk_warning_status",
    "wrong_venue",
    "excluded_instrument_type",
    "insufficient_liquidity",
    "insufficient_history",
    "redundant_with_member",
    "unverifiable_fact",
    "duplicate_asset",
    "other",
}
# Reasons this module writes into the selection audit itself.
AUDIT_CODES = {
    "outside_profile_coverage",
    "not_selected_under_budget_or_theme_cap",
    "removed_by_maintenance",
}
DECISION_OPS = {"ADD", "REMOVE", "REPLACE"}
THEME_OPS = {"ADD_THEME", "REMOVE_THEME"}
# Theme structure is resolved before membership, so a MOVE or ADD can target a theme this same
# round created, and a theme can only be retired once its members have been placed elsewhere.
OP_ORDER = {
    "ADD_THEME": 0,
    "REMOVE": 1,
    "MOVE": 2,
    "REPLACE": 3,
    "ADD": 4,
    "REMOVE_THEME": 5,
    "NO_CHANGE": 6,
}
# How far a bucket may sit above its profile target before the drift is reported.
BUCKET_DRIFT_TOLERANCE = 0.10
STRONG_EVIDENCE_TIERS = {1, 2}

_THEME_RE = re.compile(r"^\d{2}_[A-Z]$")
_CN_TICKER_RE = re.compile(r"^\d{6}$")
_US_TICKER_RE = re.compile(r"^[A-Z][A-Z0-9.\-]{0,14}$")


class UniverseError(ValueError):
    pass


def read_json(path: str | Path) -> dict[str, Any]:
    try:
        value = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise UniverseError(f"cannot read JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise UniverseError(f"{path} must contain a JSON object")
    return value


def default_policy_path() -> Path:
    return Path(__file__).resolve().parent.parent / "assets" / "default-policy.json"


def load_policy(path: str | Path | None = None) -> dict[str, Any]:
    return read_json(path or default_policy_path())


def canonical_hash(value: Any) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:12]


def universe_hash(universe: dict[str, Any]) -> str:
    """Hash membership and taxonomy, not run metadata or review history."""
    canonical = {
        "market": universe.get("market"),
        "profile": universe.get("profile"),
        "taxonomy": universe.get("taxonomy") or [],
        "members": [
            {
                "ticker": item.get("ticker"),
                "asset_id": item.get("asset_id"),
                "theme_code": item.get("theme_code"),
                "role": item.get("role"),
                "required": bool(item.get("required", False)),
            }
            for item in universe.get("members") or []
        ],
    }
    return canonical_hash(canonical)


def split_ticker(ticker: str) -> tuple[str, str]:
    value = str(ticker).strip().upper()
    if ":" not in value:
        raise UniverseError(f"ticker must include TradingView venue: {ticker}")
    venue, symbol = value.split(":", 1)
    if not venue or not symbol:
        raise UniverseError(f"invalid ticker: {ticker}")
    return venue, symbol


def default_asset_id(market: str, ticker: str) -> str:
    venue, symbol = split_ticker(ticker)
    if market == "crypto":
        symbol = symbol.removesuffix(".P")
        return symbol.removesuffix("USDT")
    if market == "cn":
        return f"{venue}:{symbol}"
    return symbol


def validate_ticker(market: str, ticker: str) -> list[str]:
    errors: list[str] = []
    try:
        venue, symbol = split_ticker(ticker)
    except UniverseError as exc:
        return [str(exc)]
    if market == "cn":
        if venue not in CN_VENUES:
            errors.append(f"{ticker}: unsupported CN venue")
        if not _CN_TICKER_RE.fullmatch(symbol):
            errors.append(f"{ticker}: CN symbol must be six digits")
    elif market == "us":
        if venue not in US_VENUES:
            errors.append(f"{ticker}: unsupported US venue")
        if not _US_TICKER_RE.fullmatch(symbol):
            errors.append(f"{ticker}: invalid US symbol")
    elif market == "crypto":
        if venue != "BINANCE":
            errors.append(f"{ticker}: Crypto V1 requires BINANCE venue")
        base = symbol.removesuffix(".P")
        if not base.endswith("USDT") or len(base) <= 4:
            errors.append(f"{ticker}: Crypto V1 requires a USDT spot or perpetual symbol")
    return errors


def normalize_taxonomy(raw: list[dict[str, Any]]) -> list[dict[str, Any]]:
    taxonomy: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index, item in enumerate(raw):
        if not isinstance(item, dict):
            raise UniverseError(f"taxonomy #{index} must be an object")
        theme_code = str(item.get("theme_code", "")).strip().upper()
        if not _THEME_RE.fullmatch(theme_code):
            raise UniverseError(f"taxonomy #{index} has invalid theme_code {theme_code!r}")
        if theme_code in seen:
            raise UniverseError(f"duplicate taxonomy theme {theme_code}")
        seen.add(theme_code)
        level = item.get("coverage_level")
        if level not in (1, 2, 3):
            raise UniverseError(f"{theme_code}: coverage_level must be 1, 2, or 3")
        l1_code = str(item.get("l1_code", "")).strip()
        if theme_code.split("_", 1)[0] != l1_code:
            raise UniverseError(f"{theme_code}: l1_code does not match theme prefix")
        l1_name = str(item.get("l1_name", "")).strip()
        theme_name = str(item.get("theme_name", "")).strip()
        if not l1_name or not theme_name:
            raise UniverseError(f"{theme_code}: l1_name and theme_name are required")
        if any(char in l1_name + theme_name for char in (",", "\n", "\r")):
            raise UniverseError(f"{theme_code}: taxonomy names cannot contain commas or newlines")
        taxonomy.append({
            "l1_code": l1_code,
            "l1_name": l1_name,
            "theme_code": theme_code,
            "theme_name": theme_name,
            "coverage_level": level,
        })
    return sorted(taxonomy, key=lambda item: item["theme_code"])


def _score_value(value: Any, field: str, ticker: str) -> float | None:
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise UniverseError(f"{ticker}: metric {field} must be numeric or null")
    number = float(value)
    if not 0 <= number <= 100:
        raise UniverseError(f"{ticker}: metric {field} must be between 0 and 100")
    return number


def validate_evidence(evidence: Any, subject: str) -> list[dict[str, Any]]:
    if not isinstance(evidence, list) or not evidence:
        raise UniverseError(f"{subject}: at least one evidence item is required")
    for item in evidence:
        url = str(item.get("url", "")) if isinstance(item, dict) else ""
        if not url.startswith(("http://", "https://")):
            raise UniverseError(f"{subject}: every evidence item needs an http(s) URL")
        if not item.get("as_of"):
            raise UniverseError(f"{subject}: every evidence item needs as_of")
        if item.get("tier") not in (1, 2, 3):
            raise UniverseError(f"{subject}: every evidence item needs tier 1, 2, or 3")
    return deepcopy(evidence)


def require_strong_evidence(evidence: list[dict[str, Any]], subject: str) -> None:
    """Admission and removal need a primary or auditable source, never market narrative alone."""
    if not any(int(item["tier"]) in STRONG_EVIDENCE_TIERS for item in evidence):
        raise UniverseError(f"{subject}: needs at least one tier 1 or tier 2 evidence item")


def _parse_date(value: Any) -> date | None:
    try:
        return date.fromisoformat(str(value)[:10])
    except (TypeError, ValueError):
        return None


def staleness_warnings(
    as_of: str, evidence_groups: list[tuple[str, list[dict[str, Any]]]], policy: dict[str, Any]
) -> list[str]:
    """Evidence that predates the snapshot by more than the policy window is reported, not trusted
    silently. An `as_of` in the future is always wrong and is reported the same way."""
    reference = _parse_date(as_of)
    limit = int((policy.get("freshness") or {}).get("evidence_warning_days", 180))
    if reference is None:
        return [f"as_of {as_of!r} is not an ISO date"]
    warnings: list[str] = []
    for subject, evidence in evidence_groups:
        for item in evidence:
            stamped = _parse_date(item.get("as_of"))
            if stamped is None:
                stale = item.get("as_of")
                warnings.append(f"{subject}: evidence as_of {stale!r} is not an ISO date")
            elif stamped > reference:
                warnings.append(f"{subject}: evidence as_of {stamped} is after the snapshot")
            elif (reference - stamped).days > limit:
                warnings.append(
                    f"{subject}: evidence is {(reference - stamped).days} days older than the "
                    f"snapshot (limit {limit})"
                )
    return sorted(set(warnings))


def normalize_measurement(raw: Any, used_fields: set[str]) -> dict[str, dict[str, Any]]:
    """Every populated metric must say how it was produced.

    `measured` carries a window and a source; `judged` carries a method and nothing else. The
    window-dependent statistics cannot be declared `judged` — a model that has not run the
    regression does not have the number, and a filled-in guess is indistinguishable from one.
    """
    if not isinstance(raw, dict):
        raise UniverseError("measurement must be an object keyed by metric name")
    declared: dict[str, dict[str, Any]] = {}
    for field, entry in raw.items():
        if field not in METRIC_FIELDS:
            raise UniverseError(f"measurement: unknown metric {field!r}")
        if not isinstance(entry, dict):
            raise UniverseError(f"measurement {field}: must be an object")
        basis = str(entry.get("basis", "")).strip().lower()
        if basis not in MEASUREMENT_BASES:
            raise UniverseError(f"measurement {field}: basis must be measured or judged")
        method = str(entry.get("method", "")).strip()
        if not method:
            raise UniverseError(f"measurement {field}: method is required")
        if basis == "judged" and field in MEASURED_ONLY_METRICS:
            raise UniverseError(f"measurement {field}: this metric cannot be judged, only measured")
        item = {"basis": basis, "method": method}
        if basis == "measured":
            window = str(entry.get("window", "")).strip()
            source = str(entry.get("source", "")).strip()
            if not window:
                raise UniverseError(f"measurement {field}: measured metrics need a window")
            if not source.startswith(("http://", "https://")):
                raise UniverseError(f"measurement {field}: measured metrics need a source URL")
            item["window"] = window
            item["source"] = source
        declared[field] = item
    missing = sorted(used_fields - set(declared))
    if missing:
        raise UniverseError("metrics used without a measurement declaration: " + ", ".join(missing))
    return dict(sorted(declared.items()))


def metrics_in_use(candidates: list[dict[str, Any]]) -> set[str]:
    return {
        field
        for candidate in candidates
        for field in METRIC_FIELDS
        if candidate.get("metrics", {}).get(field) is not None
    }


def normalize_candidate(
    market: str, raw: dict[str, Any], taxonomy_by_code: dict[str, dict[str, Any]]
) -> dict[str, Any]:
    ticker = str(raw.get("ticker", "")).strip().upper()
    ticker_errors = validate_ticker(market, ticker)
    if ticker_errors:
        raise UniverseError("; ".join(ticker_errors))
    theme_code = str(raw.get("theme_code", "")).strip().upper()
    if theme_code not in taxonomy_by_code:
        raise UniverseError(f"{ticker}: unknown theme {theme_code}")
    role = str(raw.get("role", "")).strip().upper()
    if role not in ROLES:
        raise UniverseError(f"{ticker}: invalid role {role!r}")
    evidence = validate_evidence(raw.get("evidence") or [], ticker)
    raw_metrics = raw.get("metrics") or {}
    if not isinstance(raw_metrics, dict):
        raise UniverseError(f"{ticker}: metrics must be an object")
    unknown = sorted(set(raw_metrics) - set(METRIC_FIELDS))
    if unknown:
        raise UniverseError(f"{ticker}: unknown metric fields: {', '.join(unknown)}")
    metrics = {
        field: _score_value(raw_metrics.get(field), field, ticker) for field in METRIC_FIELDS
    }
    if metrics["factor_r2"] is not None:
        derived_independence = 100 - metrics["factor_r2"]
        if metrics["independence"] is not None and abs(
            metrics["independence"] - derived_independence
        ) > 5:
            raise UniverseError(
                f"{ticker}: independence must equal 100 - factor_r2 within five points"
            )
        metrics["independence"] = derived_independence
    eligible = bool(raw.get("eligible", False))
    exclusion_reasons = [
        str(item).strip() for item in raw.get("exclusion_reasons", []) if str(item).strip()
    ]
    for reason in exclusion_reasons:
        code = reason.split(":", 1)[0].strip()
        if code not in EXCLUSION_CODES:
            raise UniverseError(
                f"{ticker}: exclusion reason must start with one of "
                f"{', '.join(sorted(EXCLUSION_CODES))}; got {code!r}"
            )
    if not eligible and not exclusion_reasons:
        raise UniverseError(f"{ticker}: ineligible candidate requires exclusion_reasons")
    if eligible and metrics["liquidity"] is None and role not in {"BENCHMARK", "ANCHOR"}:
        raise UniverseError(f"{ticker}: non-anchor candidate requires a liquidity score")
    if eligible and market == "crypto" and role not in {"BENCHMARK", "ANCHOR", "NEW_LISTING"}:
        if metrics["factor_r2"] is None:
            raise UniverseError(f"{ticker}: established Crypto candidates require factor_r2")
    if eligible and role == "INDEPENDENT_SENSOR" and (
        metrics["independence"] is None or metrics["independence"] < 50
    ):
        raise UniverseError(f"{ticker}: INDEPENDENT_SENSOR requires independence >= 50")
    if eligible and role == "BETA_SATELLITE" and (
        metrics["beta_strength"] is None or metrics["beta_stability"] is None
    ):
        raise UniverseError(f"{ticker}: BETA_SATELLITE requires beta_strength and beta_stability")
    if eligible and role in {"LIQUIDITY_SENSOR", "NEW_LISTING"} and metrics["heat"] is None:
        raise UniverseError(f"{ticker}: tactical roles require a heat score")
    asset_id = str(raw.get("asset_id") or default_asset_id(market, ticker)).strip().upper()
    if not asset_id:
        raise UniverseError(f"{ticker}: asset_id is empty")
    taxonomy = taxonomy_by_code[theme_code]
    return {
        "ticker": ticker,
        "asset_id": asset_id,
        "name": str(raw.get("name", "")).strip() or asset_id,
        "theme_code": theme_code,
        "l1_code": taxonomy["l1_code"],
        "role": role,
        "required": bool(raw.get("required", False)),
        "eligible": eligible,
        "exclusion_reasons": exclusion_reasons,
        "metrics": metrics,
        "evidence": evidence,
        "reason": str(raw.get("reason", "")).strip(),
        "tags": sorted({str(tag).strip() for tag in raw.get("tags", []) if str(tag).strip()}),
    }


def normalize_snapshot(snapshot: dict[str, Any]) -> dict[str, Any]:
    market = str(snapshot.get("market", "")).lower()
    if market not in MARKETS:
        raise UniverseError(f"snapshot market must be one of {sorted(MARKETS)}")
    if snapshot.get("schema_version") != 1:
        raise UniverseError("snapshot schema_version must be 1")
    if snapshot.get("complete") is not True:
        raise UniverseError("snapshot is incomplete; refusing a formal build")
    if not snapshot.get("as_of"):
        raise UniverseError("snapshot as_of is required")
    sources = validate_evidence(snapshot.get("sources") or [], "snapshot")
    taxonomy = normalize_taxonomy(snapshot.get("taxonomy") or [])
    if not taxonomy:
        raise UniverseError("snapshot taxonomy is empty")
    taxonomy_by_code = {item["theme_code"]: item for item in taxonomy}
    candidates = [
        normalize_candidate(market, item, taxonomy_by_code)
        for item in snapshot.get("candidates") or []
    ]
    seen_tickers: set[str] = set()
    seen_assets: set[str] = set()
    for candidate in candidates:
        if candidate["ticker"] in seen_tickers:
            raise UniverseError(f"duplicate ticker in snapshot: {candidate['ticker']}")
        if candidate["asset_id"] in seen_assets:
            raise UniverseError(f"duplicate economic asset in snapshot: {candidate['asset_id']}")
        seen_tickers.add(candidate["ticker"])
        seen_assets.add(candidate["asset_id"])
    measurement = normalize_measurement(
        snapshot.get("measurement") or {}, metrics_in_use(candidates)
    )
    return {
        "schema_version": 1,
        "market": market,
        "as_of": str(snapshot["as_of"]),
        "complete": True,
        "sources": deepcopy(sources),
        "measurement": measurement,
        "taxonomy": taxonomy,
        "candidates": candidates,
    }


def candidate_bucket(candidate: dict[str, Any]) -> str:
    return BUCKET_BY_ROLE[candidate["role"]]


def metric_score(candidate: dict[str, Any]) -> float:
    bucket = candidate_bucket(candidate)
    values = candidate["metrics"]
    weights = BETA_SCORE_WEIGHTS if candidate["role"] == "BETA_SATELLITE" else SCORE_WEIGHTS[bucket]
    weighted = [
        (float(values[field]), weight)
        for field, weight in weights.items()
        if values.get(field) is not None
    ]
    if not weighted:
        return 0.0
    return sum(value * weight for value, weight in weighted) / sum(weight for _, weight in weighted)


def rank_key(candidate: dict[str, Any]) -> tuple[float, float, str]:
    return (-ROLE_ORDER[candidate["role"]], -metric_score(candidate), candidate["ticker"])


def _add_candidate(
    selected: list[dict[str, Any]],
    selected_assets: set[str],
    theme_counts: Counter[str],
    candidate: dict[str, Any],
    theme_cap: int,
) -> bool:
    if candidate["asset_id"] in selected_assets:
        return False
    if theme_counts[candidate["theme_code"]] >= theme_cap:
        return False
    selected.append(candidate)
    selected_assets.add(candidate["asset_id"])
    theme_counts[candidate["theme_code"]] += 1
    return True


def _select_stage(
    *,
    candidates: list[dict[str, Any]],
    taxonomy: list[dict[str, Any]],
    profile: str,
    target: int,
    profile_policy: dict[str, Any],
    seed: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[str]]:
    coverage_level = int(profile_policy["coverage_level"])
    theme_cap = int(profile_policy["theme_cap"])
    allowed_themes = [
        item for item in taxonomy if int(item["coverage_level"]) <= coverage_level
    ]
    allowed_codes = {item["theme_code"] for item in allowed_themes}
    eligible = [
        candidate for candidate in candidates
        if candidate["eligible"] and candidate["theme_code"] in allowed_codes
    ]
    by_theme: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for candidate in eligible:
        by_theme[candidate["theme_code"]].append(candidate)
    for values in by_theme.values():
        values.sort(key=rank_key)

    missing = [item["theme_code"] for item in allowed_themes if not by_theme[item["theme_code"]]]
    if missing:
        raise UniverseError(
            f"{profile}: no eligible candidate for required themes: {', '.join(missing)}"
        )

    selected = list(seed)
    selected_assets = {item["asset_id"] for item in selected}
    theme_counts = Counter(item["theme_code"] for item in selected)
    warnings: list[str] = []

    required = sorted(
        (item for item in eligible if item["required"]),
        key=lambda item: (item["theme_code"], rank_key(item)),
    )
    for candidate in required:
        _add_candidate(selected, selected_assets, theme_counts, candidate, theme_cap)

    for theme in allowed_themes:
        if theme_counts[theme["theme_code"]] == 0:
            _add_candidate(
                selected, selected_assets, theme_counts, by_theme[theme["theme_code"]][0], theme_cap
            )

    if len(selected) > target:
        raise UniverseError(
            f"{profile}: anchors and required theme coverage need {len(selected)} slots, "
            f"target is {target}"
        )

    bucket_targets = profile_policy["bucket_targets"]
    bucket_counts = Counter(candidate_bucket(item) for item in selected)
    for bucket in ("core", "satellite", "tactical"):
        quota = math.floor(target * float(bucket_targets[bucket]))
        ranked = sorted(
            (item for item in eligible if candidate_bucket(item) == bucket),
            key=rank_key,
        )
        for candidate in ranked:
            if len(selected) >= target or bucket_counts[bucket] >= quota:
                break
            if _add_candidate(selected, selected_assets, theme_counts, candidate, theme_cap):
                bucket_counts[bucket] += 1

    for candidate in sorted(eligible, key=rank_key):
        if len(selected) >= target:
            break
        if _add_candidate(selected, selected_assets, theme_counts, candidate, theme_cap):
            bucket_counts[candidate_bucket(candidate)] += 1

    if len(selected) < target:
        warnings.append(
            f"qualified universe filled {len(selected)} of {target}; "
            "eligibility and theme caps were not relaxed"
        )
    return selected, warnings


def _seed_members(
    snapshot: dict[str, Any], previous: dict[str, Any] | None
) -> list[dict[str, Any]]:
    """Carry an existing universe into a wider one.

    Upgrading a tier is an extension, not a rebuild: rebuilding from scratch would churn every
    slot of a pool whose whole point is low turnover. Any incumbent the new snapshot no longer
    carries as an eligible candidate stops the build and is named, because dropping it is a
    decision the operator has to make, not one this function can make quietly.
    """
    if previous is None:
        return []
    if previous.get("market") != snapshot["market"]:
        raise UniverseError("seed universe and snapshot markets differ")
    by_ticker = {item["ticker"]: item for item in snapshot["candidates"] if item["eligible"]}
    missing = sorted(
        item["ticker"] for item in previous.get("members") or [] if item["ticker"] not in by_ticker
    )
    if missing:
        raise UniverseError(
            "seed members absent or ineligible in the new snapshot: " + ", ".join(missing)
        )
    return [deepcopy(by_ticker[item["ticker"]]) for item in previous.get("members") or []]


def build_universe(
    spec: dict[str, Any],
    snapshot_raw: dict[str, Any],
    policy: dict[str, Any],
    previous: dict[str, Any] | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    if spec.get("schema_version") != 1:
        raise UniverseError("build spec schema_version must be 1")
    market = str(spec.get("market", "")).lower()
    profile = str(spec.get("profile", "")).lower()
    if market not in MARKETS or profile not in PROFILES:
        raise UniverseError("build spec needs market=cn|us|crypto and profile=light|medium|heavy")
    snapshot = normalize_snapshot(snapshot_raw)
    if snapshot["market"] != market:
        raise UniverseError("build spec and snapshot markets differ")

    market_policy = policy["markets"][market]
    final_guide = market_policy[profile]
    target = int(spec.get("target_count") or final_guide["target"])
    hard_cap = min(int(spec.get("hard_ticker_cap", 1000)), 1000)
    token_cap = min(int(spec.get("tradingview_token_cap", 1000)), 1000)
    if target > hard_cap:
        raise UniverseError(f"target_count {target} exceeds hard_ticker_cap {hard_cap}")
    if not spec.get("allow_outside_guidance", False):
        if not int(final_guide["min"]) <= target <= int(final_guide["max"]):
            raise UniverseError(
                f"{market}/{profile} target {target} is outside guidance "
                f"{final_guide['min']}..{final_guide['max']}"
            )

    warnings: list[str] = staleness_warnings(
        snapshot["as_of"],
        [("snapshot", snapshot["sources"])]
        + [(item["ticker"], item["evidence"]) for item in snapshot["candidates"]],
        policy,
    )
    selected: list[dict[str, Any]] = _seed_members(snapshot, previous)
    if selected:
        warnings.append(
            f"seeded {len(selected)} members from universe "
            f"{previous.get('version_hash')} ({previous.get('profile')})"
        )
    # Without a seed the tiers are built in order so that Light ⊆ Medium ⊆ Heavy holds inside one
    # run. A seed already is the narrower tier, so only the final stage is left to fill.
    stages = (profile,) if selected else PROFILES[: PROFILE_INDEX[profile] + 1]
    for stage in stages:
        guide = market_policy[stage]
        stage_target = target if stage == profile else int(guide["target"])
        stage_theme_count = sum(
            1 for item in snapshot["taxonomy"]
            if item["coverage_level"] <= policy["profiles"][stage]["coverage_level"]
        )
        stage_effective = min(stage_target, token_cap - stage_theme_count, hard_cap)
        if stage_effective <= 0:
            raise UniverseError(f"{stage}: TradingView token cap leaves no ticker slots")
        if stage_effective < stage_target:
            warnings.append(
                f"{stage}: target reduced from {stage_target} to {stage_effective} by token cap"
            )
        selected, stage_warnings = _select_stage(
            candidates=snapshot["candidates"],
            taxonomy=snapshot["taxonomy"],
            profile=stage,
            target=stage_effective,
            profile_policy=policy["profiles"][stage],
            seed=selected,
        )
        warnings.extend(stage_warnings)

    selected.sort(key=lambda item: (item["theme_code"], rank_key(item)))
    selected_assets = {item["asset_id"] for item in selected}
    final_level = int(policy["profiles"][profile]["coverage_level"])
    selection_audit = []
    taxonomy_by_code = {item["theme_code"]: item for item in snapshot["taxonomy"]}
    for candidate in snapshot["candidates"]:
        if candidate["asset_id"] in selected_assets:
            continue
        if not candidate["eligible"]:
            reasons = candidate["exclusion_reasons"]
        elif taxonomy_by_code[candidate["theme_code"]]["coverage_level"] > final_level:
            reasons = ["outside_profile_coverage"]
        else:
            reasons = ["not_selected_under_budget_or_theme_cap"]
        selection_audit.append({
            "ticker": candidate["ticker"],
            "asset_id": candidate["asset_id"],
            "theme_code": candidate["theme_code"],
            "reasons": reasons,
        })
    universe_base = {
        "schema_version": 1,
        "market": market,
        "profile": profile,
        "as_of": str(spec.get("as_of") or snapshot["as_of"]),
        "source_as_of": snapshot["as_of"],
        "policy_version": canonical_hash(policy),
        "limits": {
            "hard_ticker_cap": hard_cap,
            "tradingview_token_cap": token_cap,
            "target_count": target,
        },
        "taxonomy": snapshot["taxonomy"],
        "sources": snapshot["sources"],
        "measurement": snapshot["measurement"],
        "members": selected,
        "selection_audit": selection_audit,
        "history": [],
    }
    universe = {**universe_base}
    universe["version_hash"] = universe_hash(universe)
    report = validate_universe(universe, policy)
    report["warnings"] = sorted(set(report["warnings"] + warnings))
    if not report["passed"]:
        raise UniverseError("built universe failed validation: " + "; ".join(report["errors"]))
    return universe, report


def validate_universe(
    universe: dict[str, Any], policy: dict[str, Any] | None = None
) -> dict[str, Any]:
    policy = policy or load_policy()
    errors: list[str] = []
    warnings: list[str] = []
    market = str(universe.get("market", "")).lower()
    profile = str(universe.get("profile", "")).lower()
    if market not in MARKETS:
        errors.append("invalid market")
    if profile not in PROFILES:
        errors.append("invalid profile")
    try:
        taxonomy = normalize_taxonomy(universe.get("taxonomy") or [])
    except UniverseError as exc:
        errors.append(str(exc))
        taxonomy = []
    taxonomy_by_code = {item["theme_code"]: item for item in taxonomy}
    members = universe.get("members") or []
    seen_tickers: set[str] = set()
    seen_assets: set[str] = set()
    normalized: list[dict[str, Any]] = []
    for index, raw in enumerate(members):
        try:
            item = normalize_candidate(market, raw, taxonomy_by_code)
        except UniverseError as exc:
            errors.append(f"member #{index}: {exc}")
            continue
        if not item["eligible"]:
            errors.append(f"{item['ticker']}: selected member is not eligible")
        if item["ticker"] in seen_tickers:
            errors.append(f"duplicate ticker: {item['ticker']}")
        if item["asset_id"] in seen_assets:
            errors.append(f"duplicate economic asset: {item['asset_id']}")
        seen_tickers.add(item["ticker"])
        seen_assets.add(item["asset_id"])
        normalized.append(item)
    if market in MARKETS and profile in PROFILES:
        level = policy["profiles"][profile]["coverage_level"]
        required_themes = {
            item["theme_code"] for item in taxonomy if item["coverage_level"] <= level
        }
        held_themes = {item["theme_code"] for item in normalized}
        missing = sorted(required_themes - held_themes)
        if missing:
            errors.append("uncovered required themes: " + ", ".join(missing))
        disallowed = sorted({
            item["theme_code"] for item in normalized
            if taxonomy_by_code[item["theme_code"]]["coverage_level"] > level
        })
        if disallowed:
            errors.append("themes exceed profile coverage level: " + ", ".join(disallowed))
        theme_cap = int(policy["profiles"][profile]["theme_cap"])
        over = {
            code: count
            for code, count in Counter(item["theme_code"] for item in normalized).items()
            if count > theme_cap
        }
        if over:
            errors.append(f"theme caps exceeded: {over}")
    try:
        normalize_measurement(universe.get("measurement") or {}, metrics_in_use(normalized))
    except UniverseError as exc:
        errors.append(str(exc))
    if market in MARKETS and profile in PROFILES and normalized:
        # Quotas steer the build; nothing re-checked them afterwards, so a maintenance round could
        # walk a pool from 5% tactical to 30% one evidence-backed op at a time and never be told.
        targets = policy["profiles"][profile]["bucket_targets"]
        counts = Counter(candidate_bucket(item) for item in normalized)
        for bucket, share in sorted(targets.items()):
            actual = counts[bucket] / len(normalized)
            if actual - float(share) > BUCKET_DRIFT_TOLERANCE:
                warnings.append(
                    f"{bucket} bucket holds {actual:.0%} of the pool against a "
                    f"{float(share):.0%} target"
                )
    token_count = len(normalized) + len({item["theme_code"] for item in normalized})
    limits = universe.get("limits") or {}
    hard_ticker_cap = min(int(limits.get("hard_ticker_cap", 1000)), 1000)
    tradingview_token_cap = min(int(limits.get("tradingview_token_cap", 1000)), 1000)
    if len(normalized) > hard_ticker_cap:
        errors.append(f"ticker count exceeds {hard_ticker_cap}")
    if token_count > tradingview_token_cap:
        errors.append(f"TradingView token count exceeds {tradingview_token_cap}")
    if market in MARKETS and profile in PROFILES:
        guide = policy["markets"][market][profile]
        if len(normalized) < int(guide["min"]):
            warnings.append(
                f"member count {len(normalized)} is below "
                f"{market}/{profile} guidance {guide['min']}"
            )
        if len(normalized) > int(guide["max"]):
            warnings.append(
                f"member count {len(normalized)} is above "
                f"{market}/{profile} guidance {guide['max']}"
            )
    expected = universe.get("version_hash")
    if expected and universe_hash(universe) != expected:
        errors.append("version_hash does not match universe content")
    return {
        "passed": not errors,
        "errors": errors,
        "warnings": warnings,
        "stats": {
            "tickers": len(normalized),
            "themes": len({item["theme_code"] for item in normalized}),
            "tradingview_tokens": token_count,
            "roles": dict(sorted(Counter(item["role"] for item in normalized).items())),
            "buckets": dict(sorted(Counter(candidate_bucket(item) for item in normalized).items())),
        },
    }


def render_txt(universe: dict[str, Any]) -> str:
    taxonomy = {item["theme_code"]: item for item in universe["taxonomy"]}
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for member in universe["members"]:
        grouped[member["theme_code"]].append(member)
    tokens: list[str] = []
    for code in sorted(grouped):
        tokens.append(f"###{code}_{taxonomy[code]['theme_name']}")
        tokens.extend(item["ticker"] for item in sorted(grouped[code], key=rank_key))
    return ",".join(tokens) + "\n"


def render_markdown(universe: dict[str, Any], report: dict[str, Any]) -> str:
    taxonomy = {item["theme_code"]: item for item in universe["taxonomy"]}
    lines = [
        f"# {universe['market'].upper()} Ticker Universe",
        "",
        f"- Profile: {universe['profile'].title()}",
        f"- Facts as of: {universe['source_as_of']}",
        f"- Version: `{universe['version_hash']}`",
        f"- Tickers: {report['stats']['tickers']}",
        f"- Themes: {report['stats']['themes']}",
        f"- TradingView tokens: {report['stats']['tradingview_tokens']} / "
        f"{universe.get('limits', {}).get('tradingview_token_cap', 1000)}",
        f"- Rejected or unselected candidates: {len(universe.get('selection_audit', []))}",
        f"- Validation: {'PASS' if report['passed'] else 'FAIL'}",
        "",
        "## Roles",
        "",
        "| Role | Count |",
        "|---|---:|",
    ]
    for role, count in report["stats"]["roles"].items():
        lines.append(f"| {role} | {count} |")
    measurement = universe.get("measurement") or {}
    if measurement:
        lines.extend([
            "",
            "## How the metrics were produced",
            "",
            "| Metric | Basis | Method | Window |",
            "|---|---|---|---|",
        ])
        for field, entry in measurement.items():
            lines.append(
                f"| {field} | {entry['basis']} | {entry['method']} | {entry.get('window', '—')} |"
            )
    if report["warnings"]:
        lines.extend(["", "## Warnings", ""])
        lines.extend(f"- {warning}" for warning in report["warnings"])
    if report.get("maintenance"):
        maintenance = report["maintenance"]
        lines.extend([
            "",
            "## This review",
            "",
            f"- Depth: {maintenance['review_depth']}",
            f"- Turnover: {maintenance['turnover']:.1%}",
            f"- Added: {', '.join(maintenance['added']) or 'none'}",
            f"- Removed: {', '.join(maintenance['removed']) or 'none'}",
            f"- Deferred: {len(maintenance['deferred'])}",
        ])
    lines.extend([
        "",
        "## Members",
        "",
        "| Theme | Ticker | Name | Role | Reason | Evidence |",
        "|---|---|---|---|---|---|",
    ])
    for member in universe["members"]:
        theme = taxonomy[member["theme_code"]]
        evidence = member["evidence"][0]["url"] if member["evidence"] else ""
        reason = member.get("reason") or ""
        lines.append(
            f"| {member['theme_code']} {theme['theme_name']} | {member['ticker']} | "
            f"{member['name']} | {member['role']} | {reason} | {evidence} |"
        )
    return "\n".join(lines) + "\n"


def _write_atomic(output: str | Path, files: dict[str, str]) -> Path:
    destination = Path(output).resolve()
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists() and any(destination.iterdir()):
        raise UniverseError(f"output directory is not empty: {destination}")
    scratch = Path(tempfile.mkdtemp(prefix=f".{destination.name}-", dir=destination.parent))
    try:
        for name, content in files.items():
            (scratch / name).write_text(content, encoding="utf-8")
        if destination.exists():
            destination.rmdir()
        os.replace(scratch, destination)
    except Exception:
        shutil.rmtree(scratch, ignore_errors=True)
        raise
    return destination


def write_artifacts(
    universe: dict[str, Any], report: dict[str, Any], output: str | Path
) -> Path:
    files = {
        "universe.json": json.dumps(universe, ensure_ascii=False, indent=2) + "\n",
        "validation.json": json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        "universe.txt": render_txt(universe),
        "universe.md": render_markdown(universe, report),
    }
    return _write_atomic(output, files)


def apply_change_set(
    universe_raw: dict[str, Any],
    changes: dict[str, Any],
    policy: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    universe = deepcopy(universe_raw)
    current_report = validate_universe(universe, policy)
    if not current_report["passed"]:
        raise UniverseError("current universe is invalid: " + "; ".join(current_report["errors"]))
    if changes.get("schema_version") != 1:
        raise UniverseError("changes schema_version must be 1")
    if changes.get("market") != universe.get("market"):
        raise UniverseError("changes and universe markets differ")
    if changes.get("base_version_hash") != universe.get("version_hash"):
        raise UniverseError("stale change set: base_version_hash does not match")
    if changes.get("complete") is not True:
        raise UniverseError("maintenance facts are incomplete; refusing to update")
    if not changes.get("as_of"):
        raise UniverseError("maintenance as_of is required")
    sources = validate_evidence(changes.get("sources") or [], "maintenance")
    depth = str(changes.get("review_depth", ""))
    if depth not in policy["maintenance"]:
        raise UniverseError("review_depth must be routine, deep, or event")
    coverage_level = int(policy["profiles"][universe["profile"]]["coverage_level"])
    taxonomy_by_code = {item["theme_code"]: item for item in universe["taxonomy"]}
    members = universe["members"]
    before_members = {item["ticker"]: deepcopy(item) for item in members}
    before = set(before_members)

    def locate(ticker: str) -> tuple[int, dict[str, Any]]:
        normalized = str(ticker).strip().upper()
        for index, member in enumerate(members):
            if member["ticker"] == normalized:
                return index, member
        raise UniverseError(f"ticker is not in the universe: {ticker}")

    raw_ops = changes.get("ops") or []
    if not isinstance(raw_ops, list):
        raise UniverseError("changes ops must be a list")
    if not raw_ops:
        raise UniverseError("maintenance requires at least one op; use NO_CHANGE explicitly")
    ops = sorted(
        enumerate(raw_ops),
        key=lambda pair: (OP_ORDER.get(str(pair[1].get("op", "")).upper(), 99), pair[0]),
    )
    op_evidence: list[tuple[str, list[dict[str, Any]]]] = []
    for original_index, op in ops:
        name = str(op.get("op", "")).upper()
        if name not in OP_ORDER:
            raise UniverseError(f"op #{original_index}: unsupported op {name}")
        if name == "NO_CHANGE":
            if not str(op.get("reason", "")).strip():
                raise UniverseError(f"op #{original_index}: NO_CHANGE requires reason")
            continue
        evidence = op.get("evidence") or []
        reason = str(op.get("reason", "")).strip()
        subject = f"op #{original_index} {name}"
        if name in DECISION_OPS | THEME_OPS:
            if not evidence or not reason:
                raise UniverseError(f"{subject}: requires reason and evidence")
            evidence = validate_evidence(evidence, subject)
            require_strong_evidence(evidence, subject)
            op_evidence.append((subject, evidence))
        if name == "ADD_THEME":
            theme = {
                "l1_code": str(op.get("l1_code", "")).strip(),
                "l1_name": str(op.get("l1_name", "")).strip(),
                "theme_code": str(op.get("theme_code", "")).strip().upper(),
                "theme_name": str(op.get("theme_name", "")).strip(),
                "coverage_level": op.get("coverage_level"),
            }
            if theme["theme_code"] in taxonomy_by_code:
                raise UniverseError(f"{subject}: theme {theme['theme_code']} already exists")
            level = theme["coverage_level"]
            if level not in (1, 2, 3) or int(level) > coverage_level:
                raise UniverseError(
                    f"{subject}: coverage_level must be 1..{coverage_level} for this profile"
                )
            universe["taxonomy"] = normalize_taxonomy(universe["taxonomy"] + [theme])
            taxonomy_by_code = {item["theme_code"]: item for item in universe["taxonomy"]}
        elif name == "REMOVE_THEME":
            code = str(op.get("theme", "")).strip().upper()
            if code not in taxonomy_by_code:
                raise UniverseError(f"{subject}: unknown theme {code}")
            holders = [item["ticker"] for item in members if item["theme_code"] == code]
            if holders:
                raise UniverseError(
                    f"{subject}: move or remove its members first: {', '.join(holders)}"
                )
            universe["taxonomy"] = [
                item for item in universe["taxonomy"] if item["theme_code"] != code
            ]
            taxonomy_by_code = {item["theme_code"]: item for item in universe["taxonomy"]}
        elif name == "REMOVE":
            index, member = locate(op.get("ticker", ""))
            if member["role"] in {"BENCHMARK", "ANCHOR"} or member["required"]:
                raise UniverseError(f"op #{original_index}: anchor removal requires REPLACE")
            members.pop(index)
        elif name == "MOVE":
            _, member = locate(op.get("ticker", ""))
            destination = str(op.get("to_theme", "")).upper()
            if destination not in taxonomy_by_code:
                raise UniverseError(f"{subject}: unknown destination theme {destination}")
            member["theme_code"] = destination
            member["l1_code"] = taxonomy_by_code[destination]["l1_code"]
        elif name in {"ADD", "REPLACE"}:
            candidate_input = deepcopy(op.get("candidate") or {})
            candidate_input["evidence"] = deepcopy(evidence)
            candidate = normalize_candidate(
                universe["market"], candidate_input, taxonomy_by_code
            )
            if not candidate["eligible"]:
                raise UniverseError(f"op #{original_index}: candidate is not eligible")
            candidate["reason"] = reason or candidate["reason"]
            if name == "REPLACE":
                index, old = locate(op.get("ticker", ""))
                if (old["role"] in {"BENCHMARK", "ANCHOR"} or old["required"]) and not (
                    candidate["role"] in {"BENCHMARK", "ANCHOR"} or candidate["required"]
                ):
                    raise UniverseError(
                        f"op #{original_index}: anchor replacement must remain an anchor"
                    )
                members.pop(index)
            if any(item["asset_id"] == candidate["asset_id"] for item in members):
                raise UniverseError(f"{subject}: duplicate asset {candidate['asset_id']}")
            members.append(candidate)

    members.sort(key=lambda item: (item["theme_code"], rank_key(item)))
    after = {item["ticker"] for item in members}
    added = sorted(after - before)
    removed = sorted(before - after)
    audit = [
        item for item in universe.get("selection_audit", [])
        if item.get("ticker") not in set(added)
    ]
    audited_tickers = {item.get("ticker") for item in audit}
    for ticker in removed:
        if ticker not in audited_tickers:
            audit.append({
                "ticker": ticker,
                "asset_id": before_members[ticker]["asset_id"],
                "theme_code": before_members[ticker]["theme_code"],
                "reasons": ["removed_by_maintenance"],
            })
    universe["selection_audit"] = audit
    turnover = (len(added) + len(removed)) / max(len(before), 1)
    threshold = float(policy["maintenance"][depth]["turnover_warning"])
    extra_warnings: list[str] = []
    extra_errors: list[str] = []
    if turnover > threshold * 2:
        extra_errors.append(
            f"turnover {turnover:.1%} exceeds hard limit {threshold * 2:.1%} for {depth}"
        )
    elif turnover > threshold:
        extra_warnings.append(
            f"turnover {turnover:.1%} exceeds warning {threshold:.1%} for {depth}"
        )
    recently_removed = {
        asset
        for item in universe.get("history", [])[-4:]
        for asset in item.get("removed", [])
    }
    flip_flops = sorted(set(added) & recently_removed)
    if flip_flops:
        extra_warnings.append("recently removed tickers re-added: " + ", ".join(flip_flops))

    history_entry = {
        "as_of": str(changes.get("as_of", "")),
        "review_depth": depth,
        "summary": str(changes.get("summary", "")),
        "added": added,
        "removed": removed,
        "turnover": turnover,
        "deferred": deepcopy(changes.get("deferred") or []),
    }
    universe["as_of"] = history_entry["as_of"] or universe["as_of"]
    universe["source_as_of"] = str(changes["as_of"])
    universe["sources"] = sources
    universe["measurement"] = normalize_measurement(
        changes.get("measurement") or universe.get("measurement") or {},
        metrics_in_use(members),
    )
    extra_warnings.extend(
        staleness_warnings(
            str(changes["as_of"]), [("maintenance", sources)] + op_evidence, policy
        )
    )
    universe.setdefault("history", []).append(history_entry)
    universe["version_hash"] = universe_hash(universe)
    report = validate_universe(universe, policy)
    report["errors"] = report["errors"] + extra_errors
    report["warnings"] = report["warnings"] + extra_warnings
    report["passed"] = not report["errors"]
    report["maintenance"] = history_entry
    if not report["passed"]:
        raise UniverseError("maintenance failed validation: " + "; ".join(report["errors"]))
    return universe, report
