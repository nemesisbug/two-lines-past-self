#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun entry.

Writes the two-line warning to /output/entry.txt.

Line 1 warns the past self about one specific moment: saying yes to an
overtime shift on Christmas Eve. Line 2 traces the consequence: that one
yes cost the writer his daughter's first Christmas morning, and every
Christmas since has been spent trying to make up for a morning that
never comes back.
"""

import os

ENTRY = (
    "Don't say yes to the overtime shift on Christmas Eve just to prove you can handle it.\n"
    "That one yes meant you missed your daughter's first Christmas morning, "
    "and you have spent every Christmas since trying to make up for a morning that never comes back.\n"
)


def main() -> None:
    # Gate: the entry must be UTF-8 text of 1 to 280 characters, two lines.
    text = ENTRY.rstrip("\n")
    assert 1 <= len(text) <= 280, f"entry is {len(text)} chars, must be 1-280"
    assert text.count("\n") == 1, "entry must be exactly two lines"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
