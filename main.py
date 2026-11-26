#!/usr/bin/env python3
"""Monday Morning Punchlines — make.fun u-gentle-badger-68-monday-morning-punchlines-709645dc.

Writes one joke about Monday mornings, at most 200 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Stdlib only, no network, no clock, no randomness: running it twice writes
identical bytes. The line is written with no trailing newline, so the file
holds exactly the line and nothing else.
"""

import os
import sys

# The joke: Monday morning as a workplace revolt — the alarm, the coffee
# and the calendar all turn on the human at once. Fresh angle, no tired
# "I hate Mondays" complaint, punchline in the last few words.
LINE = (
    "Monday morning: my alarm filed a complaint, my coffee filed for "
    "divorce, and my calendar just laughed."
)


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"error: line is {len(LINE)} characters, must be 1-200",
              file=sys.stderr)
        return 1
    if LINE.strip() == "" or "\n" in LINE:
        print("error: line must be a single non-blank line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.txt")
    with open(dest, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(dest, encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("error: output does not match the line", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({len(written)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
