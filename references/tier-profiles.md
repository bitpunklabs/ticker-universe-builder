# Light / Medium / Heavy

## How the counts are set

A tier is a **depth of observation**, and it costs a different number of tickers in different
markets. The same depth needs more names where more distinguishable, separately-moving stock
lists — so a market states one number, its **breadth**, and the three targets follow:

```text
target = tier base x market breadth, rounded to five
band   = target +/- 25%, rounded to ten
```

The tier bases are **60 / 160 / 400** and live in `assets/default-policy.json` under `tiers`.
Breadth lives beside each market under `markets.<code>.breadth`, and it is the only size number
a market carries. Nine numbers per market was nine chances to be inconsistent and no way to tell
which of the nine was deliberate; one number is a claim about the market that can be argued with.

Read the tiers as: Light is a focus list — every Level-1 theme represented, the important ones
several times over, scannable in one sitting. Medium is a sector-complete scanning pool. Heavy is
index-scale breadth, and even at 540 it stays under the 1000-token TradingView cap once the theme
headers are counted.

## The registered markets

| Market | | Breadth | Light | Medium | Heavy |
|---|---|---:|---:|---:|---:|
| `us` | US equities and ETFs | 1.35 | 80 | 215 | 540 |
| `cn` | China A-shares | 1.3 | 80 | 210 | 520 |
| `jp` | Japan equities | 1.05 | 65 | 170 | 420 |
| `in` | India equities | 1.0 | 60 | 160 | 400 |
| `hk` | Hong Kong equities | 0.9 | 55 | 145 | 360 |
| `kr` | Korea equities | 0.9 | 55 | 145 | 360 |
| `uk` | UK equities | 0.85 | 50 | 135 | 340 |
| `tw` | Taiwan equities | 0.8 | 50 | 130 | 320 |
| `de` | Germany equities | 0.75 | 45 | 120 | 300 |
| `fr` | Euronext Paris equities | 0.75 | 45 | 120 | 300 |
| `ca` | Canada equities | 0.75 | 45 | 120 | 300 |
| `au` | Australia equities | 0.7 | 40 | 110 | 280 |
| `crypto` | Crypto spot and perpetuals | 0.65 | 40 | 105 | 260 |
| `br` | Brazil equities | 0.55 | 35 | 90 | 220 |

Breadth is not market capitalisation. It is roughly: how many names this market lists that a
reader could tell apart, sustain a position in, and would be worse off not watching. The US and
the A-share market sit at the top because they list thousands of such names; Brazil sits at the
bottom because it lists perhaps eighty, and a Heavy Brazilian universe of 540 would be padding.

Any market not in this table builds by declaring `breadth` in its snapshot's `market_spec`, under
the same evidence gate as every other researched fact. Same arithmetic, same tiers; what it does
not carry is a second pair of eyes, and the report says so on every run.

These numbers are an initial calibration, not permanent constants. `evaluate` is what
recalibrates them — specifically its coverage section, which reports how much of the largest
realised moves a universe of this size actually contained, and names the ones it missed. Nothing
here has been recalibrated from real data yet; see the limits section of the README.

## Coverage and role quotas

| Tier | Coverage | core target | satellite cap | tactical cap |
|---|---|---:|---:|---:|
| Light | Core structure and core themes | 80% | 15% | 5% |
| Medium | All major sectors and major second-level themes | 65% | 25% | 10% |
| Heavy | Qualified broad, cold and emerging themes | 50% | 35% | 15% |

Quotas are targets, not filling instructions. With no qualified satellite, the seats return to
core; with no candidate clearing the hard gates, the universe is allowed to sit below its lower
bound. Liveness, venue, turnover and evidence requirements are never relaxed to reach a number.

The percentages are turned into whole seats by **largest remainder**, the same discipline the
themes get from Sainte-Laguë. Flooring each share instead would drop up to one seat per bucket,
and the pass that picks the leftovers up hands every one of them to core — core is the largest
bench and sorts first — so the rounding loss would be a standing transfer to the biggest bucket
rather than noise. At a Light target of 35, tactical is entitled to 1.75 seats and gets 2.

