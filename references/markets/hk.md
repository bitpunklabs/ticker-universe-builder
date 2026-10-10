# Hong Kong equities overlay

Read [shared equity rules](equity-common.md) first. Starter themes describe listed duties;
current budgets come from the [coverage plan](../coverage-plan.md), not display weights.

## Identity

- `HKEX` codes use one to five unpadded digits: `HKEX:700`, not `HKEX:00700`.
- A/H lines belong to separate market builds.

## Economic structure

- Preserve mainland internet, banking/insurance, property, foundries and electronics duties.
- Separate developers from landlords and Macau gaming from generic leisure.
- The starter includes games at Light and omits cybersecurity/managed-care pure-play duties there.

## Adverse flags

| Code | What it is |
|---|---|
| `cancellation_procedure` | In the delisting procedure under the Listing Rules |
| `prolonged_suspension` | Trading suspended long enough to be a listing question, not a halt |
| `shell_activity_concern` | Flagged for shell or backdoor-listing activity |

## Research fields

- Stock Connect eligibility, southbound holdings and suspension history.
- A quoted line can still be frozen; verify actual trading status.

Report language: `zh-Hant`, plus English when different. [Worked input](../../examples/hk-medium/build-spec.json) · [Research review](../../examples/hk-medium/research-review.json)
See [dated example limits](../../examples/README.md).
