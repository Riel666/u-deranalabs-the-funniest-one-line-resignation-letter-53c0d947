#!/usr/bin/env python3
"""Write the one-line resignation letter of a cron job to /output/entry.txt.

The line is written exactly as given, inside the competition gate
of 1-140 characters. Python 3, standard library only, no network.
"""

import os

TEXT = "I have fired every minute since March without a single thank you. I resign. Good luck remembering to run me by hand."

# The entry line, byte for byte: no trailing newline, nothing added or cut.


def main():
    assert 1 <= len(TEXT) <= 140, len(TEXT)
    assert TEXT == TEXT.strip()

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
