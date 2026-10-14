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

### Quick start: from a notebook change to every host

1. **Ship the source change to `main`** (branch → PR → merge), as usual.
2. **Export** the changed notebook(s) into the Codeberg `pages` worktree
   (`../created_with_eee-pages-worktree`) — one `notebook.py` per course
   directory, never its `_el`/`_en`/`_ru` variants:
   ```bash
   make export-notebooks NOTEBOOKS="ancient_greek/odyssey/2026_07_06/notebook.py"
   ```
   The page carries the lesson's text data files as they are on disk, so export
   from a clean `main` checkout (the export line names the branch when it is not
   `main`, and the embedded files that differ from `HEAD`). The page is a
   snapshot: after a data file changes, export again the lessons that embed it;
   `python3 tools/check-embedded-data.py --who <file>` lists them. More in
   "Export one lesson with and without the embedded data" below.
3. **Commit and push Codeberg's `pages`** from that worktree,
   then open the live Codeberg page and check it (hard-reload with Ctrl+Shift+R).
4. **Propagate to GitHub and GitLab**, including the three GitLab split
   projects. It copies the Codeberg worktree's *local* `pages`, so finish
   step 3 first:
   ```bash
   make propagate-pages                           # fetch Codeberg, prepare + commit locally, push nothing
   make propagate-pages ARGS="--push"             # prepare again, then force-push every destination whose tree the remote does not serve
   ```
   `github` or `gitlab` in `ARGS` limits the run to one host; after a failed
   push (for example a missed confirmation of your key) run the `--push` command again; a GitHub or
   GitLab repository that already serves the prepared tree is not pushed again.
   Git runs through the `GIT_CMD_*` wrappers from `.env` or the environment
   (see "What each command needs" below; the default is plain `git`), and
   every destination worktree must be clean, on `pages`, with its *own* git
   directory — the script refuses a destination that shares Codeberg's.
   Before it fetches or pushes anything, it also reads each GitLab course
   project's remote `pages` tip over HTTPS and stops if its checkout does not
   contain it (those branches refuse force-pushes).
5. **Verify** — `make verify-pages-deploy SITE=odyssey` (GitLab Pages needs its
   CI pipeline to finish first); after hub changes also `make check-hub-links`.

A hub change (`tools/gen_hub.py`, an `index.tsv`) follows the same steps with
`make gen-hub HUBS="<hub keys>"` instead of the export.

### What each command needs before you run it

Read this before the first push. Run every command from the root of this
repository (the folder with the `Makefile`).

**Tools and logins**

| You need | Used by | How to check |
| :-- | :-- | :-- |
| An SSH key with push rights on `codeberg.org`, `github.com` and `gitlab.com` | every fetch of Codeberg and every push | `git ls-remote git@codeberg.org:EEE-project/created_with_eee.git HEAD` answers (the same for the other two hosts) |
| `git` set up to sign commits (`commit.gpgsign=true` and a signing key) | `propagate-pages`, `sync-main` (they make commits) | `git log -1 --format=%G?` prints `G` after a commit |
| `gh`, logged in | `sync-main` (mirror check), `verify-pages-deploy`, the manual Pages rebuild below | `gh auth status` |
| `glab`, logged in | `sync-main` (mirror check and the `main` protection switch), `verify-pages-deploy` | `glab auth status` |
| `~/.venv/eee/bin/python3` with `marimo` (another Python: `EEE_PYTHON=...`) | `export-notebooks`, `check-embedded-data`, `gen-hub`, `sync-pages-export`, `sync-hub-pages` | `~/.venv/eee/bin/python3 -m marimo --version` |

`tools/propagate-pages.sh` itself calls neither `gh` nor `glab`.

**The git command of each host.** `GIT_CMD_CODEBERG`, `GIT_CMD_GITHUB` and
`GIT_CMD_GITLAB` name the command that runs `git` for each host. Export them, or
put them in the file `.env` in the repository root (git ignores it). Without a
value the scripts use plain `git`. There is an example under "What's automated
(reference)" below.

**Folders.** Each folder must exist before the first run. The pages folders
must be clean, on `pages`, have an `origin` remote, and not share their git
directory with the Codeberg folder; `propagate-pages` stops at once if one
of them does not. The make targets and `tools/propagate-pages.sh` use
different variable names for some of the same folders:

