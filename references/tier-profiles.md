# Light / Medium / Heavy

## How the counts are set

A count is not a fixed share of the listed universe. It falls out of four constraints:

```text
effective capacity = required structural coverage
                   + leadership density per core theme
                   + satellites that clear the marginal-information threshold
                   + a tactical observation budget with a stated purpose
```

The more homogeneous a market is, the more its main factors explain, and the fewer assets sustain
high turnover, the smaller its effective capacity. That is why Crypto is far smaller than CN or US.
The guidance ranges exist to catch abnormal inputs, not to be filled.

## V1 default ranges

| Market | Light | Medium | Heavy |
|---|---:|---:|---:|
| CN | 150–250, default 220 | 350–500, default 450 | 650–850, default 750 |
| US | 180–280, default 230 | 380–520, default 450 | 650–850, default 750 |
| Crypto | 30–50, default 40 | 60–90, default 75 | 100–150, default 125 |

These are an initial calibration, not permanent constants. Once real builds accumulate, recalibrate
against: assets clearing the listing, venue and liquidity gates; the count of first-level sectors
and viable themes; the distribution of correlation and R² against each theme's own gauge; the
marginal information a new ticker adds to actual observation; and the share of additions, removals
and round trips seen in maintenance.

Nothing in this skill produces that data yet — see the limits section of the README.

## Coverage and role quotas

| Tier | Coverage | core target | satellite cap | tactical cap | Per-theme cap |
|---|---|---:|---:|---:|---:|
| Light | Core structure and core themes | 80% | 15% | 5% | 4 |
| Medium | All major sectors and major second-level themes | 65% | 25% | 10% | 8 |
| Heavy | Qualified broad, cold and emerging themes | 50% | 35% | 15% | 15 |

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
