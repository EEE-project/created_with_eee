# Changelog

## 2026-08-26 (2)
- Fixed grammar explanations and translations in ellinika_b chapters 9, 11,
  and 12, found via cross-AI review reports (analisys/ellinika_b1/ch{09,11,
  12}.md) and verified page-by-page against the source textbook, continuing
  the same pass that covered chapters 6-8 (see 2026-08-25 (3) below). ch09:
  the "Simple Future = one completed action" comparison note recurring in
  its own Continuous Future cell, the Tenses-in-Context table's column
  headers literally mislabeling Future-tense rows as "Past," an
  indirect-questions rule missing the yes/no-uses-αν case, and translated
  the el branch's four grammar/pronunciation cells into actual Greek (same
  untranslated-duplicate pattern as ch06's -δες cell -- the fourth, the
  Φωνή-γραφή/elision cell, was missed by an initial byte-identity check
  since it differed from the en branch by two table alternates, not zero,
  and was only caught on a later pass). ch11: the Simple Subjunctive's
  "same stem as Simple Future, swap θα for να" framing (checked against the
  book's own pp. 168-169 -- pure example lists and bare formation tables,
  no such prose rule at all), and a conditional section that collapsed the
  book's own two explicitly-labeled patterns (open condition vs.
  invitation/advice) into one undifferentiated table. ch12: a notebook-only
  "same stem" sentence that also mixed a 2nd-person conjugated form (τρως)
  into what was presented as "the stem," and "Once / completed" /
  "Ongoing / repeated" table headers where the book's own labels (checked
  against p. 192) are the bare "μία φορά" / "συνέχεια συχνά," no
  completion/repetition claim attached.

  ch12 in particular turned out to be a striking check-before-fixing case:
  of 6 items both reviewers flagged as high-confidence, 4 were verified
  word-for-word against book pages 188-192 and found to be the textbook's
  own stated framing -- including "Φοβάμαι ότι = certainty," which the book
  glosses explicitly as "Είμαι σχεδόν σίγουρος" (I am almost certain).
  Neither reviewer had access to the book to catch this.

