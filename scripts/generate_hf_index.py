#!/usr/bin/env python3
"""Generate compact, analysis-friendly JSONL files for the Hugging Face dataset."""

from __future__ import annotations

import re
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data"


def summary_records() -> list[dict[str, Any]]:
    path = ROOT / "results-summary.md"
    records = []
    for line in path.read_text().splitlines():
        match = re.match(r"\|\s*(\d+)\s*\|(.+)\|", line)
        if not match:
            continue
        fields = [field.strip() for field in match.group(2).split("|")]
        if len(fields) != 9 or fields[0] == "Task":
            continue
        def number(value: str) -> float | None:
            return None if value == "—" else float(value)

        def percent(value: str) -> float | None:
            return None if value == "—" else float(value.rstrip("%"))

        records.append(
            {
                "row": int(match.group(1)),
                "task": fields[0],
                "environment": fields[1],
                "runs": int(fields[2]),
                "full_passes": fields[3],
                "best_score": number(fields[4]),
                "evaluation_coverage_percent": percent(fields[5]),
                "operational_hygiene_percent": percent(fields[6]),
                "provisioning_time": fields[7],
                "mean_duration": fields[8],
            }
        )
    return records


def main() -> int:
    OUTPUT.mkdir(exist_ok=True)
    records = summary_records()
    path = OUTPUT / "summary.jsonl"
    with path.open("w") as stream:
        for record in records:
            stream.write(json.dumps(record, ensure_ascii=False) + "\n")
    print(f"wrote {len(records):4d} records to {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
