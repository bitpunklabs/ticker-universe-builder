# Data contracts

Inputs/output records use `schema_version: 1`; policy and skill versions are separate.
JSON examples below illustrate fields and omit the complete current plan/admissions.
Use [worked inputs](../examples/README.md) for buildable snapshots.

## Coverage-first default (0.6)

[coverage-plan.md](coverage-plan.md) defines plan/admission shapes, selection, references and Core migration.
`target_count` is an entity ceiling excluding references, defaulting to plan budget. No legacy
bucket fallback. Under-ceiling output is complete if every gate passes; Max requires matching
qualified Heavy and Beta-only growth. [Partial delivery](#max-shortfall-delivery-071) waives growth only.

`policy.coverage.max_expansion` is `{"min": 0.30}`; finite minimum >=0.30, custom policies may
only tighten it. Heavy count H requires `H + ceil(H*min)` entities. Sector/share/entity/export
caps bind; no separate growth maximum. Build stops after minimum additions. Max group h adds
at most `ceil(h*A/H)` for actual additions A; only rounding permits surplus.

`stats.quality.expansion` reports `heavy_entities`, `added_beta`, fractional `growth`, `min_entities`
and `max_entities` (plan/spec ceiling, not available capacity). Stored validation/maintenance use
these rules. Older below-minimum outputs are historical, not current completions.
Explicit legacy 0.4/0.5 replay retains bucket sizing/gates and warns that coverage is uncertified.

## Research integrity (0.4)

Eligible candidates need a nonempty `reason`, T1/T2 evidence and
`listing: {status: "active", as_of: ISO date, source: http(s) URL}`. The listing URL must occur
in strong evidence; observations cannot be future-dated and expire after 30 calendar days.
Ineligible candidates may omit listing facts but retain exclusion reasons/evidence.
An active quote does not establish financial quality.

Optional `reason_summary`: nonempty single-line text <=160 characters, preferably <=60 Chinese
characters; business description without URLs/audit narration. Reports use it, or a bounded
first-sentence excerpt. Full `reason`/admission/evidence remains authoritative.

Optional `report_translations`: supported-language maps of exact source text to nonempty authored
translations. Include names, summaries, labels/purposes, notes, measurements and references.
Missing entries preserve original text for compatibility; review English content before delivery.
Translated summaries retain 160-character limits. Maps affect presentation/content hash, not
selection, codes or TXT. The CLI does not translate research.

Eligible measured candidates require a dated `measurement_record`: source, input SHA-256, actual
first/last dates, liquidity/factor counts and gauge legs/model. `measure` clears replaced fields,
including unsupported old scores; missing required data makes the merged snapshot incomplete.
`measurement_audit` retains theme/fund diagnostics. Missing-factor logs stay in JSON.

`independence = 100 - factor_r2` is measured-only. Current coverage Beta uses measured liquidity,
sourced cap and business complementarity; factor R²/strength/stability are optional, with provenance
and at least 30 overlapping returns when supplied. Legacy Beta requires R² >=30, strength >=55
(positive price beta >=1.1), stability >=50. Core/legacy role requirements still apply.

Both `version_hash` and `content_hash` are required for stored validation. Version 0.3 inputs need
listing, reasons and measurement records before rebuilding. Four current profiles are Light/Medium/
Heavy/Max. Former 45% growth/70% incremental-beta preference belongs only to archived replay.
Entities, references and headers together must fit the 1,000-token TradingView file cap.

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

One market per run. Omit `target_count` to use plan budget; it may lower, never raise the ceiling.
`allow_outside_guidance` affects legacy replay only and cannot bypass economic coverage.

## Importing an existing watchlist

`import` accepts comma-separated or one-code-per-line TradingView TXT. Sections become draft
level-1 themes; native headings such as `00_A_CORE_ASSETS` retain codes. Unmatched market tickers
enter notes. Candidates have blank role, empty metrics/evidence, `eligible: false`,
`unverifiable_fact: imported from a watchlist, not yet researched`; `complete: false` blocks build.

## Checking a theme table

`taxonomy --check FILE --market M [--profile P] [--target N]` accepts a taxonomy list or
`{schema_version, market, taxonomy}`. Default `scope: "display_structure_only"` checks duplicate/
malformed themes, parent-label conflicts and a Level-1 theme. Non-ASCII headers and late-appearing
groups warn. `stats.capacity[profile]` shows visible themes and optional target, not member floors
or expected allocations. Build checks economic feasibility/merged export capacity.
Explicit legacy policies also check theme presence/guidance/concentration/`floor_share`.
Exit 0 permits warnings; errors exit 2.

## snapshot.json

### Theme observation duties

Research themes declare nonempty `purpose` and `representative_roles`, drawn from BENCHMARK/ANCHOR/
THEME_LEADER/QUALITY_LEADER. Legacy reachable themes need one eligible member with any declared role;
current builds protect plan branches/representatives, not a floor for every display label.
A role declaration needs a purpose. Legacy tables can omit both, disclosing missing duties.

Candidate reason/evidence explains the duty; several representatives are allowed. Fields survive
hashing/rendering/ADD_THEME. UPDATE_THEME revises duties explicitly with evidence; REMOVE_THEME
retires obsolete duties. Emptying them cannot hide missing coverage.

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
      "coverage_level": 1,
      "weight": 2.5,
      "purpose": "Observe the common crypto market factors.",
      "representative_roles": ["BENCHMARK", "ANCHOR"]
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
      "reason": "Core benchmark with an active contract check",
      "listing": {"status": "active", "as_of": "2026-09-16", "source": "https://..."},
      "measurement_record": {"as_of": "2026-09-16", "source": "https://...",
        "data_sha256": "<64 hexadecimal characters from the input file>",
        "first_session": "2026-08-01", "last_session": "2026-09-16",
        "liquidity_observations": 30, "observations": 0, "benchmarks": []},
      "metrics": {"liquidity": 100, "quality": 95},
      "evidence": [{"url": "https://...", "as_of": "2026-09-16", "kind": "listing", "tier": 1}]
    }
  ]
}
```

### market_spec

Only unregistered markets can declare rules; every registered market rejects overrides.

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
  "breadth": 0.7,
  "evidence": [{"url": "https://www.set.or.th/...", "as_of": "2026-09-17", "tier": 1}]
}
```

