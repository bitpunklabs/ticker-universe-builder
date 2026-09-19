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
| `us-light/` | 80 | Sector breadth across thirty Level-1 themes, ETF benchmarks, beta satellites in the cyclical themes, two recent listings as the tactical budget, and two rejections: a second share class of a company already held, and a sector ETF redundant with its own leaders |
| `cn-light/` | 80 | Venue-bearing identity (`SSE:` / `SZSE:`), an ETF-and-single-name mix, the broker and resource beta satellites, the cash-management exclusion that every liquidity ranking otherwise puts first — and a report written end to end in Simplified Chinese |

## All three are full size

Each example is exactly its market's Light target, inside the guidance band, buckets on quota,
and **zero warnings** — no `allow_outside_guidance`, because an example that needs an escape
hatch teaches that the hatch is normal.

Three examples against fourteen registered markets is deliberate, not a backlog. Every ticker in
`seeds/*.tsv` is written from knowledge rather than read off an exchange listing, which is why
the seeds hold around a hundred names and not a thousand — and why eleven markets ship a
reviewed registry row, a theme table that checks clean at all three tiers and an overlay, but no
example. Holding a market registration hostage to a hundred verified tickers is how fourteen
markets would have stayed at three.

`us-light` is also the demonstration of the shared equity table: the thirty Level-1 themes it
covers are `assets/taxonomy/_equity.json` unchanged, which is the same table `jp`, `de`, `br` and
the rest state their delta against.

Medium and Heavy examples do not ship either. Growing a seed to 240 names is a TSV edit against a
real listing file, not a code change.

## Read one without running it

Each folder carries the report the build produces:

| File | What it is |
|---|---|
| `universe.md` | The built universe — roles, metric provenance, rejection counts, every member with its reason and evidence |
| `crypto-light/maintenance.md` | The same report after `changes.json` is applied, including the `## This review` block with turnover, additions and removals |

Both are generated, not written. Committing them means a change in selection shows up as a
reviewable diff instead of as a silently different result the next time someone runs a build.

`cn-light/universe.md` is in Simplified Chinese and the other two are in English, because the
report follows the market rather than the tool. The cn seed is written the same way — `贵州茅台`,
Chinese `l1_name`, Chinese `measurement.method` — since the renderer translates the chrome and
leaves the content exactly as the snapshot wrote it. See
[markets/adding-a-market.md](../references/markets/adding-a-market.md) for the classification.

## They are generated from seeds

`seeds/{market}.tsv` holds the part that is real and hand-maintained — ticker, name, theme, role —
and `build_examples.py` expands it into `snapshot.json`, `build-spec.json` and the reports:

```bash
python examples/build_examples.py
```

The test suite regenerates and compares every generated file, so editing one directly fails CI. Add a
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
