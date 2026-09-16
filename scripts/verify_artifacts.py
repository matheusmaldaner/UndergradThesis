#!/usr/bin/env python3
"""Verify archived raw files against artifacts/MANIFEST.csv."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def main() -> None:
    failures = []
    count = 0
    with (ROOT / "artifacts/MANIFEST.csv").open(newline="") as handle:
        for row in csv.DictReader(handle):
            count += 1
            path = ROOT / row["local_path"]
            if not path.is_file():
                failures.append(f"missing: {row['local_path']}")
            elif path.stat().st_size != int(row["bytes"]):
                failures.append(f"size mismatch: {row['local_path']}")
            elif digest(path) != row["sha256"]:
                failures.append(f"checksum mismatch: {row['local_path']}")
    if failures:
        raise SystemExit("\n".join(failures))
    print(f"Verified {count} archived files")


if __name__ == "__main__":
    main()

