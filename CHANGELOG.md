# Changelog

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
