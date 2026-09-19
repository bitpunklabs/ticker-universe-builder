# Methodology

## What the product is

A ticker universe is an observation instrument, not a recommendation list. Every member has to
answer one question: if it were deleted, which structure, leadership, risk appetite or independent
price information would be lost? If the answer is only "it is popular", the evidence is missing.

## First principles

1. **Coverage before ranking.** Market structure, first-level sectors and core themes are not
   displaced by a global score ranking.
2. **Incremental information first.** Assets with the same driver and the same path consume
   observation slots. Redundancy has to affect admission.
3. **One role per member.** A ticker carries exactly one primary role, though it may carry several
   pieces of evidence.
4. **Compare inside the market.** Equities are measured against their own sector or theme gauge,
   never against the broad index alone — a broad-index regression credits every semiconductor with
   the sector's move. Crypto is measured against the BTC/ETH/SOL factor set.
5. **Slow structure, fast signal.** Sector structure and business models change slowly; heat, new
   listings and turnover anomalies change quickly. They get different quotas and different
   maintenance thresholds.
6. **Fail closed.** Incomplete data, a stale version, missing evidence or a failed structural check
   produces no universe at all, rather than one that merely looks successful.

## Primary roles

| Role | Meaning | Bucket |
|---|---|---|
| `BENCHMARK` | Market, style or sector ruler | core |
| `ANCHOR` | Structural anchor that cannot be dropped casually | core |
| `THEME_LEADER` | Strongest leadership inside its theme | core |
| `QUALITY_LEADER` | Business durability or asset quality representative | core |
| `BETA_SATELLITE` | High-beta amplifier of a theme or market shock | satellite |
| `INDEPENDENT_SENSOR` | Price sensor the main rulers do not explain | satellite |
| `BREADTH_PROXY` | Cold sector, supply-chain position or market breadth | satellite |
| `LIQUIDITY_SENSOR` | Short-horizon sensor for turnover and speculative appetite | tactical |
| `NEW_LISTING` | Recently listed name that already clears the basic trading floor | tactical |

A high-beta claim must report beta, R² and multi-window stability together. A candidate with low R²
is not high beta; if it genuinely adds information, it belongs in `INDEPENDENT_SENSOR`.

## Deterministic selection order

The builder allocates seats in this order:

1. Eligible benchmarks and anchors marked `required=true`.
2. At least one representative for every theme the current tier must cover.
3. Expansion by the core / satellite / tactical bucket quotas.
4. Ranking inside a bucket by recomputable metrics and a fixed role order.
5. Theme caps, first-level concentration and the TradingView token cap.
6. Content hash, validation report, Markdown and txt.

Building Medium resolves the Light set first; Heavy resolves Medium first. Under one snapshot and
one policy, `Light ⊆ Medium ⊆ Heavy` therefore holds. Across snapshots it holds only if the
existing universe is passed in as `--seed`.

## Changing depth in either direction

`--seed` reads the depth of the universe you hand it and moves along the nesting from there.

- **Widening** (Light → Medium) keeps every incumbent and fills the remaining slots from the
  snapshot.
- **Narrowing** (Heavy → Light) makes the incumbents the *only* candidates and reselects inside
  them against the smaller target. Themes above the narrower coverage level fall away with the
  reason `outside_profile_coverage`; members that lost a slot to the smaller target are recorded
  as `removed_by_downgrade`; everything else in the snapshot is `not_in_seed_universe`, because
  a narrowing run never considered it and saying it lost on budget would be a different claim.

Neither direction is a rebuild. Rebuilding at the new depth would churn a pool whose entire
purpose is low turnover, and would drop incumbents for reasons that have nothing to do with the
depth that changed. An incumbent the new snapshot no longer carries as an eligible candidate
stops the build and is named either way: dropping it is the operator's decision.

## What the composite score is, and what it is not

Inside a bucket, members are ordered by role first and by a weighted metric score second. That
score is an **ordinal tie-break**, not a measurement. Two candidates separated by a couple of
points are not meaningfully different, and nothing downstream should treat the number as a rating.
Role order carries the structural judgement; the score only breaks ties inside it.

## The line between fact and judgement

The agent may judge theme boundaries, roles and the strength of evidence, but it has to write them
into a structured snapshot. Python never guesses a field out of natural language and never treats
a missing value as zero quality. Every value used for liveness, turnover, correlation or listing
status carries an `as_of` and a source, and every metric carries a `measurement` declaration that
says whether it was computed or judged.
