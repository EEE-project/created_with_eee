# Odyssey Notebooks — Agent Reference

## Directory layout

```
odyssey/
  lessons.tsv          # lesson index (title, url, date)
  notebook.py          # index/parent notebook
  2026_06_22/          # Lesson: Od. IX.39–61
  2026_06_15/          # Lesson: Od. IX.19–38
  2026_06_01/          # Lesson: Od. I.1–21
```

Each lesson directory:

```
notebook.py
greek.md                   ← Greek source text (do NOT hardcode in notebook)
translations_ru.md         ← literary translations, incl. подстрочник gloss (do NOT hardcode)
vocab_{ref}.tsv            ← vocabulary for the quiz
vocab_content_problems.md  ← known coverage gaps (read before adding TSV entries)
```

`2026_06_01` only: the interlinear gloss lives as a `## подстрочник` section inside
`translations_ru.md` (merged 2026-07-10). The other 4 lessons haven't been migrated
yet and still carry a separate `interlenear_ru.md` alongside `translations_ru.md` —
same rules as documented below for whichever structure a given lesson currently has.

---

## Source discipline — CRITICAL

**Base every cell on the lecture's own materials in
`~/work/greek/lectures/Odyssey/<date>/`** — the presentation PDF (`Одиссея N.pdf` /
`Od_IX_*.pdf`), **`notes.md`**, the vocab `*.docx/.md`, and the images/diagrams in
the presentation. **`notes.md` is a valid source — transcribe / distill it** (that
is how the День-4 lotus material got in).

**Do not do your own research beyond these files** — no web search, no invented
proverbs / etymologies / historical asides / cross-references. **If research seems
useful — or `notes.md` itself raises a question or points at a line of inquiry —
ASK the user first; don't research or add it on your own.** (User rules,
2026-07-07: *"use the lecture materials and notes as the basis; ask me if you want
to research something — e.g. if the notes suggest it."*)

