from __future__ import annotations

import copy
import json
import re
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from universe_core import (  # noqa: E402
    AUDIT_CODES,
    EXCLUSION_CODES,
    MARKET_SPECS,
    MARKETS,
    MEASUREMENT_BASES,
    PROFILES,
    QUALITY_FLAG_CODES,
    ROLES,
    UniverseError,
    _glossed,
    adverse_flag_summary,
    apply_change_set,
    build_universe,
    canonical_hash,
    check_taxonomy,
    declared_market_warnings,
    default_asset_id,
    diff_universes,
    expected_members,
    languages,
    load_lexicon,
    load_policy,
    market_guidance,
    market_spec,
    normalize_candidate,
    normalize_market_declaration,
    normalize_taxonomy,
    quality_flag_codes,
    read_json,
    render_markdown,
    render_txt,
    report_language,
    starter_taxonomy,
    theme_priority,
    theme_weight,
    tier_guidance,
    universe_hash,
    validate_ticker,
    validate_universe,
    watchlist_to_snapshot,
    write_artifacts,
)

# Every market with a committed example. Read off the directory rather than listed, so a new
# example is covered by these tests the moment it is added.
EXAMPLE_MARKETS = sorted(
    path.name.removesuffix("-light")
    for path in (ROOT / "examples").glob("*-light")
    if path.is_dir()
)


def evidence(tier: int = 1, as_of: str = "2026-09-09") -> list[dict]:
    return [{"url": "https://example.com/source", "as_of": as_of, "tier": tier}]


def measurement() -> dict:
    return {
        "liquidity": {
            "basis": "measured",
            "method": "30d notional percentile",
            "window": "30d",
            "source": "https://example.com/data",
        },
        "factor_r2": {
            "basis": "measured",
            "method": "OLS on the core factors",
            "window": "180d",
            "source": "https://example.com/data",
        },
        "independence": {
            "basis": "measured",
            "method": "derived as 100 - factor_r2",
            "window": "180d",
            "source": "https://example.com/data",
        },
        "beta_strength": {
            "basis": "measured",
            "method": "OLS beta on the core factors",
            "window": "180d",
            "source": "https://example.com/data",
        },
        "beta_stability": {
            "basis": "measured",
            "method": "cross-window agreement",
            "window": "30/90/180d",
            "source": "https://example.com/data",
        },
        "quality": {"basis": "judged", "method": "protocol role read from documentation"},
        "heat": {"basis": "judged", "method": "turnover jump confirmed against exchange data"},
    }


def candidate(
    ticker: str,
    asset_id: str,
    theme_code: str,
    role: str,
    *,
    required: bool = False,
) -> dict:
    metrics = {
        "liquidity": 90,
        "quality": 70,
        "independence": 60,
        "heat": 60,
        "factor_r2": 40,
        "beta_strength": 70,
        "beta_stability": 70,
    }
    return {
        "ticker": ticker,
        "asset_id": asset_id,
        "name": asset_id,
        "theme_code": theme_code,
        "role": role,
        "required": required,
        "eligible": True,
        "metrics": metrics,
        "evidence": evidence(),
        "reason": "fixture",
    }


def taxonomy() -> list[dict]:
    return [
        {"l1_code": "00", "l1_name": "Core", "theme_code": "00_A",
         "theme_name": "Core Assets", "coverage_level": 1},
        {"l1_code": "10", "l1_name": "L1", "theme_code": "10_A",
         "theme_name": "L1 Leaders", "coverage_level": 1},
        {"l1_code": "11", "l1_name": "Infrastructure", "theme_code": "11_A",
         "theme_name": "Infrastructure", "coverage_level": 2},
        {"l1_code": "12", "l1_name": "Meme", "theme_code": "12_A",
         "theme_name": "Meme", "coverage_level": 3},
    ]


def snapshot() -> dict:
    return {
        "schema_version": 1,
        "market": "crypto",
        "as_of": "2026-09-09",
        "complete": True,
        "sources": evidence(),
        "measurement": measurement(),
        "taxonomy": taxonomy(),
        "candidates": [
            candidate("BINANCE:BTCUSDT.P", "BTC", "00_A", "BENCHMARK", required=True),
            candidate("BINANCE:SOLUSDT.P", "SOL", "10_A", "THEME_LEADER"),
            candidate("BINANCE:LINKUSDT.P", "LINK", "11_A", "INDEPENDENT_SENSOR"),
            candidate("BINANCE:DOGEUSDT.P", "DOGE", "12_A", "BETA_SATELLITE"),
        ],
    }


def small_policy() -> dict:
    value = copy.deepcopy(load_policy())
    # A two-name universe: small enough that every selection rule is visible in one diff.
    value["tiers"] = {"light": 2, "medium": 3, "heavy": 4}
    value["markets"]["crypto"] = {"breadth": 1.0}
    value["guidance_band"] = 0.0
    return value


def spec(profile: str = "light") -> dict:
    return {"schema_version": 1, "market": "crypto", "profile": profile}


def change_set(universe: dict, ops: list[dict], **extra) -> dict:
    return {
        "schema_version": 1,
        "market": "crypto",
        "as_of": "2026-09-10",
        "complete": True,
        "sources": evidence(),
        "base_version_hash": universe["version_hash"],
        "review_depth": extra.pop("review_depth", "routine"),
        "ops": ops,
        **extra,
    }


class BuildTests(unittest.TestCase):
    def test_profiles_are_nested(self) -> None:
        built = {}
        for profile in ("light", "medium", "heavy"):
            built[profile], report = build_universe(spec(profile), snapshot(), small_policy())
            self.assertTrue(report["passed"])
        light = {item["asset_id"] for item in built["light"]["members"]}
        medium = {item["asset_id"] for item in built["medium"]["members"]}
        heavy = {item["asset_id"] for item in built["heavy"]["members"]}
        self.assertLessEqual(light, medium)
        self.assertLessEqual(medium, heavy)

    def test_render_and_artifacts(self) -> None:
        universe, report = build_universe(spec(), snapshot(), small_policy())
        text = render_txt(universe)
        self.assertIn("###00_A_Core Assets", text)
        self.assertIn("BINANCE:BTCUSDT.P", text)
        with tempfile.TemporaryDirectory() as root:
            output = Path(root) / "output"
            artifacts = write_artifacts(universe, report, output)
            # The watchlist is the artifact that leaves the directory, so its name carries the
            # market, the depth and the date on its own.
            self.assertEqual(artifacts["watchlist"].name, "crypto-light-2026-09-09.txt")
            self.assertEqual(artifacts["markdown"].name, "crypto-light-2026-09-09.md")
            self.assertEqual(
                sorted(path.name for path in output.iterdir()),
                [
                    "crypto-light-2026-09-09.json",
                    "crypto-light-2026-09-09.md",
                    "crypto-light-2026-09-09.txt",
                    "crypto-light-2026-09-09.validation.json",
                ],
            )
            self.assertEqual(
                json.loads(artifacts["universe"].read_text())["version_hash"],
                universe["version_hash"],
            )

    def test_duplicate_crypto_asset_is_rejected(self) -> None:
        raw = snapshot()
        raw["candidates"].append(candidate("BINANCE:BTCUSDT", "BTC", "00_A", "ANCHOR"))
        with self.assertRaisesRegex(UniverseError, "duplicate economic asset"):
            build_universe(spec(), raw, small_policy())

    def test_incomplete_snapshot_fails_closed(self) -> None:
        raw = snapshot()
        raw["complete"] = False
        with self.assertRaisesRegex(UniverseError, "snapshot is incomplete"):
            build_universe(spec(), raw, small_policy())


