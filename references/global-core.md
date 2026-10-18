# Global Core

Read [Global](global.md) and the [coverage checklist](global-coverage.md) first. Core is a
reviewed strict subset of a qualified Global composition, retaining all of its geographic,
theme and child-duty coverage. It is not a native Light profile or an automatic top-cap filter.

## Selection

Review every parent ticker. Define each economic function before comparing leadership,
continuing quality, liquidity, recognition and incremental observation value. A profitable
adjacent business cannot substitute for the requested theme: advertising channels and content
platforms are different functions. Never infer worldwide leadership from domestic scale alone.

Concentrated functions favor genuine leaders; dispersed functions favor qualified baskets plus
essential differentiated leaders. Normally investigate 1–3 leaders per child function, with
explained composite exceptions. Counts are guidance, not a hard cap or a quota. Large, liquid,
reasonably priced ETFs can remain for important breadth duties even alongside strong leaders.
Do not remove credible coverage merely to make Core numerically small.

Omissions name surviving instruments and explain the priority decision. Remaining ETF coverage
must be supported by holdings; a fund label is insufficient. Omission from Core does not imply
failure of Global admission. Missing companies or funds require a researched parent revision
first; Core cannot introduce tickers, promote peers, rewrite business assignments or new metrics.

## Commands

```bash
python scripts/universe.py compose-global-core \
  --parent FULL/global-2026-10-18.json --parent-contract approved-global-contract.json \
  --contract reviewed-core.json --output NEW_EMPTY_CORE_DIR
python scripts/universe.py validate-global-core \
  NEW_EMPTY_CORE_DIR/global-core-2026-10-18.json --contract reviewed-core.json
python scripts/universe.py check-watchlist \
  NEW_EMPTY_CORE_DIR/global-core-2026-10-18.txt --ticker-only
```

The parent's original expected contract and the independently reviewed Core contract are explicit
inputs. Core inherits the parent's as-of and actual evidence/measurement dates. For a current
refresh, rebuild the parent first. Validate both when maintaining an existing full/Core pair.

## Core review contract

`schema_version: 1`, `kind: "global_core_review"`, plus:

| Field | Meaning |
|---|---|
| `parent_sha256` | SHA-256 of the exact qualified parent JSON bytes. |
| `parent_contract_sha256` | SHA-256 of the exact separately reviewed full coverage contract bytes. |
| `scope` | Explicit Core observation purpose; inherited pilot/synthetic warnings cannot be removed. |
| `protected_tickers` | Unique exact parent tickers that must survive; includes every parent-required ticker. Research/user-specific choices belong here rather than global ticker overrides in code. |
| `decisions` | Every parent ticker exactly once: `{ticker, action, reason, evidence, covered_by}`. Action retain/omit. Retain has `covered_by: []`; omit names retained full tickers whose declared duties collectively preserve all omitted duties. Dated T1/T2 evidence is required for each judgement. |
| `theme_reviews` | Every parent theme exactly once: `{id, emphasis, reason, evidence}`. Emphasis leaders/basket/mixed/gauge/context. Explain business representation, basket breadth, redundancy and composite exceptions. |
| `basket_exposures` | Optional reviewed underlying-company claims: `{ticker, fund, holding_entity_id, reason, evidence}`. The omitted company names the retained fund in `covered_by`; the exact evidenced holding ID must have positive weight in the parent's full holdings. Explain issuer-name/ID differences explicitly rather than guessing an alias. One row per omitted company. |

Parent membership order is preserved. Only parent leader entities are eligible; reference funds
must still pass every Global fund gate. Markets, themes, duty definitions/minima, required and
excluded tickers and ETF rules are inherited verbatim. Original native source-theme IDs remain
complete; the engine records whether Core retains that native slice or represents the Global
function through another retained source. This does not retire the Global duty.

The code checks sourced assertions and declared coverage mechanics; it cannot independently
prove semantic leadership, that an omission reason is persuasive, or ETF exposure beyond the
supplied reviewed holdings. Perform a separate economic review before publishing.

## Portable artifacts and validation

Core outputs `global-core-DATE.json`, validation JSON, English Markdown/HTML, a ticker-only TXT
and two optional `-by-theme.txt`/`-by-market.txt` views with identical membership. All inherit
the [Global TXT rules](global.md#artifacts-and-tradingview-format), including the header-aware
1,000-token ceiling. Do not hand-edit any final TXT. A worked [Global example](../examples/global/README.md)
also demonstrates the full-to-Core workflow.

The same directory retains `global-core-contract.json`, derived `global-contract.json`, original
`parent-global.json`, `parent-contract.json`, the three `parent-global*.txt` files and exact
`source-ID.json` copies. Flat shared source copies keep the bundle relocatable without modifying
the parent's bytes. Parent JSON and its original contract must independently qualify again.

`validate-global-core` uses the caller's expected review, not stored passed flags. It checks the
pinned parent and contract bytes, full native source qualification, complete decisions, protected
tickers, surviving duties, theme reviews, unchanged parent rows, strict subset membership, derived
coverage, content hashes and exact TXT outputs. Failed builds publish no new bundle. A syntax or
source check is not a TradingView UI-import or return-performance test.

For a personal current registry, publish only generated copies and verify that the Core's pinned
parent is the current Global JSON. A Core built against an older valid superset is not the current
pair until its complete decision review has been reconciled.
