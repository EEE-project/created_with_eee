# Changelog

## 2026-08-19
- Added `verify-pages-deploy.py`, a standalone script that checks whether
  created_with_eee's Pages deployments are actually serving current content
  across all 6 known sites (Codeberg/GitHub/GitLab for the main repo, plus
  the three GitLab split projects: odyssey, palaestra, b1glc) -- a clean
  `git push` to a `pages` branch is not evidence the site updated. Built
  after GitHub's legacy Pages build got silently stuck "building" for 24+
  hours after a transient 503 from GitHub's own deploy API, with zero
  signal from the push itself. Cross-checks the legacy builds API against
  the Actions run for the same commit (the builds API can show "building"
  forever even after the Actions run actually succeeded) via `gh`, checks
  the latest pipeline for GitLab's CI/CD-based Pages via `glab`, and falls
  back to a live no-store fetch (status/last-modified/etag) everywhere,
  since Codeberg has no deploy-status API at all. Tested against the
  current, already-verified-healthy deployment state: all 6 sites report
  `[OK]` (or `[--]` for Codeberg, by design).

## 2026-08-17
- Removed the "Load nouns/verbs/adjectives/pronouns TSV" upload buttons from
  every ellinika_b chapter (01-12, including its `_el`/`_en`/`_ru` legacy
  source variants) and both kavafis_ithaki lessons -- 91 buttons across 37
  files total. First pass only matched the English "Load ... TSV" label
  text (37 buttons, 19 files); a second pass caught 54 more that used
  Greek/Russian labels or a different English wording/argument order the
  first regex didn't anticipate ("Φόρτωση TSV ουσιαστικών", "Upload nouns
  TSV", `mo.ui.file(filetypes=..., label=...)`). Each vocab table now
  always loads straight from its bundled TSV, the same fallback path every
  notebook already used when no file had been uploaded -- the override was
  never used in practice and only added a confusing extra control above
  each table. kapodistrias and zorba keep their upload widgets (never asked
  to remove them there).
- Added `eee_project` 1.8.0's `GreekUtils.vocab_table()`/`load_vocab_table()`
  (see eee-project's own changelog) and migrated every call site in the
  repo to use them instead of hand-rolled `mo.ui.table(...)`/
  `ensure_file()`+`pd.read_csv()`/`os.path.join()`+`try`-`except` code --
  189 table-construction sites and 186 load-fallback sites across 63 files
  (all of ellinika_b, kavafis_ithaki, kapodistrias, zorba). Each course's
  own quirks (kapodistrias/zorba's upload-widget override, some `_ru`
  variants unconditionally preferring the Russian file over checking the
  interface language, chapters without `RAW_BASE`/remote-fetch) are
  preserved exactly via the new helpers' `file_upload=`/`ru_variant=`/
  `language=`/`remote_base=` parameters -- a pure refactor, no behavior
  change. Verified: `py_compile` + `marimo check` clean across all 65
  files in the four affected course directories; live end-to-end retest of
  the κεμπάπ fix (search, select, fill all 6 fields, submit) on chapter_06
  after the full migration; kapodistrias smoke-tested to confirm its
  upload widget and bundled-file fallback both still work. `ruff` caught a
  real side effect of the load-cell migration: 26 `_el`/`_en`/`_ru` files'
  shared setup cell imports `pandas` only to hand it down to the old
  `pd.read_csv(...)` load cells -- now unneeded, `ruff --fix` removed the
  30 now-dead imports (`os` stays; still used locally for `notebook_dir`).

## 2026-08-16
- Every vocabulary-selection table (`mo.ui.table(df_noun/df_verb/df_adj/
  df_pron/..., selection="multi", ...)`) across every course notebook now
  passes `page_size=len(<df>)`, so the table shows every row on one
  scrollable page instead of paginating at marimo's default 10/page (max
  selectable via the "Rows per page" dropdown is 100 -- chapter_06's 135
  nouns didn't fit even at that ceiling). Reported live: a word deep in a
  long list (γαλακτοκομικά, row 106 of 135) was easy to miss when paging
  manually rather than using the search box; this removes the need to page
  or search at all. 190 call sites across 61 files (all of ellinika_b,
  kavafis_ithaki, kapodistrias, zorba). No `page_size` was previously set
  on any of these calls. Verified live on chapter_06: all three tables
  (135/74/7 rows) now render with zero pagination controls.

## 2026-08-15
- Fixed `adjective_paradigm_drill_form()`'s missing `adj_meta` threading in
  14 more notebooks -- `chapter_03` got this fix on 2026-08-14 (see below),
  but every other adjective test in the repo still called the function
  without `adj_meta`, which has been a required argument since
  `eee-project` v1.7.0. Any of them crashed with `TypeError: missing 1
  required keyword-only argument: 'adj_meta'` the instant a student picked
  a word to practice -- reported live from `chapter_04`. Audited every
  `adjective_paradigm_drill_form()` call site in the repo and fixed the
  same gap in `modern_greek/ellinika_b/chapter_01/02/06/07/08/09/11/12`,
  `ancient_greek/palaestra/ancient_greek.2026.summer/2026_07_03/07/10`,
  and `modern_greek/b1greeklanguageandculture/kavafis_ithaki/1/2`.

## 2026-08-14
- `modern_greek/ellinika_b/chapter_03`: added a dedicated pronoun test (Test 4),
  alongside the existing adjective test. κανένας is engine-mismatched as an
  adjective (the Adjective engine mis-declines it; `Pronoun('κανένας').all()`
  already gets it right) -- moved to the new pronoun-only test. ίδιος/μόνος
  are genuinely dual-class and stay in both tests. New Test 4 section mirrors
  Test 3's structure; requires `eee-project>=1.7.1`. Also fixes Test 3's own
  missing `adj_meta`/`active_slots` threading, which would have broken once a
  newer `eee-project` reaches PyPI.