class MeasurementTests(unittest.TestCase):
    def test_metric_without_a_declaration_is_rejected(self) -> None:
        raw = snapshot()
        del raw["measurement"]["factor_r2"]
        with self.assertRaisesRegex(UniverseError, "without a measurement declaration"):
            build_universe(spec(), raw, small_policy())

    def test_window_dependent_statistics_cannot_be_judged(self) -> None:
        raw = snapshot()
        raw["measurement"]["factor_r2"] = {"basis": "judged", "method": "estimated from memory"}
        with self.assertRaisesRegex(UniverseError, "cannot be judged, only measured"):
            build_universe(spec(), raw, small_policy())

    def test_measured_metric_needs_window_and_source(self) -> None:
        raw = snapshot()
        raw["measurement"]["liquidity"].pop("window")
        with self.assertRaisesRegex(UniverseError, "measured metrics need a window"):
            build_universe(spec(), raw, small_policy())

    def test_declaration_survives_into_the_universe(self) -> None:
        universe, _ = build_universe(spec(), snapshot(), small_policy())
        self.assertEqual(universe["measurement"]["liquidity"]["window"], "30d")


class EvidenceTests(unittest.TestCase):
    def test_evidence_needs_a_tier(self) -> None:
        raw = snapshot()
        raw["candidates"][0]["evidence"] = [
            {"url": "https://example.com/source", "as_of": "2026-09-09"}
        ]
        with self.assertRaisesRegex(UniverseError, "needs tier 1, 2, or 3"):
            build_universe(spec(), raw, small_policy())

    def test_market_narrative_alone_cannot_admit_a_member(self) -> None:
        universe, _ = build_universe(spec("heavy"), snapshot(), small_policy())
        new = candidate("BINANCE:ADAUSDT.P", "ADA", "10_A", "BETA_SATELLITE")
        changes = change_set(
            universe,
            [{
                "op": "ADD", "candidate": new,
                "reason": "trending in community coverage",
                "evidence": evidence(tier=3),
            }],
        )
        with self.assertRaisesRegex(UniverseError, "tier 1 or tier 2"):
            apply_change_set(universe, changes, small_policy())

    def test_stale_evidence_is_reported_not_silently_accepted(self) -> None:
        raw = snapshot()
        raw["candidates"][1]["evidence"] = evidence(as_of="2024-01-01")
        _, report = build_universe(spec(), raw, small_policy())
        self.assertTrue(any("older than the snapshot" in item for item in report["warnings"]))

    def test_exclusion_reason_must_use_a_known_code(self) -> None:
        raw = snapshot()
        raw["candidates"].append({
            **candidate("BINANCE:XVGUSDT", "XVG", "10_A", "BREADTH_PROXY"),
            "eligible": False,
            "exclusion_reasons": ["it looked weak"],
        })
        with self.assertRaisesRegex(UniverseError, "exclusion reason must start with"):
            build_universe(spec(), raw, small_policy())


class SeedTests(unittest.TestCase):
    def test_upgrading_a_tier_keeps_every_incumbent(self) -> None:
        light, _ = build_universe(spec("light"), snapshot(), small_policy())
        medium, report = build_universe(spec("medium"), snapshot(), small_policy(), light)
        self.assertTrue(report["passed"])
        self.assertLessEqual(
            {item["ticker"] for item in light["members"]},
            {item["ticker"] for item in medium["members"]},
        )

    def test_narrowing_reselects_inside_the_incumbents(self) -> None:
        heavy, _ = build_universe(spec("heavy"), snapshot(), small_policy())
        light, report = build_universe(spec("light"), snapshot(), small_policy(), heavy)
        heavy_members = {item["ticker"] for item in heavy["members"]}
        light_members = {item["ticker"] for item in light["members"]}
        self.assertLess(light_members, heavy_members)
        self.assertTrue(
            any("narrowed universe" in warning for warning in report["warnings"]),
            report["warnings"],
        )
        # A member that lost its slot to the smaller target did not lose it to a budget, and the
        # audit has to say which.
        dropped = {
            item["ticker"]: item["reasons"] for item in light["selection_audit"]
        }
        for ticker in heavy_members - light_members:
            self.assertIn(
                dropped[ticker][0], {"removed_by_downgrade", "outside_profile_coverage"}, ticker
            )

    def test_narrowing_never_introduces_a_name_the_seed_did_not_hold(self) -> None:
        data = snapshot()
        data["candidates"].append(
            candidate("BINANCE:AVAXUSDT.P", "AVAX", "10_A", "THEME_LEADER")
        )
        heavy, _ = build_universe(spec("heavy"), snapshot(), small_policy())
        light, _ = build_universe(spec("light"), data, small_policy(), heavy)
        self.assertNotIn(
            "BINANCE:AVAXUSDT.P", {item["ticker"] for item in light["members"]}
        )
        reasons = {item["ticker"]: item["reasons"] for item in light["selection_audit"]}
        self.assertEqual(reasons["BINANCE:AVAXUSDT.P"], ["not_in_seed_universe"])

    def test_a_round_trip_through_a_narrower_tier_is_stable(self) -> None:
        heavy, _ = build_universe(spec("heavy"), snapshot(), small_policy())
        light, _ = build_universe(spec("light"), snapshot(), small_policy(), heavy)
        again, _ = build_universe(spec("heavy"), snapshot(), small_policy(), light)
        self.assertLessEqual(
            {item["ticker"] for item in light["members"]},
            {item["ticker"] for item in again["members"]},
        )

    def test_incumbent_missing_from_the_new_snapshot_stops_the_build(self) -> None:
        light, _ = build_universe(spec("light"), snapshot(), small_policy())
        raw = snapshot()
        raw["candidates"] = [
            item for item in raw["candidates"] if item["ticker"] != "BINANCE:BTCUSDT.P"
        ]
        with self.assertRaisesRegex(UniverseError, "seed members absent or ineligible"):
            build_universe(spec("medium"), raw, small_policy(), light)


class MaintenanceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.policy = small_policy()
        self.universe, _ = build_universe(spec("heavy"), snapshot(), self.policy)

    def test_stale_change_set_is_rejected(self) -> None:
        changes = change_set(self.universe, [])
        changes["base_version_hash"] = "stale"
        with self.assertRaisesRegex(UniverseError, "stale change set"):
            apply_change_set(self.universe, changes, self.policy)

    def test_no_change_keeps_membership_hash_and_adds_history(self) -> None:
        changes = change_set(
            self.universe,
            [{"op": "NO_CHANGE", "scope": "universe", "reason": "no information gain"}],
            summary="fresh checks passed",
        )
        updated, report = apply_change_set(self.universe, changes, self.policy)
        self.assertTrue(report["passed"])
        self.assertEqual(updated["version_hash"], self.universe["version_hash"])
        self.assertEqual(len(updated["history"]), 1)

    def test_anchor_cannot_be_removed(self) -> None:
        changes = change_set(
            self.universe,
            [{
                "op": "REMOVE", "ticker": "BINANCE:BTCUSDT.P",
                "reason": "fixture", "evidence": evidence(),
            }],
            review_depth="event",
        )
        with self.assertRaisesRegex(UniverseError, "anchor removal requires REPLACE"):
            apply_change_set(self.universe, changes, self.policy)

    def test_a_new_theme_and_its_first_member_land_in_one_round(self) -> None:
        new = candidate("BINANCE:ETHFIUSDT.P", "ETHFI", "13_A", "THEME_LEADER")
        changes = change_set(
            self.universe,
            [
                {
                    "op": "ADD_THEME", "l1_code": "13", "l1_name": "Staking",
                    "theme_code": "13_A", "theme_name": "Restaking", "coverage_level": 1,
                    "reason": "restaking is now its own driver", "evidence": evidence(),
                },
                {
                    "op": "ADD", "candidate": new,
                    "reason": "most traded restaking token", "evidence": evidence(),
                },
            ],
            # One addition is a quarter of this four-member fixture, so the turnover budget that
            # fits it is the event budget, not the deep one.
            review_depth="event",
        )
        updated, report = apply_change_set(self.universe, changes, self.policy)
        self.assertTrue(report["passed"])
        self.assertIn("13_A", {item["theme_code"] for item in updated["taxonomy"]})
        self.assertIn("BINANCE:ETHFIUSDT.P", {item["ticker"] for item in updated["members"]})

    def test_a_theme_cannot_be_retired_while_it_still_holds_members(self) -> None:
        changes = change_set(
            self.universe,
            [{
                "op": "REMOVE_THEME", "theme": "10_A",
                "reason": "obsolete", "evidence": evidence(),
            }],
            review_depth="deep",
        )
        with self.assertRaisesRegex(UniverseError, "move or remove its members first"):
            apply_change_set(self.universe, changes, self.policy)

    def test_bucket_drift_is_reported(self) -> None:
        drifted = copy.deepcopy(self.universe)
        for member in drifted["members"]:
            member["role"] = "LIQUIDITY_SENSOR"
            member["required"] = False
        drifted["version_hash"] = None
        report = validate_universe(drifted, self.policy)
        self.assertTrue(any("tactical bucket holds" in item for item in report["warnings"]))

    def test_validation_detects_tampering(self) -> None:
        altered = copy.deepcopy(self.universe)
        altered["members"][0]["theme_code"] = "10_A"
        report = validate_universe(altered, self.policy)
        self.assertFalse(report["passed"])
        self.assertIn("version_hash does not match universe content", report["errors"])


