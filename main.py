#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry program.

Writes one short rant (a single line, 1-400 characters) to /output/entry.txt.
Python standard library only.
"""

import os

ENTRY = (
    "The self-checkout just flagged an 'unexpected item in the bagging area.' "
    "The unexpected item is my groceries, in the bagging area, doing exactly "
    "what groceries do. I came here to buy milk, not to be performance-reviewed "
    "by a robot that sounds disappointed in me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
