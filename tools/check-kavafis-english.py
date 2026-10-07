#!/usr/bin/env python3
"""Check the English data of the Kavafis «Ithaka» lessons against their Russian counterparts and the Greek stanza.

For each lesson (1, 2, 3, 4) of kavafis_ithaki:
  * every `X_en.tsv` mirrors `X.tsv` -- same header, same rows in the same order on the key columns
    (Word, plus Type for vocabulary.tsv; form/lemma/pos/context for poem_vocab.tsv), a non-empty gloss
    (Translation, or meaning for poem_vocab.tsv) and no Cyrillic;
  * `language_notes.tsv` -- the comments of the "A mixed poetic language" cell -- has the columns fragments/ru/el/en (fragments: runs of the poem's own
    words, separated by " | "; selecting the comment highlights them), no empty cell, no Cyrillic in `el`/`en`, no note repeating its fragments at the
    start, every fragment found in greek.md, and no word of the poem claimed by two fragments (eee_project's `language_notes_problems`: the
    matcher the page itself uses);
  * `translations_en.md`, parsed with eee_project's own parsers (what the notebooks run), has exactly the
    translators `literal` and `Valassopoulo`, each with one block headed by the Greek stanza's ref and exactly the
    Greek stanza's line count; `literal`, `Valassopoulo` and `Keeley/Sherrard` each carry a `<!-- **...** -->`
    description; the file has no Cyrillic and no Greek echo comments; the `literal` description makes no provenance
    claim that cannot be certified ("not taken from ...", "word-for-word"); the `Valassopoulo` description names a
    jurisdiction for "public domain" (the KB's basis is the US); `## Keeley/Sherrard` holds only its description;
  * with --kb: each block equals the same block of the KB's translations_en.md (Greek echo lines dropped).

Usage (repo root, EEE venv):
    ~/.venv/eee/bin/python3 tools/check-kavafis-english.py [KAVAFIS_DIR] [--kb PATH_TO_KB_translations_en.md]
Exit status 1 on any problem.
"""
import argparse
import csv
import re
import sys
from pathlib import Path

from eee_project import language_notes_problems, parse_stanza_text, parse_stanza_translations, strip_comment_lines

DEFAULT_DIR = Path(__file__).resolve().parent.parent / "modern_greek/b1greeklanguageandculture/kavafis_ithaki"
LESSONS = ["1", "2", "3", "4"]
TSV_KEYS = {  # file stem -> (key columns, gloss column)
    "vocabulary": (["Word", "Type"], "Translation"),
    "nouns": (["Word"], "Translation"),
    "verbs": (["Word"], "Translation"),
    "adjectives": (["Word"], "Translation"),
    "poem_vocab": (["form", "lemma", "pos", "context"], "meaning"),
}
NOTES_COLUMNS = ["fragments", "ru", "el", "en"]
ENGLISH_TRANSLATORS = ["literal", "Valassopoulo"]
DESCRIBED = ["literal", "Valassopoulo", "Keeley/Sherrard"]
UNVERIFIABLE = ("not taken from", "not copied", "not adapted", "word-for-word")  # `literal` reorders words; its independence cannot be certified
CYR = re.compile(r"[Ѐ-ӿ]")


def read_rows(path):
    with path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        return reader.fieldnames, list(reader)


def check_tsvs(lesson_dir, problems):
    for stem, (keys, gloss) in TSV_KEYS.items():
        ru, en = lesson_dir / f"{stem}.tsv", lesson_dir / f"{stem}_en.tsv"
        if not ru.exists():
            continue
        if not en.exists():
            problems.append(f"{en}: missing (the Russian {ru.name} exists)")
            continue
        ru_header, ru_rows = read_rows(ru)
        en_header, en_rows = read_rows(en)
        if en_header != ru_header:
            problems.append(f"{en.name}: header {en_header} != {ru_header}")
            continue
        if len(en_rows) != len(ru_rows):
            problems.append(f"{en.name}: {len(en_rows)} rows, {ru.name} has {len(ru_rows)}")
        for n, (r, e) in enumerate(zip(ru_rows, en_rows), start=2):
            if [r[k] for k in keys] != [e[k] for k in keys]:
                problems.append(f"{en.name} line {n}: key columns differ from {ru.name}: {[e[k] for k in keys]} != {[r[k] for k in keys]}")
            if not (e[gloss] or "").strip():
                problems.append(f"{en.name} line {n}: empty {gloss}")
            elif CYR.search(e[gloss]):
                problems.append(f"{en.name} line {n}: Cyrillic in {gloss}: {e[gloss]!r}")