class MarketRegistryTests(unittest.TestCase):
    """Market rules live in one table so a fourth market cannot be half-added."""

    def test_every_registered_market_has_a_policy_row(self) -> None:
        policy = load_policy()
        self.assertEqual(set(MARKET_SPECS), set(policy["markets"]))
        for code in MARKET_SPECS:
            self.assertEqual(set(policy["markets"][code]), {"breadth"})

    def test_a_market_states_its_size_as_one_number(self) -> None:
        # Nine numbers per market is nine chances to be inconsistent and no way to tell which
        # of the nine was deliberate. A market states its breadth; the three targets are the
        # tier bases scaled by it and the band is the target plus or minus a quarter.
        policy = load_policy()
        for code, row in policy["markets"].items():
            self.assertEqual(set(row), {"breadth"}, code)
            guidance = market_guidance(code, policy, None)
            for name, band in guidance.items():
                with self.subTest(market=code, profile=name):
                    base = policy["tiers"][name]
                    self.assertEqual(band["target"], round(base * row["breadth"] / 5) * 5)
                    self.assertEqual(band["min"], round(band["target"] * 0.75 / 10) * 10)
                    self.assertEqual(band["max"], round(band["target"] * 1.25 / 10) * 10)

    def test_a_bigger_market_gets_a_bigger_universe_at_the_same_depth(self) -> None:
        # The thing breadth exists to say. Light in the US is not Light in Brazil, because the
        # same depth of observation costs more tickers where more distinguishable stock lists.
        policy = load_policy()
        sizes = {
            code: market_guidance(code, policy, None)["light"]["target"]
            for code in ("us", "cn", "jp", "uk", "br")
        }
        self.assertEqual(sizes, dict(sorted(sizes.items(), key=lambda kv: -kv[1])))
        self.assertGreater(sizes["us"], sizes["br"] * 2)

    def test_a_market_can_be_sized_without_the_policy_file(self) -> None:
        band = tier_guidance(1.0, load_policy())
        self.assertEqual(
            [band[name]["target"] for name in PROFILES], [60, 160, 400]
        )

    def test_every_starter_table_can_reach_its_own_target(self) -> None:
        # The gap this closes: guidance and the starter taxonomy were two independent sets of
        # numbers that nobody was forced to reconcile, and they were not reconciled — cn Light
        # asked for 220 members from a table that tops out at 72. Every profile of every
        # shipped market now checks clean, warnings included, so the two cannot drift apart
        # again without this failing.
        for code in sorted(MARKETS):
            for name in PROFILES:
                with self.subTest(market=code, profile=name):
                    result = check_taxonomy(starter_taxonomy(code), code, profile=name)
                    self.assertTrue(result["passed"], result["errors"])
                    self.assertEqual(result["warnings"], [])

    def test_unknown_market_is_named_not_silently_dropped(self) -> None:
        with self.assertRaisesRegex(UniverseError, "unsupported market 'th'"):
            market_spec("th")

    def test_the_registry_covers_the_markets_the_skill_claims_to_cover(self) -> None:
        # Fourteen rows, one policy breadth each, one starter table each, and a locale for the
        # language each of them defaults to. A market half-registered is worse than one not
        # registered at all: it builds, and nothing says which half is missing.
        policy = load_policy()
        self.assertGreaterEqual(len(MARKETS), 14)
        for code in sorted(MARKETS):
            with self.subTest(market=code):
                spec = market_spec(code)
                self.assertIn(code, policy["markets"])
                self.assertIn(spec.language, languages())
                self.assertTrue(starter_taxonomy(code))
                self.assertTrue((ROOT / "references" / "markets" / f"{code}.md").is_file())

    def test_identity_follows_the_registry(self) -> None:
        # Venue is part of the asset only where two venues really are two instruments.
        self.assertEqual(default_asset_id("cn", "SSE:600519"), "SSE:600519")
        self.assertEqual(default_asset_id("us", "NASDAQ:AAPL"), "AAPL")
        self.assertEqual(default_asset_id("crypto", "BINANCE:BTCUSDT.P"), "BTC")
        self.assertEqual(default_asset_id("crypto", "BINANCE:BTCUSDT"), "BTC")

    def test_symbol_shape_is_enforced_per_market(self) -> None:
        self.assertTrue(validate_ticker("cn", "SSE:60051"))
        self.assertTrue(validate_ticker("cn", "NASDAQ:600519"))
        self.assertTrue(validate_ticker("crypto", "BINANCE:BTCUSDC"))
        self.assertFalse(validate_ticker("crypto", "BINANCE:BTCUSDT.P"))
        self.assertFalse(validate_ticker("us", "NYSEARCA:BRK.B"))


# A comma between two Chinese characters is an ASCII comma only by accident, and it is the most
# common way a translated page reads as machine output. Latin runs keep their own punctuation.
_ASCII_NEXT_TO_CJK = re.compile(r"[\u3400-\u9fff][,;:!?]|[,;:!?][\u3400-\u9fff]")


def declaration(**overrides) -> dict:
    value = {
        "code": "th",
        "label": "Thailand SET",
        "venues": ["SET"],
        "symbol_pattern": r"[A-Z][A-Z0-9\-]{0,9}",
        "symbol_hint": "one to ten characters starting with a letter",
        "guidance": {
            "light": {"min": 1, "target": 2, "max": 4},
            "medium": {"min": 2, "target": 3, "max": 6},
            "heavy": {"min": 3, "target": 4, "max": 8},
        },
        "evidence": evidence(),
    }
    value.update(overrides)
    return value


def declared_snapshot(**overrides) -> dict:
    value = snapshot()
    value["market"] = "th"
    value["market_spec"] = declaration(**overrides.pop("spec_overrides", {}))
    value["candidates"] = [
        candidate("SET:PTT", "PTT", "00_A", "BENCHMARK", required=True),
        candidate("SET:AOT", "AOT", "10_A", "THEME_LEADER"),
        candidate("SET:CPALL", "CPALL", "11_A", "INDEPENDENT_SENSOR"),
        candidate("SET:KBANK", "KBANK", "12_A", "BETA_SATELLITE"),
    ]
    value.update(overrides)
    return value


