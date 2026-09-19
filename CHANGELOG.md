# Changelog

Notable changes to the skill's behaviour and contracts. Not released on a version schedule — a
universe carries its own `policy_hash` and content hash, which is the version that matters to a
caller.

## Unreleased

### The theme cap became a share

The per-theme cap in `assets/default-policy.json` is now a **ceiling**, not the operative number.
The cap in force is `min(ceiling, round(1.5 × target / themes))`, floor 2 — one theme may hold
half again its fair share of the universe and no more. A flat 4/8/15 had let a single crypto
theme hold 10-12% of its universe against 2.5-5% for equities, which meant the cap bound in one
market and never bound in another. The report prints the cap it used.

### A tier became a depth knob on the theme table

Light, Medium and Heavy are now defined as a depth on the theme table rather than a count beside
it: `target ≈ ⅔ × reachable themes × cap`. The starter equity tables grew to about thirty
Level-1 themes each and the equity targets moved to 80 / 240 / 600 (crypto 40 / 75 / 125), which
is the first time the shipped targets have been reachable by the shipped tables — CN Light used
to ask for 220 members from a table that could not hold 72. `taxonomy --check` now passes clean
for every market at every tier, asserted by a test.

Size guidance bands are one rule rather than nine numbers: target ±25%, rounded to ten.

### Markets can name their own adverse flags

`market_spec.quality_flags` lets a market declare the adverse statuses that exist in it —
`special_treatment` in CN, `listing_deficiency` in US, `unlock_overhang` in crypto — without
letting it price them. The scoring weight stays central; only the vocabulary is per-market, it is
closed and therefore countable, and the report tallies it. A flag from the wrong market names the
market it belongs to.

### `evaluate`

A universe can now be measured against the window it lived through: survival, coverage of the
largest moves, the cost of each exclusion code, per-theme volatility, per-metric rank correlation,
declared independence against realised. It is not a backtest and never reports what a universe
"returned". Nothing in the repository has been recalibrated from it yet.

### Earlier

The first shipped capability set: `taxonomy`, `import`, `measure`, `build`, `maintain`, `diff`,
`validate`; three registered markets (`cn`, `us`, `crypto`) and declared `market_spec` for any
other; three locales (`en`, `zh-Hans`, `zh-Hant`) with the report written in the market's own
language; measurement declarations with `basis: measured | judged | blended`; turnover budgets,
hysteresis and the `deferred` queue; content hashing and atomic writes; three Light examples
rebuilt by the test suite.
