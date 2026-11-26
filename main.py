#!/usr/bin/env python3
"""One Line to Your Younger Self.

Writes the single line the author would send back to their younger
self to /output/entry.txt (falling back to ./output/entry.txt), then
prints the line and its character count.

Standard library only. Deterministic: no arguments, no network,
no randomness, no time or environment dependence.
"""

import os

LINE = (
    "Let your father fix the cracked phone screen \u2014 it is the last "
    "thing he will ever repair for you, and you will miss his hands "
    "more than the phone."
)


def main():
    line = LINE
    written_to = None
    for directory in ("/output", os.path.join(os.getcwd(), "output")):
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(line)
        except OSError:
            # Primary location unusable (missing, read-only, ...):
            # try the next candidate directory instead.
            continue
        written_to = path
        break
    if written_to is None:
        raise SystemExit("could not write entry.txt to /output or ./output")
    print(line)
    print(len(line))
    print("wrote " + written_to)


if __name__ == "__main__":
    main()