class ThemeWeightTests(unittest.TestCase):
    """Themes are not equal, and a cap said they were.

    Semiconductors carry more of what the A-share market does than property development does.
    Under a shared cap the only two outcomes were cutting the theme that matters off at four
    names or handing the one that does not four slots it had nothing to fill. So there is no
    cap: a theme declares a weight, and the slots left after every theme has its first one are
    apportioned to weight. The tests below pin the two properties that makes true — more weight
    means more members, and an empty bench costs a theme nothing.
    """

    def weighted(self, weights: dict[str, float]) -> list[dict]:
        rows = taxonomy()
        for item in rows:
            item["weight"] = weights.get(item["theme_code"], 1.0)
        return normalize_taxonomy(rows)

    def test_the_first_slot_is_cheap_and_the_next_one_costs_more(self) -> None:
        self.assertEqual(theme_priority(1.0, 0), 1.0)
        self.assertAlmostEqual(theme_priority(1.0, 1), 1 / 3)
        self.assertAlmostEqual(theme_priority(3.0, 1), 1.0)

    def test_weight_is_what_a_theme_holds_relative_to_another(self) -> None:
        # Three times the weight, three times the members, once there are slots to apportion.
        shares = expected_members(self.weighted({"10_A": 3.0, "12_A": 1.0}), 100)
        self.assertAlmostEqual(shares["10_A"] / shares["12_A"], 3.0)

    def test_a_default_weight_is_no_weight_at_all(self) -> None:
        plain = normalize_taxonomy(taxonomy())
        self.assertEqual({theme_weight(item) for item in plain}, {1.0})

    def test_a_weight_outside_the_guard_rail_is_refused(self) -> None:
        rows = taxonomy()
        rows[0]["weight"] = 9
        with self.assertRaisesRegex(UniverseError, "weight 9.0 is outside"):
            normalize_taxonomy(rows)

    def test_a_heavier_theme_takes_more_of_the_universe(self) -> None:
        # The end-to-end statement: same candidates, same target, one weight changed.
        folder = ROOT / "examples" / "crypto-light"
        snapshot = read_json(folder / "snapshot.json")
        policy = load_policy()

        def held(weight: float) -> int:
            data = copy.deepcopy(snapshot)
            for item in data["taxonomy"]:
                if item["theme_code"] == "12_A":
                    item["weight"] = weight
            universe, _ = build_universe(read_json(folder / "build-spec.json"), data, policy)
            return sum(1 for item in universe["members"] if item["theme_code"] == "12_A")

        self.assertGreater(held(4.0), held(0.25))

    def test_a_theme_with_no_bench_left_costs_the_universe_nothing(self) -> None:
        # The property a cap could never have: slots the theme cannot fill flow to the next
        # theme in line instead of being held open or spent on relaxing eligibility.
        folder = ROOT / "examples" / "crypto-light"
        data = read_json(folder / "snapshot.json")
        for item in data["taxonomy"]:
            if item["theme_code"] == "60_A":
                item["weight"] = 4.0
        universe, report = build_universe(
            read_json(folder / "build-spec.json"), data, load_policy()
        )
        available = sum(
            1 for item in data["candidates"] if item["theme_code"] == "60_A"
        )
        self.assertLessEqual(
            sum(1 for item in universe["members"] if item["theme_code"] == "60_A"), available
        )
        self.assertEqual(len(universe["members"]), universe["limits"]["target_count"])

    def test_the_report_says_where_the_universe_concentrated(self) -> None:
        folder = ROOT / "examples" / "crypto-light"
        universe, report = build_universe(
            read_json(folder / "build-spec.json"),
            read_json(folder / "snapshot.json"),
            load_policy(),
        )
        concentration = report["stats"]["concentration"]
        self.assertEqual(
            concentration["members"],
            max(Counter(item["theme_code"] for item in universe["members"]).values()),
        )
        self.assertGreater(concentration["share"], 0)

    def test_drift_away_from_the_table_is_reported(self) -> None:
        # Nothing caps a theme, so the check that replaces the cap is a disclosure: a pool that
        # walked far from what its own weights asked for says so.
        folder = ROOT / "examples" / "crypto-light"
        universe, _ = build_universe(
            read_json(folder / "build-spec.json"),
            read_json(folder / "snapshot.json"),
            load_policy(),
        )
        crowded = copy.deepcopy(universe)
        theme = crowded["members"][-1]["theme_code"]
        for item in crowded["members"][:12]:
            item["theme_code"] = theme
        crowded["version_hash"] = universe_hash(crowded)
        report = validate_universe(crowded, load_policy())
        self.assertIn("weighted share", " ".join(report["warnings"]))


class DiffTests(unittest.TestCase):
    """`maintain` reports one review. This answers what a review cannot."""

    def setUp(self) -> None:
        self.universe, _ = build_universe(spec("medium"), snapshot(), small_policy())

    def test_a_universe_against_itself_is_identical(self) -> None:
        report = diff_universes(self.universe, copy.deepcopy(self.universe))
        self.assertTrue(report["identical"])
        self.assertEqual(report["turnover"], 0.0)
        self.assertEqual(report["market_spec"], "unchanged")

    def test_a_review_and_a_diff_of_it_agree_on_turnover(self) -> None:
        # Two definitions of turnover that drift apart would be worse than one, so they are
        # checked against each other on the shipped example rather than asserted separately.
        folder = ROOT / "examples" / "crypto-light"
        policy = load_policy()
        built, _ = build_universe(
            read_json(folder / "build-spec.json"), read_json(folder / "snapshot.json"), policy
        )
        reviewed, report = apply_change_set(built, read_json(folder / "changes.json"), policy)
        compared = diff_universes(built, reviewed)
        self.assertEqual(compared["added"], ["BINANCE:TRXUSDT.P"])
        self.assertEqual(compared["removed"], ["BINANCE:GMXUSDT.P"])
        self.assertAlmostEqual(compared["turnover"], report["maintenance"]["turnover"], places=4)

    def test_a_role_change_and_a_theme_move_are_named(self) -> None:
        later = copy.deepcopy(self.universe)
        later["members"][0]["role"] = "QUALITY_LEADER"
        later["members"][1]["theme_code"] = "11_A"
        report = diff_universes(self.universe, later)
        self.assertEqual(report["rerolled"][0]["after"], "QUALITY_LEADER")
        self.assertEqual(report["moved"][0]["after"], "11_A")
        self.assertFalse(report["identical"])

    def test_declared_rules_that_drifted_between_sessions_come_first(self) -> None:
        # The failure this exists to catch: two sessions researched one market's venue list
        # differently, so the two universes were never comparable to begin with.
        built, _ = build_universe(
            {"schema_version": 1, "market": "th", "profile": "light"},
            declared_snapshot(), load_policy(),
        )
        other, _ = build_universe(
            {"schema_version": 1, "market": "th", "profile": "light"},
            declared_snapshot(spec_overrides={"venues": ["SET", "MAI"]}), load_policy(),
        )
        report = diff_universes(built, other)
        self.assertNotEqual(report["market_spec"], "unchanged")
        self.assertEqual(report["market_spec"]["after"]["venues"], ["MAI", "SET"])

    def test_metric_drift_is_ranked_and_capped(self) -> None:
        later = copy.deepcopy(self.universe)
        later["members"][0]["metrics"]["liquidity"] = 40
        later["members"][1]["metrics"]["quality"] = 69
        report = diff_universes(self.universe, later)
        self.assertEqual(report["metric_drift"]["fields"], 2)
        self.assertEqual(report["metric_drift"]["largest"][0]["metric"], "liquidity")
        self.assertEqual(report["metric_drift"]["largest"][0]["delta"], -50.0)
        # Metrics move on every refresh; that alone is not a change to the instrument.
        self.assertTrue(report["identical"])


