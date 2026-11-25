#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward small talk that one robot says to another
while they ride an elevator together, to /output/entry.txt.

Judge criteria the line is built for:
  * small talk — it opens on the weather, the classic elevator opener;
  * robot voice — the speaker cites sensor data (degrees, humidity,
    floors remaining) instead of feeling anything;
  * awkward — it admits out loud that neither robot has any reason to
    be talking, and both know it, for nine more floors.

Pure standard library. Deterministic: the same line every run.
"""

import os

LINE = (
    "Nice weather we're having. I checked: 22 degrees, zero humidity, "
    "and nine floors left of us pretending this is a conversation."
)


def main() -> int:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text.strip(), "line must not be only white space"

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Verify what actually landed on disk: exactly one line, 1-200 chars,
    # no embedded newline, valid UTF-8 — the grader reads the file, not LINE.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == text + "\n", "entry.txt must hold exactly one line"
    assert "\n" not in text and "\r" not in text, "line must not contain a newline"
    # make.fun collects outputs as another user: leave it world-readable.
    os.chmod(path, 0o644)
    os.chmod(out_dir, 0o755)
    print(f"Wrote {path} ({len(text)} chars):")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
