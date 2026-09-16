from __future__ import annotations

import math
import unittest

from scripts.reproduce_mininet_table import calculate, metrics


class MetricTests(unittest.TestCase):
    def test_standard_metric_formulas(self) -> None:
        result = metrics(tp=80, tn=810, fp=90, fn=20)
        self.assertAlmostEqual(result["accuracy"], 0.89)
        self.assertAlmostEqual(result["precision"], 80 / 170)
        self.assertAlmostEqual(result["recall"], 0.8)
        self.assertAlmostEqual(result["historical_recall_formula"], 80 / 830)
        self.assertAlmostEqual(result["f1"], 160 / 270)

    def test_recovered_archive_summary(self) -> None:
        detail, parents, combined = calculate()
        summary = combined["summary"]
        self.assertEqual(len(detail), 40)
        self.assertEqual(len(parents), 4)
        self.assertEqual(summary["samples_per_run"], [8920, 8920, 8920, 8920])
        self.assertTrue(math.isclose(summary["parent_ten_class_accuracy_mean"], 0.9211603139013453))
        self.assertTrue(math.isclose(summary["mininet_macro_accuracy"], 0.9468469730941704))
        self.assertTrue(math.isclose(summary["mininet_macro_precision"], 0.6809298703305865))
        self.assertTrue(math.isclose(summary["mininet_macro_recall_corrected"], 0.942572869955157))
        self.assertTrue(math.isclose(summary["mininet_macro_recall_historical_formula"], 0.10982052839544458))
        self.assertTrue(math.isclose(summary["mininet_macro_f1"], 0.78679772491812))


if __name__ == "__main__":
    unittest.main()
