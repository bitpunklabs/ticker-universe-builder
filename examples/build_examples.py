#!/usr/bin/env python3
"""Regenerate the shipped example snapshots from their seed tables.

The seeds under `seeds/` hold the part that is real and hand-maintained: ticker, name, theme and
role. Everything else in an example snapshot is illustrative, and writing several hundred
illustrative metrics by hand produces drift, not insight — a role gate quietly unsatisfied, a
bucket share quietly out of tolerance. So the metrics are derived here, deterministically, and
`tests/test_universe_core.py` asserts the committed snapshots match what this produces.

    python examples/build_examples.py

Nothing in this file belongs in a real universe. See `references/measurement.md` for how the
measured metrics are supposed to be obtained.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from universe_core import (  # noqa: E402
    BUCKET_BY_ROLE,
    FACTOR_EXEMPT_ROLES,
    UniverseError,
    apply_change_set,
    build_universe,
    load_policy,
    read_json,
    render_markdown,
    report_language,
    starter_taxonomy,
)

AS_OF = "2026-09-17"
TARGETS = {"crypto": 40, "us": 64, "cn": 64}

SOURCES = {
    "crypto": [
        {"url": "https://api.binance.com/api/v3/exchangeInfo",
         "as_of": AS_OF, "kind": "exchange", "tier": 1},
        {"url": "https://data.binance.vision/", "as_of": AS_OF, "kind": "market_data", "tier": 2},
    ],
    "us": [
        {"url": "https://www.nasdaq.com/market-activity/stocks/screener",
         "as_of": AS_OF, "kind": "exchange", "tier": 1},
        {"url": "https://www.nyse.com/listings_directory/stock",
         "as_of": AS_OF, "kind": "exchange", "tier": 1},
    ],
    "cn": [
        {"url": "http://www.sse.com.cn/assortment/stock/list/share/",
         "as_of": AS_OF, "kind": "exchange", "tier": 1},
        {"url": "https://www.szse.cn/market/product/stock/list/",
         "as_of": AS_OF, "kind": "exchange", "tier": 1},
    ],
}
EVIDENCE_URL = {
    "crypto": "https://api.binance.com/api/v3/exchangeInfo",
    "us": "https://www.nasdaq.com/market-activity/stocks/screener",
    "cn": "http://www.sse.com.cn/assortment/stock/list/share/",
}
LIQUIDITY_SOURCE = {
    "crypto": "https://data.binance.vision/",
    "us": "https://www.nasdaq.com/market-activity/stocks/screener",
    "cn": "http://www.sse.com.cn/market/stockdata/overview/",
}
FACTOR_LABEL = {
    "crypto": "the 00_A BTC/ETH/SOL basket",
    "us": "AMEX:SPY",
    "cn": "SSE:510300",
}


# A cn snapshot is researched and read in Chinese, so the example is written the way a real one
# would be. Only the free text moves: the metric names, the bases and the windows are the
# contract and stay as they are in every language.
METHOD_TEXT = {
    "en": {
        "liquidity": "cross-sectional percentile of mean daily turnover",
        "quality": "listing age and size percentile against a judged durability read",
        "heat": "turnover jump confirmed against exchange data, never a single-day move",
        "beta_strength": "absolute OLS beta against {factor}, beta 2.0 reads 100",
        "beta_stability": "agreement of the beta estimate across the two halves of the window",
        "factor_r2": "OLS of daily returns on {factor}",
        "independence_derived": "derived as 100 - factor_r2 by the builder",
        "independence": "100 - the OLS R-squared of daily returns on {factor}",
    },
    "zh-Hans": {
        "liquidity": "30 日日均成交额的截面分位",
        "quality": "上市时长与规模分位,叠加对经营持续性的判断",
        "heat": "成交额跃升,须以交易所数据确认,单日波动不算",
        "beta_strength": "对 {factor} 的 OLS beta 绝对值,beta 为 2.0 记 100",
        "beta_stability": "beta 估计在窗口前后两半之间的一致程度",
        "factor_r2": "日收益对 {factor} 的 OLS 回归",
        "independence_derived": "由 builder 从 100 - factor_r2 推得",
        "independence": "100 减去日收益对 {factor} 回归的 R²",
    },
}


def measurement(market: str) -> dict:
    source = LIQUIDITY_SOURCE[market]
    factor = FACTOR_LABEL[market]
    text = {
        key: value.format(factor=factor)
        for key, value in METHOD_TEXT[report_language(market)].items()
    }
    block = {
        "liquidity": {
            "basis": "measured",
            "method": text["liquidity"],
            "window": "30d",
            "source": source,
        },
        "quality": {
            "basis": "blended",
            "method": text["quality"],
            "source": EVIDENCE_URL[market],
        },
        "heat": {"basis": "judged", "method": text["heat"]},
        "beta_strength": {
            "basis": "measured",
            "method": text["beta_strength"],
            "window": "180d",
            "source": source,
        },
        "beta_stability": {
            "basis": "measured",
            "method": text["beta_stability"],
            "window": "180d",
            "source": source,
        },
    }
    span = {
        "basis": "measured",
        "method": text["factor_r2"],
        "window": "180d",
        "source": source,
    }
    if market == "crypto":
        block["factor_r2"] = span
        block["independence"] = {**span, "method": text["independence_derived"]}
    else:
        block["independence"] = {**span, "method": text["independence"]}
    return block


def read_seed(market: str) -> list[dict]:
    rows = []
    path = ROOT / "examples" / "seeds" / f"{market}.tsv"
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        parts = (line.split("\t") + ["", "", "", "", ""])[:5]
        rows.append({
            "ticker": parts[0].strip(),
            "name": parts[1].strip(),
            "theme_code": parts[2].strip(),
            "role": parts[3].strip(),
            "flags": parts[4].strip(),
        })
    return rows


def candidate(market: str, row: dict, index: int) -> dict:
    role = row["role"]
    bucket = BUCKET_BY_ROLE[role]
    eligible = not row["flags"].startswith("ineligible:")
    metrics: dict[str, int] = {
        "liquidity": max(40, 99 - index),
        "quality": max(58, 94 - index // 2),
        "heat": 55 + (index * 7) % 40,
    }
    if role == "INDEPENDENT_SENSOR":
        redundancy = 30 + index % 10
    elif role in FACTOR_EXEMPT_ROLES:
        redundancy = 88 - index % 5
    else:
        redundancy = 52 + (index * 3) % 30
    if market == "crypto":
        metrics["factor_r2"] = redundancy
    else:
        metrics["independence"] = 100 - redundancy
    if role == "BETA_SATELLITE":
        metrics["beta_strength"] = 62 + (index * 3) % 30
        metrics["beta_stability"] = 60 + (index * 5) % 32
    item = {
        "ticker": row["ticker"],
        "name": row["name"],
        "theme_code": row["theme_code"],
        "role": role,
        "eligible": eligible,
        "metrics": metrics,
        "evidence": [{
            "url": EVIDENCE_URL[market], "as_of": AS_OF, "kind": "listing", "tier": 1,
        }],
    }
    if "required" in row["flags"]:
        item["required"] = True
    if not eligible:
        item["exclusion_reasons"] = [row["flags"].removeprefix("ineligible:")]
    elif bucket == "core":
        item["quality_facts"] = {
            "listing_age_days": max(400, 5200 - index * 40),
            "size_rank_pct": max(45, 98 - index),
            "adverse_flags": [],
        }
    return item


PREAMBLE = {
    "en": """> Generated by `python examples/build_examples.py` from `examples/seeds/{market}.tsv`.
