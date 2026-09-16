#!/usr/bin/env python3
"""Fail if common credential forms appear in files intended for Git."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATTERNS = {
    "OpenAI API key": re.compile(rb"sk-[A-Za-z0-9_-]{20,}"),
    "AWS access key": re.compile(rb"(?<![A-Z0-9])(?:AKIA|ASIA)[A-Z0-9]{16}(?![A-Z0-9])"),
    "GitHub token": re.compile(
        rb"(?<![A-Za-z0-9_])(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})"
    ),
    "private key": re.compile(rb"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----"),
}


def scan_worktree() -> list[str]:
    findings: list[str] = []
    checked = 0
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        checked += 1
        data = path.read_bytes()
        for label, pattern in PATTERNS.items():
            if pattern.search(data):
                findings.append(f"{label}: {path.relative_to(ROOT)}")
    print(f"Checked {checked} working-tree files")
    return findings


def scan_git_history() -> list[str]:
    findings: list[str] = []
    object_lines = subprocess.check_output(
        ["git", "rev-list", "--objects", "--all"], cwd=ROOT, text=True
    ).splitlines()
    blobs: dict[str, str] = {}
    for line in object_lines:
        object_id, separator, path = line.partition(" ")
        if not separator or object_id in blobs:
            continue
        object_type = subprocess.check_output(
            ["git", "cat-file", "-t", object_id], cwd=ROOT, text=True
        ).strip()
        if object_type == "blob":
            blobs[object_id] = path

    for object_id, path in blobs.items():
        data = subprocess.check_output(["git", "cat-file", "blob", object_id], cwd=ROOT)
        for label, pattern in PATTERNS.items():
            if pattern.search(data):
                findings.append(f"{label}: historical blob {object_id} ({path})")
    print(f"Checked {len(blobs)} historical Git blobs")
    return findings


def main() -> None:
    findings = scan_worktree()
    if "--git-history" in sys.argv[1:]:
        findings.extend(scan_git_history())
    if findings:
        raise SystemExit("Sensitive strings found:\n" + "\n".join(findings))
    print("No sensitive strings found")


if __name__ == "__main__":
    main()
