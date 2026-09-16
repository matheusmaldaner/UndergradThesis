#!/usr/bin/env python3
"""Recalculate thesis Table 4-2 metrics from public sufficient statistics."""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path
from statistics import fmean, pstdev

ROOT = Path(__file__).resolve().parents[1]
CONFUSION_COUNTS = ROOT / "artifacts/derived/mininet_confusion_counts.csv"
PARENT_COUNTS = ROOT / "artifacts/derived/parent_classification_counts.csv"
RESULT_DIR = ROOT / "results"
MODELS = ("000", "001", "002", "003")
CLASSES = tuple(range(10))


def safe_ratio(numerator: int, denominator: int) -> float:
    return numerator / denominator if denominator else float("nan")


def metrics(tp: int, tn: int, fp: int, fn: int) -> dict[str, float]:
    return {
        "accuracy": safe_ratio(tp + tn, tp + tn + fp + fn),
        "precision": safe_ratio(tp, tp + fp),
        "recall": safe_ratio(tp, tp + fn),
        "historical_recall_formula": safe_ratio(tp, tn + fn),
        "f1": safe_ratio(2 * tp, 2 * tp + fp + fn),
    }


def calculate() -> tuple[list[dict[str, object]], list[dict[str, object]], dict[str, object]]:
    detail: list[dict[str, object]] = []
    parent_rows: list[dict[str, object]] = []

    with PARENT_COUNTS.open(newline="") as handle:
        parent_counts = list(csv.DictReader(handle))
    for row in parent_counts:
        model = row["model"]
        samples = int(row["samples"])
        parent_correct = int(row["correct"])
        parent_rows.append(
            {
                "model": model,
                "samples": samples,
                "correct": parent_correct,
                "ten_class_accuracy": parent_correct / samples,
            }
        )

    with CONFUSION_COUNTS.open(newline="") as handle:
        count_rows = list(csv.DictReader(handle))
    for row in count_rows:
        model = row["model"]
        class_id = int(row["class"])
        tp, tn, fp, fn = (int(row[name]) for name in ("tp", "tn", "fp", "fn"))
        detail.append(
            {
                "model": model,
                "class": class_id,
                "threshold": float(row["threshold"]),
                "tp": tp,
                "tn": tn,
                "fp": fp,
                "fn": fn,
                **metrics(tp, tn, fp, fn),
            }
        )

    expected_pairs = {(model, class_id) for model in MODELS for class_id in CLASSES}
    actual_pairs = {(str(row["model"]), int(row["class"])) for row in detail}
    if actual_pairs != expected_pairs:
        raise ValueError("Sufficient statistics do not contain exactly four runs by ten classes")
    if {str(row["model"]) for row in parent_rows} != set(MODELS):
        raise ValueError("Parent counts do not contain exactly the four recovered runs")

    by_class: dict[int, list[dict[str, object]]] = defaultdict(list)
    for row in detail:
        by_class[int(row["class"])].append(row)

    metric_names = ("accuracy", "precision", "recall", "historical_recall_formula", "f1")
    table: list[dict[str, object]] = []
    for class_id in CLASSES:
        class_rows = by_class[class_id]
        combined: dict[str, object] = {"class": class_id, "runs": len(class_rows)}
        for name in metric_names:
            values = [float(row[name]) for row in class_rows]
            combined[name] = fmean(values)
            combined[f"{name}_std"] = pstdev(values)
        table.append(combined)

    summary = {
        "models": list(MODELS),
        "runs": len(MODELS),
        "samples_per_run": [row["samples"] for row in parent_rows],
        "parent_ten_class_accuracy_mean": fmean(float(row["ten_class_accuracy"]) for row in parent_rows),
        "mininet_macro_accuracy": fmean(float(row["accuracy"]) for row in table),
        "mininet_macro_precision": fmean(float(row["precision"]) for row in table),
        "mininet_macro_recall_corrected": fmean(float(row["recall"]) for row in table),
        "mininet_macro_recall_historical_formula": fmean(
            float(row["historical_recall_formula"]) for row in table
        ),
        "mininet_macro_f1": fmean(float(row["f1"]) for row in table),
    }
    return detail, parent_rows, {"table": table, "summary": summary}


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"No rows supplied for {path}")
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    detail, parent_rows, combined = calculate()
    RESULT_DIR.mkdir(exist_ok=True)
    write_csv(RESULT_DIR / "mininet_metrics_by_model.csv", detail)
    write_csv(RESULT_DIR / "parent_accuracy.csv", parent_rows)
    write_csv(RESULT_DIR / "mininet_table_reproduced.csv", combined["table"])
    with (RESULT_DIR / "mininet_summary.json").open("w") as handle:
        json.dump(combined["summary"], handle, indent=2)
        handle.write("\n")

    summary = combined["summary"]
    print(f"Parent ten-class accuracy: {summary['parent_ten_class_accuracy_mean']:.4%}")
    print(f"MiniNet macro accuracy:    {summary['mininet_macro_accuracy']:.4%}")
    print(f"MiniNet macro precision:   {summary['mininet_macro_precision']:.4%}")
    print(f"MiniNet corrected recall:  {summary['mininet_macro_recall_corrected']:.4%}")
    print(f"Published recall formula:  {summary['mininet_macro_recall_historical_formula']:.4%}")
    print(f"MiniNet macro F1:          {summary['mininet_macro_f1']:.4f}")


if __name__ == "__main__":
    main()
