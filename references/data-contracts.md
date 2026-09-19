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

## Importing an existing watchlist

`import` reads a TradingView `.txt` — comma separated on one line, or one ticker per line — and
writes a snapshot skeleton. Sections become a draft taxonomy at coverage level 1; a section
already named in this skill's own format (`00_A_CORE_ASSETS`) keeps its codes, so the output of a
build round-trips back into an input.

Everything a txt file cannot carry is left empty rather than guessed: `role` is blank, `metrics`
and `evidence` are empty, every candidate is `eligible: false` with the reason
`unverifiable_fact: imported from a watchlist, not yet researched`, and `complete` is false. The
draft will not build until it has been researched, which is the correct behaviour — the import
saves the transcription, not the work. Tickers that do not match the named market are listed in
`notes` instead of being dropped.

## Checking a theme table

`taxonomy --check FILE --market M [--profile P] [--target N]` reads a taxonomy — a bare list, or
the `{schema_version, market, taxonomy}` object `taxonomy --output` writes — and reports whether
it can produce the universe being asked for, before any candidate is researched:

| | |
|---|---|
| **error** | more themes inside the coverage level than the target can hold; every theme must carry a member, so the build could not validate |
| **error** | one `l1_code` carrying two different `l1_name`s |
| **error** | no theme at `coverage_level` 1 |
| **warning** | `themes x theme_cap` below the target — the pool will fill against the cap |
| **warning** | an `l1_code` group first appearing at level 2 or 3, invisible to a Light universe |
| **warning** | a non-ASCII `theme_name`; it becomes a `###00_A_NAME` section header in the TradingView export, so the local-language label belongs in `l1_name` |
| **warning** | themes plus tickers over the 1000-token cap |

Exit 0 with warnings, 2 with errors. The shipped starters pass with capacity warnings: a starter
is a starting point, and the warning is the size of the edit it still needs.

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

### market_spec

Only for a market this skill does not register. `cn`, `us` and `crypto` carry reviewed rules and
refuse a declaration; anything else is buildable by researching the same handful of facts a
registry row would have held:

```json
"market_spec": {
  "code": "th",
  "label": "Thailand SET",
  "language": "en",
  "venues": ["SET"],
  "symbol_pattern": "[A-Z][A-Z0-9\\-]{0,9}",
  "symbol_hint": "one to ten characters starting with a letter",
  "venue_in_asset_id": false,
  "asset_id_strip": [],
  "factor_r2_required": false,
  "guidance": {
    "light":  {"min": 40, "target": 60,  "max": 90},
    "medium": {"min": 80, "target": 110, "max": 150},
    "heavy":  {"min": 140, "target": 190, "max": 260}
  },
  "evidence": [{"url": "https://www.set.or.th/...", "as_of": "2026-09-17", "tier": 1}]
}
```

Nothing else about the build changes — roles, quotas, coverage levels, evidence tiers, the
measurement rules, turnover budgets and hashing are the same as for a registered market. This
block is the *only* thing a market gets to decide for itself, which is why it is checked like any
other researched fact:

- **Strong evidence is required.** A venue code and a symbol shape are easier to invent than a
  ticker, and a wrong one changes what counts as the same asset for every member at once.
- **`guidance` is not optional.** The deeper tiers are defined relative to the shallower ones, so
  a build with no stated Light size would have to invent one — and an invented range reports
  nothing when a universe comes out the wrong size. Use `assets/default-policy.json` as the shape.
- **`language` must have a locale.** Omit it for English rather than naming a language this skill
  cannot write.
- **It is recorded and hashed.** The universe carries the declaration, `validate` re-resolves the
  rules from that record rather than from the registry, and `version_hash` covers it — two
  universes built under different identity rules are not the same universe. A change set may not
  redeclare it; different rules mean a rebuild.
- **Every report says so.** A build and every later validation both warn that the rules were
  declared rather than reviewed, and `.md` carries a `Market rules: declared` line that a
  registered market never prints.

### measurement

Every metric that appears on any candidate needs a declaration, and a metric with no declaration
stops the build. `basis` is `measured`, `judged` or `blended`:

- `measured` additionally requires `window` and a `source` URL.
- `judged` requires only `method`, and is **refused** for `liquidity`, `factor_r2`,
  `beta_strength` and `beta_stability`. Those are window-dependent statistics: a model that has
  not run the computation does not have the number, and a filled-in guess is indistinguishable
  from one that was measured. [measurement.md](measurement.md) is how you compute them.
- `blended` applies to `quality` alone and requires a `source` for the facts. It is not optional:
  if any candidate carries `quality_facts` the declaration must say `blended`, and if none does
  it may not claim otherwise.

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

### quality_facts

`quality` carries the heaviest weight in the core bucket and is the least checkable field in the
file. It stays a judgement — durability is not a statistic — but where checkable facts exist they
carry half of it, so the score cannot drift on opinion alone.

```json
"quality_facts": {
  "listing_age_days": 4380,
  "size_rank_pct": 96,
  "adverse_flags": []
}
```

The rule half is the mean of the components present, less 25 points per adverse flag, clamped to
`0..100`. Listing age is banded — five years scores 100, three 85, two 70, one 50, half a year 30,
anything shorter 10 — because the difference between four and five years of listing is not
information. `size_rank_pct` is a cross-sectional percentile within the market.

`adverse_flags` is a closed vocabulary, for the same reason the exclusion codes are:

```text
risk_warning   going_concern   regulatory_action   audit_qualification
monitoring_tag restructuring   loss_making
```

The block is optional, and needs at least one of `listing_age_days` or `size_rank_pct` — flags
alone do not make a score. It does not replace the judged value: `metrics.quality` is still
required and stays in the record exactly as supplied, while the built member carries
`quality_rule_score` and the blended `quality_score` beside it. Selection reads the blend; the
inputs stay separable, so re-validating a built universe reaches the same number rather than
compounding it. A universe where no member carries facts validates, with a warning saying so.

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

Counting these is the point of the closed vocabulary, so `universe.md` and the CLI's JSON line
both report rejections by code. A universe losing most of its candidates to `unverifiable_fact`
has a research problem; one losing them to `not_selected_under_budget_or_theme_cap` has a budget
problem. Free text cannot tell you which.

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

Four files, all stemmed `{market}-{profile}-{as_of}` — `crypto-light-2026-09-17.json`,
`.validation.json`, `.md`, `.txt`. The watchlist leaves its directory as soon as it is useful, so
the name has to say which universe and when without the directory around it. The command prints
every path it wrote under `artifacts`; read them from there instead of reconstructing them.

The `.json` is the record: spec limits, policy hash, sources, measurement, taxonomy, members, the
selection audit and the review history. `version_hash` covers membership and taxonomy only, so
re-running with fresher metrics does not churn the version. The other three are derived from it
and are never edited by hand.

The `.md` is written in the market's own language, because a universe is read by the people who
trade that market: CN is Simplified Chinese, US and Crypto are English, and `--language` overrides
it per run. Only the report's chrome is translated — headings, labels and the closed
vocabularies, printed as `基准 (BENCHMARK)` so the code a reader greps for survives the
translation. Everything else is the content this file carries: `name`, `l1_name`, `reason` and
`method` appear exactly as the snapshot wrote them, so write them in the market's language.
`.validation.json` stays English, diagnostics included; it is the machine surface, and its
messages name policy fields and code paths.
[markets/adding-a-market.md](markets/adding-a-market.md) carries the language for every
above-scale market, decided ahead of implementation.