def check_language_notes(lesson_dir, problems):
    path = lesson_dir / "language_notes.tsv"
    if not path.exists():
        problems.append(f"{path}: missing")
        return
    header, rows = read_rows(path)
    if header != NOTES_COLUMNS:
        problems.append(f"{path.name}: header {header} != {NOTES_COLUMNS}")
        return
    greek = parse_stanza_text((lesson_dir / "greek.md").read_text(encoding="utf-8"))
    for n, row in enumerate(rows, start=2):
        for column in NOTES_COLUMNS:
            if not (row[column] or "").strip():
                problems.append(f"{path.name} line {n}: empty {column}")
        for lang in ("el", "en"):
            if CYR.search(row[lang] or ""):
                problems.append(f"{path.name} line {n}: Cyrillic in {lang}")
        fragments = [f for f in (row["fragments"] or "").split(" | ") if f.strip()]
        lead = " · ".join(fragments)
        for lang in ("ru", "el", "en"):
            if lead and (row[lang] or "").startswith(lead):
                problems.append(f"{path.name} line {n}: the {lang} note repeats its fragments at the start (the card already shows them in bold)")
    # eee_project's own matcher: what the page would leave unhighlighted
    for p in language_notes_problems([line for lines in greek.values() for line in lines], rows):
        n, fragment = p["row"] + 2, p["fragment"]
        if p["problem"] == "overlaps":
            held = "an earlier fragment of the same line" if p["holder"] == p["row"] else f"line {p['holder'] + 2}"
            problems.append(f"{path.name} line {n}: fragment {fragment!r} overlaps a word already claimed by {held}")
        else:
            problems.append(f"{path.name} line {n}: fragment {fragment!r} is not in greek.md")


def check_translations(lesson_dir, kb_trans, problems):
    path = lesson_dir / "translations_en.md"
    if not path.exists():
        problems.append(f"{path}: missing")
        return
    text = path.read_text(encoding="utf-8")
    greek = parse_stanza_text((lesson_dir / "greek.md").read_text(encoding="utf-8"))
    trans, desc = parse_stanza_translations(text)
    if sorted(trans) != sorted(ENGLISH_TRANSLATORS):
        problems.append(f"{path.name}: translators {sorted(trans)} != {sorted(ENGLISH_TRANSLATORS)}")
    for name in DESCRIBED:
        if name not in desc:
            problems.append(f"{path.name}: `## {name}` has no `<!-- **...** -->` description")
    for phrase in UNVERIFIABLE:
        if phrase in desc.get("literal", ""):
            problems.append(f"{path.name}: `literal` description makes a provenance claim ({phrase!r}) that cannot be certified")
    if re.search(r"public domain(?! in the US)", desc.get("Valassopoulo", "")):
        problems.append(f"{path.name}: `Valassopoulo` description says public domain without a jurisdiction (the KB's basis is the US)")
    keeley = re.search(r"(?ms)^## Keeley/Sherrard\n(.*?)(?=^## |\Z)", text)
    if keeley and [ln for ln in keeley.group(1).splitlines()
                   if ln.strip() and ln.strip() != "---" and not (ln.startswith("<!-- **") and ln.endswith("-->"))]:
        problems.append(f"{path.name}: `## Keeley/Sherrard` must hold only its description (the translation is in copyright)")
    if CYR.search(text):
        problems.append(f"{path.name}: contains Cyrillic")
    if "<!-- el:" in text:
        problems.append(f"{path.name}: contains Greek echo comments (only the KB file carries them)")
    for name in ENGLISH_TRANSLATORS:
        blocks = trans.get(name, {})
        if list(blocks) != list(greek):
            problems.append(f"{path.name} `{name}`: blocks {list(blocks)} != Greek stanza {list(greek)}")
            continue
        for ref, lines in greek.items():
            got = blocks[ref].split("\n")
            if len(got) != len(lines):
                problems.append(f"{path.name} `{name}` {ref}: {len(got)} lines, the Greek has {len(lines)}")
            if kb_trans is not None:
                kb_text = strip_comment_lines(kb_trans.get(name, {}).get(ref, ""))
                if blocks[ref] != kb_text:
                    problems.append(f"{path.name} `{name}` {ref}: differs from the KB's translations_en.md")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("kavafis_dir", nargs="?", default=str(DEFAULT_DIR))
    parser.add_argument("--kb", help="the KB's texts/kavafis_ithaki/translations_en.md, to compare the lesson copies with")
    args = parser.parse_args()
    root = Path(args.kavafis_dir)
    kb_trans = parse_stanza_translations(Path(args.kb).read_text(encoding="utf-8"))[0] if args.kb else None
    problems = []
    for lesson in LESSONS:
        check_tsvs(root / lesson, problems)
        check_translations(root / lesson, kb_trans, problems)
        check_language_notes(root / lesson, problems)
    for p in problems:
        print(p)
    print(f"{len(problems)} problem(s) across {len(LESSONS)} lessons")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
