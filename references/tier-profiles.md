# Light / Medium / Heavy

## How the counts are set

A tier is a **depth knob on the theme table**, not a size knob. Pick a coverage level, and the
count follows from how many themes that level reaches and how deep the tier goes into each:

```text
capacity = themes reachable at this coverage level x theme_cap
target   ~ two thirds of capacity
```

Two thirds, not all of it, because a target equal to capacity means every theme is forced to
exactly `theme_cap` members and the selector has no choice left to make — the ranking stops
mattering and the universe is just the seed list. Two thirds leaves the cap binding where a
theme is genuinely crowded and slack everywhere else, which is what a cap is for.

This is also why the sizes differ per market and the tier parameters do not. The more
homogeneous a market is, the more its main factors explain and the fewer assets sustain high
turnover, so the fewer themes it can distinguish — and the count falls out. Crypto is far
smaller than CN or US because its table is, not because a smaller number was chosen for it.

## V1 default ranges

| Market | Light | Medium | Heavy |
|---|---:|---:|---:|
| CN | 60–100, default 80 | 180–300, default 240 | 450–750, default 600 |
| US | 60–100, default 80 | 180–300, default 240 | 450–750, default 600 |
| Crypto | 30–50, default 40 | 60–90, default 75 | 90–160, default 125 |

The band is one rule rather than nine numbers: **target ±25%, rounded to ten.** A test asserts
it, so a hand-edited bound fails rather than quietly becoming a market's private convention.

Read the tiers as: Light is a focus list — every Level-1 theme represented two or three times,
scannable in one sitting. Medium is a sector-complete scanning pool. Heavy is index-scale
breadth, and at 600 it still leaves room under the 1000-token TradingView cap once the theme
headers are counted.

CN and US carry identical numbers because there is no evidence to separate them: comparable
listed breadth, comparable theme tables. Two numbers that differ by ten for no stated reason are
worse than one number used twice.

These are an initial calibration, not permanent constants. `evaluate` is what recalibrates them —
specifically its coverage section, which reports how much of the largest realised moves a
universe of this size actually contained, and names the ones it missed. Nothing here has been
recalibrated from real data yet; see the limits section of the README.

## Coverage and role quotas

| Tier | Coverage | core target | satellite cap | tactical cap | `theme_cap` |
|---|---|---:|---:|---:|---:|
| Light | Core structure and core themes | 80% | 15% | 5% | 4 |
| Medium | All major sectors and major second-level themes | 65% | 25% | 10% | 8 |
| Heavy | Qualified broad, cold and emerging themes | 50% | 35% | 15% | 15 |

### What `theme_cap` actually does

It is the most-members-one-theme-may-hold limit, and it is the only thing standing between a
universe and the failure mode every hand-built watchlist has: the theme its author finds most
interesting eats the list. Ranking alone cannot prevent that — if semiconductors genuinely hold
the twenty highest-scoring names in the market, a pure ranking returns twenty semiconductors, and
the universe stops being an observation instrument for the market and becomes one for
semiconductors.

So the cap is a **diversity floor written as a ceiling**. Capping any one theme at four in Light
is what forces the twentieth slot to go to the best name in a theme not yet represented, which is
the name that actually adds information.

Three consequences worth knowing:

- **The cap scales with the tier, not with the market.** Four, eight, fifteen — going deeper into
  a market means both more themes and more names per theme. A market does not get its own cap;
  a market that appears to need one has a theme table that is too coarse.
- **The cap and the target are one constraint, not two.** `themes x cap` is a hard ceiling on the
  universe, so a table too thin for its target cannot be fixed by raising the target. Run
  `taxonomy --check` before researching anything; it does this arithmetic for you.
- **Hitting the cap is reported, not silent.** Rejected candidates carry
  `not_selected_under_budget_or_theme_cap` in the audit, and the count of them is in the report.
  A universe losing many candidates to the cap is telling you its theme table is too coarse for
  the market it is trying to observe.

Quotas are targets, not filling instructions. With no qualified satellite, the seats return to
core; with no candidate clearing the hard gates, the universe is allowed to sit below its lower
bound. Liveness, venue, turnover and evidence requirements are never relaxed to reach a number.

A bucket that ends up more than ten points above its target is reported as a warning — on a build
that means the qualified core ran out, and on a review it means the universe has been drifting one
evidence-backed operation at a time.

## Coverage levels

Every theme in the taxonomy carries one:

- `coverage_level=1` — the market skeleton Light must cover;
- `coverage_level=2` — the major themes Medium adds;
- `coverage_level=3` — the breadth, cold and emerging themes Heavy adds.

Inside a theme, members are still ordered by role and metrics. What Heavy adds should mostly be
independent sensors, supply-chain breadth, high beta, liquidity and new-listing observation — not
more names sharing a driver the universe already holds.
