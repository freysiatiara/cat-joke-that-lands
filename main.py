"""One-line cat joke entry for the make.fun bounty
"The One-Line Cat Joke That Lands".

Writes a single one-line cat joke (under 200 characters) to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt).

Deterministic, stdlib only, no network, no randomness.
"""

import os
import sys

JOKE = "I told my cat he's adopted; he blinked slowly, which in cat means either 'I already knew' or 'you're fired.'"


def main() -> int:
    """Validate the joke and write it to entry.txt."""
    joke = JOKE
    if not joke or not joke.strip():
        print("error: joke is empty", file=sys.stderr)
        return 1
    if len(joke) > 200:
        print("error: joke exceeds 200 characters", file=sys.stderr)
        return 1
    if "\n" in joke or "\r" in joke:
        print("error: joke must be a single line", file=sys.stderr)
        return 1
    if joke != joke.strip():
        print("error: joke must not have leading/trailing whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(joke + "\n")
    os.chmod(path, 0o644)
    print(f"wrote {path} ({len(joke)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
