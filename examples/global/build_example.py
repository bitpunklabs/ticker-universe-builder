"""Replay a bounded five-market Global pilot from existing dated research, not a world screen."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "scripts"))
from global_core import compose, file_hash, validate  # noqa: E402
from global_core_view import compose as compose_core  # noqa: E402
from global_core_view import validate as validate_core  # noqa: E402
from global_watchlist import export as export_view  # noqa: E402
from global_watchlist import validate as validate_view  # noqa: E402

AS_OF = "2026-10-18"
SOURCES = {
    "us": "us-light/output/us-light-2026-10-08.json",
    "cn": "cn-medium/output/cn-medium-2026-10-08.json",
    "jp": "jp-medium/output/jp-medium-2026-10-07.json",
    "hk": "hk-medium/output/hk-medium-2026-10-08.json",
    "kr": "kr-medium/output/kr-medium-2026-10-07.json",
}
# Authored research selections, not hand-written final watchlists. Source rows remain authoritative.
SELECTIONS = [
    ("us", "NASDAQ:NVDA", "US", "SEMI", "NVIDIA"),
    ("us", "NASDAQ:AVGO", "US", "SEMI", "Broadcom"),
    ("us", "NASDAQ:MSFT", "US", "PLATFORMS", "Microsoft"),
    ("us", "NASDAQ:GOOGL", "US", "PLATFORMS", "Alphabet"),
    ("us", "NYSE:JPM", "US", "FINANCE", "JPMorgan Chase"),
    ("us", "NYSE:XOM", "US", "RESOURCES", "Exxon Mobil"),
    ("cn", "SSE:600519", "CN", "CONSUMER", "Kweichow Moutai"),
    ("cn", "SSE:601899", "CN", "RESOURCES", "Zijin Mining"),
    ("cn", "SZSE:300750", "CN", "BATTERIES", "CATL"),
    ("jp", "TSE:7203", "JP", "INDUSTRY", "Toyota Motor"),
    ("jp", "TSE:8035", "JP", "SEMI", "Tokyo Electron"),
    ("jp", "TSE:6861", "JP", "INDUSTRY", "Keyence"),
    ("hk", "HKEX:700", "HK", "PLATFORMS", "Tencent"),
    ("hk", "HKEX:9988", "HK", "PLATFORMS", "Alibaba"),
    ("kr", "KRX:000660", "KR", "SEMI", "SK hynix"),
    ("kr", "KRX:005930", "KR", "SEMI", "Samsung Electronics"),
    ("us", "SP:SPX", "US", "GAUGES", "S&P 500"),
    ("cn", "SSE:000300", "CN", "GAUGES", "CSI 300"),
    ("refs", "TSE:TOPIX", "JP", "GAUGES", "TOPIX"),
    ("refs", "HSI:HSI", "HK", "GAUGES", "Hang Seng Index"),
    ("refs", "KRX:KOSPI", "KR", "GAUGES", "KOSPI"),
]


def inputs(destination, fund_catalog=None, source_root=None):
    source_root = Path(source_root) if source_root else ROOT / "examples"
    loaded, sources = {}, []
    for key, relative in SOURCES.items():
        path = source_root / relative
        if not path.exists():
            raise ValueError("Recreate worked sources first: python examples/build_examples.py")
        loaded[key] = json.loads(path.read_text())
        sources.append(dict(id=key, kind="universe", file=str(path), sha256=file_hash(path)))
    catalog = BASE / "reference-catalog.json"
    loaded["refs"] = json.loads(catalog.read_text())
    sources.append(dict(id="refs", kind="catalog", file=str(catalog), sha256=file_hash(catalog)))
    choices = list(SELECTIONS)
    if fund_catalog:
        path = Path(fund_catalog).resolve()
        loaded["funds"] = json.loads(path.read_text())
        sources.append(dict(id="funds", kind="catalog", file=str(path), sha256=file_hash(path)))
        choices.append(("funds", "NASDAQ:SOXX", "US", "SEMI", "iShares Semiconductor ETF"))
    markets = sorted({row[2] for row in choices})
    themes = sorted({row[3] for row in choices})
    contract = dict(
        schema_version=1,
        kind="global_coverage_contract",
        scope_level="pilot",
        scope="Bounded CN/US/JP/HK/KR pilot; dated company research and index identity checks. "
        "Not a completed worldwide universe or refreshed leadership census.",
        markets=[dict(id=k, name=k, purpose="Native market observation") for k in markets],
        themes=[
            dict(id=k, name=k, purpose="Dated representative business observation") for k in themes
        ],
        duties=[
            dict(
                id=k + "_MARKET",
                dimension="market",
                group=k,
                purpose="Broad native equity-market gauge",
                allowed_kinds=["index"],
                minimum=1,
            )
            for k in markets
        ]
        + [
            dict(
                id=k + "_DUTY",
                dimension="theme",
                group=k,
                purpose="Preserve this pilot's explicit observation role",
                allowed_kinds=["index"] if k == "GAUGES" else ["equity", "etf"],
                minimum=1,
                leader_minimum=0 if k == "GAUGES" else 1,
            )
            for k in themes
        ],
        source_themes=[],
    )
    spec = dict(
        schema_version=1,
        kind="global_spec",
        as_of=AS_OF,
        sources=sources,
        identities=[],
        selections=[],
    )
    mapped = defaultdict(set)
    for key, ticker, market, theme, name in choices:
        source = loaded[key]
        rows = source.get("members", []) + source.get("coverage_plan", {}).get("references", [])
        rows += source.get("references", [])
        row = next(r for r in rows if r["ticker"] == ticker)
        is_entity = "asset_id" in row
        ev = row["admission"]["evidence"] if is_entity else row["evidence"]
        spec["identities"].append(
            dict(
                ticker=ticker,
                entity_id=("ISSUER:" if is_entity else "GAUGE:")
                + {
                    "NASDAQ:NVDA": "NVIDIA",
                    "NASDAQ:AVGO": "BROADCOM",
                    "NASDAQ:MSFT": "MICROSOFT",
                    "NASDAQ:GOOGL": "ALPHABET",
                    "NYSE:JPM": "JPMORGAN",
                    "NYSE:XOM": "EXXON_MOBIL",
                    "SSE:600519": "MOUTAI",
                    "SSE:601899": "ZIJIN",
                    "SZSE:300750": "CATL",
                    "TSE:7203": "TOYOTA",
                    "TSE:8035": "TOKYO_ELECTRON",
                    "TSE:6861": "KEYENCE",
                    "HKEX:700": "TENCENT",
                    "HKEX:9988": "ALIBABA",
                    "KRX:000660": "SK_HYNIX",
                    "KRX:005930": "SAMSUNG_ELECTRONICS",
                    "SP:SPX": "SP500",
                    "SSE:000300": "CSI300",
                    "TSE:TOPIX": "TOPIX",
                    "HSI:HSI": "HSI",
                    "KRX:KOSPI": "KOSPI",
                    "NASDAQ:SOXX": "SOXX_FUND",
                }[ticker],
                name=name,
                economic_market=market,
                coverage_type="entity" if is_entity else "market" if theme == "GAUGES" else "theme",
                legal_ids=[],
                evidence=ev,
            )
        )
        reason = row.get("reason_summary") or row.get("observes") or row.get("reason")
        reason = source.get("report_translations", {}).get("en", {}).get(reason, reason)
        spec["selections"].append(
            dict(
                ticker=ticker,
                source=key,
                market=market,
                theme=theme,
                duties=(
                    [market + "_MARKET", "GAUGES_DUTY"] if theme == "GAUGES" else [theme + "_DUTY"]
                ),
                reason=reason,
                evidence=ev,
            )
        )
        if key in SOURCES:
            mapped[key + ":" + row["theme_code"]].add(theme)
    for key in SOURCES:
        for theme in loaded[key]["taxonomy"]:
            code = key + ":" + theme["theme_code"]
            targets = sorted(mapped[code])
            contract["source_themes"].append(
                dict(
                    id=code,
                    disposition="mapped" if targets else "out_of_scope",
                    themes=targets,
                    reason="Retain selected source duty in the bounded pilot."
                    if targets
                    else "Outside this bounded pilot; original theme and research retained.",
                )
            )
    if fund_catalog:
        contract["required_tickers"] = ["NASDAQ:SOXX"]
    destination.mkdir(parents=True, exist_ok=True)
    for filename, value in [("global-spec.json", spec), ("coverage-contract.json", contract)]:
        (destination / filename).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    return destination / "global-spec.json", destination / "coverage-contract.json"


def observation_view(universe, contract, destination):
    """Author this bounded pilot's display input, then use the maintained exporter."""
    path = Path(universe)
    members = json.loads(path.read_text())["members"]
    sections = []

    def section(code, name, rows):
        if rows:
            sections.append(dict(id=code, name=name, tickers=[r["ticker"] for r in rows]))

    section("I01", "CORE_INDICES_US_CHINA", [r for r in members
            if r["kind"] == "index" and r["market"] in {"US", "CN"}])
    section("I02", "INDICES_ASIA_JAPAN_HK_KOREA", [r for r in members
            if r["kind"] == "index" and r["market"] not in {"US", "CN"}])
    section("E01", "ETF_SEMICONDUCTORS", [r for r in members if r["kind"] == "etf"])
    for theme in sorted({r["theme"] for r in members if r["kind"] == "equity"}):
        section("L_" + theme, "LEADERS_" + theme,
                [r for r in members if r["kind"] == "equity" and r["theme"] == theme])
    layout = destination.parent / (path.stem + "-layout.json")
    layout.write_text(json.dumps(dict(
        schema_version=1, kind="global_watchlist_layout",
        universe_sha256=file_hash(path), sections=sections), indent=2) + "\n")
    receipt = export_view(path, contract, layout, destination)
    checked = validate_view(receipt["artifacts"]["watchlist"], path, contract,
                            receipt["artifacts"]["layout"])
    if not checked["passed"]:
        raise ValueError(checked)
    return receipt


