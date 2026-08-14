# Changelog

## 2026-08-14
- `modern_greek/ellinika_b/chapter_03`: added a dedicated pronoun test (Test 4),
  alongside the existing adjective test. κανένας is engine-mismatched as an
  adjective (the Adjective engine mis-declines it; `Pronoun('κανένας').all()`
  already gets it right) -- moved to the new pronoun-only test. ίδιος/μόνος
  are genuinely dual-class and stay in both tests. New Test 4 section mirrors
  Test 3's structure; requires `eee-project>=1.7.1`. Also fixes Test 3's own
  missing `adj_meta`/`active_slots` threading, which would have broken once a
  newer `eee-project` reaches PyPI.