Require T1/T2 evidence, a supported locale (omission defaults to English), and exactly one legacy
`breadth` or four-profile `guidance`. These compatibility fields do not override current plan budgets;
`breadth` scales historical 60/160/400/580 bases only under explicit legacy policy.

The declaration is stored/hashed, re-resolved by validate and disclosed as `Market rules: declared`.
Changed rules need a rebuild; maintenance cannot redeclare them. General admission, measurement,
turnover and evidence contracts remain unchanged.

### measurement

Every supplied metric needs a `method` and `basis`:

| Basis | Requirements |
|---|---|
| `measured` | Window and source URL |
| `judged` | Method; prohibited for liquidity, factor_r2, beta_strength, beta_stability |
| `blended` | Quality only, sourced facts; required iff any candidate has `quality_facts` |

Compute statistics with [measure](measurement.md); never substitute guessed values.

### metrics

Scores are 0..100; factor_r2 is a percentage. Python derives independence; unknown keys fail.
`null` means unmeasurable, not poor, and cannot be replaced with a guessed score.

| Role | Required metrics |
|---|---|
| Non-anchor | liquidity |
| INDEPENDENT_SENSOR | independence >=50 |
| Legacy BETA_SATELLITE | beta_strength/stability; current Beta factors are optional |
| LIQUIDITY_SENSOR / NEW_LISTING | heat |
| Established Crypto core / legacy | factor_r2; coverage Beta can omit it |

Legacy composite scores divide by full bucket field weight, including missing fields.
Normalized members retain `scored_on: {present: n, of: m}`; only legacy reports count partial
scoring. Current Beta ranks by cap and does not treat missing optional factors as incomplete research.

### quality_facts

Core requires researched `metrics.quality`; satellites may omit it. Optional historical blended facts:

```json
"quality_facts": {
  "listing_age_days": 4380,
  "size_rank_pct": 96,
  "adverse_flags": []
}
```

Require listing age or size percentile; flags alone cannot produce a score. Age bands:
>=5y:100, >=3y:85, >=2y:70, >=1y:50, >=0.5y:30, shorter:10. Rule score averages present components,
subtracts 25 per adverse flag and clamps to 0..100. `size_rank_pct` uses a declared market population.
`metrics.quality` remains separate, with `quality_rule_score`/`quality_score` in normalized records.
Only legacy selection ranks the blend; validation does not compound it. Missing facts warn.

Universal flag codes:

```text
risk_warning going_concern regulatory_action audit_qualification
monitoring_tag restructuring loss_making
```

Market-specific codes are in overlays/registry (CN special_treatment/share_pledge_risk/exchange_inquiry;
US late_filing/listing_deficiency/material_weakness; Crypto unlock_overhang/supply_concentration/
unaudited_contract). Wrong-market codes fail; registered markets cannot share local codes.
A declared market may add <=6 codes, cannot redefine universal ones and hashes them in version_hash.
Unknown locale translations print bare codes and warn. Every flag has the same 25-point penalty.

### asset_id

One economic entity may have several instruments. Crypto merges spot/perpetual, US can merge
share classes; CN keeps venue (`SSE:000001` differs from `SZSE:000001`). Duplicate asset_ids
are rejected. Verify actual identity rather than inferring aliases from ticker strings.