def build(destination, fund_catalog=None, *, source_root=None, with_core=False):
    destination = Path(destination)
    if destination.exists() and any(destination.iterdir()):
        raise ValueError("output must be new or empty")
    spec, contract = inputs(destination / "inputs", fund_catalog, source_root)
    receipt = compose(spec, contract, destination / "bundle")
    checked = validate(receipt["artifacts"]["universe"], contract)
    if not checked["passed"]:
        raise ValueError(checked)
    receipt["observation"] = observation_view(
        receipt["artifacts"]["universe"], contract, destination / "view"
    )
    results = {"global": receipt}
    if with_core:
        parent = Path(receipt["artifacts"]["universe"])
        parent_data = json.loads(parent.read_text())
        parent_contract = json.loads(contract.read_text())
        # A bounded memory-peer choice; this does not establish a worldwide Core roster.
        omitted, survivor = "KRX:005930", "KRX:000660"
        review = dict(
            schema_version=1, kind="global_core_review",
            parent_sha256=file_hash(parent), parent_contract_sha256=file_hash(contract),
            scope="Bounded pilot Core: retain all pilot duties and prioritize SK hynix as the "
            "direct memory representative. Samsung stays in the full pilot; not a world screen.",
            protected_tickers=parent_contract.get("required_tickers", []),
            decisions=[dict(
                ticker=r["ticker"], action="omit" if r["ticker"] == omitted else "retain",
                reason="Keep SK hynix's direct memory observation; Samsung remains full-only "
                "additional memory/electronics depth." if r["ticker"] == omitted else
                "Retain the pilot observation: " + r["reason"],
                evidence=r["evidence"],
                covered_by=[survivor] if r["ticker"] == omitted else [],
            ) for r in parent_data["members"]],
            theme_reviews=[dict(
                id=t["id"], emphasis="gauge" if t["id"] == "GAUGES" else "leaders",
                reason="Preserve the bounded pilot's " + t["id"] + " duty; this small replay "
                "does not replace production child-function research.",
                evidence=next(r["evidence"] for r in parent_data["members"]
                              if r["theme"] == t["id"]),
            ) for t in parent_contract["themes"]],
        )
        review_path = destination / "inputs/core-review.json"
        review_path.write_text(json.dumps(review, ensure_ascii=False, indent=2) + "\n")
        core_receipt = compose_core(parent, contract, review_path, destination / "core-bundle")
        core_check = validate_core(core_receipt["artifacts"]["universe"], review_path)
        if not core_check["passed"]:
            raise ValueError(core_check)
        core_receipt["observation"] = observation_view(
            core_receipt["artifacts"]["universe"], review_path, destination / "core-view"
        )
        results["global-core"] = core_receipt
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="new empty pilot directory")
    parser.add_argument("--fund-catalog", type=Path, help="optional researched SOXX catalog")
    parser.add_argument("--with-core", action="store_true", help="also replay a reviewed subset")
    args = parser.parse_args()
    try:
        result = build(args.output, args.fund_catalog, with_core=args.with_core)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result["global"], indent=2))


if __name__ == "__main__":
    main()
