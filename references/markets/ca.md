# Canada equities overlay

Read [equity-common.md](equity-common.md) first. The universe boundary, the fund-versus-basket
redundancy test, the cash-management exclusion and the rule about regressing against the theme
rather than the index are the same in every equity market. What follows is what is true here and
is not true elsewhere.

## Identity

- Two venues, `TSX` and `TSXV`. They are different boards with different issuers, so a symbol on one is not the symbol on the other. Venture names rarely clear a large-cap liquidity floor; admit them deliberately or not at all.
- A company cross-listed in New York is one economic asset. Hold the Canadian line in a Canadian universe.

## What this market is

Banks at 3.5 — six of them are the index — then miners at 3.0 and the energy infrastructure complex at 2.5. Metals and mining and uranium are both promoted to level 1.

Digital-asset equities keep a level-1 seat here, which they do not get in most markets. Toronto actually lists them.

Technology is thin on purpose: one enterprise software theme, no semiconductors, no AI compute.

## Adverse flags

This market's regime issues these, and no other market's does. They cost the same as any
universal flag; what is market-specific is the vocabulary, not the price.

| Code | What it is |
|---|---|
| `cease_trade_order` | Subject to a cease trade order |
| `delisting_review` | Under exchange delisting review |
| `management_cto` | Subject to a management cease trade order |

## Size

Breadth `0.75` in `assets/default-policy.json`, so the tiers are **Light 45**,
**Medium 120**, **Heavy 300** members. The starter table reaches 28 themes at
Light.

## Suggested live fields

Beyond the ones in equity-common.md:

- Cease trade orders and management cease trade orders, published per province.
- For miners: reserve and resource statements, and which of the two a figure is.

## Report language

The report is written in English by default, so write the snapshot in English
too — names, `l1_name`, reasons and measurement methods. `--language en` overrides the report
and changes nothing else about the build.
