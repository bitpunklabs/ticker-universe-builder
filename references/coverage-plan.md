# Coverage-first research contract (0.6)

The default selector requires this plan and researched admissions. Read with
[data contracts](data-contracts.md). Core membership, provider tags, size and observation roles
alone do not establish leadership. [Archived replay](../assets/legacy-policy.json) is separate.

## Plan before candidates

`snapshot.coverage_plan` requires:

| Field | Shape / meaning |
|---|---|
| `schema_version` | `1` |
| `origin` | `new` or `migration`; migrating a user Core requires `baseline` |
| `scope` | Explicit market, venues, instrument types, exclusions; do not silently narrow Crypto to Binance |
| `evidence` | Dated tier 1/2 evidence for the stable market structure, not recent news heat |
| `budgets` | `{light: int, medium: int, heavy: int, max: int}` positive, nondecreasing **entity ceilings**, excluding references |
| `sectors` | List of `{id, weight, rationale, caps}`; positive stable weight and four nondecreasing integer absolute caps keyed by profile |
| `branches` | List of `{id, sector, purpose, min_profile, representatives}`; `representatives` is a nonempty list of necessary economic `asset_id`s; each entity has one primary branch |
| `roster` | Every branch representative exactly once: `{asset_id, kind, min_profile}`; kind `leader` or `peer`, admitted by Heavy |
| `references` | List described below, may be empty; BTC/ETH/SOL are Crypto entities, not references |
| `display_groups` | Optional four-profile object; rows have constituent `id`, ASCII `name`, disjoint known `themes`, and economic-similarity `reason`; Heavy/Max maps must match |


All branch representatives occur exactly once in the roster and must be eligible, researched
candidates before building the ladder. Leaders' `min_profile` is Light/Medium/Heavy; peers enter
Heavy. Branch minimum depth needs a qualified core representative. Budgets/caps must fit every
representative due at that depth; never shift a tier to fit capacity.

Economic branches are independent of display groups. Merge sparse related groups while preserving
duties/facts; Light/Medium can be broader, Heavy/Max maps must match. Heading splits create no seats.
Light is leader-only, Medium covers at least 70% of declared leaders, Heavy selects all leaders/peers.
The roster is a researched denominator, not a market-wide leadership census.

Heavy optional seats follow stable sector weights; Max follows frozen Heavy group entity proportions.
For H Heavy entities and A additions, a group with h entities may add at most `ceil(h*A/H)`.
Only integer rounding creates surplus; shortages cannot transfer seats. Stop at minimum qualified
expansion. Heavy satellites are at most 20%, Max at most 35%; sector caps also bind protected core.
These engineering limits are not optimal portfolio weights. Recent heat and display weights do not enter.

## Candidate admission

Each selected entity adds this object to the candidate contract:

| Field | Meaning |
|---|---|
| `kind` | `leader`, `peer`, `satellite`; selection function, distinct from measured beta or observation role |
| `branch` | One economic branch id; determines primary sector independently of display theme |
| `min_profile` | Light/Medium/Heavy for leaders; Heavy for peers; Heavy/Max for satellites |
| `business` | Why this entity represents this business function; source-supported leadership/necessary differentiation |
| `quality` | Required for leaders/peers: domain-specific continuing quality/observability reasoning; optional for satellites |
| `evidence` | Tier 1/2 evidence for those assertions, no future dates and within 180 days of snapshot |
| `instrument` | `{kind, quote_currency, units}`; kind equity/spot/perpetual/etf, positive units; explicit contract multiplier |
| `ecosystem_id`, `token_role` | Required for Crypto; distinguish VET/VTHO roles without claiming two independent networks |
| `market_cap` | Satellites: `{value, currency, basis, as_of, source}`; positive finite capitalization, equity/native quote currency for stocks, circulating/USD for Crypto (never FDV); within 30 days, matching dated tier 1/2 admission evidence |
| `distinct_from`, `incremental_value` | Satellites only: nonempty core asset-id list and what is missing without this candidate |


Core admissions need compatible core observation roles; satellites use `BETA_SATELLITE`.
Entity liquidity is measured. Supplied price R²/beta/stability require valid measurements but
are optional Beta descriptors, never admission floors. Unannotated candidates remain an unverified
bench; malformed supplied admissions fail. Legacy breadth/tactical roles cannot fill new lists.

Read evidence and compare core representatives against peers; schema validity does not prove
leadership. Beta research stops at broad business/token identity, named-core complementarity and
sourced cap. Rank eligible Beta by cap, ties by ticker; detailed profitability/tokenomics is optional.
Crypto core research still covers use, token value capture, supply, liquidity and residual redundancy.
Protocol fees, holder revenue and TVL are different facts; missing revenue does not exclude every network.

## Reference instruments

Rows are `{id, ticker, theme_code, kind, observes, evidence}`; kind is
index/yield/fx/commodity/etf/spot/future/ratio. Verify the exact venue-prefixed instrument and
observation duty. Proxies add `proxy_for` and `limitation`; never rename an ETF as an index.
Direct indices/yields need no invented volume. References use export capacity, not entity/sector/
satellite seats. Companies and protocols cannot be moved here to evade ceilings.

## Core migration

```bash
python scripts/universe.py audit-core --watchlist core.txt --universe old-heavy.json --output core-audit.json
```

The audit preserves original text/SHA-256, full-code differences and pending decisions. The plan's
`baseline` is `{watchlist, sha256, decisions}`. Every original code appears exactly once as
`{ticker, action, reason, evidence}`; retain/replace binds one `asset_id` or `reference_id`.
Actions: retain/replace/remove/pending. Retain preserves the exact code; venue or spot/perpetual
conversion requires sourced identity/unit/duty explanation. Removal explains surviving coverage.
Pending blocks Heavy/Max, and retained/replacement targets must enter Heavy. No automatic aliases.
Historical Core scales and budget constraints are in [tier profiles](tier-profiles.md).

## Building and continuing

`target_count` defaults to the plan ceiling and may only lower it. Under-ceiling output is complete
when every gate passes. Missing backbone, identity or Core decisions preserve inputs/checkpoints as
`needs_research`; repair the facts, remeasure affected candidates and [resume](recovery.md).

Max requires qualified `--seed heavy.json`, identical market/date/plan and retained facts/bindings.
Its embedded `heavy_base` supports standalone validation. Add at least `ceil(0.30*H)` satellites;
references do not count. Sector/share/export caps still bind; changing Heavy requires rebuilding Max.
A growth-only gap within 5% of required total entities can be explicit partial, with positive
Beta growth and frozen planned group quotas. See [delivery](data-contracts.md#max-shortfall-delivery-071).

Legacy `taxonomy --check` is a display preflight, not economic feasibility certification.
Build/validate check the plan; legacy validation discloses absent coverage certification.
