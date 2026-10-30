# Odyssey Notebooks — Agent Reference

1. Read `../../AGENTS.md` (repo root) first — it covers policy shared by
   every course.
2. This file: what's specific to Odyssey.

## Directory layout

```
odyssey/
  index.tsv          # trilingual lesson index (url, icon, greek, label_{ru,el,en}, title_{ru,el,en}, desc_{ru,el,en}, index_url)
  notebook.py           # index/parent notebook
  eee_note_{ru,el,en}.md  # shared "О морфологическом движке EEE" text, one file per language (see below)
  odyssey_morpheus_{adjs,nouns,verbs}_lexicon.yaml  # course-local lexicon
                          # data, see "Fixing a genuine coverage gap" below
  2026_07_27/            # Lesson: Od. IX.152–180
  2026_07_20/            # Lesson: Od. IX.130–151
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
translations_{ru,en,el}.md ← not kept here: fetched at runtime from greek-knowledge-eee (see below)
ictus.html                 ← rhythm (икты) markup, one marked-up line per greek.md line
vocab_{ref}_{ru,en,el}.tsv ← vocabulary for the quiz, one file per language
vocab_content_problems.md  ← known coverage gaps (not every lesson has one; read it, where it exists, before adding TSV entries)
translation_presence.tsv   ← manually-reviewed word×translator judgments (see below)
notebook_{ru,el,en}.py, README.md ← only in a split lesson (2026_07_27): one notebook per UI language, made by `python -m eee_project.split_lesson`; change a text there, then run `python -m eee_project.join_lesson` (the README of the folder has the rules)
```

**Translations live in the knowledge base, not in the lesson folder.** The notebook fetches `translations_{ru,en,el}.md` at runtime with `ensure_files(...)` from `https://codeberg.org/EEE-project/greek-knowledge-eee/raw/branch/main/texts/odyssey` (see the cell with `_gke_remote` in `2026_07_27/notebook.py`). A copy next to a notebook is a git-ignored download cache. The one translation file kept in a lesson folder is `2026_07_20/translations_ru_starikovsky.md`: Стариковский (2025) is in copyright, so the knowledge base holds only a citation of it. The format is described under "`translations_{ru,en,el}.md`" below.

All 8 lessons share the same interactive layout (migrated July 13, 2026; `2026_07_27` was built directly on it):
clickable poem text with a click-to-gloss panel, an ictus toggle, a
homer-lexicon highlight toggle, three exercises (найди слово / сопоставь
строфу и перевод / слово в переводе), and an interlinear crib in each language
(the section `interlinear_{lang}` of the knowledge-base file; there is no standalone
interlinear file). Every lesson reads the shared `odyssey/eee_note_{lang}.md` file of its language at runtime
instead of duplicating the ~30-line explanation in every `notebook.py`, and the `morpheus`
lexicon is wired into every lesson. There is no pilot exception.

---

## Source discipline — CRITICAL

See the root `AGENTS.md`'s "Source discipline" for the policy (materials-only,
ask before researching further). This course's materials live in
`~/work/greek/lectures/Odyssey/<date>/`: the presentation PDF (`Одиссея N.pdf` /
`Od_IX_*.pdf`), the vocab file (`.docx`, `.pdf`, `.md` or `.tsv`), the
images/diagrams in the presentation, and in some folders the lecturer's notes
(`notes.md` or `notes.txt`). **Notes are a valid source — transcribe / distill
them** (that is how the День-4 lotus material got in). Most folders hold no
notes: the notes cells then hold only what the slides say.

