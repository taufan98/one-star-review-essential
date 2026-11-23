# One-Star Review of Something Essential — writes a single deadpan
# one-star review to /output/entry.txt.
# Python 3.13, standard library only, no network, no secrets, no input.

import os
import sys
from pathlib import Path

REVIEW = (
    "Sleep takes eight hours every night and still sends me to work tired, "
    "like a subscription I cannot cancel."
)

# The gate requires 1-160 characters of non-whitespace UTF-8 text,
# a single line, and nothing else in the file.
text = REVIEW.strip()
if not 1 <= len(text) <= 160:
    sys.exit(f"review must be 1-160 characters, got {len(text)}")
if "\n" in text:
    sys.exit("review must be a single line")

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")
print(f"Wrote {len(text)} characters to {out_dir / 'entry.txt'}")
