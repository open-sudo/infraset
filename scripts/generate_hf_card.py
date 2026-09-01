#!/usr/bin/env python3
"""Create the Hugging Face dataset card from the execution summary."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = Path("/tmp/infraset-hf-card.md")
METADATA = """---
pretty_name: InfraSet
license: apache-2.0
language:
  - en
tags:
  - infrastructure
  - llm-evaluation
  - linux
  - systems-administration
task_categories:
  - other
size_categories:
  - n<1K
configs:
  - config_name: execution-summary
    data_files:
      - split: tasks
        path: data/execution-summary.jsonl
  - config_name: collector
    data_files:
      - split: observations
        path: data/collector-observations.jsonl
---

"""


def main() -> None:
    OUTPUT.write_text(METADATA + (ROOT / "results-summary.md").read_text())
    print(OUTPUT)


if __name__ == "__main__":
    main()
