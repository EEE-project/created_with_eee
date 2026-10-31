# AGENTS.md

Guidance for AI coding agents (and humans) working on `created_with_eee`'s
course notebooks. This file covers what's shared across every course; each
course directory has its own `AGENTS.md` for content sources, notebook
patterns, and cell structure specific to it. Read this file first, then that
course's own file.

## Courses

- `ancient_greek/odyssey/` — see its own `AGENTS.md`
- `ancient_greek/palaestra/ancient_greek.2026.summer/` — see its own `AGENTS.md`
- `modern_greek/ellinika_b/` — see its own `AGENTS.md`
- `modern_greek/b1greeklanguageandculture/` (covers `kapodistrias/`, `zorba/`,
  `kavafis_ithaki/`) — see its own `AGENTS.md`

## Source discipline

Base every cell on the course's own lecture/textbook materials (each course's
own `AGENTS.md` says exactly where those live) — don't do your own research
(web search, invented examples/etymologies/tangents) beyond them. If research
seems useful, or the materials themselves raise a question worth pursuing, ASK
the user first rather than adding it unprompted. (User rule, 2026-07-07.)

## Cell identification

Identify a notebook's cells by their content, not by ID — marimo reassigns
cell IDs on every save, so an ID noted in a previous session (or in any
`AGENTS.md`) is not stable across the next one.

## Vocabulary TSVs

Schema and multi-word-entry handling both vary by TSV, not by one repo-wide
rule — check the specific file's header row and the owning course's own
`AGENTS.md` before assuming:

- **Courses whose drill does a literal-string match against the TSV**
  (Odyssey, Palaestra) — a multi-word form or phrase (a periphrastic
  construction, an idiom, an article+noun pair) is intentional; never split
  it into separate single-word rows.
- **Courses whose drill mechanically inflects the TSV row through a real
  backend** (Kapodistrias, Zorba) — the opposite holds: a multi-word phrase
  can't be inflected as one lemma, so it's excluded from that TSV entirely
  and kept as an inline vocabulary note instead.
- Schema shape varies too: most TSVs are plain `Word\tTranslation`, but
  Odyssey's is a richer `form\tlemma\tpos\tcontext\tmeaning` (needed for its
  click-to-gloss poem text); Kavafis Ithaki deliberately reuses that same
  schema for its own poem vocabulary; Kapodistrias's `vocabulary.tsv` is a
  3-column `Word\tTranslation\tType` reference table. See
  `modern_greek/b1greeklanguageandculture/AGENTS.md` for the fullest example
  of several schemas coexisting in one course.

## Vocabulary TSV translation collisions

Two *different* Greek words sharing the exact same `Translation` value within
one TSV makes that pair impossible for a student to distinguish in a
quiz/checker (the prompt shown is the translation, so both words look like
the "same" answer). This is a real, previously-shipped bug class — found and
fixed 2026-08-21 across `ellinika_b` and `kapodistrias` (e.g. `η συγκοινωνία`
and `η μεταφορά` both flattened to plain "транспорт"; `η καταγωγή` and `η
προέλευση` both to "происхождение").

**Mechanical check** — `python3 tools/check-vocab-collisions.py` (repo root)
groups every TSV's rows by `Translation` and flags any value shared by 2+
distinct `Word` values; exits non-zero if any are found. Takes an optional
directory argument to scope to one course, e.g.
`python3 tools/check-vocab-collisions.py modern_greek/ellinika_b`. Run this
after adding or editing vocab TSVs, not just when a report comes in.

**Resolution priority, in order:**
1. Check the same chapter's own richer content first — the notebook's own
   prose glossary table, or its `*_extracted_content.md` source — often
   already has a more precise, already-vetted distinct translation for one or
   both words that the flatter drill TSV lost when authored separately.
   Reuse that text verbatim rather than inventing new wording.
2. If the collision exists even in the source textbook material itself (not
   just the TSV), don't silently guess a fix on language-learning content —
   propose a specific distinguishing translation with your reasoning and get
   the user's confirmation before applying.
3. Watch for the case that *isn't* actually an error: genuine morphological
   doublets of the same verb (e.g. `κοιτάζω`/`κοιτάω`, an -άζω/-άω pair) can
   legitimately share one translation because they mean the same thing —
   confirm via the chapter's own grammar tables (e.g. a future-tense
   stem-formation list showing both as parallel, equally-valid forms) before
   treating a shared translation as a bug.

