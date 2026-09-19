# Examples

Three Light universes, one per market. Each builds and validates as shipped, and the test suite
rebuilds all three — a rotted example fails CI rather than a user's first attempt.

```bash
python scripts/universe.py build \
  --spec examples/crypto-light/build-spec.json \
  --snapshot examples/crypto-light/snapshot.json \
  --output /tmp/crypto-light
```

It writes `crypto-light-2026-09-17.{json,md,txt,validation.json}` and prints all four paths.

| Example | Members | Shows |
|---|---:|---|
| `crypto-light/` | 40 | A **complete** Light universe: inside its guidance range, buckets exactly on quota, zero warnings. Spot/perpetual merging via `asset_id`, the BTC/ETH/SOL factor measurement, a delisted pair and a stablecoin pair kept in the audit, and a `changes.json` that retires one satellite and adds one payment asset at 5% turnover |
| `us-light/` | 64 | Sector breadth across seventeen Level-1 themes, ETF benchmarks, beta satellites in the cyclical themes, and two rejections: a second share class of a company already held, and a sector ETF redundant with its own leaders |
| `cn-light/` | 64 | Venue-bearing identity (`SSE:` / `SZSE:`), an ETF-and-single-name mix, the broker and resource beta satellites, and the cash-management exclusion that every liquidity ranking otherwise puts first |

## Why Crypto is full size and the equity ones are not

A Light universe is led by names that turn over slowly, so a full-size Light example stays correct
for years rather than months. Crypto Light is 40 and the example is 40 — it sits inside the
guidance range and prints no warnings at all.

The equity examples stop at 64 against Light guidance of 180 (US) and 150 (CN), so both set
`allow_outside_guidance: true` and both print:

```text
member count 64 is below us/light guidance 180
```

That is the guidance range doing its job — reporting an abnormal input rather than blocking it.
They stop there because every ticker in these files is written from knowledge rather than read off
an exchange listing, and the honest limit of that is well short of 180 symbols. Growing them is a
matter of extending `seeds/*.tsv` from a real listing file, not of changing any code.

## They are generated from seeds

`seeds/{market}.tsv` holds the part that is real and hand-maintained — ticker, name, theme, role —
and `build_examples.py` expands it into `snapshot.json`:

```bash
python examples/build_examples.py
```

The test suite regenerates and compares, so editing a `snapshot.json` directly fails CI. Add a
ticker to the TSV instead. Themes must come from `assets/taxonomy/{market}.json`, which is also
asserted, so the examples and the starter taxonomy cannot drift apart.

## The numbers are illustrative

The tickers, venues and taxonomies are real. Every metric is **derived by the generator** and was
not computed from market data; the evidence URLs point at the right kind of source rather than at
a page proving the specific number. Never copy these values into a real universe — run
[the measurement command](../references/measurement.md) instead.

## Try making one fail

The fastest way to understand the contract is to break it. Each of these stops the build with a
named error:

- Delete a `measurement` entry that a candidate uses.
- Change `factor_r2` to `{"basis": "judged"}`.
- Change `quality` to `{"basis": "judged", "method": "..."}` while candidates still carry facts.
- Add an `adverse_flags` entry that is not in the closed vocabulary.
- Drop `tier` from an evidence item.
- Write an `exclusion_reasons` entry that does not start with a known code.
- Set `complete` to `false`.
- Edit a member in a built universe file, then run `validate` — the hash will not match.
