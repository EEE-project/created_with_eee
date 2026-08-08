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