When editing a TSV directly via Python (bypassing the Edit tool, which can
fail to match old_string against Greek/Cyrillic text) rather than a targeted
tool edit, check the file's original line-ending style first — some TSVs in
this repo are CRLF while sibling files in the same course are plain LF, and
Python's default text-mode write silently normalizes CRLF to LF, bloating the
diff to the whole file instead of just the changed line.

## Course-wide GreekConfig customization (nav_icons, etc.)

`GreekUtils` is constructed once per notebook from a `GreekConfig`
(`MODERN_GREEK`/`ANCIENT_GREEK` from `eee_project`). `GreekConfig` is frozen —
never assign to a field on the shared singleton directly
(`MODERN_GREEK.nav_icons = True` raises `dataclasses.FrozenInstanceError`,
and would otherwise silently affect every other course reusing that same
singleton). To opt a course into a config-level default — e.g. the ◀/▶/↺
nav-icon treatment and reviewable done screens — derive a new instance once
at construction time instead:

```python
import dataclasses
_config = dataclasses.replace(MODERN_GREEK, nav_icons=True, show_prev_when_done=True)
gu = GreekUtils(backend, mo, pd, eee_module=eee, config=_config)
```

`ellinika_b`'s 10 chapters all follow this pattern (needs `eee-project`
>=1.10.0). See eee-project's own `docs/api-patterns.md` for the full
`GreekConfig` field list and which of the nine quiz/drill functions resolve
`nav_icons`/`show_prev_when_done` from `self._cfg` when the caller omits
them. Don't repeat `nav_icons=True`/`show_prev_when_done=True` at individual
call sites once the course-level config already sets it — that's the
redundant, harder-to-maintain pattern this replaced.

## Cross-page UI language persistence

A lesson notebook's UI-language dropdown should use `eee_project`'s
`language_bridge`/`language_selector`/`save_language_selection` trio, not a
plain `mo.ui.dropdown` — see eee-project's own `docs/api-patterns.md` for the
exact 3-cell wiring (bridge, selector, save — each needs its own cell so
marimo's reactivity reruns them at the right time). It persists the choice to
the browser's `localStorage` under the key `"eee_lang"`, so navigating between
pages keeps the same language selected instead of resetting to the notebook's
hardcoded default.

This key is shared site-wide: `tools/gen_hub.py`'s static hub pages read/write
the same `"eee_lang"` key via their own vanilla-JS `setLang()` (no Pyodide —
see that course's own note on hub pages being statically generated, not a WASM
export of `notebook.py`). A language picked on a hub page carries into
whichever lesson is opened next, and vice versa, precisely because both sides
target the same key — don't invent a different key or mechanism for a new
course, or that course's pages will silently fall out of the shared
persistence.

Already wired (checked 2026-10-21): `ellinika_b`, `b1greeklanguageandculture`
(kapodistrias, zorba, kavafis_ithaki) and all 8 Odyssey lessons. All 10
Palaestra lessons still use a plain, non-persisted dropdown.

## The word-in-translation test: 10 balanced questions, the same way in every notebook

Every notebook with the «Слово в переводе» / translation-presence test (`gu.balance_presence_items`) draws exactly 10 items per session, half `yes` and half `no` where its answer key has enough `no`
rows: one `SESSION_SIZE = 10` cell and `n=SESSION_SIZE` -- the Odyssey lessons' own mechanism, since 2026-10-06 also in the four Kavafis lessons (the user: "in all nbs this test must show only 10 balanced
questions -- do it by the same way in all nbs"). No question-count dropdown and no `n=None` (every item of the pool: up to 95 questions in Kavafis lesson 4). A language whose key has fewer than 5 `no` rows
gives a shorter balanced session (as of 2026-10-26: Greek mode of Odyssey 2026_07_13 asks 8; as of 2026-10-06: English mode of Kavafis lesson 2 asks 6): add `no` judgments to the key rather than
unbalance the session. How the keys are judged (word level, one regex per meaning) is in `modern_greek/b1greeklanguageandculture/AGENTS.md`.

## Publishing a lesson/chapter to Pages

Locally (via `marimo edit`), a course's own `notebook.py` still renders its
index by reading that course's `index.tsv` and calling
`ConfigStore.from_url(...)` + `eee_card_list(...)` — that's unchanged. The
*published* hub is a separate, static `index.html` (see step 4 below), not
that live notebook.

The site is static content hosted on Codeberg, GitHub, and GitLab Pages (see
the root `README.md`) — nothing here is served from molab. A lesson only goes
live once its own WASM export lands on the `pages` branch, alongside a
regenerated hub page. `index.tsv`'s `url`/`index_url` columns are never molab
links:

1. In the course's own `index.tsv`, add a row: `url` = the new lesson's own
   directory name (e.g. `2026_07_15/` or `chapter_13/`), `index_url` = that
   course's existing root-relative Pages path (same on every row already in
   the file).
