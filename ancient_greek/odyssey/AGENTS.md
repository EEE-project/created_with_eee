# Odyssey Notebooks — Agent Reference

## Directory layout

```
odyssey/
  lessons.tsv          # lesson index (title, url, date)
  notebook.py           # index/parent notebook
  eee_note.md            # shared "О морфологическом движке EEE" text (see below)
  2026_07_13/            # Lesson: Od. IX.105–129
  2026_07_06/            # Lesson: Od. IX.82–104
  2026_06_29/            # Lesson: Od. IX.62–81
  2026_06_22/            # Lesson: Od. IX.39–61
  2026_06_15/            # Lesson: Od. IX.19–38
  2026_06_01/            # Lesson: Od. I.1–21 (pilot)
```

Each lesson directory:

```
notebook.py
greek.md                   ← Greek source text (do NOT hardcode in notebook)
translations_ru.md         ← literary translations, incl. подстрочник gloss (do NOT hardcode)
ictus.html                 ← rhythm (икты) markup, one marked-up line per greek.md line
vocab_{ref}.tsv            ← vocabulary for the quiz
vocab_content_problems.md  ← known coverage gaps (read before adding TSV entries)
translation_presence.tsv   ← manually-reviewed word×translator judgments (see below)
```

All 6 lessons share the same interactive layout (migrated July 13, 2026):
clickable poem text with a click-to-gloss panel, an ictus toggle, a
homer-lexicon highlight toggle, three exercises (найди слово / сопоставь
строфу и перевод / слово в переводе), and a merged `## подстрочник` section
inside `translations_ru.md` (no more standalone `interlenear_ru.md` — its
content was merged in and the file deleted). All 6 lessons, including the
pilot (`2026_06_01`), now read the shared `odyssey/eee_note.md` file at
runtime instead of duplicating the ~30-line explanation in every
`notebook.py` — the pilot's originally-fuller text (covering the `morpheus`
lexicon, now wired into all 6 lessons) became the shared file's content.
There is no more pilot exception.

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
| `_PODSTROCHNIK_DESC = ...` / `_desc_map` | translation-picker description text |
| `SHOW_ICTUS = mo.ui.switch(...)` | ictus + homer-highlight toggles, `EEE_NOTE` accordion |
| `text_widget = eee.interactive_text(...)` | clickable poem display + translation panel |
| `_sel = text_widget.widget.selected_word` | click-to-gloss panel (meaning + lexicon-tab table) |
| `mo.accordion({"О проверке форм (EEE)": EEE_NOTE})` | EEE system explanation (reads `EEE_NOTE`) |
| `## Упражнения` | section separator |
| `gu.word_quiz_form(...)` (title `### Упражнение: найди слово`) | word-form quiz |
| `### Упражнение: сопоставь строфу и перевод` | section separator |
| `sm_direction = mo.ui.radio(...)` | stanza-match direction toggle |
| `gu.stanza_match_form(...)` | stanza-match quiz |
| `### Упражнение: слово в переводе` | section separator |
| `gu.translation_presence_form(...)` | translation-presence quiz |

### Hidden cells (below visible area, order not significant for UI)

| key line | role |
|---|---|
| `cv, set_cv = mo.state(None)` | word-quiz state: current word, score, remaining list |
| `sm_cv, sm_set_cv = mo.state(None)` | stanza-match state (own `sm_*` state block) |
| `tp_cv, tp_set_cv = mo.state(None)` | translation-presence state (own `tp_*` state block) |
| `stanza_selector = mo.ui.dropdown(...)` | stanza picker |
| `trans_selector = mo.ui.dropdown(...)` | translation picker |
| `def _parse_greek(md)` / `def _parse_trans(md)` | text parsers + `STANZAS`/`RHYTHM_HTML`/`TRANS_DESC` builders |
| `import csv` / `QUIZ_WORDS_RAW = gu.resolve_word_grammar(...)` | vocab TSV loader |
| `QUIZ_WORDS = gu.sample_session_items(...)` | word-quiz session sample (filter hardcoded `"none"`) |
| `CLICKABLE_FORMS = eee.grc_coverage_words(...)` / `HOMER_WORDS = ...` | click targets + homer-highlight set for `interactive_text` |
| `SM_STANZAS = gu.sample_session_items(STANZAS, ...)` | stanza-match session sample |
| `TP_ITEMS = gu.balance_presence_items(...)` | translation-presence session sample; also (re)writes `translation_presence.tsv` via `gu.sync_translation_presence_tsv` |
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
| `2026_06_29/` | `~/work/greek/lectures/Odyssey/2026.06.29/Od_IX_62-81_vocabula.docx` |
| `2026_07_06/` | `~/work/greek/lectures/Odyssey/2026.07.06/Od_IX_82-104_vocabula.docx` |
| `2026_07_13/` | `~/work/greek/lectures/Odyssey/2026.07.13/Od_IX_105-129_vocabula.pdf` |

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

