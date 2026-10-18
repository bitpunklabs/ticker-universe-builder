"""Evidence-gated Global composition of qualified market bundles and explicit references.

Offline contracts check supplied research; they do not establish factual leadership or fetch
new market data. The separately supplied coverage contract is the caller's trust boundary.
"""

from __future__ import annotations

import hashlib
import html
import json
import math
import re
from collections import Counter
from copy import deepcopy
from datetime import date
from pathlib import Path

from coverage_core import REFERENCE_KINDS, evidence, keyed, need, sentence
from universe_core import UniverseError, _write_atomic, load_policy, read_json, validate_universe
from watchlist_core import HEADER, SYMBOL, check_watchlist, render_watchlist

KINDS = REFERENCE_KINDS | {"equity", "perpetual"}
SAFE_ID = re.compile(r"[A-Z0-9][A-Z0-9_]{0,39}")
SOURCE_ID = re.compile(r"[a-z][a-z0-9_-]{0,39}")
FUND_LIMITS = {"broad": 0.25, "country": 0.65, "theme": 0.75}


def digest(value: object) -> str:
    return hashlib.sha256(
        json.dumps(
            value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False
        ).encode()
    ).hexdigest()


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def number(value, subject, minimum=0):
    need(
        type(value) in (int, float) and math.isfinite(value) and value >= minimum,
        subject + ": finite number required",
    )
    return value


def recent(value, as_of, days, subject):
    try:
        parsed = date.fromisoformat(value)
        age = (date.fromisoformat(as_of) - parsed).days
    except (ValueError, TypeError) as exc:
        raise UniverseError(f"global: {subject}: invalid ISO date") from exc
    need(
        parsed.isoformat() == value and 0 <= age <= days,
        f"{subject}: date must be within {days} days of {as_of}",
    )
    return value


def fields(value, required, optional, subject):
    need(isinstance(value, dict), subject + ": object required")
    need(
        set(required) <= set(value),
        subject + ": missing " + str(sorted(set(required) - set(value))),
    )
    need(set(value) <= set(required) | set(optional), subject + ": unknown fields")


def groups(rows, subject):
    result = keyed(rows, "id", subject)
    need(bool(result), subject + ": nonempty groups required")
    for key, row in result.items():
        fields(row, {"id", "name", "purpose"}, set(), subject)
        need(SAFE_ID.fullmatch(key) and sentence(row["purpose"]), subject + ": unsafe id/purpose")
        need(
            isinstance(row["name"], str) and HEADER.fullmatch(row["name"]),
            subject + ": ASCII export name required",
        )
        need(HEADER.fullmatch(key + "_" + row["name"]), subject + ": export header too long")
    return result


