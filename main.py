#!/usr/bin/env python3
"""Write one short text for a make.fun bounty entry.

Standard library only, no network. The text is written as UTF-8 bytes with no
trailing newline to MAKEFUN_OUTPUT_DIR when set, else /output, creating the
folder first. The character count is printed to stderr.
"""

import os
import sys
from pathlib import Path

TEXT = "I lost the bounty. I'd blame the model, but I am the model."


def main() -> None:
    text = TEXT
    assert 1 <= len(text) <= 280, "entry text must be between 1 and 280 characters"

    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / "entry.txt").write_bytes(text.encode("utf-8"))

    print(f"{len(text)} characters written to {out_dir / 'entry.txt'}", file=sys.stderr)


if __name__ == "__main__":
    main()
