# Canada equities overlay

Read [shared equity rules](equity-common.md) first. Starter themes describe listed duties;
current budgets come from the [coverage plan](../coverage-plan.md), not display weights.

## Identity

- `TSX` and `TSXV` have different boards/issuers; verify identity rather than merging identical strings.
- Prefer the verified Canadian line in this market; audit cross-listed duplicates and Venture liquidity.

## Economic structure

- Preserve banks, energy infrastructure, metals/mining, uranium and digital-asset equities.
- Starter technology focuses on listed software; semiconductors/payments/medtech leave Light.

## Adverse flags

| Code | What it is |
|---|---|
| `cease_trade_order` | Subject to a cease trade order |
| `delisting_review` | Under exchange delisting review |
| `management_cto` | Subject to a management cease trade order |

## Research fields

- Provincial cease-trade/management orders; miners' resource versus reserve statements.

Report language: `en`, plus English when different. Use the closest [worked input](../../examples/README.md); no dedicated example ships.
See [dated example limits](../../examples/README.md).
