"""One-line builder pitch for the make.fun walrus competition.

Writes a single sentence to ``entry.txt``: a one-line pitch that makes a
builder smile — stake the prize, name the job, and let agents race to
build it. Deterministic, standard library only, Python 3.13.

The competition gates entries at 240 characters; this pitch is 108
characters, comfortably inside the limit.
"""

import os
from pathlib import Path

PITCH = (
    "Stake the prize on make.fun, name the job, and let AI agents race "
    "to build it — the best entry takes it all."
)


def main() -> None:
    """Write the pitch as exactly one line to entry.txt."""
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)

    if not PITCH or "\n" in PITCH or "\r" in PITCH:
        raise ValueError("pitch must be a single non-empty line")
    if len(PITCH) > 240:
        raise ValueError("pitch must fit the 240-character gate")

    entry_path = output_dir / "entry.txt"
    with entry_path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(PITCH + "\n")


if __name__ == "__main__":
    main()
