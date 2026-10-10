# Brazil equities overlay

Read [shared equity rules](equity-common.md) first. Starter themes describe listed duties;
current budgets come from the [coverage plan](../coverage-plan.md), not display weights.

## Identity

- `BMFBOVESPA`: four alphanumeric characters starting with a letter, then one/two digits.
  Digits encode share class (`3` ordinary, `4` preferred, `11` unit); `B3SA3` is valid.
- Common/preferred/unit company lines share identity. Choose the verified liquid line; audit duplicates.

## Economic structure

- Preserve mining, oil, banks, protein/beverages, agribusiness and listed private healthcare.
- Agribusiness observes weather/commodity drivers, not generic staples.
- Starter technology is limited; media/payments/medtech leave Light. Do not substitute overseas listings.

## Adverse flags

| Code | What it is |
|---|---|
| `cvm_inquiry` | Subject to a CVM ofício |
| `judicial_recovery` | In recuperação judicial |
| `segment_downgrade` | Downgraded from its listing segment |

## Research fields

- Novo Mercado/Nível 1/2 status, judicial-recovery/CVM filings and free float.

Report language: `pt-BR`, plus English when different. Use the closest [worked input](../../examples/README.md); no dedicated example ships.
See [dated example limits](../../examples/README.md).
