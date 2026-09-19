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
| `language` | Which locale the `.md` report is written in unless the caller overrides it |
| `quality_flags` | Adverse flags this market's regime issues and no other's does |

## Two ways in, and when each is right

A market outside the three is not forbidden. It has two routes, and they answer different
questions:

| | **Declared** | **Registered** |
|---|---|---|
| Where the rules live | `market_spec` in the snapshot | a row in `MARKET_SPECS` |
| Who wrote them | whoever built this universe, at run time | this repository, reviewed |
| What it costs | research, with evidence | a pull request |
| What ships | nothing | a policy row, a starter taxonomy, an overlay, an example |
| What the report says | `Market rules: declared`, on every run | nothing; silence is the reviewed case |

A declared market has no starter taxonomy, so the agent writes one from nothing;
`taxonomy --check` is the gate on that, and it is worth running before any candidate is
researched.

Declaring is the answer for a market nobody here has looked at — a smaller exchange, a market one
user cares about, a market being tried out. Registering is the answer once a market is used often
enough that leaving its venue list to be re-researched every session is the larger risk. The
first does not block on us; the second does not depend on the agent getting it right twice.

Both build under identical general logic. The only thing that differs is who vouches for those
seven fields, and the report never lets a reader confuse the two.

A new *registered* market is five additions and no edits to existing logic:

1. A `MarketSpec` row in `MARKET_SPECS`.
2. A `markets.<code>` block in `assets/default-policy.json` with Light, Medium and Heavy counts.
   `MarketRegistryTests` fails until this exists, which is the point — a market with no size
   guidance would build universes of an arbitrary size and report nothing. The band is the
   target ±25% rounded to ten, and a test asserts it; do not hand-set the bounds.
3. A starter taxonomy at `assets/taxonomy/<code>.json`, sized with the guidance rather than
   independently of it: at each tier, `reachable themes x theme_cap` should be roughly half
   again the target. `taxonomy --check` has to pass clean — errors *and* warnings — for all
   three profiles, which is also a test. A starter that cannot reach its own Light target sends
   every user down the same dead end, and that is not hypothetical: it shipped that way, and cn
   Light asked 220 members of a table that topped out at 72.
4. An overlay at `references/markets/<code>.md` covering instrument scope, venue and identity
   rules, the exclusions that market requires, and where its primary sources live.
5. One worked example under `examples/`, so the market is exercised by CI rather than merely
   declared.

Plus, if the market's regulator issues flags the universal seven cannot express, a
`quality_flags` set on the row and a `flag.<code>` entry in every locale. Three tests decide
whether a flag belongs there: does this regime issue it as a discrete, lookupable status; does
recording it as `risk_warning` or `regulatory_action` lose something that would change a
selection; and is the code meaningless in every other market. A flag that fails the third is a
universal code that has not been added yet — add it to `QUALITY_FLAG_CODES` instead, where it is
comparable across markets, rather than to two market specs where it silently is not.

## Report language

A universe is read by the people who trade that market, so the human-readable report follows the
market rather than the tool: `language` is a field of the registry the same way the symbol shape
is. `--language` overrides it per run; nothing else about the build changes.

Only the chrome is translated — headings, labels, and the closed vocabularies (roles, exclusion
and audit codes, profiles, bases, review depths). Those are finite, so
`assets/locales/<lang>.json` can be complete and `LocalizationTests` proves it is. Everything
else in the report is content the research wrote: a Chinese A-share snapshot carries Chinese
names, themes, reasons and methods without the renderer knowing anything about them, which is
also why the taxonomy's `l1_name` is authored in the market's language rather than translated.
Codes are printed beside their translation, never in place of it — `基准 (BENCHMARK)` — because
the code is what the documentation names and what a reader greps for. Validation diagnostics stay
English for the same reason: they name policy fields and code paths, and `.validation.json`
carries the identical text.

Adding a language is one JSON file with the same keys as `en.json`. `zh-Hans`, `zh-Hant` and `en`
ship. One vocabulary is deliberately outside this: a `quality_flags` code a snapshot declared at
run time has no key in any locale, because no lexicon can carry a vocabulary invented after it
shipped. Those print as the bare code, and the build warns that they will.

### Writing a locale

A wrong word is caught by reading the file. The failures that survive a careful read are the ones
that only look wrong in the rendered page, so `LocalizationTests` checks for those four directly:

| Rule | Why it is a test and not a habit |
|---|---|
| Every key present, every closed vocabulary covered | Adding a role or an exclusion code without a word for it would print a bare code into a translated report |
| CJK text uses CJK punctuation | An ASCII comma between two Chinese characters is the single clearest tell that a page was generated rather than written. `punct.colon` is part of the lexicon for the same reason |
| No word means two things in one report | `review.depth` and `depth.deep` print on one line; giving both `深度` renders "深度：深度", which is how the first draft shipped |
| `zh-Hant` stays a conversion of `zh-Hans` | Maintained as two independent translations, one term becomes two — `NEW_LISTING` was `次新` in one and `新上市` in the other. Length parity is the proxy; a regional term that changes length goes in the test's exemption set, visibly |

Two more rules the tests cannot check, so they are written here:

- **Translate the register, not the words.** `profile.light/medium/heavy` are `精简档 / 标准档 /
  完整档` — one axis, three points. The first draft mixed three axes (`轻量 / 标准 / 完整`) and
  read like three unrelated settings.
- **Watch for terms the market already owns.** `turnover` here is the share of members replaced
  in a review, and `换手` in a Chinese market report means trading turnover — a word already
  spoken for by `liquidity`. It is `成分变动`.

The example is held to the same standard as the chrome: `cn-light/universe.md` is checked line by
line, because an example that reads like machine output teaches the agent to write machine output.

## The classification

Deciding a market's language after the fact means two A-share universes built a month apart read
differently. So the language is settled for the above-scale markets before any of them is
implemented. Scope is equities and crypto; ✅ marks what ships today.

| Market | Code | Venues | Language | Locale |
|---|---|---|---|---|
| United States | `us` ✅ | `NASDAQ` `NYSE` `AMEX` `NYSEARCA` `CBOE` `IEX` `OTC` | `en` | ships |
| China A-shares | `cn` ✅ | `SSE` `SZSE` `BSE` | `zh-Hans` | ships |
| Crypto | `crypto` ✅ | `BINANCE` | `en` | ships |
| Japan | `jp` | `TSE` | `ja` | to write |
| India | `in` | `NSE` `BSE` | `en` | ships |
| Hong Kong | `hk` | `HKEX` | `zh-Hant` | ships |
| United Kingdom | `uk` | `LSE` | `en` | ships |
| Europe | `eu` | `XETR` `EURONEXT` `SIX` | `en` | ships |
| Canada | `ca` | `TSX` `TSXV` | `en` | ships |
| Saudi Arabia | `sa` | `TADAWUL` | `ar` | to write |
| Taiwan | `tw` | `TWSE` `TPEX` | `zh-Hant` | ships |
| Korea | `kr` | `KRX` | `ko` | to write |
| Australia | `au` | `ASX` | `en` | ships |
| Brazil | `br` | `BMFBOVESPA` | `pt` | to write |
| Singapore | `sg` | `SGX` | `en` | ships |

`eu` is the one row where the market has no single language of its own — a listing in Frankfurt,
Paris and Zurich is read by three readerships — so it takes English as the working language of
the cross-border market itself rather than picking one member state's. `in` is the same argument
with a domestic answer: Indian exchange filings and listing documents are published in English.

## What the registry does not decide

Roles, buckets, score weights, coverage levels, turnover budgets and evidence tiers are market
independent on purpose. So is the theme cap — not as a fixed count, which only looks
market-independent, but as a share: the tier sets a ceiling and the build tightens it to about
half again a theme's fair share, so a market never needs a cap of its own. So is what an adverse
flag *costs*: a market names its own flags and
every one of them is worth the same 25 points, because a market that could also set the penalty
could make its members score however it liked. A market that appears to need its own role vocabulary is usually a market
whose overlay has not yet been written carefully enough; reach for a new role only after the
overlay makes the case in prose.

## Sketches for the obvious next three

Not implemented. Recorded so the shape of the work is visible rather than guessed at.

| Market | Venues | Symbol | Identity | Language | Notes |
|---|---|---|---|---|---|
| `hk` | `HKEX` | four or five digits | venue-free | `zh-Hant` | Southbound-eligible subset is a taxonomy question, not a venue one; `gem_board` is the flag it needs |
| `jp` | `TSE` | four digits, sometimes with a letter | venue-free | `ja` | Prime / Standard / Growth sections belong in the overlay's eligibility rules |
| `eu` | `XETR`, `EURONEXT`, `LSE`, `SIX` | alphabetic, venue-dependent | venue-bearing | `en` | One company lists in several places; without venue in the identity, cross-listings collapse into one member |