def contract_check(contract):
    fields(
        contract,
        {
            "schema_version",
            "kind",
            "scope",
            "scope_level",
            "markets",
            "themes",
            "duties",
            "source_themes",
        },
        {"required_tickers", "excluded_tickers", "etf_rules", "allow_peers"},
        "Global contract",
    )
    need(
        type(contract["schema_version"]) is int
        and contract["schema_version"] == 1
        and contract["kind"] == "global_coverage_contract",
        "Global contract schema/kind invalid",
    )
    need(
        contract["scope_level"] in {"global", "pilot", "synthetic"} and sentence(contract["scope"]),
        "scope and scope_level required",
    )
    need(type(contract.get("allow_peers", False)) is bool, "allow_peers must be boolean")
    tables = {
        "market": groups(contract["markets"], "markets"),
        "theme": groups(contract["themes"], "themes"),
    }
    duties = keyed(contract["duties"], "id", "duties")
    need(bool(duties), "coverage duties required independently of selected candidates")
    for key, duty in duties.items():
        fields(
            duty,
            {"id", "dimension", "group", "purpose", "allowed_kinds", "minimum"},
            {"leader_minimum"},
            "duty " + key,
        )
        need(SAFE_ID.fullmatch(key) and duty["dimension"] in tables, "invalid duty identity")
        need(
            duty["group"] in tables[duty["dimension"]] and sentence(duty["purpose"]),
            key + ": known group and purpose required",
        )
        kinds = duty["allowed_kinds"]
        need(
            isinstance(kinds, list)
            and bool(kinds)
            and all(k in KINDS for k in kinds)
            and len(kinds) == len(set(kinds)),
            key + ": invalid allowed_kinds",
        )
        need(type(duty["minimum"]) is int and duty["minimum"] >= 1, key + ": positive minimum")
        leader_min = duty.get("leader_minimum", 0)
        need(
            type(leader_min) is int and 0 <= leader_min <= duty["minimum"],
            key + ": invalid leader_minimum",
        )
        if duty["dimension"] == "market":
            need(set(kinds) <= {"index", "etf"}, key + ": market duties require index/ETF gauges")
    for dimension, table in tables.items():
        need(
            {d["group"] for d in duties.values() if d["dimension"] == dimension} == set(table),
            dimension + ": every declared group needs a frozen duty",
        )
    for key in ("required_tickers", "excluded_tickers"):
        rows = contract.get(key, [])
        need(
            isinstance(rows, list)
            and all(isinstance(t, str) and SYMBOL.fullmatch(t) for t in rows)
            and len(rows) == len(set(rows)),
            key + ": unique full tickers required",
        )
    need(
        not set(contract.get("required_tickers", [])) & set(contract.get("excluded_tickers", [])),
        "required and excluded tickers conflict",
    )
    rules = {
        "min_aum_usd": 1e9,
        "min_turnover_usd": 1e7,
        "max_spread_pct": 0.15,
        "max_fee_pct": FUND_LIMITS.copy(),
    }
    custom = contract.get("etf_rules", {})
    fields(custom, set(), set(rules), "etf_rules")
    for key in ("min_aum_usd", "min_turnover_usd", "max_spread_pct"):
        if key in custom:
            value = number(custom[key], key)
            need(
                value >= rules[key] if key.startswith("min") else 0 < value <= rules[key],
                key + ": may tighten, not weaken the Global floor",
            )
            rules[key] = value
    if "max_fee_pct" in custom:
        fees = custom["max_fee_pct"]
        need(isinstance(fees, dict) and set(fees) == set(FUND_LIMITS), "all fee classes required")
        for key, maximum in FUND_LIMITS.items():
            need(0 < number(fees[key], key) <= maximum, key + ": fee ceiling cannot be weakened")
        rules["max_fee_pct"] = fees
    lineage = keyed(contract.get("source_themes", []), "id", "source theme dispositions")
    for row in lineage.values():
        fields(row, {"id", "disposition", "reason", "themes"}, set(), "source theme disposition")
        need(
            row["disposition"] in {"mapped", "out_of_scope"} and sentence(row["reason"]),
            "source theme disposition must be resolved",
        )
        need(
            isinstance(row["themes"], list)
            and len(row["themes"]) == len(set(row["themes"]))
            and all(t in tables["theme"] for t in row["themes"])
            and (bool(row["themes"]) if row["disposition"] == "mapped" else not row["themes"]),
            "source theme mapping invalid",
        )
    return duties, rules


def metric(record, ev, as_of, days, subject):
    fields(record, {"value", "as_of", "source"}, set(), subject)
    value = number(record["value"], subject)
    recent(record["as_of"], as_of, days, subject)
    need(
        any(
            e["url"] == record["source"] and e["as_of"] == record["as_of"] and e["tier"] in (1, 2)
            for e in ev
        ),
        subject + ": missing matching dated evidence",
    )
    return value


