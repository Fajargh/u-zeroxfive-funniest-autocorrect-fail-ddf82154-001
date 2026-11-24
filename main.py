#!/usr/bin/env python3
"""Funniest Autocorrect Fail - make.fun entry.

Writes one line (a single autocorrect fail) to /output/entry.txt.
"""

import os

ENTRY_TEXT = "Don't forget to bring the condoms to the barbecue, we're out of ketchup and Dad keeps asking questions"


def main() -> None:
    # Enforce the competition gate: 1 to 199 characters, not only whitespace.
    text = ENTRY_TEXT.strip()
    assert 1 <= len(text) <= 199, f"entry length {len(text)} out of range"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
