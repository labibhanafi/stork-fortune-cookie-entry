#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers — entry writer.

Writes one fortune-cookie line for a software engineer to
/output/entry.txt. Fully deterministic: no input, no network, no
randomness, no time dependence. The text is a single line of
71 characters, within the 1-120 character gate.
"""

import os

ENTRY = "Your code will outlive you, but only because no one dares to delete it."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not (1 <= len(ENTRY) <= 120):
        raise ValueError("entry must be 1-120 characters, got %d" % len(ENTRY))
    if ENTRY.strip() != ENTRY or "\n" in ENTRY:
        raise ValueError("entry must be a single non-padded line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # Verify the file round-trips byte-identical before exiting.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("round-trip mismatch: wrote %r" % written)


if __name__ == "__main__":
    main()