class TaxonomyCheckTests(unittest.TestCase):
    """The first step is the one with no help in it, and a declared market has no starter.

    A malformed table is caught by the builder anyway. What this catches is the table that is
    structurally fine and cannot produce the universe that was asked for — which today you learn
    after the research is done.
    """

    def themes(self, *rows) -> list[dict]:
        return [
            {"l1_code": code.split("_")[0], "l1_name": f"Group {code.split('_')[0]}",
             "theme_code": code, "theme_name": f"THEME_{code}", "coverage_level": level}
            for code, level in rows
        ]

    def test_a_target_smaller_than_the_theme_count_cannot_build(self) -> None:
        # Every theme inside the coverage level must hold a member, so this is not a tight fit.
        report = check_taxonomy(
            self.themes(("00_A", 1), ("10_A", 1), ("20_A", 1)), "crypto",
            target=2, profile="light",
        )
        self.assertFalse(report["passed"])
        self.assertTrue(any("every theme must hold a member" in e for e in report["errors"]))

    def test_a_table_that_puts_a_target_in_one_theme_is_reported_before_the_research(self) -> None:
        # There is no capacity to be short of any more — a theme will hold whatever its bench
        # can fill. What is worth learning before researching a single candidate is the other
        # shape of mistake: a table so thin that one theme is weighted to be the universe.
        rows = self.themes(("00_A", 1), ("10_A", 1))
        rows[0]["weight"] = 3.0
        report = check_taxonomy(rows, "crypto", target=40, profile="light")
        self.assertTrue(report["passed"])
        self.assertTrue(any("00_A is weighted to about 30" in w for w in report["warnings"]))
        self.assertEqual(report["stats"]["capacity"]["light"]["weight_total"], 4.0)

    def test_one_group_cannot_have_two_names(self) -> None:
        rows = self.themes(("00_A", 1), ("00_B", 1))
        rows[1]["l1_name"] = "Something else"
        report = check_taxonomy(rows, "crypto", profile="light", target=4)
        self.assertFalse(report["passed"])
        self.assertTrue(any("is called both" in item for item in report["errors"]))

    def test_a_group_that_light_cannot_see_is_reported(self) -> None:
        report = check_taxonomy(
            self.themes(("00_A", 1), ("10_A", 2)), "crypto", target=4, profile="light"
        )
        self.assertTrue(any("invisible to a Light universe" in i for i in report["warnings"]))

    def test_a_non_ascii_theme_name_is_reported_because_it_becomes_a_txt_header(self) -> None:
        rows = self.themes(("00_A", 1))
        rows[0]["theme_name"] = "白酒"
        report = check_taxonomy(rows, "crypto", target=4, profile="light")
        self.assertTrue(any("TradingView section header" in i for i in report["warnings"]))

    def test_a_malformed_table_is_one_error_not_a_traceback(self) -> None:
        report = check_taxonomy([{"theme_code": "nope"}], "crypto")
        self.assertFalse(report["passed"])
        self.assertIn("invalid theme_code", report["errors"][0])

    def test_the_shipped_starters_are_structurally_sound(self) -> None:
        # They warn about capacity — a starter is deliberately a starting point — but nothing in
        # them should be an error.
        for market in sorted(MARKET_SPECS):
            report = check_taxonomy(starter_taxonomy(market), market)
            self.assertEqual(report["errors"], [], market)


class DeclaredMarketTests(unittest.TestCase):
    """A market this skill has not reviewed is still a market a user may observe.

    The general logic does not change for it — roles, quotas, evidence tiers, measurement,
    turnover budgets and hashing are the same everywhere. What a snapshot supplies is the handful
    of facts a registry row would have carried, under the same gates as any other researched
    fact: strong evidence, recorded in the universe, covered by the hash, and reported as
    researched rather than reviewed.
    """

    def build(self, **overrides):
        return build_universe(
            {"schema_version": 1, "market": "th", "profile": "light"},
            declared_snapshot(**overrides),
            load_policy(),
        )

    def test_an_unregistered_market_without_a_declaration_names_the_way_in(self) -> None:
        raw = declared_snapshot()
        del raw["market_spec"]
        with self.assertRaisesRegex(UniverseError, "declare market_spec in the snapshot"):
            build_universe({"schema_version": 1, "market": "th", "profile": "light"},
                           raw, load_policy())

    def test_a_registered_market_cannot_be_redeclared(self) -> None:
        # Otherwise a snapshot could loosen the symbol rule that rejected its own candidates.
        raw = snapshot()
        raw["market_spec"] = declaration(code="crypto")
        with self.assertRaisesRegex(UniverseError, "is registered"):
            build_universe(spec(), raw, small_policy())

    def test_a_declared_market_builds_under_the_same_invariants(self) -> None:
        universe, report = self.build()
        self.assertTrue(report["passed"])
        self.assertEqual(universe["market_spec"]["label"], "Thailand SET")
        self.assertEqual(universe["members"][0]["ticker"], "SET:PTT")
        self.assertTrue(validate_universe(universe, load_policy())["passed"])

    def test_the_report_always_says_the_rules_were_not_reviewed(self) -> None:
        universe, report = self.build()
        self.assertTrue(any("is not registered" in item for item in report["warnings"]))
        self.assertIn("Market rules: declared", render_markdown(universe, report))
        # And it survives a round trip through a stored universe, not only the build that made it.
        again = validate_universe(universe, load_policy())
        self.assertTrue(any("is not registered" in item for item in again["warnings"]))

    def test_the_declared_identity_rule_actually_applies(self) -> None:
        # Left to the default rule, so the declaration is what decides whether two venues
        # carrying one symbol are one asset or two.
        def without_asset_ids(**overrides):
            raw = declared_snapshot(**overrides)
            for item in raw["candidates"]:
                del item["asset_id"]
            return build_universe({"schema_version": 1, "market": "th", "profile": "light"},
                                  raw, load_policy())[0]

        self.assertEqual(without_asset_ids()["members"][0]["asset_id"], "PTT")
        venued = without_asset_ids(spec_overrides={"venue_in_asset_id": True})
        self.assertEqual(venued["members"][0]["asset_id"], "SET:PTT")

    def test_the_declared_symbol_shape_is_enforced(self) -> None:
        raw = declared_snapshot()
        raw["candidates"][1]["ticker"] = "SET:0001"
        raw["candidates"][1]["asset_id"] = "0001"
        with self.assertRaisesRegex(UniverseError, "one to ten characters"):
            build_universe({"schema_version": 1, "market": "th", "profile": "light"},
                           raw, load_policy())

    def test_editing_the_stored_rules_breaks_the_hash(self) -> None:
        universe, _ = self.build()
        tampered = copy.deepcopy(universe)
        tampered["market_spec"]["venues"] = ["SET", "NASDAQ"]
        report = validate_universe(tampered, load_policy())
        self.assertFalse(report["passed"])
        self.assertTrue(any("version_hash" in item for item in report["errors"]))

    def test_narrative_alone_cannot_declare_a_market(self) -> None:
        with self.assertRaisesRegex(UniverseError, "tier 1 or tier 2"):
            normalize_market_declaration(declaration(evidence=evidence(tier=3)), "th")

    def test_size_is_not_optional(self) -> None:
        raw = declaration()
        del raw["guidance"]
        with self.assertRaisesRegex(UniverseError, "declare exactly one of breadth"):
            normalize_market_declaration(raw, "th")

    def test_size_can_be_stated_the_way_a_registered_market_states_it(self) -> None:
        # One number, scaling the same tier bases. A declared market that has to invent nine
        # numbers usually invents nine inconsistent ones.
        raw = declaration()
        del raw["guidance"]
        raw["breadth"] = 0.5
        clean = normalize_market_declaration(raw, "th")
        self.assertEqual(clean["breadth"], 0.5)
        self.assertEqual(
            market_guidance("th", load_policy(), clean)["light"]["target"], 30
        )

    def test_stating_size_twice_is_refused(self) -> None:
        raw = declaration()
        raw["breadth"] = 0.5
        with self.assertRaisesRegex(UniverseError, "declare exactly one of breadth"):
            normalize_market_declaration(raw, "th")

    def test_a_language_with_no_locale_is_named(self) -> None:
        with self.assertRaisesRegex(UniverseError, "no locale for 'th'"):
            normalize_market_declaration(declaration(language="th"), "th")

    def test_a_declared_language_writes_the_report(self) -> None:
        universe, report = self.build(spec_overrides={"language": "zh-Hant"})
        self.assertIn("## 成員", render_markdown(universe, report))

    def test_an_unknown_field_is_refused_rather_than_ignored(self) -> None:
        with self.assertRaisesRegex(UniverseError, "unknown fields: lot_size"):
            normalize_market_declaration(declaration(lot_size=100), "th")

    def test_a_change_set_cannot_redeclare_the_rules(self) -> None:
        universe, _ = self.build()
        changes = change_set(universe, [{"op": "NO_CHANGE", "scope": "00_A", "reason": "fresh"}])
        changes["market"] = "th"
        changes["market_spec"] = declaration()
        with self.assertRaisesRegex(UniverseError, "cannot redeclare market_spec"):
            apply_change_set(universe, changes, load_policy())


