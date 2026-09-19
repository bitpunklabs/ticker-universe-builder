from __future__ import annotations

import copy
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from universe_core import (  # noqa: E402
    AUDIT_CODES,
    EXCLUSION_CODES,
    MARKET_SPECS,
    MEASUREMENT_BASES,
    PROFILES,
    ROLES,
    UniverseError,
    apply_change_set,
    build_universe,
    default_asset_id,
    languages,
    load_lexicon,
    load_policy,
    market_spec,
    normalize_candidate,
    read_json,
    render_markdown,
    render_txt,
    report_language,
    starter_taxonomy,
    validate_ticker,
    validate_universe,
    watchlist_to_snapshot,
    write_artifacts,
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
    value["markets"]["crypto"] = {
        "light": {"min": 1, "target": 2, "max": 2},
        "medium": {"min": 2, "target": 3, "max": 3},
        "heavy": {"min": 3, "target": 4, "max": 4},
    }
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
            self.assertEqual(set(policy["markets"][code]), {"light", "medium", "heavy"})

    def test_unknown_market_is_named_not_silently_dropped(self) -> None:
        with self.assertRaisesRegex(UniverseError, "unsupported market 'hk'"):
            market_spec("hk")

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


class LocalizationTests(unittest.TestCase):
    """A universe is read by the people who trade that market, so the report follows the market.

    Only the chrome is translated. The content — names, themes, reasons, methods — is whatever
    the research wrote, and the codes stay beside their translation because the code is what the
    documentation names and what a reader greps for.
    """

    def test_every_locale_carries_every_key(self) -> None:
        english = set(load_lexicon("en"))
        self.assertIn("zh-Hans", languages())
        for language in languages():
            self.assertEqual(set(load_lexicon(language)), english, language)

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
        )
        for language in languages():
            lexicon = load_lexicon(language)
            for key in sorted(expected):
                self.assertTrue(lexicon.get(key), f"{language} is missing {key}")

    def test_the_report_language_follows_the_market(self) -> None:
        self.assertEqual(report_language("cn"), "zh-Hans")
        self.assertEqual(report_language("us"), "en")
        self.assertEqual(report_language("crypto"), "en")
        self.assertEqual(report_language("hk"), "en")

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
        with self.assertRaisesRegex(UniverseError, "unknown language 'de'"):
            load_lexicon("de")

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
        vocabulary = {"role", "basis", "profile", "depth", "reason"}
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
            for market in ("cn", "us", "crypto")
            for pattern in ("*.json", "*.md")
            for path in (ROOT / "examples" / f"{market}-light").glob(pattern)
            if path.name != "changes.json"
        }
        self.assertEqual(
            sorted(path.name for path in before if path.name.endswith(".md")),
            ["maintenance.md", "universe.md", "universe.md", "universe.md"],
        )
        build_examples.main()
        for path, text in before.items():
            self.assertEqual(path.read_text(encoding="utf-8"), text, path.name)

    def test_examples_draw_their_themes_from_the_starter_taxonomy(self) -> None:
        for market in ("cn", "us", "crypto"):
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
        for market in ("cn", "us", "crypto"):
            folder = ROOT / "examples" / f"{market}-light"
            with self.subTest(market=market):
                universe, report = build_universe(
                    read_json(folder / "build-spec.json"),
                    read_json(folder / "snapshot.json"),
                    load_policy(),
                )
                self.assertTrue(report["passed"], report["errors"])
                self.assertEqual(universe["market"], market)

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
