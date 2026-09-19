from __future__ import annotations

import json
import random
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from measure_core import (  # noqa: E402
    MeasureError,
    measure,
    merge_into_snapshot,
)
from universe_core import build_universe, load_policy  # noqa: E402

BENCHMARK = "BINANCE:BTCUSDT.P"


def price_table(
    path: Path, spec: dict[str, tuple[float, float, float]], sessions: int = 240
) -> None:
    """Write a CSV whose factor structure is known, so the statistics can be asserted.

    Each ticker is `beta` times the benchmark return plus `noise` of its own, at a fixed daily
    turnover. Nothing here pretends to be market data — it exists to pin the arithmetic.
    """
    rng = random.Random(20260917)
    factor = [rng.gauss(0, 0.02) for _ in range(sessions)]
    rows = ["date,ticker,close,turnover"]
    for ticker, (beta, noise, turnover) in spec.items():
        close = 100.0
        own = random.Random(sum(ord(char) for char in ticker))
        for index in range(sessions):
            day = f"2026-{1 + index // 28:02d}-{1 + index % 28:02d}"
            rows.append(f"{day},{ticker},{close:.6f},{turnover}")
            close *= 1 + beta * factor[index] + own.gauss(0, noise)
    path.write_text("\n".join(rows) + "\n", encoding="utf-8")


class MeasureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.prices = Path(self.tmp.name) / "prices.csv"
        self.addCleanup(self.tmp.cleanup)

    def measure(self, spec: dict, **kwargs) -> dict:
        price_table(self.prices, spec)
        return measure(
            prices=self.prices,
            benchmarks=[BENCHMARK],
            source="https://data.binance.vision/",
            **kwargs,
        )

    def test_a_pure_multiple_of_the_factor_is_fully_explained_by_it(self) -> None:
        bundle = self.measure({
            BENCHMARK: (1.0, 0.0, 1_000_000),
            "BINANCE:LEVUSDT.P": (2.0, 0.0, 500_000),
        })
        levered = bundle["metrics"]["BINANCE:LEVUSDT.P"]
        self.assertGreaterEqual(levered["factor_r2"], 95)
        # beta 2.0 is the top of the scale, and a constant beta is a perfectly stable one.
        self.assertEqual(levered["beta_strength"], 100)
        self.assertGreaterEqual(levered["beta_stability"], 95)

    def test_an_unrelated_series_is_not_explained_by_the_factor(self) -> None:
        bundle = self.measure({
            BENCHMARK: (1.0, 0.0, 1_000_000),
            "BINANCE:OWNUSDT.P": (0.0, 0.03, 500_000),
        })
        self.assertLess(bundle["metrics"]["BINANCE:OWNUSDT.P"]["factor_r2"], 20)

    def test_liquidity_is_a_cross_sectional_percentile(self) -> None:
        bundle = self.measure({
            BENCHMARK: (1.0, 0.0, 9_000_000),
            "BINANCE:MIDUSDT.P": (1.0, 0.01, 3_000_000),
            "BINANCE:THINUSDT.P": (1.0, 0.01, 10_000),
        })
        scores = {ticker: item["liquidity"] for ticker, item in bundle["metrics"].items()}
        self.assertEqual(scores[BENCHMARK], 100)
        self.assertEqual(scores["BINANCE:THINUSDT.P"], 0)
        self.assertEqual(scores["BINANCE:MIDUSDT.P"], 50)

    def test_a_short_series_yields_no_number_and_says_so(self) -> None:
        price_table(
            self.prices,
            {BENCHMARK: (1.0, 0.0, 1_000), "BINANCE:NEWUSDT.P": (1.0, 0.0, 1_000)},
            sessions=12,
        )
        bundle = measure(
            prices=self.prices,
            benchmarks=[BENCHMARK],
            source="https://data.binance.vision/",
        )
        self.assertNotIn("factor_r2", bundle["metrics"]["BINANCE:NEWUSDT.P"])
        self.assertTrue(any("sessions overlap" in note for note in bundle["notes"]))

    def test_a_local_file_is_not_a_source(self) -> None:
        price_table(self.prices, {BENCHMARK: (1.0, 0.0, 1_000)})
        with self.assertRaisesRegex(MeasureError, "http"):
            measure(prices=self.prices, benchmarks=[BENCHMARK], source="prices.csv")


