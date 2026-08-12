# Interactive learning materials created with EEE

Examples of interactive Greek-language course materials in notebook form,
built on the [EEE](https://github.com/EEE-project/eee-project) morphology
framework. No installation required — open directly in your browser:

1. **product** — [GitHub Pages](https://eee-project.github.io/created_with_eee/)
2. **mirror** — [GitLab Pages](https://eee-project.gitlab.io/created_with_eee/) (Odyssey, Palaestra, and B1 are split into their own GitLab projects — GitLab's Pages deployments are capped at 1GB uncompressed; see each course's own README for its link)
3. **devel** — [Codeberg Pages](https://eee-project.codeberg.page/created_with_eee/)

or in your Telegram messenger:

https://telegram.me/eee_project_greek_bot/created_with_eee

or run locally:

```bash
pip install marimo
git clone https://github.com/EEE-project/created_with_eee.git
cd created_with_eee
marimo edit notebook.py    # or: marimo run notebook.py
```

Want to build your own course, or notes to an existing one, using the course
materials? See
[eee-project's examples](https://github.com/EEE-project/eee-project/tree/main/examples)
for runnable starting points — write new lesson notebooks in the notebook
editor by hand, or with AI assistance.

## Courses

Very different course styles, spanning different periods of the Greek
language:

**Αρχαία Ελληνικά — Ancient Greek**
- **[Odyssey](ancient_greek/odyssey/)** — reading course through Homer's
  *Odyssey* Book IX, one lesson per lecture: Greek text with clickable
  word-by-word glosses, rhythm (ictus) markup, multiple literary translations
  side by side, and paradigm/vocabulary drills.
- **[Palaestra](ancient_greek/palaestra/)** — Ancient Greek for beginners,
  Summer 2026 intensive course.

**Σύγχρονα Ελληνικά — Modern Greek**
- **[Ελληνικά Β](modern_greek/ellinika_b/)** — chaptered course following the
  Ελληνικά Β textbook.
- **B1: Ελληνική Γλώσσα και Πολιτισμός** (`modern_greek/b1greeklanguageandculture/`)
  — Greek language and culture:
  - **[Kapodistrias](modern_greek/b1greeklanguageandculture/kapodistrias/)**
  - **[Zorba](modern_greek/b1greeklanguageandculture/zorba/)**
  - **[Kavafis' Ithaki](modern_greek/b1greeklanguageandculture/kavafis_ithaki/)**

Every course shares the same underlying drill/quiz machinery from
[eee-project](https://github.com/EEE-project/eee-project). Each course
directory has its own README (description + live links) and `AGENTS.md`
(structure and content sources, for developers).

## Maintainer tooling

`make help` lists what's automated for syncing content across hosts —
currently: syncing `main` (`make sync-main`, wraps `~/work/greek/git/push`),
re-exporting notebooks to the `pages` branch (`make export-notebooks`, see
`export-notebooks.py`), re-applying the split-course session-page fix
(`make fix-split-roots`), and re-applying the static-hub footer-host fix
(`make fix-static-footer`). All only stage local changes or run
already-established scripts; committing and pushing stays a manual,
Trezor-confirmed step per host — no target signs or pushes on its own.

**Not yet automated**: hub regeneration (card-list index pages) and
splitting a new course off into its own GitLab project (see each split
course's own README for GitLab's 1GB Pages-per-project limit that drove the
split) — both are still manual, multi-step processes.

### Course deployment (notebook source change → live pages)

A change to a notebook's own source (new/edited cells) is frozen at
`marimo export html-wasm` time — unlike a pure `eee-project` library fix,
which every already-deployed page picks up live from PyPI on next load, a
source change needs re-exporting and redeploying everywhere the affected
course is hosted. Full procedure:

1. **Ship the source change to `main`** via the normal branch+PR workflow
   (see the repo's own `CLAUDE.md`/global Claude conventions) — commit,
   push, open a PR, merge, sync `main` to all 3 hosts (`make sync-main`).

2. **Set up (or reuse) a `pages`-branch worktree per checkout** you'll
   deploy to, so the corresponding `main` checkout stays on `main`:
   ```bash
   git worktree add ../created_with_eee-pages-worktree pages
   ```
   Do this once per local clone (Codeberg checkout, GitHub checkout, GitLab
   unified checkout, and each of the 3 split-project checkouts — split
   projects have no separate `main`, they're already on `pages`).

3. **Re-export the affected notebooks** into the Codeberg pages worktree:
   ```bash
   make export-notebooks NOTEBOOKS="modern_greek/ellinika_b/chapter_01/chapter_01_notebook.py ..."
   ```
   Re-run for every changed notebook. The export is **host-portable** —
   `eee_footer()`'s "Source" link and similar host-detection logic resolve
   live in the browser (`js.self.location.hostname`), so the same exported
   `index.html`/`assets/` can be copied verbatim to every host below rather
   than re-exported per host.

4. **Verify before committing anything** — a real browser check, not a
   text-scrape (a marimo WASM export can render its own loading chrome even
   when the underlying Python cell errored). Serve the pages worktree
   locally and check with Playwright or similar:
   ```bash
   cd ../created_with_eee-pages-worktree && python3 -m http.server 8000
   ```
   Heavier notebooks (real backend/lexicon loading) can take 30–60s to
   finish booting under Pyodide — don't mistake a still-loading page for a
   broken one.

5. **Watch for `marimo export`'s bundled `CLAUDE.md`.** Every export
   directory gets its own copy of marimo's "notebook assistant" `CLAUDE.md`
   file. This project's convention is CLAUDE.md is never committed — make
   sure the checkout's `.gitignore` has `CLAUDE.md` (the main repo and the
   GitLab unified/split-project checkouts should already have it; verify
   before adding a brand-new checkout).

6. **Commit + push the Codeberg pages branch** (Trezor-confirmed).

7. **Copy the same exported directories into every other checkout that
   hosts the affected course(s), then commit + push each** (Trezor-confirmed,
   one host at a time):
   - **GitHub** — full mirror, same content as Codeberg.
   - **GitLab unified project** (`created_with_eee`) — trimmed to
     `modern_greek/ellinika_b/` only (GitLab's 1GB Pages-per-project cap
     drove the split below; this is what's left un-split).
   - **GitLab split projects** — copy only the matching course's
     directories, flattened to each project's root (no `ancient_greek/`
     or `modern_greek/...` prefix):
     - `created-with-eee-odyssey` ← `ancient_greek/odyssey/`
     - `created-with-eee-palaestra` ← `ancient_greek/palaestra/ancient_greek.2026.summer/`
     - `created-with-eee-b1glc` ← `modern_greek/b1greeklanguageandculture/{kapodistrias,kavafis_ithaki,zorba}/`

8. **Wait for GitLab Pages' CI pipeline** on every GitLab target (a push
   alone doesn't deploy there) — poll until it succeeds:
   ```bash
   glab api "projects/EEE-project%2F<repo>/pipelines?ref=pages&per_page=1"
   ```

9. **Verify live**, per host, with a real browser check (not just an HTTP
   200) — the exported bundle needs Pyodide to actually boot before the
   page is meaningfully "up".

## EEE (Ελληνικά Εκπαιδευτικά Εργαλεία — Greek Language Educational Tools)

🔓 Open source:
- prod — https://github.com/EEE-project/
- prod mirror — https://gitlab.com/EEE-project/
- dev — https://codeberg.org/EEE-project/

💬 Community: https://telegram.me/eee_greek
