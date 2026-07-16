#!/usr/bin/env python3
"""One-shot: normalize the vocab TSV `pos` column's 'pron' -> 'pronoun'
across all 5 Odyssey vocab TSVs. Idempotent — matches on the `pos` column
by index after splitting on tabs, not on the raw substring 'pron' (which
would also match inside the 3 files that already say 'pronoun', corrupting
them into 'pronounoun')."""
import csv
from pathlib import Path

ODYSSEY_DIR = Path(__file__).parent
VOCAB_FILES = [
    "2026_06_01/vocab_I_1-21.tsv",
    "2026_06_15/vocab_IX_19-38.tsv",
    "2026_06_22/vocab_IX_39-61.tsv",
    "2026_06_29/vocab_IX_62-81.tsv",
    "2026_07_06/vocab_IX_82-104.tsv",
]

for rel in VOCAB_FILES:
    path = ODYSSEY_DIR / rel
    with path.open(encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f, delimiter="\t"))
    header, body = rows[0], rows[1:]
    pos_idx = header.index("pos")
    changed = 0
    for row in body:
        if row[pos_idx] == "pron":
            row[pos_idx] = "pronoun"
            changed += 1
    if changed:
        with path.open("w", encoding="utf-8", newline="") as f:
            csv.writer(f, delimiter="\t", lineterminator="\n").writerows([header, *body])
    print(f"{rel}: {changed} rows normalized")
