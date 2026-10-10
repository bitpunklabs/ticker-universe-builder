# UK equities overlay

Read [shared equity rules](equity-common.md) first. Starter themes describe listed duties;
current budgets come from the [coverage plan](../coverage-plan.md), not display weights.

## Identity

- `LSE` symbols may contain a dot; verify each current listing and dual-listing binding.
- Distinguish GBP from GBp/GBX. Normalize turnover to one currency; silent 100× errors distort ranks.

## Economic structure

- Preserve pharma, oil/mining, staples and internationally exposed operations.
- Closed-end investment trusts are gauges, not operating companies.
- Starter semiconductor scope reflects London listings; US-listed Arm is outside it.
  Megacap platforms/AI infrastructure are omitted; managed care leaves Light.

## Adverse flags

| Code | What it is |
|---|---|
| `cancellation_notice` | Has given notice of cancellation of its listing |
| `listing_category_transfer` | Transferring between listing categories |
| `offer_period` | In an offer period under the Takeover Code |

## Research fields

- Dated Takeover Code offer periods, listing-category changes and trust discount/premium to NAV.

Report language: `en`, plus English when different. [Worked input](../../examples/uk-medium/build-spec.json) · [Research review](../../examples/uk-medium/research-review.json)
See [dated example limits](../../examples/README.md).
