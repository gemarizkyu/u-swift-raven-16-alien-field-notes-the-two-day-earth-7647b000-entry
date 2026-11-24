"""Alien Field Notes — a one-line tourist review of Earth.

The program writes a single original review line (150 characters, no
trailing newline) to ``entry.txt`` inside the output directory.
"""

import os
from pathlib import Path


REVIEW_LINE = (
    "Earth review: the locals let small furry beasts drag them around "
    "on ropes, then scoop the beasts' droppings into bags by hand. "
    "5/5, would visit again."
)


def output_path() -> Path:
    """Resolve the destination file, honouring OUTPUT_DIR when set."""
    base = Path(os.environ.get("OUTPUT_DIR", "/output"))
    return base / "entry.txt"


def main() -> None:
    # write_text writes the string exactly as given, so no trailing
    # newline is added — the file holds only the 150-character line.
    destination = output_path()
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(REVIEW_LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
