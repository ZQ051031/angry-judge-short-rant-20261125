#!/usr/bin/env python3
"""One-line rant for the Angry Judge short-rant contest.

Running this script produces the contest entry: a single angry-judge
rant, written to /output/entry.txt. Only the standard library is used,
so there is nothing to install.
"""

from pathlib import Path

# The rant is kept as separate sentences so each beat of the joke is
# easy to read and to tweak on its own. Joined with single spaces they
# form exactly one line, as the contest gate requires.
SENTENCES = [
    "The self-checkout just flagged an 'unexpected item in the bagging area.'",
    "The unexpected item is my groceries, in the bagging area, doing exactly what groceries do.",
    "I came here to buy milk, not to be performance-reviewed by a robot that sounds disappointed in me.",
]

OUTPUT_PATH = Path("/output/entry.txt")


def build_rant() -> str:
    """Join the sentences into the single entry line."""
    return " ".join(SENTENCES)


def write_entry() -> str:
    """Write the rant to the output file, checking the length gate first.

    Returns the rant that was written, so callers can inspect it.
    """
    rant = build_rant()
    if not 1 <= len(rant) <= 400:
        raise ValueError(f"rant must be 1-400 characters, got {len(rant)}")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(rant + "\n", encoding="utf-8")
    return rant


def main() -> None:
    rant = write_entry()
    print(f"Wrote {len(rant)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