- **Greek** (`greek.md`) — transcribe from the presentation slides only.
  **Translations and the interlinear crib** are not transcribed per lesson: the lesson
  reads them from `greek-knowledge-eee` (see below).
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
| `{lang_sel}{bridge}` (floating div, top-right) | language switcher, cross-page persisted via `eee_project.language_bridge`/`language_selector`/`save_language_selection` (browser `localStorage`, key `"eee_lang"` — same key `tools/gen_hub.py` uses for the hub pages, so a hub selection carries into a lesson) |
| `mo.md("# Одиссея…")` + image | title, molab badge, lesson image |
| `**Материалы занятия:**` PDF links | materials links |
| `## Слова, слова…` | per-lesson vocabulary notes (optional section) |
| `## Текст поэмы с параллельными переводами` | section separator |
| `_EDITION = (...)` | Greek text edition citation (HTML), the edition named in the first line of `greek.md`; `_MURRAY` (Murray 1919) in `2026_06_22`, `2026_06_29` and `2026_07_06`, no such cell in `2026_06_01` and `2026_06_15` |
| `_desc_map = {eee.interlinear_translator_key(...): gu.ui_label('interlinear_description', ...), **TRANS_DESC}` | translation-picker description text |
| `SHOW_ICTUS = mo.ui.switch(...)` | ictus + homer-highlight toggles, `EEE_NOTE` accordion |
| `text_widget = eee.interactive_text(...)` | clickable poem display + translation panel; a translator with margin notes (Σπανούδης) gets a second column of notes beside its verses |
| **`2026_06_01` only (pilot, needs `eee-project>=1.26.0`):** `text_widget = eee.interactive_text(..., wrap=True)` shown with `eee.stanza_view(mo, text_widget, lines_or_None, notes=...)` | narrow-screen layout: the Greek lines wrap with a hanging indent, the translation is one card for the whole stanza (beside the Greek from 600 px of container width, under it below), a margin note stands under its verse, and the blank entry of `trans_selector` (`allow_select_none=True`, value `None`) shows no translation. The other seven lessons keep the old layout until they are moved |
| `period_tables, period_selector, gloss_panel = gu.render_gloss_selector(...)` | click-to-gloss panel (meaning + real period `mo.ui.dropdown`, see `eee_project.build_grc_period_tables` — the `bridge`/`lang_sel` convention below: a plain assignment displays nothing, `gloss_panel` needs its own bare-expression line) |
| `gu.render_gloss_table(period_tables, period_selector)` | own cell, taking `period_selector` as a parameter so it (and only it) reruns on a pick — renders the selected period's table |
| **`2026_06_01` only:** the `render_gloss_selector` cell shows nothing (`return gloss_panel, period_selector, period_tables`) and the next cell calls `gu.render_gloss_sheet(gloss_panel, period_tables, period_selector, lang=..., selected_word=text_widget.widget.selected_word, click_seq=text_widget.widget.click_seq)` | the panel and the table as one sheet: a block under the text on a page of 750 px or more, a sheet fixed to the bottom of the screen below that once a word is chosen. It replaces the bare `gloss_panel` line and the `render_gloss_table` cell |
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
| `bridge = eee_project.language_bridge(mo)` | localStorage bridge for `lang_sel` (own cell, undisplayed — see visible-cells row above) |
| `eee.parse_stanza_text(...)` / `eee.parse_stanza_translations(...)` | text parsers (shared `eee_project` functions, `ref_prefix="### Odyss. "`) + `STANZAS`/`RHYTHM_HTML`/`TRANS_DESC` builders; a `STANZAS` entry also carries `margin_glosses` (see Σπανούδης below) |
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

Greek text and translations (incl. the interlinear crib, see below) live in Markdown
files read at runtime by `eee.parse_stanza_text`/`eee.parse_stanza_translations`: `greek.md`
in the lesson folder, `translations_{ru,en,el}.md` in `greek-knowledge-eee`
(shared `eee_project` functions — every lesson notebook calls these with
`ref_prefix="### Odyss. "` instead of defining its own local parser; see their
docstrings in `eee_project/notebook_utils.py` for the exact file-format contract
they implement). Never copy poem lines or translations into Python cells.

### `greek.md` — Greek source text

```markdown
<!-- Homerus. Odyssea. ed. M. West, Bibliotheca Teubneriana, De Gruyter 2017 -->

### Odyss. IX.152–155

ἦμος δ' ἠριγένεια φάνη ῥοδοδάκτυλος Ἠώς,
νῆσον θαυμάζοντες ἐδινεόμεσθα κατ' αὐτήν.
...
```

The first line is a comment that names the edition of the Greek text. The edition is not
the same in every lesson (for example Murray 1919 in `2026_06_01` to `2026_07_06`,
von der Mühll in `2026_07_13`, West in `2026_07_20` and `2026_07_27`). Copy it from the
source line that the presentation prints with the Greek text, and name the same edition in
the `_EDITION` cell. If the presentation prints none, ask the user which edition the text
follows.

