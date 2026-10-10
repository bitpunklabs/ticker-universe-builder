# Australia equities overlay

Read [shared equity rules](equity-common.md) first. Starter themes describe listed duties;
current budgets come from the [coverage plan](../coverage-plan.md), not display weights.

## Identity

- `ASX`, three to six characters starting with a letter.
- Resolve dual-listed economic identity; use the requested market's verified line.

## Economic structure

- Preserve mining, banks, medtech exports and listed property trusts.
- Starter technology emphasizes software/marketplaces; semiconductors/cybersecurity leave Light.

## Adverse flags

| Code | What it is |
|---|---|
| `asx_price_query` | Has received an ASX price or volume query |
| `capital_raising_halt` | Halted for a capital raising |
| `voluntary_administration` | In voluntary administration |

## Research fields

- ASX price/volume queries and responses, administration and capital-raising halts.

Report language: `en`, plus English when different. Use the closest [worked input](../../examples/README.md); no dedicated example ships.
See [dated example limits](../../examples/README.md).
