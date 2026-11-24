#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun bounty entry.

Writes a single line (under 200 characters) that reads as a funny
autocorrect fail to /output/entry.txt.
"""

import os

ENTRY = (
    "I meant to text my date 'can't wait to see you' — autocorrect sent "
    "'can't wait to sue you', and now I'm single and possibly in court."
)


def main() -> None:
    # The bounty requires a single line under 200 characters.
    assert len(ENTRY) < 200, f"entry too long: {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
