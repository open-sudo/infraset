#!/usr/bin/env python3
"""Copy the canonical Hugging Face dataset card to its upload location."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = Path("/tmp/infraset-hf-card.md")


def main() -> None:
    OUTPUT.write_text((ROOT / "docs" / "hf-dataset-card.md").read_text())
    print(OUTPUT)


if __name__ == "__main__":
    main()
