# Optional public-data adapters

`fetch` writes facts and bars, never membership. Build/validate/maintain/measure/evaluate are offline.
Adapters: US/JP/CN/KR/HK/UK/Crypto; other markets need externally researched inputs.

```bash
python scripts/universe.py fetch --market cn --prices-until 2026-09-28 \
  --limit 1250 --workers 6 --output temp/cn
```

Use the latest completed trading day. `--include-watchlist old.txt` requests incumbents still in
eligible listing inventory; it does not preserve unverified symbols.

## Equity data

TradingView scanner supplies observed primary listings, industry labels and cap; Yahoo supplies
adjusted daily closes. The bench includes the largest `--limit` companies, three per industry
and requested incumbents. CN retains active CNY A/H lines even when H is globally primary.
Turnover is disclosed raw close × volume, not exchange-reported notional. UK GBp normalizes to GBP.
Record currency/provider symbols. Quote activity does not certify regulatory/issuer quality;
CN ST/delisting-name exclusions do not replace exchange research.

## Crypto data

Official Binance Spot/USDⓈ-M inventories, tags and klines. Prefer USDT perpetual only when history
passes; otherwise spot. Require 180 effective bars, continuous final 30 days and $1m mean quoted
turnover over 30 days. These are adapter research floors, not universal selection rules; new
listings need separate event research. Default bench excludes untagged/perpetual-only assets,
stablecoins, leveraged/monitoring-tagged products and tokenized stocks/commodities.

`--crypto-scope all-perpetuals --limit 1000` adds active USDT perpetuals with an economic
`exchangeInfo.underlyingSubType`. Aliases normalize DeFi/L1/L2/Storage/Payment/PoW; Alpha/Crypto/
Chinese alone is no duty. Classification provenance remains exchangeInfo. TradFi/index/cross-pair
contracts stay excluded; multiplier/spot aliases need identity research. History/liquidity floors
are unchanged. This is Binance coverage, not an exhaustive multi-exchange universe.

## Outputs and recovery

| File | Content |
|---|---|
| `listings.json` | Dated inventory, classifications and exact TradingView ticker |
| `prices.csv` | Completed daily adjusted closes and turnover |
| `manifest.json` | Counts, exclusions/errors, URLs, mappings, conventions and price SHA-256 |
| `raw/*.json` | URL/body, acquisition timestamp, response hash and raw response |
| `raw/*.error.json` | Request identity, dates and failed attempts |

Exit 2 / `complete=false` means partial acquisition. A successful subset can support a disclosed
scope, not a complete screen. Cache requires exact request and same UTC acquisition day; older
responses refresh. Success clears its current failure receipt; failed responses never become cache.
Raw histories remain local; check source rights before redistribution.

Requests allow three total attempts for transient transport, truncation/invalid JSON or server
errors. HTTP 400/401/403/404 need source/request repair. Remaining attempts may use already-installed
system curl after urllib failures, with verified HTTPS and the same CA settings, never a shell.
Receipts identify transport; curl hashes its returned decompressed bytes. Responses read incrementally,
scanner pages are smaller and compression decodes before JSON.

Yahoo must match exact symbol/currency and aligned timestamps/price/volume arrays; share-class
filenames stay complete. A failed host can use the alternate public Yahoo host, recording its URL.
TLS stays verified. On macOS certificate failures may use `/etc/ssl/cert.pem` unless explicit
`SSL_CERT_FILE`/`SSL_CERT_DIR` is set. Use only verified CA bundles.

After failure, inspect receipts and research a verified alternative with exact instrument, units
and cutoff. CN alternate feeds need per-instrument share-versus-lot checks; never assume one volume
multiplier. Availability is not guaranteed. [Measurement](measurement.md) accepts the resulting CSV.
