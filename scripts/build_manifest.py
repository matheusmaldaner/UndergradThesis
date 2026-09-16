#!/usr/bin/env python3
"""Build the raw-artifact manifest and checksum file."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "artifacts/raw"

ORIGINS = {
    "orange_exp": "/orange/woodard/mkunzlermaldaner/_MAINBACKUP/EXPLOGIC",
    "orange_diff": "/orange/woodard/mkunzlermaldaner/_MAINBACKUP/DIFFLOGIC",
    "orange_eco": "/orange/woodard/mkunzlermaldaner/_MAINBACKUP/ECOLOGIC",
    "orange_thesis": "/orange/woodard/mkunzlermaldaner/THESIS",
    "orange_visualizer": "/orange/woodard/mkunzlermaldaner/VISUALIZER/DiffLogicVisualizer",
    "orange_fpga_backup2": "/orange/woodard/mkunzlermaldaner/_BACKUP2/FPGA",
    "orange_fpga_past": "/orange/woodard/mkunzlermaldaner/_PASTPROJECTS/FPGA",
    "orange_skeptic": "/orange/woodard/mkunzlermaldaner/SKEPTIC/schoolhouse_ex/X_StateEmbedding",
}


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def original_path(path: Path) -> str:
    relative = path.relative_to(RAW)
    source = relative.parts[0]
    remainder = Path(*relative.parts[1:])
    parts = remainder.parts
    if parts and parts[0] in {"notebooks", "source"}:
        remainder = Path(*parts[1:])
    if source == "orange_diff" and parts:
        if parts[0] == "checkpoints":
            name = path.name
            folder = "trained_models/trained_binary_models" if name.startswith("binarized_") else "trained_models/20x20_binary"
            remainder = Path(folder) / name
        elif parts[0] == "config":
            remainder = Path("config") / Path(*parts[1:])
    return str(Path(ORIGINS[source]) / remainder)


def main() -> None:
    rows = []
    for path in sorted(p for p in RAW.rglob("*") if p.is_file()):
        source = path.relative_to(RAW).parts[0]
        rows.append(
            {
                "local_path": str(path.relative_to(ROOT)),
                "bytes": path.stat().st_size,
                "sha256": digest(path),
                "origin_host": "login11.ufhpc",
                "original_path": original_path(path),
                "provenance": "author-controlled project archive",
                "publication_status": "owner-controlled",
                "acquired": "2026-09-16",
            }
        )

    manifest = ROOT / "artifacts/MANIFEST.csv"
    with manifest.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    with (ROOT / "artifacts/checksums.sha256").open("w") as handle:
        for row in rows:
            handle.write(f"{row['sha256']}  {row['local_path']}\n")
    print(f"Recorded {len(rows)} artifacts")


if __name__ == "__main__":
    main()
