#!/usr/bin/env python3
"""Swap tables for charts where a chart carries the same numbers better.

The article is authored with tables so the artifact stays self-contained. In
the published Markdown a chart says the same thing more clearly, so the tables
it replaces are removed rather than printed twice.

Usage:  insert_article_charts.py <findings.md> <raw-image-base-url>
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# (chart file, alt text, regex spanning the block the chart replaces)
REPLACEMENTS = [
    (
        "fail-rate-by-release.png",
        "Command fail rate by release",
        re.compile(
            r"\*\*RHEL\*\*\n\n<table.*?</table>\n\n\*\*Ubuntu\*\*\n\n<table.*?</table>",
            re.S,
        ),
    ),
    (
        "clustered-sleep.png",
        "Time spent working versus asleep, clustered-services",
        re.compile(
            r"\*\*clustered-services, by image\*\*\n\n<table.*?</table>", re.S
        ),
    ),
]

# (chart file, alt text, anchor the chart is placed above and which stays)
ADDITIONS: list[tuple[str, str, str]] = []


def main() -> int:
    document = Path(sys.argv[1])
    base = sys.argv[2].rstrip("/")
    text = document.read_text()

    for image, alt, pattern in REPLACEMENTS:
        text, count = pattern.subn(f"![{alt}]({base}/{image})", text, count=1)
        if not count:
            raise SystemExit(f"no match for {image}")

    for image, alt, anchor in ADDITIONS:
        if anchor not in text:
            raise SystemExit(f"anchor missing for {image}")
        text = text.replace(anchor, f"![{alt}]({base}/{image})\n\n{anchor}", 1)

    document.write_text(text)
    print(f"charts placed: {len(REPLACEMENTS)} replacing tables, {len(ADDITIONS)} added")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
