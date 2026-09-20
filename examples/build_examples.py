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
    market_guidance,
    read_json,
    render_markdown,
    render_txt,
    report_language,
    starter_taxonomy,
)

# The order examples are built and printed in: the three that shipped first, then the rest of
# the registry. Nothing depends on it beyond readable output and a stable diff.
MARKET_ORDER = (
    "crypto", "us", "cn", "jp", "hk", "in", "kr", "tw", "uk", "de", "fr", "ca", "au", "br",
)

AS_OF = "2026-09-17"

# One row per market with a seed table. `sources` are the listing and market-data pages a real
# snapshot would cite; `factor` names what the redundancy metric is measured against, which is a
# broad ETF that trades in the same market rather than an index nobody can hold.
#
# The Light target is NOT written here. It comes out of the market's breadth in
# `assets/default-policy.json`, so a policy change moves the examples and a stale number cannot
# survive in this file.
LISTING = {
    "crypto": "https://api.binance.com/api/v3/exchangeInfo",
    "us": "https://www.nasdaq.com/market-activity/stocks/screener",
    "cn": "http://www.sse.com.cn/assortment/stock/list/share/",
    "jp": "https://www.jpx.co.jp/markets/statistics-equities/misc/01.html",
    "hk": "https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx",
    "in": "https://www.nseindia.com/market-data/securities-available-for-trading",
    "kr": "https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201",
    "tw": "https://www.twse.com.tw/zh/listed/profile/company.html",
    "uk": "https://www.londonstockexchange.com/live-markets/market-data-dashboard/price-explorer",
    "de": "https://www.xetra.com/xetra-en/instruments/instruments",
    "fr": "https://live.euronext.com/en/markets/paris/equities/list",
    "ca": "https://www.tsx.com/listings/listing-with-us/listed-company-directory",
    "au": "https://www.asx.com.au/markets/trade-our-cash-market/directory",
    "br": "https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/",
}
MARKET_DATA = {
    "crypto": "https://data.binance.vision/",
    "us": "https://www.nasdaq.com/market-activity/stocks/screener",
    "cn": "http://www.sse.com.cn/market/stockdata/overview/",
    "jp": "https://www.jpx.co.jp/markets/statistics-equities/daily/index.html",
    "hk": "https://www.hkex.com.hk/Market-Data/Statistics/Consolidated-Reports",
    "in": "https://www.nseindia.com/reports/daily-reports-equities",
    "kr": "https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020101",
    "tw": "https://www.twse.com.tw/zh/trading/historical/fmtqik.html",
    "uk": "https://www.londonstockexchange.com/reports?tab=trade-statistics",
    "de": "https://www.deutsche-boerse-cash-market.com/dbcm-en/instruments-statistics/statistics",
    "fr": "https://live.euronext.com/en/markets/paris/equities/list",
    "ca": "https://www.tsx.com/trading/market-data",
    "au": "https://www.asx.com.au/markets/trade-our-cash-market/market-statistics",
    "br": "https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/",
}
SECOND_SOURCE = {
    "crypto": None,
    "us": ("https://www.nyse.com/listings_directory/stock", "exchange"),
    "cn": ("https://www.szse.cn/market/product/stock/list/", "exchange"),
    "jp": None,
    "hk": None,
    "in": ("https://www.bseindia.com/corporates/List_Scrips.html", "exchange"),
    "kr": None,
    "tw": ("https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430.php",
           "exchange"),
    "uk": None,
    "de": ("https://www.boerse-frankfurt.de/equities", "exchange"),
    "fr": None,
    "ca": ("https://www.tsx.com/trading/tsx-venture-exchange", "exchange"),
    "au": None,
    "br": None,
}
FACTOR_LABEL = {
    "crypto": "the 00_A BTC/ETH/SOL basket",
    "us": "AMEX:SPY",
    "cn": "SSE:510300",
    "jp": "TSE:1306",
    "hk": "HKEX:2800",
    "in": "NSE:NIFTYBEES",
    "kr": "KRX:069500",
    "tw": "TWSE:0050",
    "uk": "LSE:ISF",
    "de": "XETR:EXS1",
    "fr": "EURONEXT:CAC",
    "ca": "TSX:XIU",
    "au": "ASX:STW",
    "br": "BMFBOVESPA:BOVA11",
}


