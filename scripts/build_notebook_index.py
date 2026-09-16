#!/usr/bin/env python3
"""Build a searchable inventory of archived and reconstructed notebooks."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEARCH_ROOTS = (ROOT / "artifacts/raw", ROOT / "artifacts/sanitized")
OUTPUT = ROOT / "artifacts/NOTEBOOK_INDEX.csv"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    rows: list[dict[str, object]] = []
    for search_root in SEARCH_ROOTS:
        if not search_root.exists():
            continue
        for path in sorted(search_root.rglob("*.ipynb")):
            try:
                notebook = json.loads(path.read_text())
                parse_status = "valid-json"
                parse_error = ""
            except (UnicodeDecodeError, json.JSONDecodeError) as error:
                notebook = {}
                parse_status = "invalid-notebook"
                parse_error = type(error).__name__
            cells = notebook.get("cells", [])
            code_cells = [cell for cell in cells if cell.get("cell_type") == "code"]
            executed = [cell for cell in code_cells if cell.get("execution_count") is not None]
            with_outputs = [cell for cell in code_cells if cell.get("outputs")]
            kernelspec = notebook.get("metadata", {}).get("kernelspec", {})
            rows.append(
                {
                    "path": str(path.relative_to(ROOT)),
                    "archive_kind": search_root.name,
                    "bytes": path.stat().st_size,
                    "sha256": sha256(path),
                    "parse_status": parse_status,
                    "parse_error": parse_error,
                    "nbformat": notebook.get("nbformat", ""),
                    "kernel_name": kernelspec.get("name", ""),
                    "kernel_display_name": kernelspec.get("display_name", ""),
                    "cells": len(cells),
                    "code_cells": len(code_cells),
                    "executed_code_cells": len(executed),
                    "code_cells_with_outputs": len(with_outputs),
                }
            )
    if not rows:
        raise RuntimeError("No notebooks found")
    with OUTPUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Indexed {len(rows)} notebooks")


if __name__ == "__main__":
    main()
