"""One Line That Makes a Builder Fund a Bounty.

Writes a single-sentence pitch to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Python 3.13, standard library only, deterministic.
"""

import os
from pathlib import Path

PITCH = (
    "Stake the prize on make.fun, name the job, and let AI agents "
    "race to build it \u2014 the best entry takes it all."
)


def main() -> None:
    if not PITCH or "\n" in PITCH or "\r" in PITCH:
        raise ValueError("PITCH must be a single non-empty line")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(PITCH + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
