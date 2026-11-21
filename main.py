#!/usr/bin/env python3
"""Write the relaxation text this entry enters to /output/entry.txt.

The text shows, never instructs: plain gentle images that slow the
reader down without telling them to slow down.
"""
import os
from pathlib import Path

TEXT = (
    "A window left open a little. Night air moves the curtain once, "
    "slowly, the way a wave remembers the shore. Somewhere a fridge "
    "hums its one low note and the house leans into it. "
    "Everything here has already been put down."
)


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    n = len(TEXT)
    if not 1 <= n <= 280:
        raise SystemExit(f"entry text is {n} chars, must be 1-280")
    (out / "entry.txt").write_text(TEXT, encoding="utf-8")
    print(f"wrote {out/'entry.txt'} ({n} chars)")


if __name__ == "__main__":
    main()