| Folder | Default path | Branch | Another path with |
| :-- | :-- | :-- | :-- |
| Codeberg pages worktree | `../created_with_eee-pages-worktree` (next to this repository) | `pages` | `PAGES_DIR` (make targets), `CODEBERG_PAGES_DIR` (`propagate-pages`) |
| GitHub pages worktree | `~/work/greek/git/github/EEE-project/created_with_eee-pages-worktree` | `pages` | `GITHUB_PAGES_DIR` |
| GitLab unified pages worktree | `~/work/greek/git/gitlab/EEE-project/created_with_eee-pages-worktree` | `pages` | `GITLAB_UNIFIED_PAGES_DIR` (make targets), `GITLAB_PAGES_DIR` (`propagate-pages`) |
| GitLab split projects, one clone each (`python3 tools/_split_courses.py projects` lists them) | `~/work/greek/git/gitlab/EEE-project/<project>` | `pages` | `SPLIT_PROJECTS_DIR` (make targets), `GITLAB_SPLIT_DIR` (`propagate-pages`) |
| GitHub mirror checkout, for `sync-main` | `~/work/greek/git/github/EEE-project/created_with_eee` | `main`, remote `codeberg` | none (fixed in `tools/push.sh`) |
| GitLab mirror checkout, for `sync-main` | `~/work/greek/git/gitlab/EEE-project/created_with_eee` | `main`, remote `codeberg` | none (fixed in `tools/push.sh`) |

**Set up the folders once.** Clone over HTTPS (no key is needed to read), then
make `origin` the SSH address: the scripts push through `origin`. The `codeberg`
remote of a mirror checkout stays on HTTPS, so `sync-main` fetches Codeberg
without your key.

```bash
# Codeberg pages worktree, next to this repository
git worktree add ../created_with_eee-pages-worktree pages

# GitHub: the mirror checkout (for sync-main) and the pages worktree next to it
git clone https://github.com/EEE-project/created_with_eee.git ~/work/greek/git/github/EEE-project/created_with_eee
git -C ~/work/greek/git/github/EEE-project/created_with_eee remote set-url origin git@github.com:EEE-project/created_with_eee.git
git -C ~/work/greek/git/github/EEE-project/created_with_eee remote add codeberg https://codeberg.org/EEE-project/created_with_eee.git
git -C ~/work/greek/git/github/EEE-project/created_with_eee worktree add ../created_with_eee-pages-worktree pages

# GitLab: the same steps with gitlab.com and ~/work/greek/git/gitlab/EEE-project/,
# then one clone per split project, on `pages`
git clone https://gitlab.com/EEE-project/created-with-eee-odyssey.git ~/work/greek/git/gitlab/EEE-project/created-with-eee-odyssey
git -C ~/work/greek/git/gitlab/EEE-project/created-with-eee-odyssey remote set-url origin git@gitlab.com:EEE-project/created-with-eee-odyssey.git
git -C ~/work/greek/git/gitlab/EEE-project/created-with-eee-odyssey checkout pages
```

**Commands.** A *key use* is one SSH fetch or push, or one signed commit. If
your key asks for a confirmation on each use, you confirm that many times. The
times are what a run took on 2026-10-15, key uses included.

| Command | What it changes | Key uses | Takes about | Check afterwards |
| :-- | :-- | :-- | :-- | :-- |
| `make export-notebooks NOTEBOOKS="..."` | the lesson folders in the Codeberg pages worktree (each is cleared, then written again); commits nothing | 0 | one marimo export per lesson | `make check-embedded-data`; `git status` in the worktree |
| `make propagate-pages` | one signed commit in each of the GitHub, GitLab unified and three split folders that changes; pushes nothing | 1 (fetch of Codeberg `pages`) + 1 per commit, 6 at most | 3 minutes | `git log -1 --format='%h %G?'` in each folder |
| `make propagate-pages ARGS="github --push"` | repeats the preparation for GitHub (the folder is reset to Codeberg `pages`, the signed commit is made again), then force-pushes `pages:pages` to GitHub | 3: fetch, signature, push | 1 minute | `git ls-remote https://github.com/EEE-project/created_with_eee.git refs/heads/pages`; wait for the Pages build (2 minutes), then `make verify-pages-deploy SITE=GitHub` (see the rebuild rule below) |
| `make propagate-pages ARGS="gitlab --push"` | repeats the preparation for the GitLab unified project and force-pushes it; pushes the three split projects (a commit that an earlier dry run made is pushed as it is) | 6 after a dry run: fetch, 1 signature, 4 pushes; 9 without one | 3 minutes | `git ls-remote` of the four projects; wait for their Pages pipelines (1 minute), then `make verify-pages-deploy` |
| `make sync-main ARGS=github` | resets the GitHub mirror checkout to Codeberg `main`, converts it with `codeberg2github.sh`, makes one signed commit and force-pushes it to GitHub `main` | 2: signature, push | 1 minute | `git ls-remote https://github.com/EEE-project/created_with_eee.git refs/heads/main` shows a new commit whose parent is Codeberg `main` |
| `make sync-main ARGS=gitlab` | the same with `codeberg2gitlab.sh`; the script allows a force-push to GitLab `main` only while it pushes | 2 | 1 minute | the same check on `gitlab.com`; `glab api projects/EEE-project%2Fcreated_with_eee/protected_branches/main` must show `"allow_force_push":false` |
| `make sync-pages-export`, `sync-hub-pages`, `fix-split-roots`, `fix-gitlab-unified-scope`, `fix-static-footer`, `fix-split-hub-links` (the steps `propagate-pages` runs for you), and `make gen-hub` | files in the folders above only; they never commit or push | 0 | seconds | `git status` and `git diff` in each folder |
| `make verify-pages-deploy [SITE=...]`, `make check-hub-links [URL=...]`, `make check-embedded-data [SCOPE=...]` | nothing (read-only) | 0 | seconds | exit status 0 |

