# Examples

Three small universes, one per market. Each builds and validates as shipped — the test suite
rebuilds all three, so a rotted example fails CI rather than a user's first attempt.

```bash
python scripts/universe.py build \
  --spec examples/crypto-light/build-spec.json \
  --snapshot examples/crypto-light/snapshot.json \
  --output /tmp/crypto-light
```

It writes `crypto-light-2026-09-16.{json,md,txt,validation.json}` and prints all four paths.

| Example | Shows |
|---|---|
| `crypto-light/` | Spot/perpetual merging via `asset_id`, the BTC/ETH/SOL factor measurement, a tactical `LIQUIDITY_SENSOR`, and a `changes.json` that adds a theme and its first member in one round |
| `us-light/` | Sector-ETF benchmarking, a `BETA_SATELLITE` with beta plus stability, and two rejections: a fund that duplicates an incumbent and a second share class of a company already held |
| `cn-light/` | Venue-bearing identity (`SSE:` / `SZSE:`), an ETF-and-single-name mix, and the cash-management exclusion that every liquidity ranking otherwise puts first |

## They are deliberately small

Each holds 14 members against a Light guidance range that starts at 30 (Crypto) or 150 (CN/US), so
each sets `allow_outside_guidance: true` and each build prints one expected warning:

```text
member count 14 is below crypto/light guidance 30
```

That is the point of a guidance range — it reports an abnormal input instead of blocking it. A
production build stays inside the range and prints no such warning.

## The numbers are illustrative

The tickers, venues and taxonomies are real. The metric values are **hand-written for the example**
and were not computed from market data, and the evidence URLs point at the right kind of source
rather than at a page that proves the specific number. Never copy these values into a real
universe: run the measurements named in each snapshot's `measurement` block.

## Try making one fail

The fastest way to understand the contract is to break it. Each of these stops the build with a
named error:

- Delete a `measurement` entry that a candidate uses.
- Change `factor_r2` to `{"basis": "judged"}`.
- Drop `tier` from an evidence item.
- Write an `exclusion_reasons` entry that does not start with a known code.
- Set `complete` to `false`.
- Edit a member in a built `universe.json`, then run `validate` — the hash will not match.
