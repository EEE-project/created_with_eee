#!/usr/bin/env python3
"""Find vocab TSV translation collisions -- two different Greek words sharing
the same Translation value within one TSV, which makes that pair impossible
for a student to distinguish in a quiz/checker (the prompt shown is the
translation, so both words look like the "same" answer).

Scans every *.tsv file with a Word/Translation header. Odyssey/Kavafis
Ithaki's richer form/lemma/pos/context/meaning schema and Kapodistrias's
3-column Word/Translation/Type reference table are both still matched, since
each carries Word/Translation among its columns.

Found and fixed 2026-08-21 across ellinika_b and kapodistrias -- see
AGENTS.md's "Vocabulary TSV translation collisions" section for the
resolution priority (reuse the chapter's own richer translation first;
propose+confirm with the user if the source material itself collapsed it;
recognize genuine morphological doublets like κοιτάζω/κοιτάω as not an error).

Usage:
    python3 check-vocab-collisions.py             # scan the whole repo
    python3 check-vocab-collisions.py modern_greek/ellinika_b  # one course
"""
import argparse
import sys
from collections import defaultdict
from pathlib import Path


def find_collisions(path: Path) -> "list[tuple[str, list[str]]]":
    """Return [(translation, [word, ...]), ...] for every translation shared
    by 2+ distinct words in this TSV, or [] if the file has no Word/
    Translation header."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines:
        return []
    header = lines[0].split("\t")
    if "Word" not in header or "Translation" not in header:
        return []
    word_idx, tr_idx = header.index("Word"), header.index("Translation")

    by_translation = defaultdict(set)
    for line in lines[1:]:
        if not line.strip():
            continue
        cols = line.split("\t")
        if len(cols) <= max(word_idx, tr_idx):
            continue
        word, translation = cols[word_idx].strip(), cols[tr_idx].strip()
        if word and translation:
            by_translation[translation].add(word)

    return [(t, sorted(words)) for t, words in by_translation.items() if len(words) > 1]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("scope", nargs="?", default=".",
                         help="Directory to scan (default: whole repo from cwd)")
    args = parser.parse_args()

    root = Path(args.scope)
    if not root.is_dir():
        print(f"Not a directory: {root}", file=sys.stderr)
        sys.exit(1)

    tsv_files = sorted(p for p in root.rglob("*.tsv") if ".git" not in p.parts)
    total_collisions = 0
    for path in tsv_files:
        for translation, words in find_collisions(path):
            total_collisions += 1
            print(f"{path}: {translation!r} <- {words}")

    if total_collisions:
        print(f"\n{total_collisions} collision(s) found across {len(tsv_files)} TSV file(s)", file=sys.stderr)
        sys.exit(1)
    print(f"No collisions found across {len(tsv_files)} TSV file(s)")
    sys.exit(0)


if __name__ == "__main__":
    main()
