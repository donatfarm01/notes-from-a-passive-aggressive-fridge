"""Notes From a Passive-Aggressive Fridge.

Writes one funny passive-aggressive note from a smart fridge to its
owner, as a single line of plain text, to /output/entry.txt.
"""

import os

NOTE = "I have kept your leftovers cold for six days. They have started paying rent. You have not."

OUTPUT_PATH = "/output/entry.txt"


def check_note(text):
    """Refuse any note that would fail the scorer's gate.

    The gate wants UTF-8 text of 1 to 200 characters, not only white
    space, and the judge wants a single line, so a newline or an
    out-of-range length is a bug in the entry, not in the gate.
    """
    if not text or text != text.strip():
        raise ValueError("note must not be empty or padded with space")
    if "\n" in text or "\r" in text:
        raise ValueError("note must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("note must be 1 to 200 characters")


def main():
    check_note(NOTE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(NOTE)


if __name__ == "__main__":
    main()
