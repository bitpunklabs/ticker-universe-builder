# US overlay

Read [shared equity rules](equity-common.md) first.

## Universe boundary

- Flag ADRs. Never treat two securities of one economic entity as two information sources.

## US economic map

The US starter follows the legacy map: AI hardware/semiconductors, platforms, data-center
infrastructure and software remain distinct. Payments, credit, banking, insurance and market
infrastructure are different business models. Separate regulated utilities, merchant power,
fuel and equipment; separate REIT operating exposures. Include eligible ADRs after identity
research; a provider's primary-listing flag is not a reason to erase US-listed foreign exposure.

Review functional lookalikes: [UiPath](https://www.uipath.com/product) automates software
workflows, not physical robots; [Recursion](https://www.recursion.com/pipeline) has a drug
development pipeline, not just diagnostic tools. Separate automakers from retail, payment
processors from card networks, and mixed storage-property exposures from pure data centers.
Keep these as evidence-backed research decisions, not permanent ticker rules in Python.

Market/macro, funds and commodity-underlying observation are separate duties from company
exposure. The standard equity adapter does not fetch all these automatically. Research the
missing gauges explicitly; a verified listed ETF may serve a declared proxy duty, but disclose
tracking/basis differences and do not invent an unsupported index/CFD symbol. Cash substitutes
remain excluded; duration, currency and commodity signals require actual observable movement.

## Adverse flags

| Code | What it is |
|---|---|
| `late_filing` | An NT 10-K or NT 10-Q, or a filing past its extended deadline |
| `listing_deficiency` | An exchange deficiency notice: price, market value, float or governance |
| `material_weakness` | A disclosed material weakness in internal control over financial reporting |

## Example

[`examples/us-medium/`](../../examples/us-medium/) contains a current coverage-first Medium
research snapshot, measured statistics, dated listing evidence, reports and script-generated watchlist.
Read [the scope and limitations](../../examples/README.md) before reusing it.

## Research fields

Use shared equity fields, SEC/exchange disclosures and current ETF holdings; review US-listed
foreign businesses, banking models, underwriting/brokerage, software functions, drugs/devices,
logistics, regulated utilities and consumer formats. Toys/IP are not household-care coverage.
