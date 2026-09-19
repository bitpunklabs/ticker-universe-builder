# Brazil equities overlay

Read [equity-common.md](equity-common.md) first. The universe boundary, the fund-versus-basket
redundancy test, the cash-management exclusion and the rule about regressing against the theme
rather than the index are the same in every equity market. What follows is what is true here and
is not true elsewhere.

## Identity

- One venue, `BMFBOVESPA`. A symbol is four letters and one or two digits, and the digit is the share class: `3` ordinary, `4` preferred, `11` unit.
- `PETR3` and `PETR4` are the same company. Hold the liquid line — usually the preferred or the unit — and audit the other as `duplicate_asset`. This is the mistake that fills a Brazilian universe with pairs.

## What this market is

Miners at 3.5, oil at 3.0, banks at 3.0, protein and beverage at 2.5. That ordering is the market.

Agribusiness is its own group and exists in no other shipped table. Filing it under staples loses the fact that it trades on weather and on the soybean curve.

Twenty-five themes from the shared base are dropped, including all of technology except software and internet. The resulting table is the shortest of the fourteen, which matches a market with the smallest breadth factor.

## Adverse flags

This market's regime issues these, and no other market's does. They cost the same as any
universal flag; what is market-specific is the vocabulary, not the price.

| Code | What it is |
|---|---|
| `cvm_inquiry` | Subject to a CVM ofício |
| `judicial_recovery` | In recuperação judicial |
| `segment_downgrade` | Downgraded from its listing segment |

## Size

Breadth `0.55` in `assets/default-policy.json`, so the tiers are **Light 35**,
**Medium 90**, **Heavy 220** members. The starter table reaches 25 themes at
Light.

## Suggested live fields

Beyond the ones in equity-common.md:

- Novo Mercado / Nível 2 / Nível 1 listing segment, and any downgrade.
- Recuperação judicial filings and CVM ofícios.
- Free float: control blocks here are large and a float-blind turnover figure misleads.

## Report language

The report is written in Brazilian Portuguese by default, so write the snapshot in Brazilian Portuguese
too — names, `l1_name`, reasons and measurement methods. `--language en` overrides the report
and changes nothing else about the build.
