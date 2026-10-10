# Sources and evidence

| Tier | Sources | Permitted use |
|---|---|---|
| T1 | Exchanges, filings, official company/fund/protocol disclosures | Identity, listing, venue, business and formal events |
| T2 | Auditable market data, fundamentals and ETF holdings | Liquidity, returns, factors, quality and holdings mapping |
| T3 | News, community, search results and social heat | Discovery/context; insufficient alone for admission |

`ADD`, `REMOVE`, `REPLACE`, `ADD_THEME` and `REMOVE_THEME` require T1/T2 evidence.
Every evidence item carries its original `as_of`. General evidence outside the policy window
(180 days by default) or after the snapshot is warned; mandatory listing/admission dates have
stricter gates in [data contracts](data-contracts.md) and [coverage](coverage-plan.md).

## Research checks

Read actual source content: HTTP 200, a JavaScript shell or robots page proves no business fact.
Distinguish newly verified, carried dated and unknown facts; never redate old evidence.
Check primary business against the observation duty, corporate actions, share classes and exact
Crypto contracts. Record venue/namespace conflicts instead of guessing replacements.

CN uses exchange/company disclosure; US adds SEC filings and official fund holdings; Crypto uses
exchange contract inventories and protocol disclosures. Structured quotes/bars compute liquidity
and factors, with adjustment and currency conventions disclosed.

## Provider boundary

[Adapters](providers.md) write timestamped facts and bars, never membership. Retain source URL,
request time, raw receipts, symbol mappings, units and anomalies locally. Failed acquisition is
stale/incomplete, not fresh. Prefer official/public endpoints without keys; disclose purpose and
terms when a key is required. Do not redistribute restricted histories or caches without rights.

Formal records retain snapshot completeness, evidence, measurement declarations, policy/content/
version hashes, rejection codes, validation findings and maintenance/deferred history.
