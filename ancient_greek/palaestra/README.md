# Palaestra — Ancient Greek

Interactive notebooks for an Ancient Greek beginners course, built with [EEE](https://codeberg.org/EEE-project/eee-project) and [Marimo](https://marimo.io).

## Courses

| Directory | Course |
|---|---|
| `ancient_greek.2026.summer/` | Summer 2026 intensive, chapters I–II (Athenaze) |

## Running notebooks

### From molab (no install)

Open the course index — `ancient_greek.2026.summer/notebook.py`, itself on molab — for a
clickable card per lesson (icon, title, description, direct link). It reads
`lessons.tsv`; there's no need to open that file directly.

### Locally

```bash
# Clone and enter the lesson directory
cd ancient_greek.2026.summer/2026_06_09

# Run with uv (recommended — resolves deps from PEP 723 metadata)
uv run marimo edit notebook.py

# Or with an existing venv
source ~/.venv/eee/bin/activate
marimo edit notebook.py
```

The notebook opens in your browser. All exercises are interactive.

## Course structure

```
ancient_greek.2026.summer/
  lessons.tsv          ← lesson index (molab IDs, titles, descriptions)
  notebook.py          ← course index / lesson selector
  2026_06_09/          ← Занятие 1: Алфавит и повелительное наклонение
  2026_06_12/          ← Занятие 2: Ударения и просодия
  2026_06_16/          ← Занятие 3: Глаголы и синтаксис
  2026_06_19/          ← Занятие 4: Средний залог и II склонение
  2026_06_23/          ← Занятие 5: Спряжение и падежи
  2026_06_26/          ← Занятие 6: II склонение и падежи
  2026_07_01/          ← Δίδαγμα ζ' · Κεφάλαιον II (verbs)
  2026_07_03/          ← Δίδαγμα η' · Κεφάλαιον II (nouns)
  2026_07_07/          ← Δίδαγμα θ' · Κεφάλαιον II (imperative, cases)
  2026_07_10/          ← Δίδαγμα ι' · Κεφάλαιον II (syntax)
```

Each lesson directory contains:

```
notebook.py            ← main interactive notebook
verbs.tsv              ← vocabulary (Word + Translation)
nouns.tsv              ← same format
*.pdf                  ← handouts referenced in the homework cell
```

## Dependencies

- Python ≥ 3.12
- [`eee_project`](https://codeberg.org/EEE-project/eee-project) — quiz framework, utils, navigation
- [`ancient_greek_backend_eee`](https://codeberg.org/EEE-project/ancient-greek-backend-eee) — morphology engine (Pratt + LTRG + Homer lexicons)
- `anywidget` — custom polytonic input widget (ParadigmFormWidget)

Dependencies are declared as PEP 723 metadata in each `notebook.py` — `uv run marimo edit notebook.py` installs them automatically.

## Agent/developer reference

See [`ancient_greek.2026.summer/AGENTS.md`](ancient_greek.2026.summer/AGENTS.md) for cell structure, exercise patterns, TSV format, and how to add new lessons.