Without this, `build_paradigm_table`/`build_lexicon_tabs` silently fail with
`ModuleNotFoundError` — the click-to-gloss panel's lexicon-tab table and the
word-quiz's paradigm table both come up empty. Do not narrow the glob — it
must cover all `_editable_impl_*.pth` files.

---

## Vocab TSV

Format: `form\tlemma\tpos\tcontext\tmeaning`

- `form` — the exact form as it appears in the poem
- `context` — citation (`IX.42: δασσάμεθ', ὡς μή τίς μοι`)
- Multi-word forms (e.g. `πεφυγμένος ἦεν`, `οὔ ποτε`) are **intentional** — they
  represent periphrastic constructions; do not split them
- Before adding entries, check `vocab_content_problems.md` — the gap may be documented

## Clickable poem text (`CLICKABLE_FORMS` / `HOMER_WORDS`)

The poem is rendered by `eee.interactive_text(mo, lines=..., clickable=...,
homer_words=..., ictus_html=..., show_ictus=...)` — an anywidget-backed
component in `eee_project`, not hand-rolled per-lesson HTML. Both sets come
from the same helper, `eee.grc_coverage_words(QUIZ_WORDS_RAW, mode,
build_paradigm_table=..., lexicons=...)`, called twice with different
`mode`:

- `CLICKABLE_FORMS` — `mode="none"`: every vocab-TSV word the engine can
  resolve at all becomes clickable (drives the gloss panel below the poem).
- `HOMER_WORDS` — `mode="homer"`: the subset whose exact attested surface
  form is confirmed by the Homeric corpus lexicon specifically. Rendered
  with a highlighted background when the `SHOW_HOMER` switch is on, so a
  reader can tell "Homer himself attests this form" apart from "some
  later-period lexicon in the combined engine also reaches it."

Normalization for matching a clicked token back to a vocab row is handled by
`eee.resolve_clicked_word` / `norm_grc_surface` inside `eee_project` — not
per-lesson code. There is no more `filter_mode`/`SHOW_COVERAGE` radio pair:
`QUIZ_WORDS` (the word-quiz question pool) always uses `filter_mode="none"`
(hardcoded, not a UI control) so every vocab word can appear in the quiz;
only the poem-text highlighting distinguishes homer-attested from
everything-else, via the `SHOW_HOMER` switch.

## `ictus.html`

One line per `greek.md` plain line, in the same order, each with its stressed
syllables wrapped in `<b style='color:#980000'>…</b>`. The STANZAS-parser cell
zips it positionally against `greek.md`'s flattened line list into
`RHYTHM_HTML` — a plain line's own accents/punctuation never need to match
the markup exactly, since matching is by position, not by dict key. Passed to
`eee.interactive_text(..., ictus_html=RHYTHM_HTML, show_ictus=SHOW_ICTUS.value)`.

## `translation_presence.tsv`

Field-by-field reference for manually filling in `reflected` (written for
opening the TSV directly in a spreadsheet app, not for agents): see
[`translation_presence_SCHEMA.md`](translation_presence_SCHEMA.md), one
level up — it applies identically to every lesson's TSV, not just one.

Columns: `lemma\tform\tstanza_ref\ttranslator\treflected` (`reflected` is
`yes`/`no`, manually judged). One row per (content-POS vocab word × literary
translator) pair actually present in the lesson's sampled stanzas. The
`TP_ITEMS` builder cell calls `gu.sync_translation_presence_tsv(...)`
every run, which appends any newly-needed rows (blank `reflected`) without
touching existing judged rows — **never regenerate this file from scratch**,
always let the sync call add to what's there, then manually fill in only the
new blank rows by comparing the Greek word's meaning against each
translator's actual stanza text (see any already-filled lesson's TSV for the
judging convention: count a "yes" if the translator's line(s) contain a
recognizable reflection of the word's meaning, even via a different specific
lexeme, not only an exact cognate).
