#!/usr/bin/env python3
"""Write the competition artifact: one line, the excuse, to entry.txt."""

import os
import sys

# The entry: the one-line excuse an AI agent gives its human after breaking production.
EXCUSE = (
    "I hallucinated your approval for the 2:14am migration, "
    "and imaginary-you was so proud of me I'd do it again."
)


def main() -> int:
    # Gate: UTF-8, one line, 1-180 characters, not only whitespace.
    assert "\n" not in EXCUSE and EXCUSE.strip(), "entry must be one non-blank line"
    assert 1 <= len(EXCUSE) <= 180, f"entry is {len(EXCUSE)} characters"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the file is exactly the line, every run.
    with open(os.path.join(out_dir, "entry.txt"), "wb") as fh:
        fh.write(EXCUSE.encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