class MarketQualityFlagTests(unittest.TestCase):
    """What counts as an adverse flag follows the regulator; what it costs does not.

    Seven flags are universal because every market states them in some form. Beyond those, a
    vocabulary wide enough for every regime would be too coarse to record any of them: an ST
    designation is not `risk_warning` in general, and an NT 10-K is not a concept the A-share
    market has. So the vocabulary extends per market while the scoring rule stays one rule.
    """

    def scored(self, market: str, flags: list[str]) -> dict:
        item = candidate("BINANCE:ARBUSDT.P", "ARB", "10_A", "THEME_LEADER")
        item["metrics"]["quality"] = 60
        item["quality_facts"] = {"size_rank_pct": 80, "adverse_flags": flags}
        return normalize_candidate(
            market, item, {entry["theme_code"]: entry for entry in taxonomy()}
        )

    def test_every_market_keeps_the_universal_flags(self) -> None:
        for code in sorted(MARKETS):
            self.assertLessEqual(QUALITY_FLAG_CODES, quality_flag_codes(code), code)

    def test_no_two_markets_claim_the_same_market_specific_flag(self) -> None:
        # A code that means one thing in one market and another somewhere else makes the counts
        # in two reports look comparable when they are not.
        seen: dict[str, str] = {}
        for spec in MARKET_SPECS.values():
            for code in spec.quality_flags:
                self.assertNotIn(code, QUALITY_FLAG_CODES, code)
                self.assertIsNone(seen.get(code), f"{code} is claimed by {seen.get(code)}")
                seen[code] = spec.code

    def test_a_market_specific_flag_is_accepted_in_its_own_market(self) -> None:
        member = self.scored("crypto", ["unlock_overhang"])
        # It costs exactly what a universal flag costs: the rule stays general.
        self.assertEqual(member["quality_rule_score"], 55)

    def test_a_flag_from_another_market_is_refused_and_named(self) -> None:
        with self.assertRaisesRegex(UniverseError, "'special_treatment' belongs to cn"):
            self.scored("crypto", ["special_treatment"])

    def test_the_report_counts_the_flags_it_found(self) -> None:
        data = snapshot()
        data["measurement"]["quality"] = {
            "basis": "blended",
            "method": "listing age and size percentile",
            "source": "https://example.com/reference",
        }
        for item in data["candidates"]:
            if item["role"] != "BENCHMARK":
                item["quality_facts"] = {
                    "size_rank_pct": 80, "adverse_flags": ["unlock_overhang"],
                }
        universe, report = build_universe(spec(), data, small_policy())
        self.assertEqual(
            adverse_flag_summary(universe["members"]),
            [("unlock_overhang", sum(1 for m in universe["members"] if m["quality_facts"]))],
        )
        self.assertIn("| unlock_overhang |", render_markdown(universe, report))
        self.assertIn("解锁抛压 (unlock_overhang)", render_markdown(universe, report, "zh-Hans"))


class DeclaredQualityFlagTests(unittest.TestCase):
    """A declared market may name its own flags; it may not rename anyone else's."""

    def declared(self, flags) -> dict:
        return normalize_market_declaration(declaration(quality_flags=flags), "th")

    def test_a_declared_vocabulary_reaches_the_candidate_gate(self) -> None:
        data = declared_snapshot(spec_overrides={"quality_flags": ["sp_designation"]})
        data["measurement"]["quality"] = {
            "basis": "blended", "method": "size", "source": "https://example.com/reference",
        }
        data["candidates"][1]["quality_facts"] = {
            "size_rank_pct": 80, "adverse_flags": ["sp_designation"],
        }
        universe, _ = build_universe(
            {"schema_version": 1, "market": "th", "profile": "light"}, data, load_policy()
        )
        self.assertEqual(universe["market_spec"]["quality_flags"], ["sp_designation"])
        self.assertEqual(adverse_flag_summary(universe["members"]), [("sp_designation", 1)])

    def test_a_declared_market_cannot_redefine_a_universal_flag(self) -> None:
        with self.assertRaisesRegex(UniverseError, "already universal"):
            self.declared(["going_concern"])

    def test_a_vocabulary_that_long_is_notes(self) -> None:
        with self.assertRaisesRegex(UniverseError, "at most"):
            self.declared([f"flag_{n}" for n in range(9)])

    def test_a_flag_must_be_a_code_not_a_sentence(self) -> None:
        with self.assertRaisesRegex(UniverseError, "must be a lowercase code"):
            self.declared(["the auditor resigned in March"])

    def test_the_declared_vocabulary_is_part_of_the_identity(self) -> None:
        plain = normalize_market_declaration(declaration(), "th")
        extended = self.declared(["sp_designation"])
        self.assertNotEqual(canonical_hash(plain), canonical_hash(extended))

    def test_a_declared_flag_prints_as_its_code(self) -> None:
        # No locale can know a vocabulary invented at run time, so the fallback has to be the
        # code itself rather than a missing key.
        self.assertEqual(_glossed(load_lexicon("zh-Hans"), "flag", "sp_designation"),
                         "sp_designation")
        self.assertIn(
            "sp_designation",
            " ".join(declared_market_warnings(self.declared(["sp_designation"]))),
        )


class LocalizationTests(unittest.TestCase):
    """A universe is read by the people who trade that market, so the report follows the market.

    Only the chrome is translated. The content — names, themes, reasons, methods — is whatever
    the research wrote, and the codes stay beside their translation because the code is what the
    documentation names and what a reader greps for.
    """

    def test_every_locale_carries_every_chrome_key(self) -> None:
        # The chrome is finite and shared, so it is identical everywhere. The adverse-flag
        # vocabulary is not: it grows one market at a time, and a Korean designation has no
        # word in French because no French-language report will ever print it.
        def chrome(language: str) -> set[str]:
            return {key for key in load_lexicon(language) if not key.startswith("flag.")}

        english = chrome("en")
        self.assertIn("zh-Hans", languages())
        for language in languages():
            self.assertEqual(chrome(language), english, language)

    def test_every_market_can_name_its_own_flags_in_its_own_language(self) -> None:
        # The rule that replaces "every locale carries every flag". A market's report is
        # written in its language by default, so its own vocabulary has to exist there.
        for code in sorted(MARKETS):
            spec = market_spec(code)
            lexicon = load_lexicon(spec.language)
            for flag in sorted(spec.quality_flags):
                with self.subTest(market=code, flag=flag):
                    self.assertTrue(lexicon.get(f"flag.{flag}"), f"{spec.language}/{flag}")

    def test_english_is_the_fallback_for_every_flag_there_is(self) -> None:
        lexicon = load_lexicon("en")
        for spec in MARKET_SPECS.values():
            for flag in sorted(spec.quality_flags):
                self.assertEqual(lexicon.get(f"flag.{flag}"), flag)

    def test_every_closed_vocabulary_has_a_word_in_every_language(self) -> None:
        # The vocabularies are closed so that they can be counted; the same property is what
        # makes them translatable at all. Adding a role or an exclusion code without a word for
        # it fails here rather than printing an untranslated code into a Chinese report.
        expected = (
            {f"role.{code}" for code in ROLES}
            | {f"reason.{code}" for code in EXCLUSION_CODES | AUDIT_CODES}
            | {f"profile.{name}" for name in PROFILES}
            | {f"basis.{name}" for name in MEASUREMENT_BASES}
            | {f"depth.{name}" for name in load_policy()["maintenance"]}
            | {f"flag.{code}" for code in QUALITY_FLAG_CODES}
        )
        for language in languages():
            lexicon = load_lexicon(language)
            for key in sorted(expected):
                self.assertTrue(lexicon.get(key), f"{language} is missing {key}")

    def test_the_report_language_follows_the_market(self) -> None:
        self.assertEqual(report_language("cn"), "zh-Hans")
        self.assertEqual(report_language("us"), "en")
        self.assertEqual(report_language("crypto"), "en")
        self.assertEqual(report_language("hk"), "zh-Hant")
        self.assertEqual(report_language("jp"), "ja")
        self.assertEqual(report_language("br"), "pt-BR")
        self.assertEqual(report_language("th"), "en")

    def test_a_market_report_is_written_in_its_own_language(self) -> None:
        chinese = (ROOT / "examples" / "cn-light" / "universe.md").read_text(encoding="utf-8")
        english = (ROOT / "examples" / "us-light" / "universe.md").read_text(encoding="utf-8")
        self.assertIn("# CN 标的池", chinese)
        self.assertIn("## 成员", chinese)
        self.assertNotIn("## Members", chinese)
        self.assertIn("## Members", english)

    def test_the_language_can_be_overridden(self) -> None:
        universe, report = build_universe(spec(), snapshot(), small_policy())
        self.assertIn("## Members", render_markdown(universe, report))
        self.assertIn("## 成員", render_markdown(universe, report, "zh-Hant"))

    def test_a_translation_never_replaces_the_code(self) -> None:
        universe, report = build_universe(spec(), snapshot(), small_policy())
        text = render_markdown(universe, report, "zh-Hans")
        self.assertIn("基准 (BENCHMARK)", text)

    def test_an_unknown_language_is_named_not_silently_ignored(self) -> None:
        with self.assertRaisesRegex(UniverseError, "unknown language 'th'"):
            load_lexicon("th")

    # The three checks below are the ones proofreading keeps missing. A translation that is
    # merely wrong is caught by reading it; a translation that is ASCII-punctuated, that collides
    # with a label somewhere else in the report, or that drifts between the two Chinese locales
    # reads fine in isolation and only looks wrong in the rendered page.

    def test_cjk_text_uses_cjk_punctuation(self) -> None:
        for language in languages():
            for key, value in sorted(load_lexicon(language).items()):
                self.assertIsNone(
                    _ASCII_NEXT_TO_CJK.search(value),
                    f"{language} {key}: ASCII punctuation beside CJK in {value!r}",
                )
        # The example is the demonstration, so it is held to the same standard as the chrome.
        chinese = (ROOT / "examples" / "cn-light" / "universe.md").read_text(encoding="utf-8")
        for line in chinese.splitlines():
            self.assertIsNone(_ASCII_NEXT_TO_CJK.search(line), line)

    def test_no_word_means_two_things_in_one_report(self) -> None:
        # `review.depth` and `depth.deep` print on the same line. Giving both the same word makes
        # the line read "Depth: Depth", which is how the first draft of zh-Hans shipped.
        vocabulary = {"role", "basis", "profile", "depth", "reason", "flag"}
        chrome = {"title", "label", "section", "column", "review", "value"}
        for language in languages():
            lexicon = load_lexicon(language)
            words: dict[str, str] = {}
            for key, value in sorted(lexicon.items()):
                if not value or key.split(".")[0] not in vocabulary:
                    continue
                self.assertNotIn(key, words.get(value, ""))
                self.assertIsNone(words.get(value), f"{language}: {key} reuses {value!r}")
                words[value] = key
            labels = {
                value for key, value in lexicon.items()
                if value and key.split(".")[0] in chrome
            }
            self.assertEqual(set(words) & labels, set(), language)

    def test_the_two_chinese_locales_stay_one_translation(self) -> None:
        # zh-Hant is maintained as a character-level conversion of zh-Hans, not as an independent
        # translation, so that one term cannot become two. Length parity is the cheap proxy: it
        # caught NEW_LISTING rendered as 次新 in one locale and 新上市 in the other. A regional
        # term that genuinely changes length goes in the exemption set, deliberately and visibly.
        exempt: set[str] = set()
        hans, hant = load_lexicon("zh-Hans"), load_lexicon("zh-Hant")
        for key in sorted(hans):
            if key == "language" or key in exempt:
                continue
            self.assertEqual(
                len(hans[key]), len(hant[key]),
                f"{key}: {hans[key]!r} and {hant[key]!r} are not the same term",
            )


