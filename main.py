#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes the entry -- one single-line safety warning label that should come
printed on every human being -- to /output/entry.txt.
"""

import os

ENTRY = "WARNING: Contains one (1) human. May spontaneously start a podcast, a diet, or a sentence it will never finish."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
