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
   listings and turnover anomalies change quickly. They must not redefine the permanent coverage roster.
6. **Fail closed.** Incomplete data, a stale version, missing evidence or a failed structural check
   blocks formal publication while preserving research and a resumable checkpoint.

## Economic-driver maps in every market

Preserve the legacy pool's classification logic: primary business or protocol function, earnings
or token value capture, persistent catalyst, then supply-chain/network position. A country adapts
this logic to its own listed economy; it does not copy the US sector weights or force identical
themes. A provider label or a passing narrative is a discovery aid, not a permanent section.

The economic plan is separate from display themes. Define stable parent sectors, important
business branches, and a reviewed leader/necessary-peer roster before optional candidates.
Every necessary representative is protected at its declared depth; one arbitrary anchor in a
large bank or consumer section cannot certify all its economic roles. See the
[coverage contract](coverage-plan.md).

Research representation, differentiated business function and continuing quality from sources.
Market cap, turnover and a low R² alone do not establish these. Each satellite explains what
would be lost without it relative to named core members. A deletion explains how observation
survives or why the function left scope. Neither recent weakness nor news heat changes the
backbone. Sector caps and weights reflect stable structure, never provider inventory or the
number of display headings. Preserve direct indices/yields separately from tradable proxies.

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

1. Validate the sourced market plan, complete core roster, instrument identity and admissions.
2. Select every necessary leader/peer due at the depth; fail if missing or infeasible.
3. Check Core migration decisions and economic branch coverage before optional additions.
4. For Heavy/Extreme only, add measured Beta with sourced quality and incremental value,
   within hard sector, satellite-share, entity and TradingView ceilings. Stable parent-sector
   weight divided by `2 * held + 1` orders optional seats; display weights and heat do not.
5. Validate again, including Extreme's 30%–40% entity growth, then hash and render TXT/JSON/reports.
   Unused capacity above that minimum is allowed. Missing backbone or expansion is a recoverable
   research gap, not a completed production watchlist.

Light/Medium select leaders only. All declared leaders and necessary peers must enter Heavy;
Extreme requires an embedded, validated same-date Heavy and adds satellites only. Rebuilding
Light/Medium from the same roster preserves nesting; expanding Extreme preserves Heavy's exact
members and facts. A changed Heavy requires a new Extreme. Historical quota/stability selection
is available only through the explicit archived example policy; it does not certify this model.

## What the composite score is, and what it is not

The existing measured score breaks ties between already-qualified satellites inside sector
budgets. Heat is excluded. It cannot buy a place ahead of a necessary representative or excuse
missing business/quality evidence. The old observation roles remain measurable descriptors;
new admission roles (leader/peer/satellite) carry the researched selection function. Do not
promote a BREADTH_PROXY, ANCHOR or high-beta candidate into leadership to fill capacity.

## The line between fact and judgement

The agent may judge theme boundaries, roles and the strength of evidence, but it has to write them
into a structured snapshot. Python never guesses a field out of natural language and never treats
a missing value as zero quality. Every value used for liveness, turnover, correlation or listing
status carries an `as_of` and a source, and every metric carries a `measurement` declaration that
says whether it was computed or judged.