A bucket that ends up more than ten points above its target is reported as a warning — on a build
that means the qualified core ran out, and on a review it means the universe has been drifting one
evidence-backed operation at a time.

## There is no theme cap

There used to be one: a ceiling on how many members any single theme could hold. It is gone, and
what replaced it is the reason it had to go.

A cap says every theme is worth the same. That is false in every market and obviously false in
some. Semiconductors, the battery chain and the software complex carry what the A-share market
does; property development is still listed, still liquid, and worth watching — but not on the
same shelf. Under a shared ceiling there were only two outcomes, and both were wrong: cut the
theme that matters off at four names, or hand four slots to the theme that does not and watch the
selector fill them with whatever was least bad.

So a theme now carries a **weight** instead, and the ceiling is gone entirely.

```text
priority(theme) = weight / (2 x members already held + 1)
```

Every theme reachable at the tier's coverage level gets its first member before any theme gets a
second — breadth is a floor and is not negotiable. After that, each remaining slot goes to the
theme with the highest priority, which is the Sainte-Laguë divisor rule used to apportion seats
to votes. Run to convergence it gives a theme members in proportion to its weight: three times
the weight, about three times the members. Within the chosen theme, the slot goes to the
best-ranked candidate the bucket quotas still allow.

Three properties follow, and they are the ones a cap could not give:

- **An empty bench costs nothing.** A theme with no eligible candidates left simply stops winning
  slots, and they flow to the next theme in line. Under a cap, a thin theme held its allowance
  open while the universe finished short.
- **Weights are auditable and local.** They live in the taxonomy, beside the theme they describe,
  where the person arguing about semiconductors versus property can see and change the number.
  A cap lived in the policy file and applied to everything.
- **Concentration is disclosed, not prevented.** The report prints the largest theme, its share
  of the universe, and what its weight asked for. If a market really is one theme deep — Taiwan
  is — the universe says so instead of hiding it behind a ceiling.

Weights run from 0.25 to 4.0, default 1.0. The range is a guard rail, not a judgement: below a
quarter a theme is not worth a row in the table, and above four the apportionment is being used
to hand-pick the universe, which is what roles and buckets are for. `taxonomy --check` reports
any theme weighted to hold more than 15% of the universe — not as an error, because that may be
exactly right, but because it should be deliberate.

Validation is a disclosure too. A theme holding three or more members and more than 2.5x its
weighted share is reported, because a build apportions but maintenance does not: a pool can walk
a long way into one theme, one evidence-backed operation at a time, and nothing else would say so.

Both sides of that comparison count only **apportioned** seats. A required benchmark is in the
universe because the market spec names it, not because its theme won a slot, so counting it
against a weighted share compares an assigned seat to an earned one. Every market carries two or
three required seats and they all sit in its benchmark themes, so leaving them in skewed the same
theme in the same direction in all fourteen — Korea's `00_A` holds three against an expectation
of one, and two of the three are required. The floor of three only became usable once they were
out; at five, a Light universe (where most themes expect one to five members) could hold a theme
at four times its share and say nothing.

## Coverage levels

Every theme in the taxonomy carries one:

- `coverage_level=1` — the market skeleton Light must cover;
- `coverage_level=2` — the major themes Medium adds;
- `coverage_level=3` — the breadth, cold and emerging themes Heavy adds.

A market's own table moves themes between levels. Autos sit at level 2 in the shared equity base
and at level 1 in Japan and Germany; games and interactive sit at level 3 in the base and at
level 1 in Japan and Korea. That is the same statement as a weight, made at a coarser grain: not
how much of the universe this theme is worth, but whether the shallowest tier has to look at it
at all.

Inside a theme, members are still ordered by role and metrics. What Heavy adds should mostly be
independent sensors, supply-chain breadth, high beta, liquidity and new-listing observation — not
more names sharing a driver the universe already holds.
