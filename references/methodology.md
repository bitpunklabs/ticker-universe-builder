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

## Economic-driver maps in every market

Preserve the legacy pool's classification logic: primary business or protocol function, earnings
or token value capture, persistent catalyst, then supply-chain/network position. A country adapts
this logic to its own listed economy; it does not copy the US sector weights or force identical
themes. A provider label or a passing narrative is a discovery aid, not a permanent section.

Each theme declares an observation `purpose` and acceptable `representative_roles`. Market and
sector gauges have duties distinct from operating-company exposure. A company, upstream input,
sector basket and macro factor are not interchangeable just because prices correlate. Reuse the
existing theme code when the duty is unchanged; revise the taxonomy explicitly when it changes.

Research representatives first. Candidate `reason` explains the business variable or instrument
function, its relation to the theme and the evidence. Market cap, turnover or a low R² alone does
not establish leadership or information gain. Two leaders can be complementary; no one-leader
limit exists. For each extension, explain what would be lost without it. For deletion or
replacement, explain who retains that observation duty, or why the duty itself is obsolete.

Weights reflect the importance of durable drivers and differentiated positions. Do not derive
them from the candidate count returned by one data source. Recent performance does not justify
retiring a cold industry, and an unfit gauge requires fixing the measurement before judging names.

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
3. Expansion by the core / satellite / tactical bucket quotas, apportioned by largest
   remainder so the seats add up to the target rather than rounding into core.
4. Ranking inside a bucket by recomputable metrics and a fixed role order. A candidate is
   scored against the full weight of its bucket's fields, so a field it did not bring costs what
   that field weighs. Scoring only what is present would reward the absence, and this skill
   manufactures absences on purpose — an unmeasurable statistic is left `null` rather than
   guessed. A metric nobody measured does not earn a seat and does not get out of the way.
5. Apportionment of the remaining seats to theme weight, then the TradingView token cap.
   First-level concentration is measured and disclosed at this step, not capped.
6. Content hash, validation report, Markdown and txt.

The build then runs the whole order twice more on a bench whose measured metrics have been
nudged by ±1%, and reports what share of the membership all three runs agree on. A pool sold on
low turnover should be able to say how much of itself survives its own numbers being slightly
wrong, and the answer is a measurement rather than an assurance. The direction of the nudge is
drawn per ticker from a hash: shifting every number the same way would rescale the scores and
reorder nothing, and drawing it from a random number generator would make the reported number
unreproducible. Judged fields are not nudged — a judgement is not an estimate with an error bar.

It is a build-time number. Answering it needs the candidates that lost, and a stored universe
keeps only the members, so `validate` on a file reports no stability at all rather than a stale
one.

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

Inside each bucket, role priority precedes the role-appropriate score. The score is an
**ordinal tie-break**, not a rating or a forecast. This priority only makes sense when roles
are researched: low R² alone is not enough to assign `INDEPENDENT_SENSOR`; identify the
additional observed driver and check residual overlap with existing sensors. Otherwise use
`BREADTH_PROXY` and retain the measurements without claiming independent information.
The declared theme duties, required anchors and bucket budgets protect structure before
extension scores act. Do not tune role labels to manufacture a preferred ordering.

## The line between fact and judgement

The agent may judge theme boundaries, roles and the strength of evidence, but it has to write them
into a structured snapshot. Python never guesses a field out of natural language and never treats
a missing value as zero quality. Every value used for liveness, turnover, correlation or listing
status carries an `as_of` and a source, and every metric carries a `measurement` declaration that
says whether it was computed or judged.