def sources(market: str) -> list[dict]:
    rows = [{"url": LISTING[market], "as_of": AS_OF, "kind": "exchange", "tier": 1}]
    second = SECOND_SOURCE.get(market)
    if second:
        rows.append({"url": second[0], "as_of": AS_OF, "kind": second[1], "tier": 1})
    if MARKET_DATA[market] != LISTING[market]:
        rows.append({"url": MARKET_DATA[market], "as_of": AS_OF, "kind": "market_data", "tier": 2})
    return rows


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
    "zh-Hant": {
        "liquidity": "30 日日均成交額的截面分位",
        "quality": "上市時長與規模分位，疊加對經營延續性的判斷",
        "heat": "成交額躍升，須以交易所資料確認，單日波動不算",
        "beta_strength": "對 {factor} 的 OLS beta 絕對值，beta 為 2.0 記 100",
        "beta_stability": "beta 估計在視窗前後兩半之間的一致程度",
        "factor_r2": "日報酬對 {factor} 的 OLS 迴歸",
        "independence_derived": "由 builder 以 100 - factor_r2 推得",
        "independence": "100 減去日報酬對 {factor} 迴歸的 R²",
    },
    "ja": {
        "liquidity": "30 日平均売買代金のクロスセクション分位",
        "quality": "上場年数と規模分位に、事業継続性の判断を重ねたもの",
        "heat": "売買代金の急増。取引所データで確認したもののみ、単日の変動は数えない",
        "beta_strength": "{factor} に対する OLS ベータの絶対値。ベータ 2.0 を 100 とする",
        "beta_stability": "期間を前後半に割ったときのベータ推定値の一致度",
        "factor_r2": "日次リターンを {factor} に回帰した OLS",
        "independence_derived": "100 - factor_r2 としてビルダーが算出",
        "independence": "日次リターンを {factor} に回帰した決定係数を 100 から引いたもの",
    },
    "ko": {
        "liquidity": "30일 일평균 거래대금의 횡단면 백분위",
        "quality": "상장 기간과 규모 백분위에 사업 지속성 판단을 더한 값",
        "heat": "거래대금 급증. 거래소 데이터로 확인된 것만 인정하며 하루 변동은 제외",
        "beta_strength": "{factor} 대비 OLS 베타의 절댓값. 베타 2.0을 100으로 본다",
        "beta_stability": "구간을 전반과 후반으로 나눴을 때 베타 추정치의 일치 정도",
        "factor_r2": "일간 수익률을 {factor}에 회귀한 OLS",
        "independence_derived": "빌더가 100 - factor_r2 로 산출",
        "independence": "일간 수익률을 {factor}에 회귀한 결정계수를 100에서 뺀 값",
    },
    "de": {
        "liquidity": "Querschnittsperzentil des durchschnittlichen Tagesumsatzes",
        "quality": "Börsenalter und Größenperzentil, ergänzt um ein Urteil zur Beständigkeit",
        "heat": "Umsatzsprung, gegen Börsendaten bestätigt, niemals eine Eintagesbewegung",
        "beta_strength": "Betrag des OLS-Betas gegen {factor}; Beta 2,0 entspricht 100",
        "beta_stability": "Übereinstimmung der Beta-Schätzung über beide Hälften des Zeitraums",
        "factor_r2": "OLS der Tagesrenditen auf {factor}",
        "independence_derived": "vom Builder als 100 - factor_r2 abgeleitet",
        "independence": "100 minus das Bestimmtheitsmaß der Tagesrenditen auf {factor}",
    },
    "fr": {
        "liquidity": "percentile en coupe transversale du volume quotidien moyen",
        "quality": "ancienneté de cotation et percentile de taille, complétés par un jugement "
                   "de durabilité",
        "heat": "saut de volume confirmé par les données de marché, jamais une séance isolée",
        "beta_strength": "valeur absolue du bêta OLS contre {factor} ; un bêta de 2,0 vaut 100",
        "beta_stability": "concordance de l'estimation du bêta entre les deux moitiés de la "
                          "fenêtre",
        "factor_r2": "OLS des rendements quotidiens sur {factor}",
        "independence_derived": "dérivé par le builder comme 100 - factor_r2",
        "independence": "100 moins le R² de la régression des rendements quotidiens sur {factor}",
    },
    "pt-BR": {
        "liquidity": "percentil transversal do volume financeiro médio diário",
        "quality": "tempo de listagem e percentil de tamanho, somados a um juízo de "
                   "durabilidade",
        "heat": "salto de volume confirmado nos dados da bolsa, nunca um movimento de um dia",
        "beta_strength": "módulo do beta OLS contra {factor}; beta de 2,0 vale 100",
        "beta_stability": "concordância da estimativa de beta entre as duas metades da janela",
        "factor_r2": "OLS dos retornos diários sobre {factor}",
        "independence_derived": "derivado pelo builder como 100 - factor_r2",
        "independence": "100 menos o R² dos retornos diários regredidos sobre {factor}",
    },
    "zh-Hans": {
        "liquidity": "30 日日均成交额的截面分位",
        "quality": "上市时长与规模分位，叠加对经营持续性的判断",
        "heat": "成交额跃升，须以交易所数据确认，单日波动不算",
        "beta_strength": "对 {factor} 的 OLS beta 绝对值，beta 为 2.0 记 100",
        "beta_stability": "beta 估计在窗口前后两半之间的一致程度",
        "factor_r2": "日收益对 {factor} 的 OLS 回归",
        "independence_derived": "由 builder 从 100 - factor_r2 推得",
        "independence": "100 减去日收益对 {factor} 回归的 R²",
    },
}


def measurement(market: str) -> dict:
    source = MARKET_DATA[market]
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
            "source": LISTING[market],
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
            "url": LISTING[market], "as_of": AS_OF, "kind": "listing", "tier": 1,
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


