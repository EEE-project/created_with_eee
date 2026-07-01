# Palaestra — Ancient Greek

Interactive notebooks for an Ancient Greek beginners course, built with [EEE](https://codeberg.org/EEE-project/eee-project) and [Marimo](https://marimo.io).

## Courses

| Directory | Course |
|---|---|
| `ancient_greek.2026.summer/` | Summer 2026 intensive, chapters I–II (Athenaze) |

## Running notebooks

### From molab (no install)

Each lesson has a molab link in `lessons.tsv` → click the `nb_id` URL.

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
