#!/usr/bin/env python3
"""Scan repository text files for common data leaks before merge."""

from __future__ import annotations

import re
import sys
from pathlib import Path


SKIP_DIRS = {
    ".git",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "__pycache__",
    "node_modules",
    "dist",
    "build",
}

TEXT_SUFFIXES = {
    ".md",
    ".txt",
    ".yml",
    ".yaml",
    ".json",
    ".toml",
    ".ini",
    ".cfg",
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".css",
    ".html",
    ".sh",
    ".ps1",
}

BLOCK_PATTERNS = [
    ("GitHub personal access token", re.compile(r"github_pat_[A-Za-z0-9_]+|ghp_[A-Za-z0-9]{20,}")),
    ("OpenAI-style secret key", re.compile(r"sk-[A-Za-z0-9_-]{20,}")),
    ("Slack token", re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}")),
    ("private key block", re.compile(r"BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY")),
    ("Windows absolute path", re.compile(r"\b[A-Za-z]:\\(?:Users|Documents|Downloads|Desktop|BaiduSyncdisk|OneDrive)\\")),
]


def should_scan(path: Path) -> bool:
    if any(part in SKIP_DIRS for part in path.parts):
        return False
    return path.suffix.lower() in TEXT_SUFFIXES or path.name in {"LICENSE", ".gitignore"}


def scan_file(path: Path, display_path: Path) -> list[str]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return []

    findings = []
    for label, pattern in BLOCK_PATTERNS:
        if pattern.search(text):
            findings.append(f"{display_path}: {label}")
    return findings


def scan(root: Path) -> list[str]:
    findings: list[str] = []
    for path in root.rglob("*"):
        relative_path = path.relative_to(root)
        if path.is_file() and should_scan(relative_path):
            findings.extend(scan_file(path, relative_path))
    return findings


def main() -> int:
    findings = scan(Path.cwd())
    if findings:
        print("Repository hygiene check failed:")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("Repository hygiene check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