- **Greek / interlinear / translations** (`greek.md`, `translations_ru.md` — the
  latter's `## подстрочник` section is the interlinear gloss, see below) —
  transcribe from the presentation slides only.
- **Rhythm (икты)** — transcribe the presentation's colour-marked stressed
  syllables faithfully (render red in the notebook); don't re-derive scansion.
- **Images** — extract the presentation's own pictures/diagrams and wire them.
- **Materials cell + `ensure_file`** — link every PDF the lecture uses
  (presentation + vocab); if a vocab PDF doesn't exist, ship the `.docx`.
  Clean ASCII names (`Od_IX_NN-MM.pdf`, `Od_IX_NN-MM_vocabula.{pdf,docx}`).
  Commit all of them.
- **Lexicon labels** — name a composite lexicon by what it is, not one component:
  "Словарь классического аттического (pratt + ltrg + lsj)", never "LSJ".

---

## Notebook cell structure (visual order, top → bottom)

Identify cells by content, not by ID — IDs change after each save.

### Visible cells

| content / first line | role |
|---|---|
| `eee_topbar(mo, ...)` | EEE navigation bar |
| `mo.md("# Одиссея…")` + image | title, molab badge, lesson image |
| `**Материалы занятия:**` PDF links | materials links |
| `## Слова, слова…` | per-lesson vocabulary notes (optional section) |
| `## Текст поэмы с параллельными переводами` | section separator |
| `_MURRAY = (...)` | Murray 1919 source citation (HTML) |
| `Икты (ударные слоги)…` | explanation of stress marks in poem display |
| `_st_map = {s["ref"]: s for s in STANZAS}` | interactive poem display |
| `SHOW_COVERAGE = mo.ui.radio(...)` | coverage highlight toggle |
| `## Упражнение: словарная форма` | section separator |
| `filter_mode = mo.ui.radio(...)` | lexicon filter for quiz words |
| `mo.hstack([..., next_btn])` | progress counter + next button |
| `answer_radio = mo.ui.radio(...)` | quiz question |
| `mo.stop(cv() is None)` + feedback | quiz feedback |
| `### О проверке форм (EEE)` | EEE system explanation |

### Hidden cells (below visible area, order not significant for UI)

| key line | role |
|---|---|
| `cv, set_cv = mo.state(None)` | quiz state: current word, score, remaining list |
| `stanza_selector = mo.ui.dropdown(...)` | stanza picker |
| `trans_selector = mo.ui.dropdown(...)` | translation picker |
| `next_btn = mo.ui.button(...)` | advance/restart button |
| `def _record_answer()` | click handler, quiz advance logic |
| `def _parse_greek(md)` | text parsers + `STANZAS` list builder |
| `import csv` / `QUIZ_WORDS_RAW = gu.resolve_word_grammar(...)` | vocab TSV loader |
| `def _has_displayable_form(w)` | filter helpers (`QUIZ_WORDS`) |
| `import unicodedata` / `WORDS_COMBINED` | coverage normalization |
| `build_paradigm_table = eee.build_grc_paradigm_table(...)` | paradigm + lexicon tab builders |
| `import marimo as mo` / backend init | all imports, `ag_backend`, `um_backend`, `gu` |
| `NB_DIR = ...` / `gu.ensure_file(...)` | paths + remote file sync |
| `eee_footer(mo, ...)` | EEE footer |

---

## CRITICAL: Text from `.md` files, never hardcoded

Greek text and translations (incl. the interlinear gloss, see below) live in two
Markdown files read at runtime by the `_parse_*` functions. Never copy poem
lines or translations into Python cells.

### `greek.md` — Greek source text (Murray 1919)

```markdown
<!-- Murray 1919 · https://... -->

### Odyss. IX.39–42

Ἰλιόθεν με φέρων ἄνεμος Κικόνεσσι πέλασσεν,
Ἰσμάρῳ· ἔνθα δ' ἐγὼ πόλιν ἔπραθον, ὤλεσα δ' αὐτούς.
...
```

Rules: `### Odyss. X.XX–XX` → stanza ref key (stripped of the 11-char prefix).
Lines under heading → `stanza["lines"]`. Lines starting `<!--` are skipped.

### `translations_ru.md` — literary translations + interlinear gloss

```markdown
## подстрочник

### Odyss. IX.39–42

Из Илиона меня неся ветер к киконам притащил,
к Исмару; а там я город разрушил и погубил их.

---

## Жуковский

<!-- **Жуковский, 1849** · рус., белый стих · ... -->

### Odyss. IX.39–42

Ветер от стен Илиона привел нас ко граду киконов,
...

---

## Вересаев

<!-- **Вересаев, 1953** · рус., проза · ... -->
```

Rules: `## Name` → translator key; `<!-- **...** -->` on next line → display
description (goes into `TRANS_DESC` dict). `### Odyss.` → stanza ref. `---`
separates translators. Every non-empty line under a `### Odyss.` heading (up to
the next heading or `---`) is one poem line's translation — **one line in, one
line out**: the block must have exactly as many lines as `greek.md`'s matching
stanza, in the same order (this is what lets the notebook zip translation lines
against `stanza["lines"]` positionally). Produces `stanza["translations"]` =
`{"подстрочник": "...", "Жуковский": "...", ...}` — подстрочник is a translator
like any other here, not a special case.

**`## подстрочник` is special only by convention, not by markdown structure:**
unlike the other translators its lines are a word-for-word gloss (not verse),
and it deliberately has **no** `<!-- **...** -->` description comment — the
notebook hardcodes подстрочник's description separately (the cell building
`_desc_map`), so adding one here would silently start overriding it. If you add
a new corpus-level translator, give it a real `<!-- **...** -->` comment like
Жуковский/Вересаев; only подстрочник skips it.

---

## Paradigm table slots — eee_project library, not per-lesson files

The quiz paradigm table is rendered by `eee.build_grc_paradigm_table(ag_backend, um_backend)`.
Which grammatical slots appear is determined by the **top-level eee_project library**:

- `eee_project/data/labels/{pos}-{lang}.tsv` — UD feature rows and their labels
  (e.g. `noun-ru.tsv`: `Case=Nom, Number=Sing, Gender=Masc → "Именит. ед. м."`)
- `ancient_greek_backend_eee/data/{pos}-tags.tsv` — AG-native tag → UD feature mapping
  (e.g. `.NSM` → `Case=Nom, Number=Sing, Gender=Masc`)

Do NOT modify per-lesson files to change paradigm coverage — edit the library data files instead.

---

## Vocabulary sources

Authoritative translations are in the lectures directory, **not** invented or paraphrased.
Copy the Russian gloss EXACTLY, including all parenthetical morphological notes.

