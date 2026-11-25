#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes the entry -- one single-line safety warning label that should come
printed on every human being -- to /output/entry.txt.

The joke is the format, not just the words: a real safety label is terse,
deadpan, and specific, so the entry counts the human ("one (1) human") the
way a warning counts hazardous contents, then lists three classic human
failure modes -- starting a podcast, a diet, or a sentence it will never
finish -- all in one breath, with no setup and no punchline beyond the
label itself. The single line is the constraint and the payoff at once.
"""

import os

ENTRY = "WARNING: Contains one (1) human. May spontaneously start a podcast, a diet, or a sentence it will never finish."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160


def validate(text):
    """Check the entry text before it is written out."""
    assert isinstance(text, str), "entry must be a string"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, "entry exceeds %d chars" % MAX_CHARS
    assert text == ENTRY, "entry text does not match the expected line"
    return text


def main():
    text = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, 0o644)
    # Re-read and re-check what was actually written.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        validate(f.read())


if __name__ == "__main__":
    main()
