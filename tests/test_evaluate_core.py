from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import evaluate_core  # noqa: E402
from evaluate_core import EvaluateError, evaluate  # noqa: E402

DAYS = 30


def prices(paths: dict[str, list[float]], directory: Path) -> Path:
    """One CSV in the format `measure` reads, from an explicit close series per ticker."""
    lines = ["date,ticker,close"]
    for ticker, closes in paths.items():
        for index, close in enumerate(closes):
            lines.append(f"2026-09-{index + 1:02d},{ticker},{close}")
    path = directory / "prices.csv"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def ramp(total: float, days: int = DAYS) -> list[float]:
    """A straight line from 100 to 100 * (1 + total), so the window return is exactly `total`."""
    return [100.0 * (1.0 + total * step / (days - 1)) for step in range(days)]


def member(ticker: str, theme: str = "00_A", role: str = "THEME_LEADER", **metrics) -> dict:
    return {"ticker": ticker, "asset_id": ticker, "theme_code": theme, "role": role,
            "metrics": metrics or {"liquidity": 50}}


def universe(members: list[dict], audit: list[dict] | None = None) -> dict:
    return {
        "market": "crypto", "profile": "light", "version_hash": "abc123", "as_of": "2026-09-01",
        "members": members, "selection_audit": audit or [],
    }


class SurvivalTests(unittest.TestCase):
    def test_a_member_the_table_cannot_see_is_named(self) -> None:
        with tempfile.TemporaryDirectory() as root:
            table = prices({"A:ONE": ramp(0.1), "A:TWO": ramp(0.2)}, Path(root))
            report = evaluate(
                universe=universe([member("A:ONE"), member("A:TWO"), member("A:GONE")]),
                prices=table,
            )
        self.assertEqual(report["survival"]["unobservable"], ["A:GONE"])
        self.assertEqual(report["survival"]["observed"], 2)

    def test_a_ticker_with_too_little_history_is_unobservable_not_scored(self) -> None:
        with tempfile.TemporaryDirectory() as root:
            table = prices({"A:ONE": ramp(0.1), "A:SHORT": ramp(0.9, days=4)}, Path(root))
            report = evaluate(universe=universe([member("A:ONE"), member("A:SHORT")]),
                              prices=table)
        self.assertEqual(report["survival"]["unobservable"], ["A:SHORT"])

    def test_a_table_nothing_can_be_read_from_is_an_error(self) -> None:
        with tempfile.TemporaryDirectory() as root:
            table = prices({"A:ONE": ramp(0.1, days=3)}, Path(root))
            with self.assertRaisesRegex(EvaluateError, "observations"):
                evaluate(universe=universe([member("A:ONE")]), prices=table)


class CoverageTests(unittest.TestCase):
    """The question a universe exists to answer: did the instrument see what happened."""

    def setUp(self) -> None:
        self.series = {f"A:M{i}": ramp(0.01 * i) for i in range(1, 6)}
        # The rejected candidate is the largest move in the window by a wide margin.
        self.series["A:DROPPED"] = ramp(2.0)
        self.members = [member(f"A:M{i}") for i in range(1, 6)]
        self.audit = [{"ticker": "A:DROPPED", "reasons": ["insufficient_liquidity: thin book"]}]

    def run_report(self, **kwargs):
        with tempfile.TemporaryDirectory() as root:
            return evaluate(
                universe=universe(self.members, self.audit),
                prices=prices(self.series, Path(root)),
                **kwargs,
            )

    def test_the_biggest_move_the_universe_missed_is_named(self) -> None:
        report = self.run_report(top=3)
        top = report["coverage"]["top"]["3"]
        self.assertEqual(top["missed"], ["A:DROPPED"])
        self.assertAlmostEqual(top["rate"], 2 / 3, places=3)

    def test_the_share_of_the_pool_is_reported_beside_the_coverage(self) -> None:
        # A table holding nothing but members makes every coverage number 1.0 and meaningless,
        # so the reader is told how much wider the pool was.
        report = self.run_report(top=3)
        self.assertEqual(report["coverage"]["pool"], 6)
        self.assertAlmostEqual(report["coverage"]["member_share_of_pool"], 5 / 6, places=3)

    def test_the_rejection_code_carries_the_cost(self) -> None:
        # "Some rejections were expensive" changes nothing. Naming the code changes a threshold.
        report = self.run_report(top=3)
        code = report["rejections"]["by_code"]["insufficient_liquidity"]
        self.assertEqual(code["in_top_3"], ["A:DROPPED"])
        self.assertAlmostEqual(code["median_absolute_move"], 2.0, places=3)
        self.assertLess(report["rejections"]["selected_median_absolute_move"], 0.1)

    def test_a_cut_wider_than_the_pool_is_skipped_rather_than_padded(self) -> None:
        report = self.run_report()
        self.assertEqual(report["coverage"]["top"], {})