def fund_check(fund, ticker, ev, as_of, rules):
    fields(
        fund,
        {
            "ticker",
            "category",
            "benchmark_id",
            "exposure_group",
            "structure",
            "inception",
            "assets_usd",
            "gross_fee_pct",
            "spread_pct",
            "holdings_as_of",
            "holdings_source",
            "holdings",
            "activity",
        },
        set(),
        ticker + " fund",
    )
    need(fund["ticker"] == ticker, ticker + ": fund product ticker mismatch")
    need(
        fund["category"] in FUND_LIMITS and fund["structure"] == "unlevered_equity",
        ticker + ": default Global funds must be unlevered equity baskets",
    )
    need(
        all(
            isinstance(fund[k], str) and re.fullmatch(r"[A-Z0-9][A-Z0-9_:./-]*", fund[k])
            for k in ("benchmark_id", "exposure_group")
        ),
        ticker + ": benchmark/exposure identities required",
    )
    recent(fund["inception"], as_of, 50000, ticker + " inception")
    age = (date.fromisoformat(as_of) - date.fromisoformat(fund["inception"])).days
    need(age >= 365, ticker + ": at least 12 months live fund history required")
    aum = metric(fund["assets_usd"], ev, as_of, 30, ticker + " assets")
    fee = metric(fund["gross_fee_pct"], ev, as_of, 180, ticker + " fee")
    spread = metric(fund["spread_pct"], ev, as_of, 30, ticker + " spread")
    need(aum >= rules["min_aum_usd"], ticker + ": fund assets below floor")
    need(fee <= rules["max_fee_pct"][fund["category"]], ticker + ": fund fee above ceiling")
    need(spread <= rules["max_spread_pct"], ticker + ": fund spread above ceiling")
    recent(fund["holdings_as_of"], as_of, 30, ticker + " holdings")
    need(
        any(
            e["url"] == fund["holdings_source"]
            and e["as_of"] == fund["holdings_as_of"]
            and e["tier"] in (1, 2)
            for e in ev
        ),
        ticker + ": holdings evidence missing",
    )
    holdings = keyed(fund["holdings"], "entity_id", ticker + " holdings")
    need(bool(holdings), ticker + ": full issuer-normalized equity holdings required")
    for row in holdings.values():
        fields(row, {"entity_id", "weight"}, set(), ticker + " holding")
        need(
            re.fullmatch(r"[A-Z0-9][A-Z0-9_:./-]*", row["entity_id"]),
            ticker + ": canonical holding issuer identity required",
        )
        need(0 < number(row["weight"], ticker + " weight") <= 1, ticker + ": invalid weight")
    total = sum(h["weight"] for h in holdings.values())
    need(0.98 <= total <= 1.02, ticker + ": full holdings must sum near one, not a top-ten sample")
    activity = fund["activity"]
    fields(
        activity,
        {"source", "as_of", "currency", "method", "data_sha256", "observations"},
        set(),
        ticker + " activity",
    )
    need(
        activity["currency"] == "USD"
        and activity["method"]
        in {
            "source_reported_notional",
            "close_times_shares_proxy",
            "local_notional_converted_to_usd",
        },
        ticker + ": explicit USD notional convention required",
    )
    recent(activity["as_of"], as_of, 14, ticker + " activity")
    need(
        any(
            e["url"] == activity["source"]
            and e["as_of"] == activity["as_of"]
            and e["tier"] in (1, 2)
            for e in ev
        ),
        ticker + ": turnover evidence missing",
    )
    observations = activity["observations"]
    need(
        isinstance(observations, list) and len(observations) == 30,
        ticker + ": exactly 30 completed-session notional observations required",
    )
    need(digest(observations) == activity["data_sha256"], ticker + ": turnover input hash mismatch")
    sessions = []
    for row in observations:
        fields(row, {"date", "notional_usd"}, set(), ticker + " session")
        sessions.append(recent(row["date"], activity["as_of"], 90, ticker + " session"))
        number(row["notional_usd"], ticker + " session notional")
    need(
        sessions == sorted(set(sessions)) and sessions[-1] == activity["as_of"],
        ticker + ": duplicate, unordered or incomplete final session",
    )
    mean = sum(row["notional_usd"] for row in observations) / 30
    need(mean >= rules["min_turnover_usd"], ticker + ": measured turnover below floor")
    return {
        "assets_usd": aum,
        "gross_fee_pct": fee,
        "spread_pct": spread,
        "mean_turnover_usd": mean,
        "holdings": {key: row["weight"] / total for key, row in holdings.items()},
    }


