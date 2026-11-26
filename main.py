#!/usr/bin/env python3
"""Entry for make.fun "The Dog Reviews the Mailman".

Writes one line to /output/entry.txt: the dog's review of the mailman.
Gate: UTF-8 text of 1 to 200 characters, not only whitespace.
Deterministic, no network, no randomness.
"""

import os

ENTRY = (
    "He only comes when my human is out, slips paper through the slot, "
    "and runs. She calls it the post. I call it a break-in."
)

MAX_CHARS = 200


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise SystemExit(f"entry is {len(ENTRY)} chars, gate is 1-{MAX_CHARS}")
    if not ENTRY.strip():
        raise SystemExit("entry is only whitespace")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != ENTRY:
        raise SystemExit("read-back mismatch")
    print(f"wrote {path}: {len(ENTRY)} characters")


if __name__ == "__main__":
    main()
