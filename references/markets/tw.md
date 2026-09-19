# Taiwan equities overlay

Read [equity-common.md](equity-common.md) first. The universe boundary, the fund-versus-basket
redundancy test, the cash-management exclusion and the rule about regressing against the theme
rather than the index are the same in every equity market. What follows is what is true here and
is not true elsewhere.

## Identity

- Two venues, `TWSE` (the main board) and `TPEX` (the over-the-counter board). A company is on one or the other, so the venue is not part of identity but it does change the liquidity floor you should apply.
- Codes are four to six digits, sometimes with a trailing letter for a fund line.

## What this market is

This is one supply chain observed at four depths: foundry (4.0), ODM hardware (3.0), AI compute (2.5) and IC design, which is split out as its own theme because MediaTek and Novatek are a different business from the fabs.

Everything else on this table is weighted at or below 1.0 on purpose. Taiwan lists banks, food and cement, and none of them is why anyone observes this market.

Nineteen themes from the shared base are dropped. A short table is the honest answer when a market is concentrated; padding it produces themes with one illiquid member.

## Adverse flags

This market's regime issues these, and no other market's does. They cost the same as any
universal flag; what is market-specific is the vocabulary, not the price.

| Code | What it is |
|---|---|
| `altered_trading_method` | 變更交易方法 — moved to an altered trading method |
| `disposition_stock` | 處置股票 — under disposition measures for abnormal trading |
| `full_delivery` | 全額交割 — full-delivery settlement required |

## Size

Breadth `0.8` in `assets/default-policy.json`, so the tiers are **Light 50**,
**Medium 130**, **Heavy 320** members. The starter table reaches 30 themes at
Light.

## Suggested live fields

Beyond the ones in equity-common.md:

- Monthly revenue disclosures, which Taiwan publishes and most markets do not — the highest-frequency fundamental in the table.
- Disposition (處置) status and altered trading method, both exchange-published.

## Report language

The report is written in Traditional Chinese by default, so write the snapshot in Traditional Chinese
too — names, `l1_name`, reasons and measurement methods. `--language en` overrides the report
and changes nothing else about the build.