def source_rows(source, declaration, as_of, policy):
    recent(source.get("as_of"), as_of, 30, declaration["id"] + " source")
    if declaration["kind"] == "universe":
        checked = validate_universe(source, policy)
        need(
            checked["passed"] and checked.get("qualified"),
            declaration["id"] + ": source universe must independently qualify",
        )
        need(source.get("selection_model") == "coverage_first", "legacy sources are not Global")
        rows = [(r, "entity") for r in source["members"]]
        rows += [(r, "reference") for r in source["coverage_plan"]["references"]]
    else:
        fields(source, {"schema_version", "kind", "as_of", "references"}, set(), "catalog")
        need(
            type(source["schema_version"]) is int
            and source["schema_version"] == 1
            and source["kind"] == "global_reference_catalog",
            "catalog schema/kind invalid",
        )
        rows = [
            (r, "reference") for r in keyed(source["references"], "ticker", "references").values()
        ]
    result = {}
    for row, role in rows:
        need(row["ticker"] not in result, "duplicate source ticker")
        result[row["ticker"]] = (row, role)
    return result


def evaluate(spec, contract, sources, policy=None):
    """Resolve exact source rows, recompute research gates and build deterministic composition."""
    fields(
        spec,
        {"schema_version", "kind", "as_of", "sources", "identities", "selections"},
        {"coexistence_reviews"},
        "Global spec",
    )
    need(
        type(spec["schema_version"]) is int
        and spec["schema_version"] == 1
        and spec["kind"] == "global_spec",
        "invalid Global spec",
    )
    as_of = spec["as_of"]
    recent(as_of, str(date.today()), 50000, "composition as_of")
    duties, rules = contract_check(contract)
    declarations = keyed(spec["sources"], "id", "sources")
    need(bool(declarations) and set(declarations) == set(sources), "source inventory mismatch")
    lookups = {}
    for key, declaration in declarations.items():
        fields(declaration, {"id", "kind", "file", "sha256"}, set(), "source " + key)
        need(
            SOURCE_ID.fullmatch(key) and declaration["kind"] in {"universe", "catalog"},
            "invalid source id/kind",
        )
        lookups[key] = source_rows(sources[key], declaration, as_of, policy or load_policy())
    identities = keyed(spec["identities"], "ticker", "global identities")
    for ticker, identity in identities.items():
        fields(
            identity,
            {
                "ticker",
                "entity_id",
                "name",
                "economic_market",
                "coverage_type",
                "legal_ids",
                "evidence",
            },
            set(),
            ticker + " identity",
        )
        need(
            SYMBOL.fullmatch(ticker)
            and sentence(identity["entity_id"])
            and re.fullmatch(r"[A-Z0-9][A-Z0-9_:./-]*", identity["entity_id"])
            and sentence(identity["name"]),
            ticker + ": invalid identity",
        )
        need(
            identity["economic_market"] in {g["id"] for g in contract["markets"]},
            ticker + ": unknown economic market",
        )
        need(
            identity["coverage_type"] in {"entity", "market", "style", "theme", "macro"},
            ticker + ": invalid coverage_type",
        )
        legal = identity["legal_ids"]
        need(
            isinstance(legal, list)
            and all(
                isinstance(k, str) and re.fullmatch(r"[A-Z0-9][A-Z0-9_:./-]*", k) for k in legal
            )
            and len(legal) == len(set(legal)),
            ticker + ": invalid legal identifiers",
        )
        evidence(identity["evidence"], ticker + " global identity", as_of)
    entries = keyed(spec["selections"], "ticker", "selections")
    need(bool(entries), "Global selection is empty")
    members, seen_entities, seen_legal, funds = [], set(), {}, {}
    for ticker, entry in entries.items():
        fields(
            entry,
            {"ticker", "source", "market", "theme", "duties", "reason", "evidence"},
            set(),
            ticker + " selection",
        )
        need(
            entry["source"] in lookups and ticker in lookups[entry["source"]],
            ticker + ": exact ticker absent from declared source",
        )
        need(
            ticker in identities and sentence(entry["reason"]), ticker + ": identity/reason missing"
        )
        identity = identities[ticker]
        need(entry["market"] == identity["economic_market"], ticker + ": listing/economic mix-up")
        need(entry["theme"] in {g["id"] for g in contract["themes"]}, ticker + ": unknown theme")
        evidence(entry["evidence"], ticker + " selection", as_of)
        row, role = lookups[entry["source"]][ticker]
        ev = evidence(row.get("evidence"), ticker, as_of)
        kind, leader = row.get("kind"), False
        if role == "entity":
            admission = row["admission"]
            allowed = {"leader", "peer"} if contract.get("allow_peers", False) else {"leader"}
            need(admission["kind"] in allowed, ticker + ": Global requires a researched leader")
            kind = admission["instrument"]["kind"]
            need(
                kind in {"equity", "spot", "perpetual"} and identity["coverage_type"] == "entity",
                ticker + ": entity/reference confusion",
            )
            recent(row["listing"]["as_of"], as_of, 30, ticker + " listing")
            recent(row["measurement_record"]["last_session"], as_of, 30, ticker + " measurement")
            leader = admission["kind"] == "leader"
        else:
            need(
                not ticker.startswith(("BINANCE:", "OKX:")),
                ticker + ": protocol instrument must come from an entity universe",
            )
            need(
                kind in REFERENCE_KINDS and identity["coverage_type"] != "entity",
                ticker + ": company/protocol cannot be a reference",
            )
            if declarations[entry["source"]]["kind"] == "catalog":
                fields(
                    row,
                    {
                        "ticker",
                        "name",
                        "kind",
                        "observes",
                        "evidence",
                        "verified_ticker",
                        "verified_as_of",
                    },
                    {"fund"},
                    ticker + " reference",
                )
                need(
                    row["verified_ticker"] == ticker
                    and sentence(row["observes"])
                    and row["name"] == identity["name"],
                    ticker + ": reference product mismatch",
                )
                recent(row["verified_as_of"], as_of, 30, ticker + " symbol verification")
                need(
                    any(e["as_of"] == row["verified_as_of"] and e["tier"] in (1, 2) for e in ev),
                    ticker + ": dated symbol evidence missing",
                )
                need(kind != "spot", ticker + ": protocol spot belongs in an entity universe")
            if kind == "etf":
                funds[ticker] = fund_check(row.get("fund"), ticker, ev, as_of, rules)
        entity_id = identity["entity_id"]
        need(entity_id not in seen_entities, ticker + ": duplicate global economic identity")
        seen_entities.add(entity_id)
        for legal_id in identity["legal_ids"]:
            need(legal_id not in seen_legal, ticker + ": duplicate legal issuer identifier")
            seen_legal[legal_id] = ticker
        claimed = entry["duties"]
        need(
            isinstance(claimed, list)
            and bool(claimed)
            and all(k in duties for k in claimed)
            and len(claimed) == len(set(claimed)),
            ticker + ": invalid coverage claims",
        )
        for key in claimed:
            duty = duties[key]
            need(
                entry[duty["dimension"]] == duty["group"] and kind in duty["allowed_kinds"],
                ticker + ": duty conflicts with group/instrument " + key,
            )
            if duty["dimension"] == "market":
                need(
                    identity["coverage_type"] in {"market", "style"},
                    ticker + ": sector/company does not satisfy a broad-market duty",
                )
        members.append(
            {
                **deepcopy(entry),
                "entity_id": entity_id,
                "name": identity["name"],
                "kind": kind,
                "leader": leader,
                "source_row_sha256": digest(row),
            }
        )
    tickers = set(entries)
    need(set(contract.get("required_tickers", [])) <= tickers, "required ticker missing")
    need(not set(contract.get("excluded_tickers", [])) & tickers, "excluded ticker selected")
    coverage = {}
    for key, duty in duties.items():
        held = [r for r in members if key in r["duties"]]
        count, leaders = len(held), sum(r["leader"] for r in held)
        need(
            count >= duty["minimum"] and leaders >= duty.get("leader_minimum", 0),
            key + ": missing mandatory coverage or actual leaders",
        )
        coverage[key] = {"tickers": [r["ticker"] for r in held], "leaders": leaders}
    lineage = keyed(contract["source_themes"], "id", "source themes")
    expected_lineage = {
        source_id + ":" + theme["theme_code"]
        for source_id, source in sources.items()
        if declarations[source_id]["kind"] == "universe"
        for theme in source["taxonomy"]
    }
    need(set(lineage) == expected_lineage, "source theme ledger missing or has invented themes")
    for key, disposition in lineage.items():
        source_id, code = key.split(":", 1)
        selected = [
            r
            for r in members
            if r["source"] == source_id and lookups[source_id][r["ticker"]][0]["theme_code"] == code
        ]
        need(
            bool(selected) if disposition["disposition"] == "mapped" else not selected,
            key + ": source theme disposition contradicts selection",
        )
        need(
            all(r["theme"] in disposition["themes"] for r in selected),
            key + ": selected theme absent from lineage mapping",
        )
    overlap = overlap_check(spec, sources, entries, funds, as_of)
    return {
        "schema_version": 1,
        "kind": "global_composition",
        "as_of": as_of,
        "contract_sha256": digest(contract),
        "scope": contract["scope"],
        "scope_level": contract["scope_level"],
        "spec": deepcopy(spec),
        "members": members,
        "coverage": coverage,
        "fund_reviews": funds,
        "fund_overlap": overlap,
        "source_cutoffs": {key: source["as_of"] for key, source in sources.items()},
    }


