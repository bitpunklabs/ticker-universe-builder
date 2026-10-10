# Japan equities overlay

Read [shared equity rules](equity-common.md) first. Starter themes describe listed duties;
current budgets come from the [coverage plan](../coverage-plan.md), not display weights.

## Identity

- `TSE`: three digits followed by a digit or letter; alphanumeric codes are valid.
- One economic company per member. TOPIX ETFs and direct indices remain different instruments.

## Economic structure

- Distinguish autos, semiconductor equipment, games and interactive businesses.
- Trading houses combine commodity/logistics/investment exposure; they are not wholesalers.
- Mixed-use developers are distinct from REITs. The starter omits managed care from Light.

## Adverse flags

| Code | What it is |
|---|---|
| `listing_criteria_shortfall` | Below a continued-listing criterion for its market segment |
| `security_on_alert` | 特設注意市場銘柄 — the exchange has flagged an internal-control concern |
| `supervision_post` | 監理銘柄 — under supervision pending a delisting determination |

## Research fields

- TSE segment (Prime/Standard/Growth) and its continued-listing criteria.
- Cross-shareholding unwind disclosures and resulting float changes.

Report language: `ja`, plus English when different. [Worked input](../../examples/jp-medium/build-spec.json) · [Research review](../../examples/jp-medium/research-review.json)
See [dated example limits](../../examples/README.md).
