# Adding a market

This document is for whoever extends the skill, not for the agent using it. `cn`, `us` and
`crypto` are the markets that ship; nothing about the design stops at three.

Every market-specific rule lives in one row of `MARKET_SPECS` in `scripts/universe_core.py`:

| Field | What it decides |
|---|---|
| `venues` | Which `EXCHANGE:` prefixes are accepted |
| `symbol_pattern` / `symbol_hint` | The shape of a legal symbol, and the error text when it is not |
| `venue_in_asset_id` | Whether two venues carrying one symbol are two assets or one |
| `asset_id_strip` | Suffixes removed to reach economic identity (a perpetual and its spot pair) |
| `factor_r2_required` | Whether every non-anchor member must state its redundancy with the market factor |

A new market is five additions and no edits to existing logic:

1. A `MarketSpec` row in `MARKET_SPECS`.
2. A `markets.<code>` block in `assets/default-policy.json` with Light, Medium and Heavy counts.
   `MarketRegistryTests` fails until this exists, which is the point — a market with no size
   guidance would build universes of an arbitrary size and report nothing.
3. A starter taxonomy at `assets/taxonomy/<code>.json`.
4. An overlay at `references/markets/<code>.md` covering instrument scope, venue and identity
   rules, the exclusions that market requires, and where its primary sources live.
5. One worked example under `examples/`, so the market is exercised by CI rather than merely
   declared.

## What the registry does not decide

Roles, buckets, score weights, coverage levels, turnover budgets and evidence tiers are market
independent on purpose. A market that appears to need its own role vocabulary is usually a market
whose overlay has not yet been written carefully enough; reach for a new role only after the
overlay makes the case in prose.

## Sketches for the obvious next three

Not implemented. Recorded so the shape of the work is visible rather than guessed at.

| Market | Venues | Symbol | Identity | Notes |
|---|---|---|---|---|
| `hk` | `HKEX` | four or five digits | venue-free | Southbound-eligible subset is a taxonomy question, not a venue one |
| `jp` | `TSE` | four digits, sometimes with a letter | venue-free | Prime / Standard / Growth sections belong in the overlay's eligibility rules |
| `eu` | `XETR`, `EURONEXT`, `LSE`, `SIX` | alphabetic, venue-dependent | venue-bearing | One company lists in several places; without venue in the identity, cross-listings collapse into one member |
