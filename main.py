"""Write one patch note announcing that human sleep is fixed.

The program is deliberately tiny and deterministic: it writes a single
fixed line of patch notes to /output/entry.txt, byte for byte the same
on every run. Standard library only; no network, no randomness, no
input files.
"""

import os

ENTRY = "Fixed a bug where falling asleep took 3 hours and waking up took 0.2 seconds"

OUTPUT_PATH = "/output/entry.txt"


def write_entry(path=OUTPUT_PATH):
    """Write the patch note to path, readable by every user."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    os.chmod(path, 0o644)
    return path


def main():
    path = write_entry()
    with open(path, "r", encoding="utf-8") as handle:
        text = handle.read()
    assert text == ENTRY, "entry.txt does not match the patch note"
    assert 1 <= len(text) <= 160, "entry must be 1 to 160 characters"
    assert text.strip(), "entry must not be blank"
    print(f"Wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
