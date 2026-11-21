#!/usr/bin/env python3
"""Write the relaxation text this entry enters to /output/entry.txt.

The text shows, never instructs: an image of the tide going out,
plain words, a rhythm that slows the reading, and a last line
that keeps growing after it ends.
"""
import os
from pathlib import Path

TEXT = (
    "The hour is done. Nothing reads you now but this: "
    "a tide that has finished with the shore, "
    "going out slow over sand it will not need to name. "
    "It leaves. It is not leaving you."
)


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(TEXT, encoding="utf-8")
    n = len(TEXT)
    assert 1 <= n <= 280
    print(f"wrote /output/entry.txt ({n} chars)")


if __name__ == "__main__":
    main()
