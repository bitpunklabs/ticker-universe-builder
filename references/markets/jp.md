# Japan equities overlay

Read [equity-common.md](equity-common.md) first. The universe boundary, the fund-versus-basket
redundancy test, the cash-management exclusion and the rule about regressing against the theme
rather than the index are the same in every equity market. What follows is what is true here and
is not true elsewhere.

## Identity

- One venue, `TSE`. A code is four characters: three digits and a digit or a letter — the alphanumeric codes issued since 2024 are not a typo.
- A company has one line, so the venue is not part of identity. A TOPIX ETF and the index it tracks are two instruments and only one of them trades.

## What this market is

Autos carry this market and the weights say so: the OEMs at 3.0 against 1.0 in the shared base. Semicap equipment outweighs semiconductors here, which is the inversion of every other developed market — Tokyo Electron, Advantest and Lasertec sell into fabs that are mostly not Japanese.

The trading houses have no analogue anywhere else in the table, so they are their own group rather than being filed under distribution. They are commodity, logistics and private-equity exposure in one listed line, and treating one as a wholesaler loses every driver it actually has.

Games and interactive sits at coverage level 1 here and level 3 in the base.

Managed care leaves Light entirely: a single-payer system lists no insurer to observe, and the theme would have held a hole. The mixed-use developers get a theme of their own instead — Mitsui Fudosan and Mitsubishi Estate are not REITs and filing them as one loses what they are.

## Adverse flags

This market's regime issues these, and no other market's does. They cost the same as any
universal flag; what is market-specific is the vocabulary, not the price.

| Code | What it is |
|---|---|
| `listing_criteria_shortfall` | Below a continued-listing criterion for its market segment |
| `security_on_alert` | 特設注意市場銘柄 — the exchange has flagged an internal-control concern |
| `supervision_post` | 監理銘柄 — under supervision pending a delisting determination |

## Size

Breadth `1.05` in `assets/default-policy.json`, so the tiers are **Light 65**,
**Medium 170**, **Heavy 420** members. The starter table reaches 34 themes at
Light.

## Example

[`examples/jp-light/`](../../examples/jp-light/) is a full-size Light universe for this market: the seed table it is built from, the snapshot, the report in this market's language, and the TradingView watchlist. Every metric value in it is illustrative; the tickers, themes and roles are not.

## Suggested live fields

Beyond the ones in equity-common.md:

- TSE market segment (Prime, Standard, Growth) — the continued-listing criteria differ and so does what a shortfall means.
- Cross-shareholding unwind disclosures, which move float without moving the business.

## Report language

The report is written in Japanese by default, so write the snapshot in Japanese
too — names, `l1_name`, reasons and measurement methods. `--language en` overrides the report
and changes nothing else about the build.
