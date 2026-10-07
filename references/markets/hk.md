# Hong Kong equities overlay

Read [equity-common.md](equity-common.md) first. The universe boundary, the fund-versus-basket
redundancy test, the cash-management exclusion and the rule about regressing against the theme
rather than the index are the same in every equity market. What follows is what is true here and
is not true elsewhere.

## Identity

- One venue, `HKEX`. Codes are one to five digits and TradingView does not pad them: `HKEX:700`, not `HKEX:00700`.
- A company with an A-share line in Shanghai or Shenzhen and an H-share line here is two instruments in two markets. Build them separately; they are not one universe.

## What this market is

The China internet platforms are the heaviest theme at 3.0, followed by the banks and the insurers. This is not a technology market in the US sense — there is no listed semiconductor complex worth a level-1 seat and the weight reflects it.

Property is split from the base's REIT theme: the developers are their own theme because a Hong Kong developer and a Hong Kong landlord are different businesses with different balance sheets.

Macau gaming is a theme rather than a line in leisure. It is one regulatory regime, six concessions, and it moves together.

Games sit at Light here and nowhere else in the Chinese-language tables: this is where the gaming majors list. Cybersecurity and managed care leave Light in the same edit — neither has a listed pure play here.

## Adverse flags

This market's regime issues these, and no other market's does. They cost the same as any
universal flag; what is market-specific is the vocabulary, not the price.

| Code | What it is |
|---|---|
| `cancellation_procedure` | In the delisting procedure under the Listing Rules |
| `prolonged_suspension` | Trading suspended long enough to be a listing question, not a halt |
| `shell_activity_concern` | Flagged for shell or backdoor-listing activity |

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

- Stock Connect eligibility and southbound holding percentage — the marginal buyer.
- Suspension history: HKEX suspensions run long and a name can be quoted-but-frozen.

## Report language

The report is written in Traditional Chinese by default, so write the snapshot in Traditional Chinese
too — names, `l1_name`, reasons and measurement methods. `--language en` overrides the report
and changes nothing else about the build.