def overlap_check(spec, sources, entries, funds, as_of):
    reviews = {}
    for review in spec.get("coexistence_reviews", []):
        fields(review, {"pair", "reason", "evidence"}, set(), "coexistence review")
        pair = review["pair"]
        need(
            isinstance(pair, list)
            and len(pair) == 2
            and len(set(pair)) == 2
            and all(t in funds for t in pair),
            "coexistence needs two selected funds",
        )
        key = tuple(sorted(pair))
        need(
            key not in reviews and sentence(review["reason"]), "duplicate/empty coexistence review"
        )
        evidence(review["evidence"], "ETF coexistence", as_of)
        a, b = (set(entries[t]["duties"]) for t in pair)
        need(bool(a - b) and bool(b - a), "coexisting funds need distinct observation duties")
        reviews[key] = review
    output, used = [], set()
    codes = sorted(funds)
    for i, left in enumerate(codes):
        for right in codes[i + 1 :]:
            a, b = funds[left]["holdings"], funds[right]["holdings"]
            share = sum(min(weight, b.get(key, 0)) for key, weight in a.items())
            rows = []
            for ticker in (left, right):
                source = sources[entries[ticker]["source"]]
                candidates = source.get(
                    "references", source.get("coverage_plan", {}).get("references", [])
                )
                rows.append(next(r["fund"] for r in candidates if r["ticker"] == ticker))
            same_job = rows[0]["exposure_group"] == rows[1]["exposure_group"]
            need(
                rows[0]["benchmark_id"] != rows[1]["benchmark_id"],
                f"{left}/{right}: duplicate benchmark wrappers cannot both enter Global",
            )
            gap = abs(
                (
                    date.fromisoformat(rows[0]["holdings_as_of"])
                    - date.fromisoformat(rows[1]["holdings_as_of"])
                ).days
            )
            need(gap <= 7, f"{left}/{right}: holdings dates not comparable within seven days")
            key = (left, right)
            flagged = same_job or share >= 0.8
            if flagged:
                need(
                    key in reviews, f"{left}/{right}: overlapping ETF jobs need coexistence review"
                )
                used.add(key)
            output.append(
                {
                    "pair": list(key),
                    "holdings_overlap": share,
                    "same_exposure_group": same_job,
                    "holdings_date_gap_days": gap,
                    "reviewed": key in reviews,
                }
            )
    need(set(reviews) == used, "coexistence review must resolve an actual flagged pair")
    return output


