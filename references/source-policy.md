# Sources and evidence

## Source tiers

Every evidence item declares its tier.

| Tier | Scope | What it may decide |
|---|---|---|
| T1 | Exchanges, regulatory filings, official company / fund / protocol disclosure | Identity, listing, venue, contract status, core business, formal events |
| T2 | Auditable structured market data, fundamentals, ETF holdings | Liquidity, returns, beta, R², quality, holdings mapping |
| T3 | News, community, search results, social heat | Discovering candidates and explaining heat — never permanent admission on its own |

`ADD`, `REMOVE`, `REPLACE`, `ADD_THEME` and `REMOVE_THEME` require at least one T1 or T2 item; the
builder refuses the operation otherwise. T3 can start research; it cannot stand in for a fact.

## Freshness

Evidence carries `as_of`. Anything dated after the snapshot, or older than the policy window
(`freshness.evidence_warning_days`, 180 by default), is reported as a warning. Old evidence is not
forbidden — a company's business description does not expire in six months — but it has to be
visible, because the failure mode is a live claim resting on a stale page.

## Provider boundary

- A network adapter produces a timestamped raw snapshot. It never produces a universe.
- Raw responses, provider, request time, symbol mapping and anomalies must stay auditable.
- When a source fails, never present old data as fresh — mark it stale or incomplete.
- Do not couple scraping to selection logic. Providers are replaceable; the snapshot schema is not.
- Prefer official or public endpoints that need no key. If a key is needed, state the purpose and
  the data terms first.
- Do not redistribute restricted history, paid data, or cached data you have no right to cache.

This skill deliberately ships no network layer. The snapshot **is** the boundary: whatever fetches
the facts, the contract in [data-contracts.md](data-contracts.md) is what the builder accepts.

## Market defaults

- **CN** — exchange and company disclosure confirm identity; public market data computes turnover
  and returns.
- **US** — exchange and SEC filings plus official ETF holdings come first; third-party quotes must
  record their adjustment convention.
- **Crypto** — Binance Spot and USDⓈ-M exchange information confirm trading status; ticker and
  kline data compute turnover, heat and factor redundancy. Other venues cross-check by default.

## Reproducibility

Each formal build keeps: the snapshot's `as_of`, sources and completeness; the measurement
declarations; the policy hash; the final universe hash; machine-readable reasons for every rejected
candidate; validator errors and warnings; and the maintenance history with its deferred candidates.