Rules (implemented by `eee.parse_stanza_text`): `### Odyss. X.XX–XX` → stanza ref
key (stripped of the `ref_prefix`). Lines under heading → `stanza["lines"]`.
Lines starting `<!--` are skipped.

### `translations_{ru,en,el}.md` — literary translations + interlinear crib (in `greek-knowledge-eee`)

The files are `texts/odyssey/translations_ru.md` (interlinear_ru, Жуковский, Вересаев),
`translations_en.md` (Pope, Murray, Chapman, interlinear_en) and `translations_el.md`
(Πολυλάς, Σπανούδης, interlinear_el), next to `text.md` (the Greek original) and `index.md` (how to
read them). Each file starts with YAML front matter (`type: Literary Translation`, the
translators, the sources). Today they cover Odyssey I.1-21 and IX.19-180. Chapman has 8 stanzas only (I.1-21 and IX.19-38), and `TRANS_BY_LANG` in the notebooks does not
offer Chapman.

**Σπανούδης** (Β' έκδοση, Λάρνακα 2020) is a Cypriot-dialect rendering, offered in Greek mode only (`TRANS_BY_LANG["el"]`, picker label
`Σπανούδης (2020, κυπριακή διάλεκτος)`). It is in copyright, so the knowledge base holds fragments only (Ραψωδία Α' στ. 1-30 and
Ι' στ. 19-166 of the edition), by the translator's permission to the maintainer, and the lessons read them from
`translations_el.md` (`greek-knowledge-eee` 0.10.4) like Πολυλάς: no copy is kept in a lesson folder, unlike Стариковский.
The rendering is free and rhymed in couplets, so its verses were assigned to the lesson stanzas by sense, verse by verse: a stanza can hold
a verse more or less than its Greek lines, a couplet is split where its two verses render different stanzas, and a verse that renders Greek lines of two stanzas stands in both
blocks (`Ι' 35, 70, 71, 117, 136`); `IX.29–33` has two verses only: the Calypso lines have no counterpart.

**Margin notes.** The edition marks Cypriot words with an asterisk and translates each into standard Greek in its right
margin; those notes matter and the lessons show them. In the knowledge base the starred word carries its asterisk in the
verse (`πολλοπάητον*`) and the note is the line right after the verse, `<!-- gloss: word — meaning -->` (several notes of
one verse are joined with ` · `). `eee.strip_comment_lines` removes comments, so the cell that builds `STANZAS` reads
the `gloss` lines first (`_margin_glosses`: shown line index → `[(word, meaning)]`, kept in `STANZAS[...]["margin_glosses"]`,
looked up like the shown text: by exact key in `2026_06_01` and `2026_06_15`, with `find_stanza_translation` in the others),
and the text-widget cell draws them as a second grid column, `* word — meaning`, at the height of their verse. A translator
without notes is drawn exactly as before. The `<!-- Ραψωδία … στ. … -->` lines name the edition's verses of a stanza and are
only stripped.

```markdown
## interlinear_ru

### Odyss. IX.39–42

<!-- grc: Ἰλιόθεν με φέρων ἄνεμος Κικόνεσσι πέλασσεν, -->
Из Илиона меня неся ветер к киконам притащил,

<!-- grc: Ἰσμάρῳ. ἔνθα δ᾽ ἐγὼ πόλιν ἔπραθον, ὤλεσα δ᾽ αὐτούς: -->
к Исмару; а там я город разрушил и погубил их (жителей).

---

## Жуковский

<!-- Жуковский В. А. Одиссея. СПб., 1849 · https://ru.wikisource.org/... -->
<!-- **Жуковский, 1849** · ... -->

### Odyss. IX.39–42

Ветер от стен Илиона привел нас ко граду киконов,
Исмару: град мы разрушили, жителей всех истребили.
...

---

## Вересаев

<!-- Вересаев В. В. Одиссея. М., 1953 · http://az.lib.ru/... -->
<!-- **Вересаев, 1953** · ... -->
```

Rules (implemented by `eee.parse_stanza_translations`; see its docstring in `eee_project/notebook_utils.py`): `## Name` opens a translator's section and is the
translator key. A `<!-- **...** -->` comment line between the heading and the first stanza heading is the display description (it goes into the `TRANS_DESC` dict). The knowledge-base
files put a plain source comment (`<!-- Author. Title. Place, year · URL -->`) before it; the parser ignores that line.
`### Odyss.` opens a stanza. `---` separates translators. Every non-empty line under a `### Odyss.` heading (up to the next
heading or `---`) belongs to that stanza's text. The result is `{translator: {stanza_ref: text}}`.

**How the notebook finds and shows a stanza.** The notebooks from `2026_06_22` on look up each lesson stanza (the ref from `greek.md`) with `eee.find_stanza_translation`; the
first two lessons use an exact `d.get(ref, "—")`, which is enough for their stanzas. An `interlinear_{lang}` section needs the exact ref (`allow_coarse_fallback=False`); a
missing ref shows "—". For a literary translator, the lookup also accepts a stored range that contains the
lesson stanza. Pope (from IX.39) and Chapman mark such refs `### Odyss. IX.39–46 (equivalent passage)`. After `eee.strip_comment_lines` removes the `<!-- ... -->` lines, the
notebook shows each text line on its own line beside the Greek lines (the cell with `_txt_lines`). It does not pair a translation line with a Greek line, so a literary
translation can have any number of lines: Murray's prose has one line for IX.39–42, where the Greek has four. The interlinear crib keeps one gloss line for each Greek line,
each after an echo of that Greek line.

**The interlinear crib is a section like any other, with three conventions.** Its name is `interlinear_{lang}`: get it from `eee.interlinear_translator_key(lang)` and
never hardcode it (the old name `подстрочник` once made the interlinear option show no text). It has **no** `<!-- **...** -->` description: the notebook supplies
the description from the UI label `interlinear_description` (the cell that builds `_desc_map`), so a description comment here would override it. Each gloss line
is preceded by an `<!-- grc: ... -->` comment that echoes its Greek source line (as in the example above); the notebooks strip these comments. A new corpus-level
translator gets a real `<!-- **...** -->` description like Жуковский/Вересаев. A section titled `## Name (reference only, not reproduced)` is the citation of a
translation in copyright: it has no stanzas and no description.

**Adding translations for a new passage.** The notebooks fetch `main` of `greek-knowledge-eee`, so the stanzas must be there before a lesson can show them (a missing
stanza shows "—"). That repository describes how a work is authored in `texts/index.md` (copy a template, then run `uv run greek-knowledge check`) and says that the
Odyssey is not migrated to it yet. The Odyssey files are built by `scripts/populate_odyssey_texts.py`, a one-off, re-runnable script that holds each section as a Python
constant. Its docstring says that the sections come from the old `translations` branch of this repository. That branch no longer exists, and the comments in the script name
other sources: Wikisource, Project Gutenberg, the Internet Archive, and `interlinear_en` and `interlinear_el` text for I.1-21 that was written for the knowledge base.
Read `texts/index.md` and that script, and ask before you change either.

---

## Paradigm table slots — eee_project library, not per-lesson files

The quiz paradigm table is rendered by `eee.build_grc_paradigm_table(ag_backend, um_backend, lang=lang_sel.value)`
(the `lang=` argument must track `lang_sel` — see the language-switcher row above — so the labels re-render when the UI language changes).
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
| `2026_07_20/` | `~/work/greek/lectures/Odyssey/2026.07.20/Od IX 130-151 vocabula.docx` |
| `2026_07_27/` | `~/work/greek/lectures/Odyssey/2026.07.27/Od IX 152-180  vocabula.pdf` |

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

Without this, `build_paradigm_table`/`build_period_tables` silently fail
with `ModuleNotFoundError` — the click-to-gloss panel's period table and
the word-quiz's paradigm table both come up empty. Do not narrow the glob
— it must cover all `_editable_impl_*.pth` files.

---

## Vocab TSV

Format: `form\tlemma\tpos\tcontext\tmeaning`

- `form` — the exact form as it appears in the poem
- `context` — citation (`IX.42: δασσάμεθ', ὡς μή τίς μοι`)
- Multi-word forms (e.g. `πεφυγμένος ἦεν`, `οὔ ποτε`) are **intentional** — they
  represent periphrastic constructions; do not split them
- Before adding entries, check `vocab_content_problems.md` if the lesson has one — the gap may be documented

### Fixing a genuine coverage gap (not already documented)

The three `odyssey_morpheus_{adjs,nouns,verbs}_lexicon.yaml` files at this
directory's top level (sibling to the lesson dirs, not per-lesson) are
**course-local** — same mechanism as Palaestra's `athenaze_capN_*.yaml`
(see that course's own AGENTS.md), a raw file path in
`AncientGreekBackend`'s `lexicons=[...]`/`extra_lexicons=[...]`, not a
registered package name. (History: 2026-07-11 → 2026-07-31 these lived as
a named `"odyssey_morpheus"` lexicon inside `greek-inflexion-eee` itself —
moved back out because the course was still growing lesson by lesson, and
each addition had forced a full package version bump + PyPI republish, 7
in 16 days, just to gap-mine a few more words. Bundling this kind of data
into the shared package is still the right move eventually, but only as a
one-time consolidation once a course is actually finished — see
`feedback_check_course_local_lexicons_first.md`-style reasoning in the
package's own README if this comes up again for a different course.)

Every lesson's own setup cell resolves and downloads these files, then
passes them to both diachronic backends:

```python
ag_backend = AncientGreekBackend.for_period("epic", "attic", "hellenistic_koine", "roman_koine", extra_lexicons=ODYSSEY_EXTRA_LEXICONS)
ag_homer = AncientGreekBackend.for_period("epic", extra_lexicons=ODYSSEY_EXTRA_LEXICONS)
```

`ODYSSEY_EXTRA_LEXICONS` (a list of 3 absolute paths) is built in its own
cell, separate from the cell that constructs `ag_backend`/`ag_homer` —
this split exists specifically to avoid a circular dependency: the
download step needs `cfg` (for `cfg.raw_base`), but `cfg`'s own cell needs
`mo`, and `mo` is imported in the backend-construction cell — so `import
marimo as mo` also lives in its own minimal cell, ahead of both. Don't
collapse these back into one cell without re-checking `marimo check` for a
`cycle-dependencies` error.

`for_period()` merges named *period* presets (`"epic"` → `"homer"`; `"attic"`
→ `"pratt"`/`"ltrg"`/`"lsj"`; etc. — see `ancient_greek_backend_eee`'s own
`_PERIOD_PRESETS`), plus `extra_lexicons` layered on top — raw file paths
work here exactly like they do in a plain `lexicons=[...]` list. Every
entry in the 3 lexicon files is a verbatim attested-form `forms:` block
(never generative `stems:` — they exist specifically for forms the other
period lexicons can't derive correctly). **A new entry for a genuine gap
should follow the same `forms:`-only convention**, confirmed via
`greek-inflexion-eee`'s own `tools/morpheus/query_morpheus.py` before
adding — matching the methodology and skip-list already documented in
each file's own header comments (the "gap-mining" passes; read one before
adding a new lemma, it lists words deliberately excluded and why). Homer's
own dialect is Epic/Ionic, not Doric — but a single spelling can be
grammatically ambiguous across dialects, and Morpheus returns every
reading it recognizes for that exact surface form, each tagged with which
dialect(s) attest it. When a candidate reading's *only* attested dialect
tag is Doric (no Epic/Ionic reading matches that same grammatical
analysis), that specific reading is excluded as the wrong parse for this
text — a reading valid in Epic too is kept even if Doric also happens to
share it (see e.g. `ἀρόω`/`ναίω` in `odyssey_morpheus_verbs_lexicon.yaml`'s
own header for a worked example). So a "gap" isn't always a bug — check
the skip-list first.

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

One run of the notebook appends the rows of the literary translators of the
selected UI language only (`TRANS_BY_LANG[lang_sel.value]`, without the
interlinear key). Run the notebook once in each UI language (ru, en, el) so
that every translator has its rows, then fill in the blank ones.

Σπανούδης joined the Greek list on 2026-10-28, so the first run of a lesson in Greek appends its rows with a blank `reflected`.
Until someone judges them they are never asked (`build_translation_presence_items` skips a row that is not `yes` or `no`).