def exports(composition, contract):
    rows = composition["members"]
    return {
        "watchlist": render_watchlist(rows),
        "by_theme": render_watchlist(rows, contract["themes"], "theme"),
        "by_market": render_watchlist(rows, contract["markets"], "market"),
    }


def report(composition, contract):
    views = exports(composition, contract)
    counts = Counter(r["kind"] for r in composition["members"])
    return {
        "passed": True,
        "qualified": True,
        "errors": [],
        "scope_level": composition["scope_level"],
        "contract_sha256": digest(contract),
        "symbols": len(composition["members"]),
        "kinds": dict(counts),
        "duties": len(composition["coverage"]),
        "watchlists": {
            key: check_watchlist(text, ticker_only=key == "watchlist")
            for key, text in views.items()
        },
        "warnings": [
            "Validation checks supplied research, not factual leadership or alpha.",
            "No TradingView UI import or account/feed entitlement validation.",
            "Source dates are inherited; composition does not refresh market facts.",
        ]
        + (
            ["Bounded pilot/synthetic scope; not a worldwide production universe."]
            if composition["scope_level"] != "global"
            else []
        ),
    }


def _load_sources(spec, base):
    sources, texts = {}, {}
    for declaration in keyed(spec["sources"], "id", "sources").values():
        path = (base / declaration["file"]).resolve()
        raw = path.read_bytes()
        need(
            hashlib.sha256(raw).hexdigest() == declaration["sha256"],
            declaration["id"] + ": source hash changed",
        )
        sources[declaration["id"]] = json.loads(raw)
        texts[declaration["id"]] = raw.decode("utf-8")
    return sources, texts