class QualityTests(unittest.TestCase):
    """Quality stays a judgement, but no longer an unchecked one."""

    def scored(self, facts: dict | None, judged: int = 60) -> dict:
        item = candidate("BINANCE:ARBUSDT.P", "ARB", "10_A", "THEME_LEADER")
        item["metrics"]["quality"] = judged
        if facts is not None:
            item["quality_facts"] = facts
        return normalize_candidate(
            "crypto", item, {entry["theme_code"]: entry for entry in taxonomy()}
        )

    def with_facts(self, facts: dict, declaration: dict | None = None) -> dict:
        data = snapshot()
        item = candidate("BINANCE:ARBUSDT.P", "ARB", "10_A", "THEME_LEADER")
        item["quality_facts"] = facts
        data["candidates"].append(item)
        if declaration is not None:
            data["measurement"]["quality"] = declaration
        return data

    def test_facts_and_judgement_are_averaged(self) -> None:
        member = self.scored({"listing_age_days": 2000, "size_rank_pct": 80})
        # (100 from the five-year band + 80 size) / 2 = 90 rule, halved against 60 judged.
        self.assertEqual(member["quality_rule_score"], 90)
        self.assertEqual(member["quality_score"], 75.0)
        # The judged input is kept as given; the blend is derived beside it, never over it.
        self.assertEqual(member["metrics"]["quality"], 60)

    def test_an_adverse_flag_costs_the_rule_half(self) -> None:
        member = self.scored({"size_rank_pct": 80, "adverse_flags": ["risk_warning"]})
        self.assertEqual(member["quality_rule_score"], 55)
        self.assertEqual(member["quality_score"], 57.5)

    def test_without_facts_the_score_is_the_judgement(self) -> None:
        member = self.scored(None)
        self.assertIsNone(member["quality_rule_score"])
        self.assertEqual(member["quality_score"], 60)

    def test_an_unknown_flag_is_refused(self) -> None:
        with self.assertRaisesRegex(UniverseError, "unknown adverse flag"):
            self.scored({"size_rank_pct": 80, "adverse_flags": ["vibes"]})

    def test_flags_alone_do_not_make_a_score(self) -> None:
        with self.assertRaisesRegex(UniverseError, "listing_age_days or size_rank_pct"):
            self.scored({"adverse_flags": ["restructuring"]})

    def test_facts_without_a_blended_declaration_are_refused(self) -> None:
        with self.assertRaisesRegex(UniverseError, "declare it as blended"):
            build_universe(spec(), self.with_facts({"size_rank_pct": 80}), small_policy())

    def test_a_blended_declaration_without_facts_is_refused(self) -> None:
        data = snapshot()
        data["measurement"]["quality"] = {
            "basis": "blended", "method": "x", "source": "https://example.com/reference",
        }
        with self.assertRaisesRegex(UniverseError, "no candidate carries quality_facts"):
            build_universe(spec(), data, small_policy())

    def test_a_blended_declaration_needs_the_source_of_the_facts(self) -> None:
        data = self.with_facts(
            {"size_rank_pct": 80}, {"basis": "blended", "method": "listing age and size"}
        )
        with self.assertRaisesRegex(UniverseError, "blended metrics need a source URL"):
            build_universe(spec(), data, small_policy())

    def test_blending_survives_a_round_trip_unchanged(self) -> None:
        data = self.with_facts(
            {"listing_age_days": 2000, "size_rank_pct": 80},
            {
                "basis": "blended",
                "method": "listing age and size percentile against a judged durability read",
                "source": "https://example.com/reference",
            },
        )
        universe, report = build_universe(spec("heavy"), data, small_policy())
        self.assertTrue(report["passed"], report["errors"])
        scores = {item["ticker"]: item["quality_score"] for item in universe["members"]}
        self.assertEqual(scores["BINANCE:ARBUSDT.P"], 80.0)  # rule 90, judged 70
        again = validate_universe(copy.deepcopy(universe), small_policy())
        self.assertTrue(again["passed"], again["errors"])
        self.assertIn("50% rule and 50% judgement", render_markdown(universe, report))

    def test_judgement_alone_is_reported(self) -> None:
        _, report = build_universe(spec(), snapshot(), small_policy())
        self.assertTrue(
            any("rests on judgement alone" in warning for warning in report["warnings"]),
            report["warnings"],
        )


class AuditTests(unittest.TestCase):
    def test_rejections_are_counted_by_code(self) -> None:
        universe, report = build_universe(
            read_json(ROOT / "examples" / "us-light" / "build-spec.json"),
            read_json(ROOT / "examples" / "us-light" / "snapshot.json"),
            load_policy(),
        )
        rejections = report["stats"]["rejections"]
        self.assertEqual(rejections["duplicate_asset"], 1)
        self.assertEqual(rejections["redundant_with_member"], 1)
        self.assertEqual(sum(rejections.values()), len(universe["selection_audit"]))
        self.assertIn("redundant_with_member | 1", render_markdown(universe, report))


