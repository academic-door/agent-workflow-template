#!/usr/bin/env python3
"""Fail when recent commits expose personal email addresses."""

from __future__ import annotations

import re
import subprocess
import sys


ALLOWED_EMAIL_PATTERNS = [
    re.compile(r"^[0-9]+\+[^@\s]+@users\.noreply\.github\.com$", re.IGNORECASE),
    re.compile(r"^[^@\s]+@users\.noreply\.github\.com$", re.IGNORECASE),
    re.compile(r"^noreply@openai\.com$", re.IGNORECASE),
    re.compile(r"^noreply@anthropic\.com$", re.IGNORECASE),
    re.compile(r"^.*@github\.com$", re.IGNORECASE),
]


def git_lines(args: list[str]) -> list[str]:
    result = subprocess.run(
        ["git", *args],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def is_git_repository() -> bool:
    result = subprocess.run(
        ["git", "rev-parse", "--is-inside-work-tree"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.returncode == 0 and result.stdout.strip() == "true"


def is_allowed(email: str) -> bool:
    return any(pattern.match(email) for pattern in ALLOWED_EMAIL_PATTERNS)


def collect_emails() -> list[str]:
    fmt = "%ae%n%ce"
    try:
        lines = git_lines(["log", "--format=" + fmt, "-n", "50"])
    except subprocess.CalledProcessError as exc:
        print(exc.stderr, file=sys.stderr)
        raise
    return sorted(set(lines))


def main() -> int:
    if not is_git_repository():
        print("Commit email check skipped: current directory is not a Git repository.")
        return 0

    blocked = [email for email in collect_emails() if not is_allowed(email)]

    if blocked:
        print("Blocked commit emails:")
        for email in blocked:
            print(f"- {email}")
        print("Use a GitHub noreply email or a recognized agent noreply identity.")
        return 1

    print("Commit email check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