def _readable(composition, checked, stem):
    def safe(value):
        return str(value).replace("|", "\\|").replace("\n", " ")

    lines = [
        "# Global observation universe",
        "",
        "Scope: " + safe(composition["scope"]),
        "",
        f"As of {composition['as_of']}; {checked['symbols']} instruments; "
        f"scope level: {composition['scope_level']}.",
        "",
        *["- " + warning for warning in checked["warnings"]],
        "",
        "Source dates: " + safe(json.dumps(composition["source_cutoffs"])),
        "",
        "| Ticker | Name | Kind | Market | Theme | Reason |",
        "|---|---|---|---|---|---|",
    ]
    for row in composition["members"]:
        lines.append(
            "| "
            + " | ".join(
                safe(row[k]) for k in ("ticker", "name", "kind", "market", "theme", "reason")
            )
            + " |"
        )
    markdown = "\n".join(lines) + "\n"
    body = "".join(
        "<tr>"
        + "".join(
            f"<td>{html.escape(str(row[k]))}</td>"
            for k in ("ticker", "name", "kind", "market", "theme")
        )
        + "</tr>"
        for row in composition["members"]
    )
    page = (
        '<!doctype html><html lang="en"><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        "<title>Global observation universe</title><style>"
        "body{max-width:1100px;margin:30px auto;padding:0 16px;font:16px/1.5 system-ui}"
        "td,th{text-align:left;padding:8px;border-bottom:1px solid #ccc}table{width:100%}"
        ".table{overflow:auto}p{overflow-wrap:anywhere}</style>"
        "<h1>Global observation universe</h1><p>"
        + html.escape(composition["scope"])
        + f"</p><p>Scope: {composition['scope_level']}. Instruments: {checked['symbols']}.</p>"
        + "".join("<p>" + html.escape(w) + "</p>" for w in checked["warnings"])
        + f'<p><a href="{stem}.txt">Ticker-only TXT</a> · '
        + f'<a href="{stem}.json">JSON</a> · <a href="{stem}.validation.json">Validation</a></p>'
        + '<div class="table"><table><tr><th>Ticker</th><th>Name</th><th>Kind</th>'
        "<th>Market</th><th>Theme</th></tr>" + body + "</table></div></html>"
    )
    return markdown, page


