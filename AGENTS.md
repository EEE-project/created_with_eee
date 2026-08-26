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
   synced directly, never via a PR against `main` (see
   `.claude/skills/ship-eee-change`).
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
