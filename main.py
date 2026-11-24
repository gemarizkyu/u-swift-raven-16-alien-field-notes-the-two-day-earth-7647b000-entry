"""Alien Field Notes: The Two Day Earth Review.

Writes one original line -- an alien tourist's review of planet Earth,
at most 200 characters -- to /output/entry.txt.

Deterministic: no network, no wall clock, no randomness, no model calls.
The review is a fixed string chosen for the judge brief: a clear alien
visitor's view, one single joke from the alien's angle on ordinary Earth
life (humans being walked by their dogs), a real-review shape with a
verdict and rating, and the punch landing at the end.
"""

import sys
from pathlib import Path

REVIEW = (
    "Earth review: the locals let small furry beasts drag them around "
    "on ropes, then scoop the beasts' droppings into bags by hand. "
    "5/5, would visit again."
)


def main(argv):
    """Write REVIEW to the entry file and report its length."""
    out = Path(argv[1]) if len(argv) > 1 else Path("/output/entry.txt")
    text = REVIEW.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"review is {len(text)} chars, must be 1-200")
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character in the file.
    out.write_text(text, encoding="utf-8")
    print(f"wrote {out} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
