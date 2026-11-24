"""One Word From Your Ex.

Writes exactly one word -- the word my ex would use to describe me --
to entry.txt in MAKEFUN_OUTPUT_DIR (fallback ".").
No trailing newline, no extra text.
"""
import os

# The word: "Detour".
# The ex's verdict on what I turned out to be -- not the destination,
# just the scenic route she took on the way to someone better.
# It lands instantly, it stings because it is true, and no near
# synonym ("sidetrack", "diversion") keeps the same edge. Six bytes.
WORD = "Detour"


def main():
    # Guard the gate: exactly one word, 1-24 characters, UTF-8.
    assert 1 <= len(WORD) <= 24 and " " not in WORD, WORD
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
