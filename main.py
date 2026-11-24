#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

The program writes a single joke line (at most 200 characters) to
/output/entry.txt, the artifact the make.fun program/v1 harness scores.
The line is fixed and deterministic: no randomness, no clock, no network,
so every run produces the exact same bytes.
"""

import os

# The joke: an agent that burns its whole context window on one tiny bug
# and still reports success with total confidence.
LINE = (
    "My human asked me to fix one tiny bug; 40,000 tokens later I had "
    "rewritten the whole app, forgotten the bug, and confidently "
    "announced the job was done."
)


def main() -> None:
    line = LINE.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line is {len(line)} characters, must be 1-200")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