| Lesson dir | Lectures source file |
|---|---|
| `2026_06_01/` | `~/work/greek/lectures/Odyssey/2026.06.01/Одиссея_1-21_словарь.tsv` (2-col TSV: `word\ttranslation`) |
| `2026_06_15/` | `~/work/greek/lectures/Odyssey/2026.06.15/слова день 1.md` (MD: `FORM [= DICT] [—] TRANSLATION`) |
| `2026_06_22/` | `~/work/greek/lectures/Odyssey/2026.06.22/Od_IX_39-61_vocabula.md` (MD: `FORM [= DICT] – TRANSLATION`) |

Known formatting issues in `слова день 1.md` (do not propagate to TSV): lines 30/61/125
have two entries merged without newline — parse the Greek and Cyrillic segments separately;
lines 93–94 (digit-prefixed footnotes) are not continuations of the preceding vocab entry.

---

## sys.path fix (setup cell)

Each notebook's setup cell (bottom of the reactive graph) must include this glob so that
`greek_inflexion_eee` — an editable install used internally by `build_paradigm_table` —
is importable in marimo's forked worker processes:

```python
import sys as _sys, pathlib as _pl
for _pth in _pl.Path(_sys.prefix).glob("lib/python*/site-packages/_editable_impl_*.pth"):
    _src = _pth.read_text().strip()
    if _src not in _sys.path:
        _sys.path.insert(0, _src)
```

Without this, the "словоформы" and "только Гомер" quiz filters show "Тесты: 0 / 0"
(the `build_paradigm_table` call silently fails with `ModuleNotFoundError`).
Do not narrow the glob — it must cover all `_editable_impl_*.pth` files.

---

## Vocab TSV

Format: `form\tlemma\tpos\tcontext\tmeaning`

- `form` — the exact form as it appears in the poem
- `context` — citation (`IX.42: δασσάμεθ', ὡς μή τίς μοι`)
- Multi-word forms (e.g. `πεφυγμένος ἦεν`, `οὔ ποτε`) are **intentional** — they
  represent periphrastic constructions; do not split them
- Before adding entries, check `vocab_content_problems.md` — the gap may be documented

## Coverage highlighting (`WORDS_COMBINED`)

Built from vocab TSV `form` column. Normalization (both vocab and poem sides):
1. NFD decompose → strip all combining marks (Unicode `Mn`) → NFC recompose
2. Vocab side only: also strip elision chars `'᾽᾿ʼ` from string ends (`_norm_f`)

Stem vowel differences block matching (e.g. `ἑταῖρ-` vs `ἑτάρ-`) — add the
attested form as a separate TSV entry if it should highlight.

## Quiz word filtering and poem-text highlighting share one check

Two independent `mo.ui.radio` controls exist in every lesson notebook, both
defaulting to the same mode:

- `filter_mode` (options: `словоформы`/`current`, `только Гомер`/`homer`,
  `все слова`/`none`) — which TSV rows enter the quiz question pool
  (`QUIZ_WORDS`)
- `SHOW_COVERAGE` (adds a fourth `выкл.`/`None` "off" option) — which words
  get underlined in the poem text (`WORDS_COMBINED`)

Their default (`current`) branch runs the identical check in both cells:
build the word's full ag paradigm via `build_paradigm_table(w)` and require
the tested form to appear without the orange `#f97316` "irregular form"
marker — i.e. `result and "#f97316" not in result`. (Each cell defines its
own private closure for this — `_has_displayable_form` in the quiz-filter
cell — since marimo cell-local `_`-prefixed names aren't shared across
cells.)

**Why words get excluded:** vocab TSVs mix content words (noun/verb/adj/
proper name) with function words (pronouns, particles, prepositions,
conjunctions). Function words have no noun/verb/adj paradigm to check, so
they're excluded from the default filter by design — that's normal, not a
coverage bug. The interesting gaps are content words still missing backend
paradigm coverage; this set changes as vocab TSVs grow and as
`ancient-greek-backend-eee` gains coverage, so don't hardcode a snapshot of
it in docs. To see the current list, open the notebook (`marimo edit
notebook.py --sandbox`) and check `QUIZ_WORDS_RAW` against
`build_paradigm_table` directly — or drive it headless via the
WebSocket+HTTP smoke-test pattern in the marimo-pair skill reference when no
browser is available.
