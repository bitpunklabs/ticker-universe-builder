# Korea equities overlay

Read [shared equity rules](equity-common.md) first. Starter themes describe listed duties;
current budgets come from the [coverage plan](../coverage-plan.md), not display weights.

## Identity

- `KRX` covers KOSPI/KOSDAQ; codes have six digits.
- Common/preferred lines are one asset; choose the liquid observed line and audit the duplicate.

## Economic structure

- Preserve memory semiconductors, battery-chain, shipbuilding and entertainment/music duties.
- Provider chemicals classifications do not replace battery-chain coverage.
- The starter omits managed care from Light.

## Adverse flags

| Code | What it is |
|---|---|
| `administrative_issue` | 관리종목 — designated an administrative issue by KRX |
| `investment_alert` | Under an investment caution, warning or risk designation |
| `trading_halt_review` | Halted pending a listing eligibility review |

## Research fields

- Administrative issue and its reason; separate caution/warning/risk alert tiers.
- Foreign ownership limits and current holdings.

Report language: `ko`, plus English when different. [Worked input](../../examples/kr-medium/build-spec.json) · [Research review](../../examples/kr-medium/research-review.json)
See [dated example limits](../../examples/README.md).
