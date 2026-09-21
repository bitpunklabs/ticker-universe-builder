# Changelog

Notable changes to the skill's behaviour and contracts.

**Two version numbers live here, and they answer different questions.** The **skill** is
versioned with semver in `SKILL.md`, because a registry has to know when a new one exists and a
git tag has to point at the commit it was cut from. A **universe** carries its own `policy_hash`
and content hash, because a caller comparing two files needs to know whether they are the same
instrument — a question no release number can answer. The first does not date the second: a
universe built under 0.1.0 stays valid when 0.2.0 ships, and its hashes are what say so.

Each released heading below matches a `version:` in `SKILL.md`, a git tag of the same name, and
a ClawHub publish.

## 0.1.0 — 2026-09-21

First public release. Fourteen markets, each with reviewed rules, its own theme table, a
full-size Light example and a report in its own language.

Why 0.1.0 and not 1.0.0: the contracts are frozen and tested, but nobody outside this repository
has driven the CLI yet. Semver's promise is about what happens next, and claiming 1.0 stability
before a single outside caller has exercised it would be the kind of unearned claim the rest of
these documents refuse to make.

### A version number, and a much shorter description

`SKILL.md` carries `version: 0.1.0`, `metadata.openclaw.homepage` and an emoji, so a registry
listing has something to show. `CONTRIBUTING.md` has the release order — bump, head the
changelog, test, commit, tag, publish — and a test fails if the frontmatter version and the
newest changelog heading disagree.

The description went from 564 characters to 151. OpenClaw omits a long description rather than
truncating it, so brevity is functional there and a test pins the ceiling. The cost is real and
worth stating plainly: the old text named all fourteen markets, and that list is what routed
"build me a Japan ticker universe" to this skill without the asker using the repository's words.
The short text keeps `ticker universe`, `watchlist`, `TradingView` and `markets`. If routing
turns out to suffer, that is the first thing to look at, not the last.

### Release preparation

Both README media slots are GIFs and both are commented out until the files exist: the skill
building a US Medium universe, and that watchlist being imported into TradingView. The capture
instructions carry a constraint that is easy to hit mid-recording — US Medium targets 215 members
with a floor of 160, and the shipped US seed holds 101, so a Medium demo needs a real research
pass first or a Light universe instead.

`uv.lock` is gone. It was three lines, locked nothing — there is no `[project]` table — and
asserted `requires-python >= 3.13` against a README and a CI matrix that both say 3.10.

### The docs caught up with the last two rounds

Six documents still described a three-market skill with a theme cap. `methodology.md` listed
theme caps as step 5 of the selection order, where apportionment now is. `adding-a-market.md`
carried a classification table where eleven of the fourteen shipped markets were marked "to
write", explained the theme cap as a live mechanism, and closed with sketches for `hk`, `jp` and
`eu` — two of which ship and the third of which became `de` and `fr`, for a reason now recorded:
a cross-border row would have to carry venue *in* the identity, and every other row strips it.
`SKILL.md` and `AGENTS.md` told the agent three examples ship. `CONTRIBUTING.md` still described
registering a market as three additions.

`data-contracts.md` documented a `scope` field on `NO_CHANGE` that the parser has never read.
An agent filling it in would have believed it was recorded.

### Every registered market ships an example

`jp`, `hk`, `in`, `kr`, `tw`, `uk`, `de`, `fr`, `ca`, `au` and `br` join `us`, `cn` and `crypto`
under `examples/`: a seed table of real listings, a snapshot, a full-size Light universe at that
market's own target, and a report in that market's language. A test asserts the set of examples
equals the set of registered markets, so a row added without one fails on the same commit.

The examples now commit their **TradingView watchlist** as well. It is the artifact that actually
leaves the repository, and it should be readable and diffable without running a build.

Two symbol rules were wrong and are now fixed, both found by a real listing rather than by
reading the rule: `de` required a leading letter and rejected `4GLD`, and `br` required four
letters and rejected `B3SA3`.

Nine theme tables moved with them. A theme with nothing listed in it is worse than no theme,
because the breadth floor spends a slot on it anyway: managed care leaves Light in Japan, Korea,
Hong Kong and the UK, where health cover is single-payer; energy, payments and the data-centre
theme leave the German table entirely; megacap platforms leave the Indian one; Taiwan loses four
themes and gains property developers; Brazil raises managed care *into* Light, which no other
table does. Each change is recorded in the market's taxonomy note and its overlay.

`examples/build_examples.py` no longer carries a table of targets. Each example builds at the
target its market's `breadth` produces, so a policy change moves the examples and a stale number
cannot survive in the generator.

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
