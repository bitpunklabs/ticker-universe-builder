# Germany equities overlay

Read [equity-common.md](equity-common.md) first. The universe boundary, the fund-versus-basket
redundancy test, the cash-management exclusion and the rule about regressing against the theme
rather than the index are the same in every equity market. What follows is what is true here and
is not true elsewhere.

## Identity

- `XETR` is the venue that matters; `FWB` is accepted for lines Xetra does not carry. The same company on both is one economic asset — hold the Xetra line.
- Symbols are one to six characters.

## What this market is

Autos at 3.0 and one software company at 2.5. That is most of the index, and the weights refuse to pretend otherwise.

Electrical equipment and chemicals are promoted to level 1: Siemens and BASF are primary themes here, not the support sectors they are in the shared base.

Insurance is weighted at 2.0 against 1.0 in the base — Allianz and Munich Re are a reinsurance complex, and reinsurance moves on things nothing else in the index moves on.

## Adverse flags

This market's regime issues these, and no other market's does. They cost the same as any
universal flag; what is market-specific is the vocabulary, not the price.

| Code | What it is |
|---|---|
| `delisting_offer` | Subject to a delisting offer (Delisting-Angebot) |
| `prime_standard_breach` | In breach of a Prime Standard obligation |
| `squeeze_out` | In a squeeze-out of minority shareholders |

## Size

Breadth `0.75` in `assets/default-policy.json`, so the tiers are **Light 45**,
**Medium 120**, **Heavy 300** members. The starter table reaches 29 themes at
Light.

## Suggested live fields

Beyond the ones in equity-common.md:

- Index membership (DAX, MDAX, SDAX, TecDAX) and pending changes, which move float.
- Squeeze-out and delisting-offer announcements, both of which end a listing on a date.

## Report language

The report is written in German by default, so write the snapshot in German
too — names, `l1_name`, reasons and measurement methods. `--language en` overrides the report
and changes nothing else about the build.
