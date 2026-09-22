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

## 0.2.0 — unreleased

### A score no longer improves because a field is missing

`metric_score` renormalised over whichever weighted fields were present, so the denominator
shrank with the data and absence paid: a candidate carrying only `liquidity 0.95` outranked one
carrying `0.90 / 0.85 / 0.80 / 0.75` across all four. Scoring is now against the full weight of
the bucket's fields, so an absent field costs exactly what it weighs.

The absence was manufactured. `measurement.md` requires that a ticker with no usable volume
"gets no liquidity score rather than a guessed one" — the honesty rule was feeding the scoring
rule precisely the input it paid for. Two rules, each right alone, pulling against each other.

Every member now records `scored_on` — `{"present": n, "of": m}` — because `0.62` from four
fields and `0.62` from two are not the same claim. The build report prints the count of
partially scored members, and prints it only when it is not zero.

This fix moved no membership in the fourteen shipped examples, which is worth stating rather than
dressing up: every candidate with a gap was already losing on the fields it did bring. The unit
tests pin the behaviour; the examples happened not to hold the pathological case anywhere it was
contested. The seats that did change hands in this release changed for the rounding fix below.

### A percentile names the population it ranked against

`liquidity` is a rank over whichever bench got researched, and a seed holds sixty to a hundred
and twenty names — 0.9 against a hundred researched names may be 0.4 against the market. A
`measured` declaration of a cross-sectional metric now carries `population`; `measure` writes it
from the price table, and a declaration that omits it builds and warns. This does not make a
narrow bench acceptable. It makes it visible.

### Three quantities the build knew and never said

**What the breadth floor costs.** Every reachable theme takes a seat before weight is consulted,
which across the fourteen reviewed tables is 38–66% of a Light universe — Brazil spends 23 of its
35 seats before a single weight is read. `taxonomy --check` now reports `floor_share` on every
run, and warns only past 75%, where the table's weights have almost nothing left to order.

**The seat lost to rounding.** Bucket quotas were floored, and the pass that picked up the
leftovers handed them to `core` every time — the largest bench, sorted first — so the rounding
loss was a standing transfer rather than noise. Quotas are now apportioned by largest remainder,
the same discipline the themes already get from Sainte-Laguë. At a Light target of 35, tactical
is entitled to 1.75 seats and gets 2.

This is the change that moved the shipped universes. Nine of the fourteen markets gain an
entitlement, and four had a candidate to spend it on: br, fr, jp and tw each hand one seat from a
core member to the satellite or tactical member the bucket had been owed. One seat each, in the
direction the quota always intended.

**Drift measured against the wrong population.** A required benchmark never went through
apportionment, so counting it against a theme's weighted share compared an assigned seat to an
earned one — and since every market's required seats sit in its benchmark themes, the comparison
was skewed the same way in all fourteen. Required seats now leave both sides. With them out, the
reporting floor could come down from five members to three, which is where it becomes useful: at
Light most themes expect one to five members, so a floor of five left a theme at four times its
share invisible in the tier most people build.

### A build says how much of itself survives its own numbers being wrong

`build` reruns the entire selection twice on a bench whose measured metrics have been nudged by
±1%, and reports the share of members all three runs agree on. A pool whose stated purpose is low
turnover had no measurement of its own churn.

The industry answer is a buffer — a higher bar to enter than to stay. It may well be right here
later, but it is a constraint, and a constraint hides the quantity it acts on. Measure first, and
let a real number argue for it. Across the fourteen markets at Light the number lands between
**0.90 and 1.00**, median 0.97; uk gives up five of fifty seats to a 1% nudge and kr and fr give
up none. Build-time only: it needs the candidates that lost, so `validate` on a stored universe
reports no stability rather than a stale one.

### `evaluate` can finally see a pair

`factor_r2` measures a member against the factor complex and `independence` measures it against
the benchmark basket. Nothing compared two members to each other, so the breadth floor could
guarantee that every theme was represented while two seats quietly watched the same hill. The new
`redundancy` section reports the most correlated pairs over the window, with their themes beside
them. It reports and never gates — two names in one sector move together because that is what a
sector is, and the reader is better placed to judge the pair than a threshold would be.

Design note: [`docs/design/0.2.0-what-a-number-carries.md`](docs/design/0.2.0-what-a-number-carries.md),
including the two places the implementation came back different from the design.

## 0.1.0 — 2026-09-21

First public release. Fourteen markets, each with reviewed rules, its own theme table, a
full-size Light example and a report in its own language.

Why 0.1.0 and not 1.0.0: the contracts are frozen and tested, but nobody outside this repository
has driven the CLI yet. Semver's promise is about what happens next, and claiming 1.0 stability
before a single outside caller has exercised it would be the kind of unearned claim the rest of
these documents refuse to make.

### Community files, and a licence stated twice on purpose

`SECURITY.md`, issue templates and a PR template. The security document states a verified threat
model rather than a padded one: no sockets, no credentials, no subprocesses, no `eval` or
`pickle`; untrusted JSON parsed as data and validated against the contract; prose from a
third-party snapshot reaching a report the agent reads back; an output directory that refuses to
overwrite. It also says what is not a security issue.

The repository is MIT. The OpenClaw registry listing is **MIT-0**, because ClawHub carries no
licence field and distributes on those terms. Both are stated — in the README for users, in
CONTRIBUTING for contributors — rather than left to disagree quietly.

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