class MetricPowerTests(unittest.TestCase):
    """Which metric ordered anything, and which one was decoration."""

    def report(self, metric_values: list[int]):
        series = {f"A:M{i}": ramp(0.05 * (i + 1)) for i in range(len(metric_values))}
        members = [
            member(f"A:M{i}", liquidity=value) for i, value in enumerate(metric_values)
        ]
        with tempfile.TemporaryDirectory() as root:
            return evaluate(universe=universe(members), prices=prices(series, Path(root)))

    def test_a_metric_that_ranked_the_moves_scores_one(self) -> None:
        report = self.report([10, 20, 30, 40, 50, 60, 70, 80])
        self.assertAlmostEqual(report["metrics"]["liquidity"]["vs_absolute_move"], 1.0)

    def test_a_metric_that_says_nothing_scores_nothing(self) -> None:
        report = self.report([50] * 8)
        self.assertIsNone(report["metrics"]["liquidity"]["vs_absolute_move"])

    def test_too_few_members_produce_no_correlation_rather_than_a_confident_one(self) -> None:
        report = self.report([10, 20, 30, 40])
        self.assertEqual(report["metrics"]["liquidity"]["scored"], 4)
        self.assertIsNone(report["metrics"]["liquidity"]["vs_absolute_move"])

    def test_ties_do_not_invent_an_ordering(self) -> None:
        self.assertEqual(evaluate_core._ranks([5, 5, 9]), [1.5, 1.5, 3.0])


class IndependenceTests(unittest.TestCase):
    def series(self) -> dict[str, list[float]]:
        return {"A:BENCH": ramp(0.3), "A:CLONE": ramp(0.3), "A:M1": ramp(0.1)}

    def test_without_a_benchmark_it_says_so_rather_than_guessing(self) -> None:
        with tempfile.TemporaryDirectory() as root:
            report = evaluate(
                universe=universe([member("A:M1", liquidity=50, independence=80)]),
                prices=prices(self.series(), Path(root)),
            )
        self.assertIn("note", report["independence"])

    def test_a_benchmark_missing_from_the_table_is_an_error(self) -> None:
        with tempfile.TemporaryDirectory() as root:
            with self.assertRaisesRegex(EvaluateError, "benchmark not in the price table"):
                evaluate(
                    universe=universe([member("A:M1")]),
                    prices=prices(self.series(), Path(root)),
                    benchmarks=["A:NOPE"],
                )

    def test_a_member_that_tracks_the_benchmark_shows_its_declared_score_was_wrong(self) -> None:
        with tempfile.TemporaryDirectory() as root:
            report = evaluate(
                universe=universe([member("A:CLONE", liquidity=50, independence=90)]),
                prices=prices(self.series(), Path(root)),
                benchmarks=["A:BENCH"],
            )
        worst = report["independence"]["largest_errors"][0]
        self.assertEqual(worst["ticker"], "A:CLONE")
        self.assertAlmostEqual(worst["realised_independence"], 0.0, places=1)
        self.assertAlmostEqual(worst["error"], -90.0, places=1)


class ThemeTests(unittest.TestCase):
    def test_the_theme_carrying_the_volatility_is_named(self) -> None:
        zigzag = [100.0 + (index % 2) * 40 for index in range(DAYS)]
        series = {"A:CALM": ramp(0.05), "A:WILD": zigzag}
        members = [member("A:CALM", theme="00_A"), member("A:WILD", theme="10_A")]
        with tempfile.TemporaryDirectory() as root:
            report = evaluate(universe=universe(members), prices=prices(series, Path(root)))
        self.assertEqual(report["themes"]["most_volatile"], "10_A")
        self.assertGreater(
            report["themes"]["themes"]["10_A"]["share_of_volatility"],
            report["themes"]["themes"]["00_A"]["share_of_volatility"],
        )


