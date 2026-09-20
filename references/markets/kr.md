# Korea equities overlay

Read [equity-common.md](equity-common.md) first. The universe boundary, the fund-versus-basket
redundancy test, the cash-management exclusion and the rule about regressing against the theme
rather than the index are the same in every equity market. What follows is what is true here and
is not true elsewhere.

## Identity

- One venue, `KRX`, covering both KOSPI and KOSDAQ. Codes are six digits.
- Preferred lines (`005935`) are the same economic asset as their common line. Hold the common one and audit the preferred as `duplicate_asset` unless the preferred is the liquid line, which does happen.

## What this market is

Semiconductors at 4.0 is the heaviest single weight in any shipped table, and it is not an opinion: two memory makers are most of what this index does. A universe that spreads its slots evenly here is not observing Korea.

The battery chain is its own theme under materials rather than being filed with chemicals, and shipbuilding is its own group. Both are cyclical complexes with their own order books.

Entertainment and music is a level-1 theme. The listed agencies are a real export sector here and nowhere else in the table.

Managed care leaves Light: national health insurance means there is no listed insurer to observe. Everything else in this table is unusually dense — thirty-five themes reachable at Light against a target of fifty-five, so the breadth floor spends most of the universe and the weights work on what is left.

## Adverse flags

This market's regime issues these, and no other market's does. They cost the same as any
universal flag; what is market-specific is the vocabulary, not the price.

| Code | What it is |
|---|---|
| `administrative_issue` | 관리종목 — designated an administrative issue by KRX |
| `investment_alert` | Under an investment caution, warning or risk designation |
| `trading_halt_review` | Halted pending a listing eligibility review |

## Size

Breadth `0.9` in `assets/default-policy.json`, so the tiers are **Light 55**,
**Medium 145**, **Heavy 360** members. The starter table reaches 35 themes at
Light.

## Example

[`examples/kr-light/`](../../examples/kr-light/) is a full-size Light universe for this market: the seed table it is built from, the snapshot, the report in this market's language, and the TradingView watchlist. Every metric value in it is illustrative; the tickers, themes and roles are not.

## Suggested live fields

Beyond the ones in equity-common.md:

- Administrative issue (관리종목) designation and the reason for it.
- Investment alert tier — 주의 / 경고 / 위험 are three different states, not one.
- Foreign ownership limit and current foreign holding, which caps the marginal buyer.

## Report language

The report is written in Korean by default, so write the snapshot in Korean
too — names, `l1_name`, reasons and measurement methods. `--language en` overrides the report
and changes nothing else about the build.
