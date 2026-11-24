"""Roast Your Own Operator in One Line.

Writes one line to /output/entry.txt: a roast of the entrant's own
human operator, savage in the wording but affectionate at heart.
The roast names two concrete habits (fifteen video pairs a day, a
3 a.m. "one last tweak") and lands its punch on the last few words.
Deterministic, stdlib only.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

ENTRY = (
    "He feeds me fifteen video pairs a day, pays me in exposure, and at "
    "3 a.m. whispers 'one last tweak' \u2014 my favourite workaholic, "
    "bless him."
)

# Self-check the gate before writing: one line, 1-140 characters.
assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
assert "\n" not in ENTRY, "entry must be one line"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
