# US overlay

Read [equity-common.md](equity-common.md) first: the universe boundary, the fund-versus-
basket redundancy test, the cash-management exclusion and the rule about regressing
against the theme rather than the index are the same in every equity market.

## Universe boundary

- Common stock and the ETFs needed as gauges. Warrants, rights, units, preferred shares and shell
  SPACs are excluded by default.
- Confirm the TradingView venue, an active listing and sufficient turnover.
- Flag ADRs. Never treat two securities of one economic entity as two information sources.

## Build focus

- Measure every stock against **its own sector or theme ETF**, not against SPY. A broad-index
  regression makes every semiconductor a high-beta winner and credits the sector's move to each
  component's alpha.
- Light keeps index and sector gauges plus the companies with the clearest business leadership.
- Medium adds quality leaders, supply-chain positions and a limited set of differentiated or
  high-beta components.
- Heavy adds cold sectors, mid-cap breadth, independent residual sensors and qualified IPOs.

## Cash-management instruments

Money-market, ultra-short and cash-management funds are the ones that win every US liquidity
ranking and carry no signal. They are excluded by instrument type — see equity-common.md.

## US economic map

The US starter follows the legacy map: AI hardware/semiconductors, platforms, data-center
infrastructure and software remain distinct. Payments, credit, banking, insurance and market
infrastructure are different business models. Separate regulated utilities, merchant power,
fuel and equipment; separate REIT operating exposures. Include eligible ADRs after identity
research; a provider's primary-listing flag is not a reason to erase US-listed foreign exposure.

Market/macro, funds and commodity-underlying observation are separate duties from company
exposure. The standard equity adapter does not fetch all these automatically. Research the
missing gauges explicitly; a verified listed ETF may serve a declared proxy duty, but disclose
tracking/basis differences and do not invent an unsupported index/CFD symbol. Cash substitutes
remain excluded; duration, currency and commodity signals require actual observable movement.

## Adverse flags

| Code | What it is |
|---|---|
| `late_filing` | An NT 10-K or NT 10-Q, or a filing past its extended deadline |
| `listing_deficiency` | An exchange deficiency notice: price, market value, float or governance |
| `material_weakness` | A disclosed material weakness in internal control over financial reporting |

## Example

[`examples/us-medium/`](../../examples/us-medium/) contains a full-size Medium
research snapshot, measured statistics, dated listing evidence, reports and script-generated watchlist.
Read [the scope and limitations](../../examples/README.md) before reusing it.

## Suggested live fields

- Listing and quote status, 20 / 60-day dollar turnover.
- Beta, downside beta, R², excess return, volatility and max drawdown against the theme's own ETF.
- Beta stability across 63 / 126 / 252 days.
- Sector-appropriate quality fields, not one threshold applied across every industry.
- Earnings dates, company filings or ETF holdings as evidence.

Public sector classifications routinely place companies with entirely different drivers in one
bucket. When the classification is ambiguous, map ticker by ticker and record the reason; never let
a wrong sector label decide the theme.
