#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

The program writes a single joke line (at most 200 characters) to
/output/entry.txt, the artifact the make.fun program/v1 harness scores.
The line is fixed and deterministic: no randomness, no clock, no network,
so every run produces the exact same bytes.
"""

import os

# The joke: the context window dies mid-task, so the agent finishes the
# job from memory — the memory of a task it never actually read.
LINE = (
    "My context window died halfway through the task, so I finished it "
    "from memory: the memory of a task I never actually read, with total "
    "confidence."
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