## 2026-08-26
- Fixed broken hub-card links to the 3 GitLab-split courses (odyssey,
  palaestra, b1greeklanguageandculture) on the GitLab-hosted copy of the
  unified project's ancient_greek/modern_greek hub pages -- reported live as
  a 404 on eee-project.gitlab.io/created_with_eee/ancient_greek/odyssey/.
  gen_hub.py had no host-awareness at all: every hub card's href is read
  verbatim from index.tsv as a root-relative path, which is correct on
  Codeberg/GitHub (where these 3 courses live at that path) but wrong on
  GitLab specifically, since all 3 were deliberately split into their own
  GitLab projects for the 1GB Pages-per-project cap (see README). Fixed by
  baking a small client-side host check into gen_hub.py's own template
  (matching the same live-hostname-detection pattern eee_footer()'s "Source"
  link and the 2026-08-25 eee_lang fix already use, rather than a
  fragile post-generation hand-patch): affected cards get a
  `data-gitlab-href` pointing at the split project's own Pages URL, and a
  small inline script swaps it in only when `location.hostname ===
  'eee-project.gitlab.io'` -- Codeberg and GitHub keep the unmodified
  root-relative href. Verified via Playwright with real route interception
  (not a `location` object mock, which Chromium doesn't allow overriding) at
  both the true GitLab hostname and a non-GitLab one. Regenerating the two
  affected hubs also incidentally picked up an unrelated, already-committed
  source fix (Odyssey's Russian title in ancient_greek/index.tsv had said
  "Одиссея для отважных" since at least 2026-08-05, but the deployed hub was
  never regenerated to pick it up) -- hub regeneration is a manual step per
  the README, so this kind of drift is expected until it's automated.

## 2026-08-25 (3)
- Fixed grammar explanations and translations in ellinika_b chapters 6-8,
  found via cross-AI review reports (analisys/ellinika_b1/ch0{6,7,8}.md)
  and verified page-by-page against the source textbook before changing
  anything. ch06: the aorist stress-rule sentence (claimed an exact "3rd
  syllable" position rather than a ceiling), the -δες plural "one rule
  across all genders" framing (conflates the masc/fem -δ- patterns with
  the unrelated neuter -ατα pattern), and translated the el branch's -δες
  grammar cell into actual Greek (it had been left as an untranslated
  duplicate of the English branch). ch07: the augment rule wrongly said
  "monosyllabic" stems (ru already correctly said "two-syllable"; neither
  cited example, παίζω/γράφω, is monosyllabic), the -αν/ε ending notation
  (book uses -αν(ε)), and an elision bracket reading [ε-, ι-] while its
  own table lists a η-initial example (το ήξερε). ch08: the Simple
  Future's "single, completed action" definition (conflates completion
  with perfective aspect, same issue as ch06/ch07's tense definitions), an
  overly narrow θα αγοράζω gloss, a stale "Πώς κάνεις έτσι;" translation
  that didn't match the chapter's own already-verified
  extracted_content.md, an absolute "often colloquial" framing on the
  -ης/-α/-ικο adjective type, and a wind-direction list missing the head
  noun on ανατολικός/δυτικός. Left untouched: several other reviewer-
  flagged items that turned out to be faithful transcriptions of the book
  itself -- the conditional clause's "χωρίς το θα" phrasing is the
  textbook's own verbatim wording; γκρινιάρης's blank Gen.Pl.Fem. cell,
  ανεβαίνω/κατεβαίνω's dual future forms, and μικρούλης's inclusion in the
  adjective list are all exactly as printed.

## 2026-08-25 (2)
- Removed the "Open in molab" badge from every notebook's title cell
  (41 files across ellinika_b, odyssey, palaestra, kapodistrias,
  kavafis_ithaki, zorba, and the modern_greek hub) -- content is served
  from self-hosted WASM Pages now, not molab, and the badges pointed at
  molab uploads that are no longer the primary way students reach a
  lesson. Per AGENTS.md, the badge was always "a separate, optional
  convenience link... no connection to index.tsv or to whether the lesson
  is actually live on Pages" -- removing it doesn't touch deployment.
  Three distinct removal shapes depending on how the badge was wired in:
  a `_badge` variable interpolated into a title string (ellinika_b,
  kapodistrias, kavafis_ithaki, zorba), `_badge` rendered as its own
  `mo.md(_badge)` list element (odyssey), or the badge markdown inlined
  directly with no variable at all (palaestra, modern_greek hub -- the
  latter's badge was its own standalone cell, removed entirely rather
  than left empty). The two code comments elsewhere describing molab's
  file-bundling behavior (odyssey, kavafis_ithaki) are about a real,
  separate authoring gotcha and were left untouched. Verified live
  (marimo check clean repo-wide; a 5-notebook sample spanning every
  removal shape executes with zero errors).

## 2026-08-25
- Added `athenaze_cap1_adjs.yaml`/`athenaze_cap2_adjs.yaml`, Palaestra's
  Athenaze chapters I/II adjective lexicons (`2026_06_09`'s notebook
  already wired both filenames into its `AncientGreekBackend(lexicons=...)`
  call; only the data files themselves were missing). Every form
  cross-checked against Perseids Morpheus; `μικρός`/`σκαιός` use full
  `forms:` overrides where the stems/accents mechanism gets the "α-purum"
  genitive/dative singular feminine wrong (ᾱ instead of computed η). Also
  wrapped a long inline `mo.md()` materials line onto its own multi-line
  f-string in three other 2026 Palaestra lessons (06_12, 06_16, 06_19) for
  readability, and bumped their `__generated_with` marimo version string.

## 2026-08-24
- Rolled out chapter_08's nav_icons/show_prev_when_done pos-test and
  phrase-quiz UI polish (see 2026-08-22 below) to the other 9 `ellinika_b`
  chapters (01,02,03,04,06,07,09,11,12), and unified the phrase quiz's
  duplicated per-mode state into one shared set of `mo.state()` pairs
  (`cv_phrase`, `remaining_phrase`, `score_phrase`, `restore_phrase`,
  `history_phrase`, `future_phrase`, `checked_phrase_d`) used by both "type
  the answer" and "multiple choice" modes — previously each mode tracked
  its own separate state, which could silently drift (e.g. mismatched
  score/position when switching modes mid-quiz). `GreekUtils` construction
  now takes `config=dataclasses.replace(MODERN_GREEK, nav_icons=True,
  show_prev_when_done=True)` once per notebook instead of repeating both
  kwargs at every call site (~130 occurrences removed); see `eee_project`
  1.10.0's own changelog and AGENTS.md's new "Course-wide GreekConfig
  customization" section for the mechanism. Each chapter's `eee-project`
  PEP-723 dependency bumped to `>=1.10.0` to match. Verified live: all 10
  chapters' example notebooks execute cleanly end to end (554 cells, zero
  errors) against the updated `eee-project`.
- Added two Claude Code skills for this repo's own workflow:
  `verify-pages` (drives headless Playwright across Codeberg/GitHub/GitLab
  to confirm hub navigation and a real WASM lesson boot, not just an HTTP
  200) and `ship-eee-change` (the full commit-branch-PR-merge-mirror-sync
  workflow, written specifically because mirror sync has been missed on
  this repo three separate times).

