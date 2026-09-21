# Security

## What this thing is, in security terms

A directory of Markdown and standard-library Python that an agent reads and runs locally. It
opens no sockets, holds no credentials, spawns no subprocesses, and calls no `eval`, `exec` or
`pickle`. There is no server to attack and no account to take over.

That is most of the threat model. What is left is worth stating precisely, because it is the
part people get wrong about agent skills.

## The part that is real

**The scripts read untrusted input.** `snapshot.json`, `changes.json`, a theme table and an
exported watchlist all arrive from whoever is driving the agent. They are parsed as data — never
evaluated — and every field is validated against `references/data-contracts.md` before it is
used. A malformed file should produce a `UniverseError` and exit 2, writing nothing.

**Prose from that input reaches a report the agent then reads.** Member names, reasons and theme
names are rendered into `universe.md`. A snapshot is a document the operator supplies, so text
in it is as trustworthy as they are — but an agent that fetched a snapshot from somewhere else
is reading attacker-influenced prose back into its own context. Treat a third-party snapshot the
way you would treat any untrusted document.

**It writes files.** `build` and `maintain` refuse a non-empty output directory, write into a
scratch directory they create, and rename it into place. They do not delete anything they did
not create. `--output` is still a path you are handing to a program; point it somewhere you
intend to write.

## Not security issues

- A universe that performed badly, or that excluded something you wanted. It is an observation
  instrument, not advice, and it makes no claim about returns. See "Not investment advice" in
  the README.
- A wrong ticker, a stale listing status or a theme table that does not match a market. Those
  are correctness bugs and belong in a normal issue — there is a template for them.
- The skill declining to invent data, bypass its validator or execute a trade. Those are the
  design working.

## Reporting

Report privately through GitHub: **Security → Report a vulnerability** on
[this repository](https://github.com/bitpunklabs/ticker-universe-builder/security). Please do not
open a public issue for something exploitable.

Include what you ran, what input you gave it, and what it did that it should not have. A failing
input file is worth more than a description of one.

Expect an acknowledgement within a week. This is a single-maintainer project and there is no
paid disclosure programme; what you get is a fix, a changelog line and credit if you want it.

## Supported versions

The newest release, and `main`. Older tags are not patched — this is a directory you clone, so
upgrading is `git pull` and there is no migration to be afraid of.
