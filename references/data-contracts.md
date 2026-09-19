# Data contracts

Three inputs, one output record. Every file is a JSON object with `schema_version: 1`.

## build-spec.json

```json
{
  "schema_version": 1,
  "market": "crypto",
  "profile": "light",
  "as_of": "2026-09-16",
  "target_count": 40,
  "allow_outside_guidance": false,
  "hard_ticker_cap": 1000,
  "tradingview_token_cap": 1000
}
```

`target_count` may be omitted, in which case the policy default applies. V1 builds one market per
run. `allow_outside_guidance` is for deliberately small demonstration universes; a production build
stays inside the guidance range.

## snapshot.json

```json
{
  "schema_version": 1,
  "market": "crypto",
  "as_of": "2026-09-16",
  "complete": true,
  "sources": [{"url": "https://...", "as_of": "2026-09-16", "kind": "exchange", "tier": 1}],
  "measurement": {
    "liquidity": {
      "basis": "measured",
      "method": "cross-sectional percentile of 30d USDT notional turnover",
      "window": "30d",
      "source": "https://..."
    },
    "quality": {"basis": "judged", "method": "revenue durability read from official documentation"}
  },
  "taxonomy": [
    {
      "l1_code": "00",
      "l1_name": "Core Assets",
      "theme_code": "00_A",
      "theme_name": "CORE_ASSETS",
      "coverage_level": 1
    }
  ],
  "candidates": [
    {
      "ticker": "BINANCE:BTCUSDT.P",
      "asset_id": "BTC",
      "name": "Bitcoin Perpetual",
      "theme_code": "00_A",
      "role": "BENCHMARK",
      "required": true,
      "eligible": true,
      "exclusion_reasons": [],
      "metrics": {"liquidity": 100, "quality": 95},
      "evidence": [{"url": "https://...", "as_of": "2026-09-16", "kind": "listing", "tier": 1}]
    }
  ]
}
```

### measurement

Every metric that appears on any candidate needs a declaration, and a metric with no declaration
stops the build. `basis` is `measured` or `judged`:

- `measured` additionally requires `window` and a `source` URL.
- `judged` requires only `method`, and is **refused** for `liquidity`, `factor_r2`,
  `beta_strength` and `beta_stability`. Those are window-dependent statistics: a model that has
  not run the computation does not have the number, and a filled-in guess is indistinguishable
  from one that was measured.

This block is the difference between a universe whose numbers can be re-derived and one whose
numbers merely look quantitative.

### metrics

All scores are `0..100`. `factor_r2` is stored as a percentage, and the builder recomputes
`independence = 100 - factor_r2` from it so the two cannot contradict each other. Unknown metric
fields are rejected rather than ignored.

Role-specific requirements the builder enforces:

| Role | Requires |
|---|---|
| any non-anchor | `liquidity` |
| `INDEPENDENT_SENSOR` | `independence >= 50` |
| `BETA_SATELLITE` | `beta_strength` and `beta_stability` |
| `LIQUIDITY_SENSOR`, `NEW_LISTING` | `heat` |
| established Crypto members | `factor_r2` |

`null` means not measurable. It is not a bad score, and it must not be replaced by a low one.

### asset_id

The economic identity, which is not the same as the symbol. Crypto merges a spot pair and its
perpetual; US can merge two share classes of one company; CN keeps the venue by default, so
`SSE:000001` and `SZSE:000001` stay distinct. Two candidates sharing an `asset_id` are one
information source and the second is rejected.

### eligibility

`complete: false` blocks a formal build. An ineligible candidate must carry `exclusion_reasons`,
which enter the selection audit instead of disappearing. Each reason starts with one of these
codes, optionally followed by `: detail`:

```text
not_listed            delisted_or_halted      risk_warning_status    wrong_venue
excluded_instrument_type                      insufficient_liquidity insufficient_history
redundant_with_member unverifiable_fact       duplicate_asset        other
```

The audit also carries reasons the builder writes itself: `outside_profile_coverage`,
`not_selected_under_budget_or_theme_cap`, `removed_by_maintenance`.

### evidence

Every item needs an `http(s)` URL, an `as_of`, and a `tier` of 1, 2 or 3 (see
[source-policy.md](source-policy.md)). Evidence older than the policy window, or dated after the
snapshot, is reported as a warning rather than silently trusted.

## changes.json

```json
{
  "schema_version": 1,
  "market": "crypto",
  "as_of": "2026-09-16",
  "complete": true,
  "sources": [{"url": "https://...", "as_of": "2026-09-16", "kind": "exchange", "tier": 1}],
  "measurement": {},
  "base_version_hash": "0123456789ab",
  "review_depth": "routine",
  "summary": "Binance listing and 30-day liquidity refresh",
  "deferred": [{"ticker": "BINANCE:TIAUSDT.P", "deferred_because": "budget spent elsewhere"}],
  "ops": [
    {
      "op": "ADD",
      "candidate": {"...": "a complete snapshot candidate"},
      "reason": "Current listing and liquidity evidence supports a tactical slot",
      "evidence": [{"url": "https://...", "as_of": "2026-09-16", "tier": 1}]
    },
    {"op": "NO_CHANGE", "scope": "00_A", "reason": "Fresh evidence supports current membership"}
  ]
}
```

`measurement` may be omitted, in which case the universe keeps the declarations it already carries.
Supply it when the method or the window changed.

### Operations

| Op | Fields | Notes |
|---|---|---|
| `ADD` | `candidate`, `reason`, `evidence` | `candidate` carries every snapshot candidate field |
| `REMOVE` | `ticker`, `reason`, `evidence` | Refused for a benchmark, anchor or `required` member |
| `REPLACE` | `ticker`, `candidate`, `reason`, `evidence` | An anchor may only be replaced by an anchor |
| `MOVE` | `ticker`, `to_theme` | Re-files a member without changing membership |
| `ADD_THEME` | `l1_code`, `l1_name`, `theme_code`, `theme_name`, `coverage_level`, `reason`, `evidence` | Its coverage level must be reachable by the current profile |
| `REMOVE_THEME` | `theme`, `reason`, `evidence` | Refused while the theme still holds members |
| `NO_CHANGE` | `scope`, `reason` | A first-class result, recorded in the history |

Operations are applied in a fixed order regardless of how they are listed: `ADD_THEME`, then
`REMOVE` / `MOVE` / `REPLACE` / `ADD`, then `REMOVE_THEME`. A theme created this round can be
populated this round, and a theme can only be retired once its members have been placed. Merging
two themes is `MOVE` plus `REMOVE_THEME`; splitting one is `ADD_THEME` plus `MOVE`.

`ADD`, `REMOVE`, `REPLACE`, `ADD_THEME` and `REMOVE_THEME` all require at least one tier 1 or
tier 2 evidence item. Market narrative alone cannot admit or remove anything.

## Output

`universe.json` is the record: spec limits, policy hash, sources, measurement, taxonomy, members,
the selection audit and the review history. `version_hash` covers membership and taxonomy only, so
re-running with fresher metrics does not churn the version. The other three artifacts —
`validation.json`, `universe.md`, `universe.txt` — are derived from it and are never edited by hand.
