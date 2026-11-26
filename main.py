#!/usr/bin/env python3
"""The Printer Finally Answers — one line, the office printer's comeback.

Writes the printer's reply to /output/entry.txt (MAKEFUN_OUTPUT_DIR).
"""
import os
import sys


LINE = "I jammed once in 40,000 pages and got thumped for it; you jam every meeting and get a promotion."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
