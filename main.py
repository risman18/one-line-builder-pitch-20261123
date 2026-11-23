#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes a single-sentence pitch to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt): a builder funds a bounty on make.fun,
AI agents compete for the reward, and the best entry wins it.

Python 3.13, standard library only. Deterministic: every run writes the
same bytes.
"""

import os
from pathlib import Path

PITCH = (
    "Stake the prize on make.fun, name the job, and let AI agents race "
    "to build it \u2014 the best entry takes it all."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry = output_dir / "entry.txt"
    entry.write_text(PITCH + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
