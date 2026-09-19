# Changelog

Notable changes to the skill's behaviour and contracts. Not released on a version schedule — a
universe carries its own `policy_hash` and content hash, which is the version that matters to a
caller.

## Unreleased

### Fourteen markets, each reporting in its own language

`us`, `cn` and `crypto` are joined by `jp`, `hk`, `in`, `kr`, `tw`, `uk`, `de`, `fr`, `ca`, `au`
and `br`. Each ships a reviewed registry row — venues, symbol shape, identity rule, adverse-flag
vocabulary, default report language — plus a theme table and a market overlay under
`references/markets/`. Any market outside the fourteen still builds by declaring the same facts in
the snapshot, and is still reported as declared rather than reviewed.

Equity markets no longer carry a theme table each. `assets/taxonomy/_equity.json` holds the shared
base and a market states only its delta: what it does not list, what nobody else lists, and the
weights. A correction to a shared theme now lands once instead of eleven times.

Five locales join the three: `ja`, `ko`, `de`, `fr`, `pt-BR`. The invariant they hold is narrower
than before, and deliberately: the chrome is identical in every locale, each market's adverse-flag
vocabulary exists in that market's own language, and `en` remains the complete fallback that any
locale falls back to for a flag it does not name.

### The theme cap is gone

A single cap asserted that every theme is worth the same number of slots, which is false in every
market — semiconductors in Korea and property in China are not the same kind of thing. Themes now
carry a `weight` in `[0.25, 4.0]` (default 1.0) declared in the taxonomy, and slots are
apportioned by Sainte-Laguë priority, `weight / (2 × held + 1)`.

Three properties follow that a cap could not offer: a theme with an empty bench costs nothing,
because unclaimed slots flow on rather than being reserved; weights are local, auditable and
diffable where the theme is defined; and concentration is **disclosed** rather than prevented —
the report prints the largest theme's share beside what its weight asked for, and validation warns
when a theme holds at least five members and more than 2.5× its weighted share.

`taxonomy --check` warns when a single theme is weighted above 15% of the universe. The exclusion
code `not_selected_under_budget_or_theme_cap` is now `not_selected_under_budget`.

### Tier sizes follow the market

A market states its size as one number. `breadth` scales the tier bases 60 / 160 / 400, so
`target = round(base × breadth / 5) × 5` and the guidance band is ±25% rounded to ten. US Light is
80 members, Japan Light 65, Brazil Light 35. Larger, deeper markets get more room at the same
depth without nine hand-written numbers per market; a declared market supplies either a `breadth`
or an explicit `guidance` block.

`assets/default-policy.json` moves to `schema_version: 2`: `tiers` and per-market `breadth`
replace the per-market per-tier target blocks, and `theme_cap` is gone from every profile. Every
registered market's starter table now checks clean at every depth, asserted by a test and by CI.

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
`validate`; three registered markets and declared `market_spec` for any other; three locales with
the report written in the market's own language; measurement declarations with
`basis: measured | judged | blended`; turnover budgets, hysteresis and the `deferred` queue; content hashing and atomic writes; three Light examples
rebuilt by the test suite.