`make sync-main` without `ARGS` first pushes this repository's current branch
and its tags to Codeberg (one more key use), then does GitHub and GitLab.
The three mirror `main` branches differ on purpose: each mirror is Codeberg's
`main` plus one conversion commit.

**Rules that save time**

- If git fails while it waits for your key (a missed confirmation, a locked
  key), that command pushes nothing. Run the same command again.
  `gpg: signing failed: End of file` means the signing key did not answer:
  unlock it and run the command again. Nothing was committed.
- Do one host at a time and check it before the next one: `github`, check,
  `gitlab`, check. Push and check Codeberg `pages` before any mirror (step 3
  above).
- `--push` repeats the whole preparation. A dry run lets you review the
  commits, but it does not save key uses: the GitHub and GitLab unified
  commits are made again.
- The output is long: about 14,500 lines for `gitlab`, about 42,000 for all
  hosts with `--verbose`. If your terminal or tool keeps only part of it, send
  it to a file (`make propagate-pages ARGS="gitlab --push" > /tmp/propagate.log 2>&1`).
- A force-push to GitHub's `pages` branch usually starts a Pages build, but
  sometimes it starts none: the site then stays on the old commit with the
  status `built`. `make verify-pages-deploy SITE=GitHub` prints the commit of
  the latest build. If it is not the pushed commit after 3 minutes, queue a
  build and check again:
  `gh api --method POST repos/EEE-project/created_with_eee/pages/builds`.
- After `sync-main`, compare the tips with `git ls-remote`. When the mirror
  checkout is missing or has uncommitted changes, the script prints `⚠️ ...
  skipping GitHub sync` (or GitLab) and still exits 0.
- `sync-main ARGS=gitlab` allows the force-push to GitLab `main` only for the
  push, and switches it off again even when the push fails. After a sync, still
  check it with the `glab api` command in the table. If it shows `true`, set
  it back:
  `glab api --method PATCH projects/EEE-project%2Fcreated_with_eee/protected_branches/main -f allow_force_push=false`.
- To undo a pages push for GitHub or for the GitLab unified project, force-push
  the previous tip (`git -C <folder> push --force <ssh-url> <previous-sha>:pages`;
  `git reflog` in the folder shows the SHA), then check the site as above. The
  three GitLab split projects refuse force pushes: commit a revert in the
  project folder and push it normally.

### Export one lesson with and without the embedded data

The export embeds a lesson's text data files (TSV, Markdown, YAML) by default
(step 2 above), so the page makes no request for them while it starts. PDFs,
images, `index.tsv`, `ga.json` and files of other repositories stay run-time
fetches. `ARGS=--no-embed` gives the plain export: the page then downloads the
text files while it starts, as before. To compare the two, export the lesson
twice into scratch folders, not into the pages worktree:

```bash
make export-notebooks PAGES_DIR=/tmp/wasm-with    NOTEBOOKS="ancient_greek/odyssey/2026_07_06/notebook.py"
make export-notebooks PAGES_DIR=/tmp/wasm-without NOTEBOOKS="ancient_greek/odyssey/2026_07_06/notebook.py" ARGS=--no-embed
```

