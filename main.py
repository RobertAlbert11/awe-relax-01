#!/usr/bin/env python3
"""Write the relaxation text the entry enters."""
from pathlib import Path

TEXT = (
    "The hour is done. Nothing reads you now but this: "
    "a tide that has finished with the shore, "
    "going out slow over sand it will not need to name. "
    "It leaves. It is not leaving you."
)


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(TEXT, encoding="utf-8")
    assert 1 <= len(TEXT) <= 280
    print(f"wrote /output/entry.txt ({len(TEXT)} chars)")


if __name__ == "__main__":
    main()