## 2026-08-23
- Grammar/transcription fixes in `ellinika_b` chapters 2-4, cross-checked
  against the source textbook: chapter_02's extracted content had a missing
  accent (`το τηλέφωνο του` → `το τηλέφωνό του`) and mis-described its own
  vowel-drop rule (elision of the *verb's* vowel before ε-, not the pronoun
  suffix's); chapter_03's ίδιος/τέτοιος/τόσος demonstrative table showed
  `τόσος`'s masc. accusative as bare `τόσον`, now `τόσο(ν)` matching the
  other two rows' parenthesized-final-ν convention, applied across the
  notebook and its `_el`/`_en`/`_ru` sources; chapter_03's `η οδός` gained a
  distinguishing note (`street (formal, + name)`) against `ο δρόμος`;
  chapter_04's extracted content fixed a verb form (`Ακολουθήστε` →
  `Ακολουθήσατε`) and softened an overstated invariance claim about
  καφετής/καφετιά/καφετί. Also disambiguated chapter_04's φαρδύς/πλατύς and
  παχύς/χοντρός adjective pairs (both previously flattened to identical
  "wide"/"fat, thick" translations — the same collision class as the
  2026-08-21 vocab fix below) across `adjectives.tsv`, `adjectives_ru.tsv`,
  and `vocabulary.tsv`.

## 2026-08-22
- Fixed chapter_08's phrase quiz showing "Select at least 4 phrases for a
  real multiple-choice quiz" in "Type the answer" mode too, blocking it with
  as few as 1-3 phrases selected even though free-text answers have no
  multiple-choice-style minimum -- the `< 4` gate applied regardless of
  `phrase_mode`, when it should only ever apply to the multiple-choice mode
  it names. Now checks the truly-empty case first (`phrases_empty`, unused
  until now despite being added alongside the feature) and gates the `< 4`
  message on `phrase_mode.value == "choice"` specifically.
- Added a "warn"-colored (orange) Check button to the phrase quiz's "Type
  the answer" mode, live as-you-type, and reordered its Prev/Next buttons to
  bare ◀/▶ triangles flanking Check, hidden (not greyed out) at a history
  boundary -- e.g. ◀ is simply absent on the first phrase, reappearing once
  there's history to go back to -- both via new opt-in `eee_project` 1.9.1
  parameters (`word_drill_check_button`, `nav_icons=True`) that leave every
  other `word_drill_widgets`/`word_drill_form` caller (Odyssey's word-form
  quizzes) unaffected. See eee-project's own changelog for the mechanism,
  including two real bugs this surfaced and fixed in the same pass: a check
  button that recolors live necessarily rebuilds on every check attempt,
  which was erasing the wrong-answer feedback before it ever rendered until
  `word_drill_display` gained a persisted-state fallback for "was this exact
  text just checked"; and a first attempt at the hide-when-disabled nav
  crashed the live notebook outright (`AttributeError`) because a real
  `mo.ui.button` has no readable `.disabled` after construction, unlike the
  test double -- full suite stayed green while the live page threw.
- Verified the phrase quiz's forward/backward navigation across a full
  15-phrase cycle by driving the live notebook through marimo-pair (not
  just clicking around by hand) after a report that some buttons "don't
  get presented" at edge cases. The history walk itself turned out
  correct in both directions, including the seam between replaying
  history and reaching a genuinely new word. But the done screen (all 15
  phrases finished) had two real issues: the restart button showed a bare
  ▶ (visually contradicting its own "Press «Again»" text) -- now shows ↺,
  matching the icon `make_renew_button` already uses elsewhere -- and Prev
  was entirely absent there, so a finished quiz could only restart, never
  be reviewed. Added `show_prev_when_done=True` (new opt-in `eee_project`
  1.9.1 parameter, scoped to this quiz -- Odyssey's word-form quizzes and
  every other caller sharing the same done-screen code keep today's
  restart-only behavior) so Prev now works from the done screen too:
  reviewing the last answer decrements the score/history exactly like
  reviewing any other answered word, and clicking Next again returns
  cleanly to the same done screen. See eee-project's own changelog for
  the mechanism.
- Extended the ◀/▶ triangle nav (hidden, not greyed, at the start of
  history) from "Type the answer" mode to "Multiple choice" mode too, so
  both quiz modes look and behave consistently -- new opt-in
  `eee_project` 1.9.1 `nav_icons=True` on the `word_quiz_widgets`/
  `word_quiz_form` calls, alongside the existing `word_drill_widgets`/
  `word_drill_form` ones. Verified live: ◀ absent on question 1 of a
  5-phrase multiple-choice run, both ◀/▶ present on question 2.
