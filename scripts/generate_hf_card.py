#!/usr/bin/env python3
"""Create the Hugging Face README from the clean GitHub execution summary."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = Path("/tmp/infraset-hf-card.md")
METADATA = """---
pretty_name: InfraSet execution summary
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
  - config_name: summary
    data_files:
      - split: summary
        path: data/summary.jsonl
---

"""


def main() -> None:
    OUTPUT.write_text(METADATA + (ROOT / "results-summary.md").read_text())
    print(OUTPUT)


if __name__ == "__main__":
    main()