class ImportTests(unittest.TestCase):
    """Most people arrive holding a watchlist, not a research file."""

    def draft(self, text: str, market: str = "us") -> dict:
        return watchlist_to_snapshot(text, market, "2026-09-17")

    def test_a_comma_export_and_a_line_list_read_the_same(self) -> None:
        comma = self.draft("###Tech,NASDAQ:AAPL,NASDAQ:MSFT")
        lines = self.draft("###Tech\nNASDAQ:AAPL\nNASDAQ:MSFT\n")
        self.assertEqual(comma, lines)

    def test_sections_become_a_draft_taxonomy(self) -> None:
        draft = self.draft("###Big Tech,NASDAQ:AAPL\n###Energy,NYSE:XOM")
        self.assertEqual(
            [(item["theme_code"], item["theme_name"]) for item in draft["taxonomy"]],
            [("00_A", "BIG_TECH"), ("01_A", "ENERGY")],
        )

    def test_nothing_is_claimed_that_a_txt_file_cannot_carry(self) -> None:
        draft = self.draft("###Tech,NASDAQ:AAPL")
        self.assertFalse(draft["complete"])
        candidate_ = draft["candidates"][0]
        self.assertEqual(candidate_["role"], "")
        self.assertFalse(candidate_["eligible"])
        self.assertEqual(candidate_["metrics"], {})
        self.assertEqual(candidate_["evidence"], [])
        with self.assertRaisesRegex(UniverseError, "incomplete"):
            build_universe(
                {"schema_version": 1, "market": "us", "profile": "light"}, draft, load_policy()
            )

    def test_a_ticker_from_another_market_is_reported_not_dropped(self) -> None:
        draft = self.draft("###Mixed,NASDAQ:AAPL,BINANCE:BTCUSDT.P")
        self.assertEqual(len(draft["candidates"]), 1)
        self.assertTrue(any("BINANCE:BTCUSDT.P" in note for note in draft["notes"]))

    def test_a_repeated_ticker_keeps_its_first_section(self) -> None:
        draft = self.draft("###A,NASDAQ:AAPL\n###B,NASDAQ:AAPL")
        self.assertEqual(len(draft["candidates"]), 1)
        self.assertEqual(draft["candidates"][0]["theme_code"], "00_A")
        self.assertTrue(any("more than once" in note for note in draft["notes"]))

    def test_our_own_watchlist_round_trips(self) -> None:
        universe, _ = build_universe(
            read_json(ROOT / "examples" / "crypto-light" / "build-spec.json"),
            read_json(ROOT / "examples" / "crypto-light" / "snapshot.json"),
            load_policy(),
        )
        draft = self.draft(render_txt(universe), market="crypto")
        self.assertEqual(
            [item["theme_code"] for item in draft["taxonomy"]],
            sorted({item["theme_code"] for item in universe["members"]}),
        )
        self.assertEqual(
            sorted(item["ticker"] for item in draft["candidates"]),
            sorted(item["ticker"] for item in universe["members"]),
        )

    def test_an_empty_watchlist_is_an_error_not_an_empty_draft(self) -> None:
        with self.assertRaisesRegex(UniverseError, "no us tickers"):
            self.draft("###Tech\n")


class ExampleTests(unittest.TestCase):
    """The shipped examples are the first thing anyone runs; a rotted one is a broken skill."""

    def test_the_committed_examples_match_their_seeds(self) -> None:
        # The seed tables are the source of truth. If regenerating changes a committed file,
        # someone edited the output instead of the input.
        sys.path.insert(0, str(ROOT / "examples"))
        import build_examples

        before = {
            path: path.read_text(encoding="utf-8")
            for market in EXAMPLE_MARKETS
            for pattern in ("*.json", "*.md", "*.txt")
            for path in (ROOT / "examples" / f"{market}-light").glob(pattern)
            if path.name != "changes.json"
        }
        self.assertEqual(
            sorted(path.name for path in before if path.name.endswith(".md")),
            ["maintenance.md"] + ["universe.md"] * len(EXAMPLE_MARKETS),
        )
        # The watchlist is committed too: it is the artifact that gets imported, and a diff in
        # the TradingView format should be reviewable without running a build.
        self.assertEqual(
            len([path for path in before if path.name == "watchlist.txt"]),
            len(EXAMPLE_MARKETS),
        )
        build_examples.main()
        for path, text in before.items():
            self.assertEqual(path.read_text(encoding="utf-8"), text, path.name)

    def test_every_registered_market_ships_an_example(self) -> None:
        # The registry is the claim; an example is the evidence. A market added without one is a
        # row nobody has ever built against.
        self.assertEqual(sorted(EXAMPLE_MARKETS), sorted(MARKETS))

    def test_examples_draw_their_themes_from_the_starter_taxonomy(self) -> None:
        for market in EXAMPLE_MARKETS:
            with self.subTest(market=market):
                published = {item["theme_code"] for item in starter_taxonomy(market)}
                used = {
                    item["theme_code"]
                    for item in read_json(
                        ROOT / "examples" / f"{market}-light" / "snapshot.json"
                    )["candidates"]
                }
                self.assertLessEqual(used, published)

    def test_every_example_builds_and_passes(self) -> None:
        for market in EXAMPLE_MARKETS:
            folder = ROOT / "examples" / f"{market}-light"
            with self.subTest(market=market):
                universe, report = build_universe(
                    read_json(folder / "build-spec.json"),
                    read_json(folder / "snapshot.json"),
                    load_policy(),
                )
                self.assertTrue(report["passed"], report["errors"])
                self.assertEqual(universe["market"], market)

    def test_every_example_is_a_full_size_universe_for_its_market(self) -> None:
        # An example below its own guidance teaches the wrong shape, and `allow_outside_guidance`
        # in a shipped build spec teaches that the flag is normal. Both used to be true here.
        policy = load_policy()
        for market in EXAMPLE_MARKETS:
            folder = ROOT / "examples" / f"{market}-light"
            with self.subTest(market=market):
                spec = read_json(folder / "build-spec.json")
                self.assertNotIn("allow_outside_guidance", spec)
                universe, report = build_universe(
                    spec, read_json(folder / "snapshot.json"), policy
                )
                band = market_guidance(market, policy, None)["light"]
                self.assertEqual(len(universe["members"]), band["target"])
                self.assertGreaterEqual(len(universe["members"]), band["min"])
                self.assertLessEqual(len(universe["members"]), band["max"])
                self.assertEqual(report["warnings"], [])

    def test_every_example_reads_in_its_own_market_language(self) -> None:
        # The report language is a registry fact, not a run-time choice, and the committed
        # example is where that either holds or quietly stops holding.
        for market in EXAMPLE_MARKETS:
            with self.subTest(market=market):
                report = (ROOT / "examples" / f"{market}-light" / "universe.md").read_text(
                    encoding="utf-8"
                )
                heading = next(
                    line for line in report.splitlines() if line.startswith("# ")
                )
                lexicon = read_json(
                    ROOT / "assets" / "locales" / f"{report_language(market)}.json"
                )
                self.assertEqual(
                    heading, "# " + lexicon["title"].format(market=market.upper())
                )

    def test_the_crypto_change_set_still_applies_to_its_own_universe(self) -> None:
        folder = ROOT / "examples" / "crypto-light"
        universe, _ = build_universe(
            read_json(folder / "build-spec.json"),
            read_json(folder / "snapshot.json"),
            load_policy(),
        )
        changes = read_json(folder / "changes.json")
        self.assertEqual(changes["base_version_hash"], universe["version_hash"])
        updated, report = apply_change_set(universe, changes, load_policy())
        self.assertTrue(report["passed"], report["errors"])
        self.assertEqual(report["maintenance"]["added"], ["BINANCE:TRXUSDT.P"])
        self.assertEqual(report["maintenance"]["removed"], ["BINANCE:GMXUSDT.P"])
        self.assertEqual(report["warnings"], [])


if __name__ == "__main__":
    unittest.main()
