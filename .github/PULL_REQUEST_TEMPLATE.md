## What changed about the design

Not which files moved — what a caller or a reader should now believe that they did not before.

## Checklist

- [ ] `python -m pytest tests -q`
- [ ] `ruff check .`
- [ ] `python examples/build_examples.py && git diff --exit-code examples/` — and if the examples
      moved, the diff is in this PR and I have read it. It is not noise; it is this change shown
      as its effect on fourteen real universes.
- [ ] Deterministic logic changed → a test pins which behaviour is correct
- [ ] Contract changed → `references/data-contracts.md` changed first
- [ ] Nothing weakens the validator to make an output pass

## Licensing

By opening this PR you agree your contribution may be distributed under MIT and, through the
OpenClaw registry, under MIT-0. See [CONTRIBUTING.md](../CONTRIBUTING.md#licensing).