### eligibility

`complete: false` blocks formal build. Ineligible candidates retain coded `exclusion_reasons`,
optionally followed by `: detail`:

```text
not_listed delisted_or_halted risk_warning_status wrong_venue
excluded_instrument_type insufficient_liquidity insufficient_history
redundant_with_member unverifiable_fact duplicate_asset other
```

Python also records `outside_profile_coverage`, `not_selected_under_budget`, `removed_by_maintenance`.
Reports/receipts aggregate codes so research gaps and capacity exclusions remain distinguishable.

### evidence

Each item needs an http(s) URL, `as_of` and tier 1/2/3. General evidence freshness warns;
mandatory listing/admission gates are stricter. [Source policy](source-policy.md).

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

Optional measurement declarations retain existing ones when omitted; supply them for changed methods/windows.
Include `base_content_hash` as well as `base_version_hash` to prevent applying over another fact refresh.

### Operations

| Op | Fields / constraints |
|---|---|
| ADD | Complete candidate, reason, evidence |
| REMOVE | ticker, reason, evidence; protected benchmark/anchor/required members cannot be removed |
| REPLACE | ticker, complete candidate, reason, evidence; anchor successor must be anchor |
| MOVE | ticker, to_theme |
| ADD_THEME | l1_code/name, theme_code/name, reachable coverage_level, reason/evidence; accepts weight and duties |
| REMOVE_THEME | theme, reason/evidence; empty theme only |
| UPDATE_THEME | theme, one or more of weight/theme_name/purpose/representative_roles, reason/evidence |
| REFRESH | ticker, complete candidate, reason/evidence; preserve identity/theme/role/required status |
| NO_CHANGE | reason; recorded in history |

Apply ADD_THEME before member operations, then REMOVE_THEME. Merge using MOVE + REMOVE_THEME;
split using ADD_THEME + MOVE. ADD/REMOVE/REPLACE/ADD_THEME/REMOVE_THEME require T1/T2 evidence.
UPDATE_THEME/REFRESH also need strong evidence. Hysteresis is research policy; Python enforces
turnover/flip-flop disclosure, not a two-snapshot state machine. [Maintenance](maintenance.md).

## Output

[Output-artifacts.md](output-artifacts.md) defines bundle formats, paths and status.
Derived TXT/validation/MD/HTML are script outputs, never hand-edited.

### Build-run checkpoint

`OUTPUT.run/run.json` is `{schema_version: 1, kind: "build_run", inputs, status, attempts,
resume_command}`. Inputs store absolute spec/snapshot/policy/seed/output paths and language;
attempts store numbered receipts, input SHA-256, archived parsed inputs, UTC dates, diagnostics
and artifact paths. Statuses: running/needs_research/partial/complete.
Legacy partial stays partial until its target fills; current completion requires coverage and Max
minimum growth, allowing unused ceiling capacity. [Recovery](recovery.md) defines continuation.

`artifacts.reports` and `artifacts.html_reports` map languages to actual paths. English is always
present, with market companions where applicable. The authoritative JSON retains all facts,
selection audit and history. Content hash covers the full record; current version hash also covers
plan/admissions, while legacy version hash covers membership/taxonomy without metric drift.
Skill version is separate; upgrading does not rewrite historical artifacts. Policy_version records
the producing policy. Changed contracts may require archived replay or renewed research.

Legacy build-only `stats.stability: {shift, draws, survived, of, share}` needs the full bench;
stored validation omits it rather than reporting zero or an old result.

## Comparing two universes

`diff before.json after.json` reports rules, membership, themes and roles. Declared market_spec
differences come first because changed identity rules can make records incomparable.
`identical` concerns the observation instrument, not metric drift; only the twenty largest metric
moves are listed. Locales translate fixed labels, authored maps translate content, and validation
messages remain English.

## Max shortfall delivery (0.7.1)

`build-spec.shortfall_action`: auto (default), deliver or retry. CLI overrides persist on resume.
Auto/deliver may publish partial only for a growth-only deficit, at least one new Beta, and
`required_entities - actual_entities <= 0.05 * required_entities`. Retry requires full growth.

Partial output adds `delivery: {status: "partial", reason: "max_growth_shortfall",
required_entities: int, shortfall: int, allowed_gap_ratio: 0.05}`. Validation recomputes values;
identity/listing/measurement/admission/core/Heavy-retention/cap gates remain mandatory.
Partial group ceilings use planned additions (`required_entities - Heavy_entities`), keeping
vacancies. Complete Max uses actual additions. References never count as growth.

Valid partial: passed true, qualified false, stats.quality.status partial; exit 3 with continuation.
Stems carry `-partial` before extension/language. Reports/JSON disclose actual growth/required/gap;
TXT remains importable. Rebuild revised inputs to complete it; metadata relabeling is invalid.