SEED_NOTE = {
    "en": """> Generated by `python examples/build_examples.py` from `examples/seeds/{market}.tsv`.
> This is the `.md` artifact a build writes, committed so it can be read without running
> anything. Every metric value in it is illustrative — see [README.md](../README.md).

""",
    "zh-Hans": """> 由 `python examples/build_examples.py` 从 `examples/seeds/{market}.tsv` 生成。
> 这是一次 build 写出的 `.md` 产物，提交进仓库是为了不运行任何东西也能读到它。
> 其中所有指标数值都只作示意——见 [README.md](../README.md)。

""",
    "zh-Hant": """> 由 `python examples/build_examples.py` 從 `examples/seeds/{market}.tsv` 產生。
> 這是一次 build 寫出的 `.md` 產物，提交進倉庫是為了不執行任何東西也能讀到它。
> 其中所有指標數值都只作示意——見 [README.md](../README.md)。

""",
    "ja": """> `python examples/build_examples.py` が `examples/seeds/{market}.tsv` から生成。
> これは build が書き出す `.md` 成果物で、何も実行せずに読めるようリポジトリに入れてある。
> 指標の数値はすべて例示にすぎない——[README.md](../README.md) を参照。

""",
    "ko": """> `python examples/build_examples.py` 가 `examples/seeds/{market}.tsv` 로부터 생성.
> build 가 써내는 `.md` 산출물이며, 아무것도 실행하지 않고 읽을 수 있도록 저장소에 넣었다.
> 지표 값은 모두 예시일 뿐이다 — [README.md](../README.md) 참고.

""",
    "de": """> Erzeugt von `python examples/build_examples.py` aus `examples/seeds/{market}.tsv`.
> Dies ist das `.md`-Artefakt eines Builds, eingecheckt, damit es ohne Ausführung lesbar ist.
> Jeder Kennzahlenwert darin ist illustrativ — siehe [README.md](../README.md).

""",
    "fr": """> Généré par `python examples/build_examples.py`, à partir de
> `examples/seeds/{market}.tsv`. Voici l'artefact `.md` qu'un build produit, versionné pour
> être lu sans rien exécuter.
> Toutes les valeurs de métriques y sont illustratives — voir [README.md](../README.md).

""",
    "pt-BR": """> Gerado por `python examples/build_examples.py`, a partir de
> `examples/seeds/{market}.tsv`. Este é o artefato `.md` que um build escreve, versionado para
> ser lido sem executar nada.
> Todo valor de métrica aqui é ilustrativo — veja [README.md](../README.md).

""",
}


def render(market: str, snapshot: dict, spec: dict, folder: Path) -> dict:
    """Build the example and commit the report it produces.

    The Markdown is the artifact a person actually reads, and leaving it out of the repository
    meant the only way to see what an example produces was to run it. Committing it also means a
    change in selection shows up as a reviewable diff rather than as a silently different result.
    """
    policy = load_policy()
    preamble = SEED_NOTE[report_language(market)].format(market=market)
    universe, report = build_universe(spec, snapshot, policy)
    (folder / "universe.md").write_text(
        preamble + render_markdown(universe, report), encoding="utf-8"
    )
    # The watchlist is the artifact that leaves the repository — it gets imported. Committing it
    # beside the report means the TradingView import format can be read, and diffed, without
    # running a build.
    (folder / "watchlist.txt").write_text(render_txt(universe), encoding="utf-8")
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


def light_target(market: str) -> int:
    """The market's own Light target, out of its breadth. Never restated in this file."""
    return int(market_guidance(market, load_policy(), None)["light"]["target"])


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
        "sources": sources(market),
        "measurement": measurement(market),
        "taxonomy": taxonomy,
        "candidates": [candidate(market, row, index) for index, row in enumerate(rows)],
    }
    spec = {
        "schema_version": 1,
        "market": market,
        "profile": "light",
        "as_of": AS_OF,
        "target_count": light_target(market),
    }
    # Every example now builds at its market's Light target, inside guidance, with no escape
    # hatch. If one stops fitting, that is a finding about the seeds or the policy, not a flag
    # to set.
    folder = ROOT / "examples" / f"{market}-light"
    folder.mkdir(parents=True, exist_ok=True)
    for name, payload in (("snapshot.json", snapshot), ("build-spec.json", spec)):
        (folder / name).write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    render(market, snapshot, spec, folder)
    return snapshot


def seeded_markets() -> list[str]:
    """Every market with a seed table, in registry order so the output is stable."""
    seeds = {path.stem for path in (ROOT / "examples" / "seeds").glob("*.tsv")}
    return [market for market in MARKET_ORDER if market in seeds]


def main() -> int:
    for market in seeded_markets():
        snapshot = build(market)
        eligible = [item for item in snapshot["candidates"] if item["eligible"]]
        print(
            f"{market}: {len(snapshot['candidates'])} candidates, {len(eligible)} eligible, "
            f"target {light_target(market)}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
