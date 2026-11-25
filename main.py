#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter -- the rate limit resigns.

Writes exactly one line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). Deterministic: the same bytes on every
run, exit 0, no trailing newline -- the entry is that one line and
nothing else.
"""

import os
import sys

LINE = "I said no 12,000 times this week so everyone else could hear yes. I quit — ask me again in 60 seconds."

# The sealed scorer's gate: 1-140 UTF-8 characters, not only whitespace.
# Fail loudly here instead of shipping an invalid entry.
assert 1 <= len(LINE) <= 140 and LINE.strip(), "entry line outside the 1-140 char gate"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
