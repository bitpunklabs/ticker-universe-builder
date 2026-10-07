# UK equities overlay

Read [equity-common.md](equity-common.md) first. The universe boundary, the fund-versus-basket
redundancy test, the cash-management exclusion and the rule about regressing against the theme
rather than the index are the same in every equity market. What follows is what is true here and
is not true elsewhere.

## Identity

- One venue, `LSE`. Symbols are two to six characters and may carry a dot.
- Prices quote in pence for most lines and in pounds for a few. Whatever you use, say which in `measurement.method` — a turnover figure that is silently 100x wrong ranks the whole universe wrong.
- Dual-listed lines (`LSE:BHP` and its Australian line) are one economic asset across two markets. Build them in whichever market you were asked about, not both.

## What this market is

Pharma, oil majors and miners at 2.5 each, staples at 2.0. Almost none of the revenue behind those weights is British, which is the single most important fact about this index and the reason regressing against a UK index gauge tells you nothing.

There is no megacap platform theme and no AI infrastructure. They are dropped, not weighted down.

Closed-end investment trusts are their own group. They are a large, liquid part of this market with no equivalent anywhere else in the table, and they are gauges rather than operating companies.

Semiconductors are weighted to what London actually lists rather than to what the sector is worth globally — Arm is in New York, and pretending otherwise would hand a heavy weight to a theme with one mid-cap in it. Managed care leaves Light: the NHS is not a listed sector.

## Adverse flags

This market's regime issues these, and no other market's does. They cost the same as any
universal flag; what is market-specific is the vocabulary, not the price.

| Code | What it is |
|---|---|
| `cancellation_notice` | Has given notice of cancellation of its listing |
| `listing_category_transfer` | Transferring between listing categories |
| `offer_period` | In an offer period under the Takeover Code |

## Size

Research the leader/necessary-peer roster and declare four entity ceilings in `coverage_plan`.
Reference instruments are additional. Medium covers most reviewed leaders; Heavy protects the
full necessary backbone; Max adds at least 30% sourced Beta following that Heavy's distribution.
Starter theme levels/weights do not set current member quotas.

## Example

Use the closest [current equity example](../../examples/README.md) for the coverage-plan,
admission and output contracts, then research this market under its own overlay. No dedicated
current snapshot ships for this market.

## Suggested live fields

Beyond the ones in equity-common.md:

- Takeover Code offer period status — a published, dated state, not a rumour.
- Listing category (Equity Shares Commercial Companies and its transitions).
- Investment trust discount or premium to NAV, where the member is a trust.

## Report language

The report is written in English by default, so write the snapshot in English
too — names, `l1_name`, reasons and measurement methods. `--language en` overrides the report
and changes nothing else about the build.
