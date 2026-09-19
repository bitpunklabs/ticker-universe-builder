# README imagery

Two assets, and deliberately only two. Of fourteen well-known skill repositories surveyed, five
carry any image at all and none carries more than three: a logo, a terminal recording, an output
screenshot. Everything else in a skill README is better as a fenced code block, because a code
block is greppable, diffable and translatable and a screenshot of text is none of those.

Both slots are commented out in `README.md`. Drop the file in, delete the two comment lines
around the image, commit.

---

## 1. `demo.gif` — the skill firing end to end

**What it must show**, in this order, in under 40 seconds:

1. A fresh agent session, one typed line: `Build me a Light crypto ticker universe for
   observation, using Binance perpetuals.`
2. The skill loading — the line naming `ticker-universe-builder`.
3. The agent running `taxonomy`, then `build`.
4. The four artifact paths printed.
5. `Validation: PASS` and the member count.

Stop there. Do not record the research phase; it is minutes of web calls and it is not what the
GIF is for. If the real session is slow, run it once to get the transcript, then re-record with
the snapshot already on disk so `build` returns immediately — the point is the shape of the
workflow, not the wall-clock.

**How to record it (macOS):**

```bash
brew install asciinema agg      # agg renders a cast to gif; no video editor involved
asciinema rec demo.cast --cols 100 --rows 30
#   … run the session …  Ctrl-D to stop
agg --font-size 16 --theme asciinema demo.cast docs/media/demo.gif
```

`asciinema` records the terminal as text, so the GIF comes out sharp at any size and stays
small. Keep it **under 5 MB** — GitHub will serve a larger file but nobody waits for it. If it
is over, lower `--font-size`, cut the recording shorter, or add `--speed 1.5` to `agg`.

Screen-recording alternatives, if you would rather not install anything: macOS **⇧⌘5** records
the screen to `.mov`, and `ffmpeg -i in.mov -vf "fps=12,scale=1000:-1" docs/media/demo.gif`
converts it. The result is 3-5× larger than the asciinema path for the same legibility.

**Before recording:** set the terminal to a light or dark theme with real contrast, widen to
about 100 columns, clear the scrollback, and check no absolute path in the prompt leaks anything
personal (`~/workspace/...` is fine; a client name is not).

## 2. `watchlist-in-tradingview.png` — the artifact, in the tool it was built for

**What it must show:** the TradingView watchlist panel after importing a generated `.txt`, with
the theme sections visible as section headers (`00_A_CORE_ASSETS`, `10_A_L1_MAJORS`, …) and
enough rows under two or three of them to make the structure obvious.

**How to capture it:**

```bash
python scripts/universe.py build \
  --spec examples/crypto-light/build-spec.json \
  --snapshot examples/crypto-light/snapshot.json \
  --output /tmp/crypto-light
# it prints the .txt path
```

Then in TradingView: **Watchlist panel → ⋯ menu → Import list…** → pick the `.txt`. The sections
appear as collapsible headers. Collapse the ones you are not showing, screenshot the panel only
(macOS **⇧⌘4**, then Space to snap to the window, or drag a tight rectangle around the panel).

**Before capturing:** log out or switch to a throwaway layout so no personal watchlist, account
name, P/L figure or alert appears in the frame. Crop to the panel — a full 5K desktop screenshot
reads as a blurry smear at README width. Target roughly 900-1200 px wide.

---

## If you would rather ship neither

The README renders correctly with both slots commented out, and nine of the fourteen surveyed
repositories — including `anthropics/skills` and `obra/superpowers` — ship no imagery at all.
Leaving them out is a defensible choice, not an unfinished one. What is not defensible is a
broken image link, which is why the placeholders are comments rather than missing files.