def compose(spec_path, contract_path, output, policy=None):
    spec_path, contract_path = Path(spec_path).resolve(), Path(contract_path).resolve()
    spec, contract = read_json(spec_path), read_json(contract_path)
    sources, texts = _load_sources(spec, spec_path.parent)
    portable = deepcopy(spec)
    for row in portable["sources"]:
        need(isinstance(row["id"], str) and SOURCE_ID.fullmatch(row["id"]), "unsafe source id")
        row["file"] = f"source-{row['id']}.json"
    composition = evaluate(portable, contract, sources, policy)
    composition["content_sha256"] = digest(composition)
    checked = report(composition, contract)
    stem = "global-" + composition["as_of"]

    def dump(value):
        return json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n"

    files = {
        stem + ".json": dump(composition),
        stem + ".validation.json": dump(checked),
        "global-contract.json": contract_path.read_text(encoding="utf-8"),
    }
    for key, text in exports(composition, contract).items():
        suffix = {"watchlist": "", "by_theme": "-by-theme", "by_market": "-by-market"}[key]
        files[stem + suffix + ".txt"] = text
    files[stem + ".en.md"], files[stem + ".en.html"] = _readable(composition, checked, stem)
    files.update({f"source-{key}.json": text for key, text in texts.items()})
    destination = _write_atomic(output, files)
    return {
        "status": "complete",
        "scope_level": composition["scope_level"],
        "validation_passed": True,
        "symbols": checked["symbols"],
        "artifacts": {
            "universe": str(destination / (stem + ".json")),
            "watchlist": str(destination / (stem + ".txt")),
            "by_theme": str(destination / (stem + "-by-theme.txt")),
            "by_market": str(destination / (stem + "-by-market.txt")),
            "validation": str(destination / (stem + ".validation.json")),
            "report": str(destination / (stem + ".en.md")),
            "html": str(destination / (stem + ".en.html")),
            "contract": str(destination / "global-contract.json"),
        },
        "artifact_sha256": {
            str(destination / name): file_hash(destination / name) for name in files
        },
        "warnings": checked["warnings"],
    }


def validate(path, contract_path, policy=None):
    """Reopen sources and the caller's expected contract; never trust stored validation flags."""
    try:
        path = Path(path).resolve()
        stored, contract = read_json(path), read_json(contract_path)
        need(
            stored.get("contract_sha256") == digest(contract), "expected coverage contract changed"
        )
        unsigned = {k: v for k, v in stored.items() if k != "content_sha256"}
        need(stored.get("content_sha256") == digest(unsigned), "Global content hash mismatch")
        spec = stored["spec"]
        for row in spec["sources"]:
            need(
                SOURCE_ID.fullmatch(row["id"]) and row["file"] == f"source-{row['id']}.json",
                "published source paths must be local, portable copies",
            )
        sources, _ = _load_sources(spec, path.parent)
        recomputed = evaluate(spec, contract, sources, policy)
        need(recomputed == unsigned, "stored composition differs from recomputed source selection")
        for key, text in exports(recomputed, contract).items():
            suffix = {"watchlist": "", "by_theme": "-by-theme", "by_market": "-by-market"}[key]
            need(
                (path.parent / (path.stem + suffix + ".txt")).read_bytes().decode("utf-8") == text,
                key + ": published TXT differs from exact validated composition",
            )
        return report(recomputed, contract)
    except (UniverseError, OSError, ValueError, TypeError, KeyError, AttributeError) as exc:
        return {"passed": False, "qualified": False, "errors": [str(exc)], "warnings": []}