class RedundancyTests(unittest.TestCase):
    def test_the_pair_moving_together_is_named_first(self) -> None:
        # Two names on the same hill and one that is genuinely somewhere else. Nothing here is
        # a gate: the report has to make the pair visible, and the reader decides.
        twin = [100.0 + (index % 2) * 10 for index in range(DAYS)]
        series = {
            "A:ONE": twin,
            "A:TWO": [value * 3 for value in twin],
            "A:OTHER": ramp(0.2),
        }
        members = [member("A:ONE"), member("A:TWO", theme="10_A"), member("A:OTHER")]
        with tempfile.TemporaryDirectory() as root:
            report = evaluate(universe=universe(members), prices=prices(series, Path(root)))
        top = report["redundancy"]["most_correlated"][0]
        self.assertEqual(top["pair"], ["A:ONE", "A:TWO"])
        self.assertGreater(top["correlation"], 0.99)
        self.assertFalse(top["same_theme"])
        self.assertEqual(report["redundancy"]["compared"], 3)
        self.assertEqual(report["redundancy"]["pairs"], 3)

    def test_nothing_is_gated_on_the_correlation(self) -> None:
        # The section counts what sits above the line and never acts on it. If this ever grows
        # an error or a warning, the skill has quietly started constraining what it discloses.
        twin = [100.0 + (index % 2) * 10 for index in range(DAYS)]
        series = {"A:ONE": twin, "A:TWO": [value * 3 for value in twin]}
        with tempfile.TemporaryDirectory() as root:
            report = evaluate(
                universe=universe([member("A:ONE"), member("A:TWO")]),
                prices=prices(series, Path(root)),
            )
        self.assertEqual(report["redundancy"]["above_high"], 1)
        self.assertNotIn("errors", report["redundancy"])
        self.assertNotIn("warnings", report["redundancy"])

    def test_one_short_history_does_not_shorten_the_window_for_everyone(self) -> None:
        # A new listing has half a window. Joining it to the shared grid would silently turn
        # every correlation in the report into a fifteen-day statistic, so it is set aside and
        # named instead.
        series = {
            "A:ONE": ramp(0.1),
            "A:TWO": ramp(0.2),
            "A:NEW": ramp(0.3, days=12),
        }
        members = [member("A:ONE"), member("A:TWO"), member("A:NEW")]
        with tempfile.TemporaryDirectory() as root:
            report = evaluate(universe=universe(members), prices=prices(series, Path(root)))
        self.assertEqual(report["redundancy"]["short_history"], ["A:NEW"])
        self.assertEqual(report["redundancy"]["compared"], 2)
        self.assertGreaterEqual(report["redundancy"]["observations"], DAYS - 2)

    def test_a_member_that_never_moved_is_named_not_dropped(self) -> None:
        # Its correlation with anything is undefined, not zero, so it cannot join a pair. A
        # flat sensor is worth naming on its own — nothing else in the report would say so.
        series = {"A:ONE": ramp(0.1), "A:TWO": ramp(0.2), "A:FLAT": [100.0] * DAYS}
        members = [member("A:ONE"), member("A:TWO"), member("A:FLAT")]
        with tempfile.TemporaryDirectory() as root:
            report = evaluate(universe=universe(members), prices=prices(series, Path(root)))
        self.assertEqual(report["redundancy"]["no_variation"], ["A:FLAT"])
        self.assertEqual(report["redundancy"]["compared"], 2)

    def test_a_universe_with_one_observable_member_says_so(self) -> None:
        with tempfile.TemporaryDirectory() as root:
            report = evaluate(
                universe=universe([member("A:ONE"), member("A:GONE")]),
                prices=prices({"A:ONE": ramp(0.1)}, Path(root)),
            )
        self.assertEqual(report["redundancy"]["compared"], 0)
        self.assertIn("two members", report["redundancy"]["note"])


if __name__ == "__main__":
    unittest.main()