> This is the `.md` artifact a build writes, committed so it can be read without running
> anything. Every metric value in it is illustrative — see [README.md](../README.md).

""",
    "zh-Hans": """> 由 `python examples/build_examples.py` 从 `examples/seeds/{market}.tsv` 生成。
> 这是一次 build 写出的 `.md` 产物,提交进仓库是为了不运行任何东西也能读到它。
> 其中所有指标数值都只作示意 — 见 [README.md](../README.md)。

""",
}


def render(market: str, snapshot: dict, spec: dict, folder: Path) -> dict:
    """Build the example and commit the report it produces.

    The Markdown is the artifact a person actually reads, and leaving it out of the repository
    meant the only way to see what an example produces was to run it. Committing it also means a
    change in selection shows up as a reviewable diff rather than as a silently different result.
    """
    policy = load_policy()
    preamble = PREAMBLE[report_language(market)].format(market=market)
    universe, report = build_universe(spec, snapshot, policy)
    (folder / "universe.md").write_text(
        preamble + render_markdown(universe, report), encoding="utf-8"
    )
    changes_path = folder / "changes.json"
    if changes_path.is_file():
        changes = read_json(changes_path)
        if changes.get("base_version_hash") != universe["version_hash"]:
            raise UniverseError(
                f"{market}: changes.json targets {changes.get('base_version_hash')} but the "
                f"rebuilt universe is {universe['version_hash']}; update base_version_hash"
            )
        reviewed, review_report = apply_change_set(universe, changes, policy)
        (folder / "maintenance.md").write_text(
            preamble + render_markdown(reviewed, review_report), encoding="utf-8"
        )
    return universe


def build(market: str) -> dict:
    taxonomy = starter_taxonomy(market)
    known = {item["theme_code"] for item in taxonomy}
    rows = read_seed(market)
    for row in rows:
        if row["theme_code"] not in known:
            raise UniverseError(f"{market}: {row['ticker']} names theme {row['theme_code']}, "
                                "which the starter taxonomy does not carry")
    snapshot = {
        "schema_version": 1,
        "market": market,
        "as_of": AS_OF,
        "complete": True,
        "sources": SOURCES[market],
        "measurement": measurement(market),
        "taxonomy": taxonomy,
        "candidates": [candidate(market, row, index) for index, row in enumerate(rows)],
    }
    spec = {
        "schema_version": 1,
        "market": market,
        "profile": "light",
        "as_of": AS_OF,
        "target_count": TARGETS[market],
    }
    # Crypto reaches its Light guidance range; the two equity seeds do not yet, and say so
    # rather than being waved through by a policy edit.
    if TARGETS[market] < 100:
        spec["allow_outside_guidance"] = market != "crypto"
    folder = ROOT / "examples" / f"{market}-light"
    folder.mkdir(parents=True, exist_ok=True)
    for name, payload in (("snapshot.json", snapshot), ("build-spec.json", spec)):
        (folder / name).write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    render(market, snapshot, spec, folder)
    return snapshot


def main() -> int:
    for market in ("crypto", "us", "cn"):
        snapshot = build(market)
        eligible = [item for item in snapshot["candidates"] if item["eligible"]]
        print(
            f"{market}: {len(snapshot['candidates'])} candidates, {len(eligible)} eligible, "
            f"target {TARGETS[market]}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