Each export lands in `<PAGES_DIR>/<the lesson's folder>/`. Serve that folder
(`python3 -m http.server --directory /tmp/wasm-with/ancient_greek/odyssey/2026_07_06`),
open it, and filter the browser's Network tab by `raw`. The page without the
embedded data downloads the lesson's data files; the page with it downloads
`index.tsv` and `ga.json`, and the PDFs, images and files of other repositories
that the lesson asks for. `make check-embedded-data` checks the embedding rules
and the data cell of every lesson.

### What's automated (reference)

`make help` lists what's automated for syncing content across hosts —
currently: syncing `main` (`make sync-main`, see `tools/push.sh`),
re-exporting notebooks to the `pages` branch (`make export-notebooks`, see
`tools/export-notebooks.py`), copying that export into every other host's
checkout (`make sync-pages-export`, see `tools/sync-pages-export.py`),
regenerating a hub's static index page (`make gen-hub`, see
`tools/gen_hub.py`), copying that into every other host's checkout (`make
sync-hub-pages`, see `tools/sync-hub-pages.py`), re-applying the
split-course session-page fix (`make fix-split-roots`), re-applying the
static-hub footer-host fix (`make fix-static-footer`), re-applying the
split-project hub card-link fix (`make fix-split-hub-links`, see
`tools/fix-split-hub-card-links.py`), re-applying GitLab's unified-project
scope after a reset of its `pages` branch (`make fix-gitlab-unified-scope`,
see `tools/fix-gitlab-unified-pages-scope.py`: removes the split-off courses,
points their hub cards at their own GitLab projects, restores the CI file),
checking whether Pages deployments are actually live rather than just pushed
(`make verify-pages-deploy`, see `tools/verify-pages-deploy.py`), and
checking that no hub card, back link or asset is dead on any host (`make
check-hub-links`, see `tools/check-hub-links.py`), and checking the data files
that each export embeds (`make check-embedded-data`, see
`tools/check-embedded-data.py`). All but the last three
only stage local changes or run already-established scripts;
`verify-pages-deploy`, `check-hub-links` and `check-embedded-data` are
read-only and make no local changes at all.

For a complete propagation of an already-correct Codeberg `pages` branch,
including all GitLab split projects, use:

```bash
tools/propagate-pages.sh           # prepare and commit every destination locally
tools/propagate-pages.sh --push    # additionally push each changed destination
tools/propagate-pages.sh -v --push # show every command while pushing
```

Through Make, pass script options with `ARGS` (use `--verbose` or `-v`;
`make -v` means Make's own version option):

```bash
make propagate-pages ARGS="--push"
make propagate-pages ARGS="github --push" # GitHub only
make propagate-pages ARGS="gitlab --push"  # GitLab unified + split repos
```

`--verbose` prints every shell command, about 42,000 lines for a full run;
leave it off unless you need the trace.

With no host argument, `propagate-pages` defaults to `all`. The explicit
`all` selector is also accepted.

Remote fetches and pushes (in `tools/propagate-pages.sh` and in `tools/push.sh`,
which `make sync-main` runs) use separate commands for each host:
`GIT_CMD_CODEBERG`, `GIT_CMD_GITHUB`, and `GIT_CMD_GITLAB` (each defaults to
`git`). Authentication wrappers remain personal environment settings rather
than being embedded in the repository script. You can export them in the
environment or put them in the repository-root `.env` file, which is ignored
by Git. For example:

```bash
GIT_CMD_CODEBERG="codeberg-git" \
GIT_CMD_GITHUB="github-git" \
GIT_CMD_GITLAB="gitlab-git" \
make propagate-pages ARGS="--push"
```

This covers GitHub's unified Pages project, GitLab's unified Pages project,
and the Odyssey, Palaestra, and b1glc split GitLab Pages projects. It runs
the export, hub, GitLab scope, split-root/link, and host URL/footer tools.
Destination worktrees must be clean and checked out on `pages`.
The script automatically removes the exact canonical untracked `.gitlab-ci.yml`
left by the GitLab unified-scope repair; any other uncommitted or untracked
content still stops the run.

The propagation script commits locally; `--push` is the only mode that pushes.
All maintainer scripts live under `tools/`.

**Not yet automated**: splitting a new course off into its own GitLab
project (see each split course's own README for GitLab's 1GB
Pages-per-project limit that drove the split) — still a manual, multi-step
process. The split-off courses are listed once, in `tools/_split_courses.py`:
add a row there and the sync, hub, GitLab-scope and link tools, `make`,
`propagate-pages.sh` and `codeberg2gitlab.sh` pick it up (the hub-card link fix
in the Makefile and `propagate-pages.sh` still names the B1 project). The
GitLab project itself, its Pages settings and its `.gitlab-ci.yml` (a copy of
`tools/gitlab-ci-pages.yml`) are still set up by hand.

### Course deployment (notebook source change → live pages)

A change to a notebook's own source (new/edited cells) is frozen at
`marimo export html-wasm` time — unlike a pure `eee-project` library fix,
which every already-deployed page picks up live from PyPI on next load, a
source change needs re-exporting and redeploying everywhere the affected
course is hosted. Full procedure (step 7 is automated by `make
propagate-pages` — see the Quick start above; the manual route stays for
single-host work):

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

6. **Commit + push the Codeberg pages branch**.

7. **Copy the same export into every other checkout that hosts the
   affected course(s)**, then review and commit + push each
   (one host at a time):
   ```bash
   make sync-pages-export NOTEBOOKS="modern_greek/ellinika_b/chapter_01/chapter_01_notebook.py ..."
   ```
   Destination layout differs per host (see `tools/sync-pages-export.py`):
   - **GitHub** — full mirror, same content as Codeberg.
   - **GitLab unified project** (`created_with_eee`) — mirrored too, except
     a split-off course is skipped there (GitLab's 1GB Pages-per-project cap
     drove the split below) — `modern_greek/ellinika_b/` is what's left
     un-split.
   - **GitLab split projects** — the matching course's directories only,
     flattened to each project's root (no `ancient_greek/` or
     `modern_greek/...` prefix):
     - `created-with-eee-odyssey` ← `ancient_greek/odyssey/`
     - `created-with-eee-palaestra` ← `ancient_greek/palaestra/ancient_greek.2026.summer/`
     - `created-with-eee-b1glc` ← `modern_greek/b1greeklanguageandculture/{kapodistrias,kavafis_ithaki,zorba}/`

   Run `make fix-split-roots` afterward for any split-project destination
   touched.

8. **Wait for GitLab Pages' CI pipeline** on every GitLab target (a push
   alone doesn't deploy there) — poll until it succeeds:
   ```bash
   glab api "projects/EEE-project%2F<repo>/pipelines?ref=pages&per_page=1"
   ```

9. **Verify live**, per host, with a real browser check (not just an HTTP
   200) — the exported bundle needs Pyodide to actually boot before the
   page is meaningfully "up".

### Hub deployment (title/hero/switcher/index.tsv change → live pages)

A hub page (root, category, or course card-list index) is static HTML from
`tools/gen_hub.py`, not a WASM export — see `tools/gen_hub.py`'s own module
comment before touching any of the 10 hubs' config. The cycle is shorter
than a notebook's, since there's no Pyodide boot to wait for:

1. Ship the source change (`tools/gen_hub.py`'s `HUBS` dict, or the
   affected course's `index.tsv`) to `main` via the normal branch+PR
   workflow, then `make sync-main`.
2. `make gen-hub HUBS="<hub keys>"` (default: all 10) into the Codeberg
   pages worktree — review with `git status`/`git diff`, commit + push.
3. `make sync-hub-pages HUBS="<hub keys>"` to copy the regenerated
   `index.html` files into GitHub / GitLab-unified / each affected GitLab
   split project's checkout — review, commit + push each by hand
   (one host at a time). Destination layout follows the
   same split-course rules as `sync-pages-export` (see
   `tools/sync-hub-pages.py`). On GitLab-unified, run `make
   fix-gitlab-unified-scope` first: the copied hubs link the split courses
   (Odyssey, Palaestra, B1's three courses) by paths that don't exist there,
   and it points those cards at the courses' own GitLab projects.
4. Wait for GitLab Pages' CI pipeline on every GitLab target touched (step
   8 above).
5. Verify live — `make verify-pages-deploy` confirms each host's deployed
   commit matches what was pushed; `make check-hub-links` crawls every
   host's hubs and fails on any dead card, back link or asset; a quick
   `curl`/browser check confirms the actual rendered content.

## EEE (Ελληνικά Εκπαιδευτικά Εργαλεία — Greek Language Educational Tools)

🔓 Open source:
- prod — https://github.com/EEE-project/
- prod mirror — https://gitlab.com/EEE-project/
- dev — https://codeberg.org/EEE-project/

💬 Community: https://telegram.me/eee_greek