class MergeTests(unittest.TestCase):
    """The point of the command: a snapshot the contract would have refused now builds."""

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.prices = Path(self.tmp.name) / "prices.csv"
        price_table(self.prices, {
            BENCHMARK: (1.0, 0.0, 9_000_000),
            "BINANCE:ETHUSDT.P": (1.1, 0.01, 6_000_000),
            "BINANCE:SOLUSDT.P": (1.4, 0.02, 3_000_000),
        })
        self.snapshot = {
            "schema_version": 1,
            "market": "crypto",
            "as_of": "2026-09-17",
            "complete": True,
            "sources": [{
                "url": "https://api.binance.com/api/v3/exchangeInfo",
                "as_of": "2026-09-17", "tier": 1,
            }],
            "measurement": {
                "quality": {"basis": "judged", "method": "protocol revenue durability"},
            },
            "taxonomy": [{
                "l1_code": "00", "l1_name": "Core Assets",
                "theme_code": "00_A", "theme_name": "CORE_ASSETS", "coverage_level": 1,
            }],
            "candidates": [
                {
                    "ticker": ticker, "name": ticker, "theme_code": "00_A", "role": role,
                    "eligible": True, "metrics": {"quality": 90},
                    "evidence": [{
                        "url": "https://api.binance.com/api/v3/exchangeInfo",
                        "as_of": "2026-09-17", "tier": 1,
                    }],
                }
                for ticker, role in (
                    (BENCHMARK, "BENCHMARK"),
                    ("BINANCE:ETHUSDT.P", "THEME_LEADER"),
                    ("BINANCE:SOLUSDT.P", "QUALITY_LEADER"),
                )
            ],
        }
        self.spec = {
            "schema_version": 1, "market": "crypto", "profile": "light",
            "as_of": "2026-09-17", "target_count": 3, "allow_outside_guidance": True,
        }

    def test_the_snapshot_is_refused_before_measuring_and_builds_after(self) -> None:
        with self.assertRaisesRegex(Exception, "liquidity score|factor_r2"):
            build_universe(self.spec, self.snapshot, load_policy())

        bundle = measure(
            prices=self.prices,
            benchmarks=[BENCHMARK],
            source="https://data.binance.vision/",
        )
        merged = merge_into_snapshot(self.snapshot, bundle)
        universe, report = build_universe(self.spec, merged, load_policy())
        self.assertTrue(report["passed"], report["errors"])
        self.assertEqual(universe["measurement"]["factor_r2"]["basis"], "measured")
        self.assertEqual(universe["measurement"]["quality"]["basis"], "judged")
        self.assertEqual(
            universe["measurement"]["liquidity"]["source"], "https://data.binance.vision/"
        )

    def test_a_candidate_the_table_does_not_cover_is_named(self) -> None:
        self.snapshot["candidates"].append({
            "ticker": "BINANCE:XRPUSDT.P", "name": "XRP", "theme_code": "00_A",
            "role": "THEME_LEADER", "eligible": True, "metrics": {"quality": 70},
            "evidence": [{
                "url": "https://api.binance.com/api/v3/exchangeInfo",
                "as_of": "2026-09-17", "tier": 1,
            }],
        })
        bundle = measure(
            prices=self.prices,
            benchmarks=[BENCHMARK],
            source="https://data.binance.vision/",
        )
        merged = merge_into_snapshot(self.snapshot, bundle)
        self.assertIn("BINANCE:XRPUSDT.P: not covered by the price table", merged["notes"])
        # Silence would be worse than the failure: the build still refuses it for the metric it
        # never received.
        with self.assertRaisesRegex(Exception, "liquidity score|factor_r2"):
            build_universe(self.spec, merged, load_policy())


class CliTests(unittest.TestCase):
    def test_measure_writes_a_bundle(self) -> None:
        sys.path.insert(0, str(ROOT / "scripts"))
        import universe as cli

        with tempfile.TemporaryDirectory() as folder:
            prices = Path(folder) / "prices.csv"
            output = Path(folder) / "bundle.json"
            price_table(prices, {BENCHMARK: (1.0, 0.0, 1_000_000)})
            code = cli.main([
                "measure", "--prices", str(prices), "--benchmark", BENCHMARK,
                "--source", "https://data.binance.vision/", "--output", str(output),
            ])
            self.assertEqual(code, 0)
            bundle = json.loads(output.read_text())
            self.assertEqual(bundle["metrics"][BENCHMARK]["factor_r2"], 100)


if __name__ == "__main__":
    unittest.main()
