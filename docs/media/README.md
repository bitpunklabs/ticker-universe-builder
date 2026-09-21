# README imagery

Two assets, and deliberately only two. Of fourteen well-known skill repositories surveyed, five
carry any image at all and none carries more than three: a logo, a terminal recording, an output
screenshot. Everything else in a skill README is better as a fenced code block, because a code
block is greppable, diffable and translatable and a screenshot of text is none of those.

Both are GIFs, because both show an action rather than a state. Both slots are commented out in
`README.md`. Drop the file in, delete the two comment lines around the image, commit.

Together they are one story in two halves — the skill produces a watchlist, the watchlist goes
into TradingView — so record them in that order and keep the same terminal and browser theme
across the pair.

---

## 1. `demo.gif` — the skill firing end to end

Recorded in **OpenClaw**, building a **US Medium** universe.

**What it must show**, in this order, in under 40 seconds:

1. One typed line: `Build me a Medium US ticker universe for observation.`
2. The skill loading — the line naming `ticker-universe-builder`.
3. The agent running `taxonomy`, then `build`.
4. The four artifact paths printed.
5. `Validation: PASS`, the member count, and the largest-theme line.

Stop there.

### Read this before recording a Medium

US Medium targets **215 members with a floor of 160**, and the shipped seed at
`examples/seeds/us.tsv` holds 101 candidates. That seed cannot build a Medium, and it is not
meant to — it exists to build the Light example. A real Medium run has to research roughly 215
verified US listings, which is minutes of web calls, and **that is the part not to record**.

So record in two passes:

1. Run the session for real, all the way through. Keep `snapshot.json`.
2. Re-record with that snapshot already on disk, so `taxonomy` and `build` return immediately.

The GIF is showing the *shape* of the workflow and the fact that it ends in `PASS`. It is not
claiming the wall-clock. What it must not do is show a build that fails its floor, which is what
a live run against the shipped seed would produce.

If two passes is more than this is worth, `Build me a Light US ticker universe for observation.`
is the honest alternative: it targets 80, the shipped seed covers it, and the run is short enough
to record in one take.

**How to record it:**

```bash
brew install asciinema agg      # agg renders a cast to gif; no video editor involved
asciinema rec demo.cast --cols 100 --rows 30
#   … run the session …  Ctrl-D to stop
agg --font-size 16 --theme asciinema demo.cast docs/media/demo.gif
```

`asciinema` records the terminal as text, so the GIF comes out sharp at any size and stays
small. Keep it **under 5 MB** — GitHub will serve a larger file but nobody waits for it. If it
is over, lower `--font-size`, cut the recording shorter, or add `--speed 1.5` to `agg`.

If OpenClaw is being driven through a GUI rather than a terminal, asciinema cannot see it: macOS
**⇧⌘5** records the screen to `.mov`, and
`ffmpeg -i in.mov -vf "fps=12,scale=1000:-1" docs/media/demo.gif` converts it. The result is 3-5×
larger than the asciinema path for the same legibility, so crop tightly to the pane that is
changing.

**Before recording:** set a theme with real contrast, widen to about 100 columns, clear the
scrollback, and check no absolute path leaks anything personal (`~/workspace/...` is fine; a
client name is not).

## 2. `watchlist-import.gif` — the artifact going into the tool it was built for

**What it must show:** importing a generated `.txt` into TradingView, then **holding the final
frame for about two seconds** on the populated watchlist panel with the theme sections visible as
headers (`00_A_CORE_ASSETS`, `10_A_L1_MAJORS`, …) and two or three of them expanded.

That hold is the whole point. The import click-through is TradingView's UI; the populated panel
is the skill's output. A reader who only sees the last frame should still learn what they get.

**Which file to import:** if `demo.gif` produced a real US Medium watchlist, use that one — the
pair then tells one continuous story. Otherwise the repository already ships every watchlist, so
there is nothing to build first:

```text
examples/us-light/watchlist.txt         80 members, 30 theme sections
examples/crypto-light/watchlist.txt     40 members, 13 theme sections
```

215 sections do not fit on a screen; scrolling through them reads as clutter. Whichever file you
use, frame two or three expanded sections and collapse the rest.

**How to capture it:** **Watchlist panel → ⋯ menu → Import list…** → pick the `.txt`. The sections
arrive as collapsible headers. Record the screen (macOS **⇧⌘5**), then
`ffmpeg -i in.mov -vf "fps=12,scale=1000:-1" docs/media/watchlist-import.gif`.

**Before capturing:** log out or switch to a throwaway layout so no personal watchlist, account
name, P/L figure or alert appears in the frame. Crop to the panel — a full 5K desktop recording
reads as a blurry smear at README width. Target roughly 900-1200 px wide, and keep it under 5 MB.

---

## If you would rather ship neither

The README renders correctly with both slots commented out, and nine of the fourteen surveyed
repositories — including `anthropics/skills` and `obra/superpowers` — ship no imagery at all.
Leaving them out is a defensible choice, not an unfinished one. What is not defensible is a
broken image link, which is why the placeholders are comments rather than missing files.