2. Export the notebook: `marimo export html-wasm <lesson-dir>/<notebook>.py --mode run -o <tmp-dir>`.
3. Copy that export into the `pages` branch at the matching path — `pages` is
   synced directly, never via a PR against `main` (see the README, "Quick
   start: from a notebook change to every host").
4. Regenerate that course's own hub — it's static HTML now, not a live
   notebook, so it won't pick up the new `index.tsv` row on its own:
   `python3 tools/gen_hub.py <hub-key>` from `main` (see `tools/gen_hub.py`'s
   own `HUBS` dict for each course's key), then copy the resulting
   `index.html` into `pages` at that course's own path.
5. Commit + push `pages`, then sync it to the GitHub/GitLab mirrors the same
   way `main` is synced (`~/work/greek/EEE/CLAUDE.md`'s "Git & Codeberg
   Integration").
6. Verify with `.claude/skills/verify-pages` before calling it done.

The "Open in molab" badge some notebooks' title cells carry is a separate,
optional convenience link (paste a real molab upload's `/app` URL there if you
want one) — it has no connection to `index.tsv` or to whether the lesson is
actually live on Pages.

## Known gap: bare local-file reads break on a raw pre-publish molab upload

A manually-uploaded single `.py` file (the only way to preview a notebook in
molab before it's committed/pushed — molab has no CLI/API) does not bring
same-directory sibling files (TSVs, `.md` sources, images) along with it —
only the uploaded file itself lands in molab's sandbox. A notebook that reads
its own local files as a bare `pd.read_csv(...)`/`open(...)` 404s in that one
specific scenario, even though the identical code is correct once the
notebook is actually published (imported from the committed Codeberg raw
URL). Fix: route local file reads through `gu.ensure_file(filename,
nb_dir=..., remote_base=...)` — a no-op when the file's already local, a
download when it isn't. Each course's own `AGENTS.md` tracks which of its
files have/haven't been converted yet.

## Data files in WASM exports

`make export-notebooks` embeds the text data files a lesson can ask for (TSV, Markdown, YAML, JSON, HTML up to 250 KB) in
the exported page: every such file in the lesson's own folder, and the files in the folder directly above it that the
lesson names (as a string or an f-string). A lesson needs no list and no code for this. A file in a subfolder, two or more
folders up, in another repository, a PDF or an image is not embedded; the page fetches it while it starts. `index.tsv` and
`ga.json` are never embedded, and only git-tracked files are (see `tools/_embed_data.py`). A page is a snapshot: after a change
to a data file, export the lessons that read it again (`python3 tools/check-embedded-data.py --who <file>` lists them).
`make check-embedded-data` lists a lesson whose requested file is not embedded. `make export-notebooks ARGS=--no-embed`
exports a lesson without the embedded data; the README section "Export one lesson with and without the embedded data"
shows how to compare the two.

## Paradigm packs in WASM exports

`make export-notebooks` also runs an ancient Greek lesson once with `uv` (environment from the lesson's own script header) and
puts the paradigms its backends built into the page as an extra first cell (`tools/_paradigm_pack.py`). A lesson needs no code for
this. The page pins the four library versions that made the pack (`ARGS=--no-pin`, `ARGS=--no-pack`); a lesson with fewer than
20 paradigms gets no pack. Do not run a lesson natively inside the repository to make a pack: `ensure_file()` downloads files next to
the notebook (the tool runs a copy in a temporary folder). `make check-paradigm-pack` checks the step. See the README section
"The paradigm pack of an ancient Greek lesson".

## The stanza layout of the Odyssey lessons (browser check, release order)

A lesson that draws its stanza with `eee.interactive_text(..., wrap=True, translation=..., notes=...)` and its word panel with
`gu.render_gloss_sheet(...)` (eee-project 1.26.0) is laid out by CSS: the Greek wraps with a hanging indent, the translation is one
card beside the Greek (a box 600 px wide or more) or under it, and the word sheet is fixed to the bottom of the screen below 750 px.
`marimo check`, an export and the library's unit tests cannot see any of that, so `make check-lesson-layout` runs every lesson that
calls `render_gloss_sheet` in a real browser (`marimo run`, Chromium) at 390 and 830 px in Greek, Russian and English. It checks that
the block fits, where the card and the sheet stand, that a tap opens the sheet (and a closed one opens again), that every translator of
the dropdown draws a card (on the narrow page in every stanza of the lesson), that a starred word shows its margin note, that the blank
entry removes the card, and that neither the page nor a cell of the lesson raises an error (a `NameError` left behind by a merge fails
the run with its line). It takes about a minute per lesson. Run it after a change to a lesson's text cell, gloss cells or translator dropdown, and after raising the
`eee-project` floor of a lesson. `SCOPE=<notebook or folder>` limits it, `ARGS="--langs el --widths 390"` makes fewer runs; a lesson
needs `translations_{ru,en,el}.md` next to it (git-ignored; the lesson fetches them from Codeberg when they are missing) and the tool
puts the lesson folder's files back after the run. See `tools/check-lesson-layout.py` for the exit statuses.

The check runs `marimo run` natively; it does not see Pyodide. `marimo export html-wasm` writes every package of the lesson's script
header into the page pinned (`==`) to the version that the exporting Python has installed (`lock_kind = "observed"` in the page's
header), and the page installs those versions (`tools/_paradigm_pack.py` relies on that when it pins the libraries of the pack; the
install itself was not observed, because Pyodide cannot be reached from where this was written).
Checked on `2026_06_01`: a Python whose installed metadata said `eee-project` 1.25.0 gave a page that pins `eee-project==1.25.0`, and
the same export after the reinstall gave `==1.26.0`. So **a lesson whose header says `eee-project>=1.26.0` goes to `pages` only after
1.26.0 is on PyPI and installed in `EEE_PYTHON`**: exported from a Python that still has 1.25, the page pins 1.25 and stops at the
first `wrap=` (`unexpected keyword argument`); exported from one that has an unreleased 1.26.0 (an editable install), the page asks PyPI
for a version that is not there and does not start; and `make export-notebooks` builds no paradigm pack for the lesson (`uv` resolves
the header from PyPI; the export goes on without a pack and says why). Before the export run
`$EEE_PYTHON -c "import importlib.metadata as m; print(m.version('eee-project'))"`: it must print 1.26.0 or newer (an editable install
keeps the version it was made with, so it prints the old one although `eee_project.__version__` is new; reinstall it). After the export,
`grep -o 'eee-project==[0-9.]*'` in the page's `index.html` shows what it pinned. After the release, check the published page with
`.claude/skills/verify-pages`.

**Merging `claude/cypriot-dialect-translation-be01kl` (Σπανούδης) into this layout.** Tried in a scratch worktree: git reports two
conflicts, `CHANGELOG.md` (keep both sections) and `ancient_greek/odyssey/AGENTS.md` (keep the layout side of the cell table), and
merges the 11 notebooks without a conflict, but the old text cell's note block of the Σπανούδης branch (from the comment `# A translator
with margin notes (Σπανούδης): the edition's right margin, as a second column beside` to the `_right = mo.Html(...)` that follows it)
stays in the merged text cell and reads `_txt_lines`, which the layout deleted: choosing Σπανούδης then raises `NameError`. Delete that
block from the text cell of each of the 8 lessons, make the three language notebooks of `2026_07_27` again from its `notebook.py`
(`rm notebook_{ru,el,en}.py README.md; python -m eee_project.split_lesson notebook.py`; `join_lesson` must then report no change), and run
`make check-lesson-layout`: it fails on a leftover block with the line `NameError: name '_txt_lines' is not defined`, and with the block
gone it passes (checked on the trial merge: 8 lessons, Greek interface, 390 and 830 px, margin notes tapped in 6 lessons).
