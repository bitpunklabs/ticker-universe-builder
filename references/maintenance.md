# Maintenance contract

## Maintenance is not regeneration

The agent emits operations, never a rewritten universe. The script applies them to one exact
`base_version_hash`, then revalidates and re-renders. A hard finding produces no new version at
all — a partially applied universe is worse than an unchanged one.

Rewriting a full membership list cannot be reviewed: silently dropping twenty names, reordering
sections or mistyping a venue would all pass unnoticed. Operations can each be checked, rejected
individually and reversed.

## Three review depths

| depth | Purpose | Turnover warning |
|---|---|---:|
| `routine` | Liveness, venue, liquidity, recent leadership, tactical slots | 5% |
| `deep` | Taxonomy, sector structure, quality, redundancy, coverage gaps | 10% |
| `event` | Delisting, merger, regime or theme break with a dated cause | 20% |

These are how deep to dig, not calendar periods you must wait for. Exceeding the warning line
produces a warning; exceeding twice the line is a hard failure. An urgent delisting still needs
evidence.

## A verdict comes with an operation

Judging a theme overweight means issuing `REMOVE` or `MOVE` in the same round. Judging it
underweight or missing means issuing `ADD` or `ADD_THEME` in the same round. A note that says "to
be handled in the next deep review" is a verdict nobody owns, and it is the mechanism by which a
universe quietly rots.

The turnover budget is a ranking pressure, not a reason to do nothing: take the highest-information
changes first, spend the budget, and write the rest into `deferred` with a stated reason so the
next round inherits them as machine-readable input.

Restraint applies to chasing heat — do not create a permanent theme out of three months of price —
not to fixing a known defect.

## Live-information priority

1. Listing, contract or spot status, halts, delistings, venue changes.
2. 7 / 20 / 30 / 60-day turnover and data completeness.
3. 30 / 63 / 90 / 126 / 180 / 252-day correlation, beta, R² and residual stability.
4. ETF holdings, company disclosures, protocol and exchange announcements.
5. Theme heat and news — used to explain priority, never to decide permanent membership alone.

## Low turnover and hysteresis

- A challenger must clearly beat the entry threshold, not merely edge past the incumbent.
- Incumbents are held to a looser exit threshold.
- Outside a hard event, a failure should be confirmed by two consecutive snapshots.
- Re-adding a ticker removed within the last four rounds raises a flip-flop warning.
- High-value candidates that did not fit this round's budget go into `deferred`.
- When there is not enough information gain, `NO_CHANGE` is the correct result.

## Review checklist

- Is every existing member still live, tradable and on the right venue?
- Is a current theme leader or a genuinely new sector missing?
- Is a highly redundant member occupying a seat?
- Do cold sectors and market breadth still have representation?
- Is every high-beta label still supported by stable beta and R²?
- For Crypto: is each member still active on its Binance market with sustained turnover?
- Do tier, theme, role and concentration still match the policy?
- Has any bucket drifted above its target share? The validator reports this; act on it.