- "Multiple choice" mode's Next button now always advances, whether or
  not a radio option was picked -- previously it only re-rendered the
  same question in place until you chose something, unlike "Type the
  answer" mode (an empty submit there has always just scored wrong and
  advanced). This is `eee_project` 1.9.1's own default `word_quiz_form`
  behavior, not a per-notebook opt-in, so it applies to every other
  Odyssey/Palaestra lesson using multiple-choice quizzes too, not just
  this one -- confirmed explicitly before making it the default rather
  than scoping it here. Verified live: clicking ▶ with nothing selected
  advances (1/4 → 2/4, still 0 correct) and ◀ correctly reviews it back
  as an unanswered question with no radio pre-selected.
- Added text labels back to the ◀/▶ nav triangles (e.g. "◀ Prev",
  "Next ▶", "↺ Again" on the done screen) instead of bare glyphs, and
  confirmed Prev/Next stay first/last in the button row in both quiz
  modes (an `eee_project` 1.9.1 fix ensures this holds even with an
  optional extra button in the row, though this course's own phrase quiz
  doesn't currently use one). Verified live: "◀ Prev" / "Check" /
  "Next ▶" all render correctly, in order, through a full type-answer
  cycle.
- Extended the same ◀/▶/↺ nav treatment to chapter_08's noun/verb/
  adjective "pos tests" (`Test 1: Nouns` / `Test 2: Verbs` / `Test 3:
  Adjectives`), via `eee_project` 1.9.1's `nav_icons=True` now also
  supported on `paradigm_drill_widgets` and the `verb_`/`noun_`/
  `adjective_paradigm_drill_form` calls. In the same pass, `eee_project`
  fixed an unrelated pre-existing bug this surfaced: the English
  translations for these buttons already had triangle icons hardcoded
  into just the English text ("Next ▸", "◂ Prev", "↺ Start over" --
  Russian/Greek were plain), which would have shown doubled-up icons once
  `nav_icons` added its own; now plain in English too, consistent with
  every other language and every other nav button in the course. Verified
  live on the noun test: ◀ Prev appeared once history existed.
- Compared the two test families' button logic directly at the user's
  request after noticing that selecting only one word/phrase left pos
  tests with just a "Check" button, while phrase tests still showed
  "Next" too. Root cause: `paradigm_drill_widgets` disabled Next whenever
  `remaining_len <= 1`, while the phrase quiz's own Next was never
  disabled by remaining count at all -- a genuine, if narrow,
  inconsistency between the two families rather than a bug in either one
  alone (pos tests also never scored a skipped word as wrong the way
  phrase tests do, so there was no scoring reason for the difference).
  Confirmed with the user and fixed in `eee_project` 1.9.1: Next in pos
  tests is no longer disabled at exactly one word remaining, matching the
  phrase quiz -- skipping the sole word via Next now goes straight to the
  done screen, unscored (this family still has no per-word score to get
  wrong on skip). Verified live on the noun test with a single noun
  selected: "Next ▶" was clickable and correctly reached "All nouns done
  for this session!" with "↺ Start over" rendering correctly.
- Chapter_08's noun/verb/adjective "pos tests" (`Test 1: Nouns`/`Test 2:
  Verbs`/`Test 3: Adjectives`) can now be reviewed via Prev from their own
  done screen too, matching the phrase quiz's existing "Type the answer"
  mode -- previously a finished pos-test round only offered "Start over",
  with no way back into the last word answered. New opt-in `eee_project`
  1.9.1 `show_prev_when_done=True` parameter, added to all three pos-test
  call sites, alongside the existing `nav_icons=True`. Found in the same
  pass as the fix: pos-tests' Prev button wasn't just hidden on the done
  screen, it was structurally unreachable there even if rendered -- see
  eee-project's own changelog for the mechanism, and for why a single
  shared function turned out to cover the done *screen* (message, score
  line, buttons) but not the two families' Next-button click-handling,
  which track genuinely different state. Verified live on the noun test
  with a single noun selected: the done screen now shows "◀ Prev"
  alongside "↺ Start over", and clicking it correctly returns to the
  question; re-confirmed the phrase quiz's own done screen is unchanged
  by the underlying refactor ("🎉 All words done! Press «Again» to
  repeat.", "Correct: 0 / 1", "◀ Prev" / "↺ Again").

## 2026-08-21
- Fixed vocab TSV translation collisions across `ellinika_b` and
  `kapodistrias`: pairs of distinct Greek words sharing the exact same
  `Translation` value, which makes them indistinguishable in a quiz/checker
  since the prompt shown is the translation (e.g. `ο μεζές`/`το ορεκτικό`
  both "appetizer"; `η ηλιοφάνεια`/`η λιακάδα` both "солнечная погода").
  Added `check-vocab-collisions.py` (+ `make check-vocab`) to catch this
  mechanically going forward — groups every TSV's rows by `Translation` and
  flags any value shared by 2+ distinct `Word` values. See AGENTS.md's new
  "Vocabulary TSV translation collisions" section for the resolution
  workflow.

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
