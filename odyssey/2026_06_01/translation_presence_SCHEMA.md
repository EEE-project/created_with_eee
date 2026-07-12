# translation_presence.tsv — field reference

Answer key for the "слово в переводе" (word-in-translation) exercise in `notebook.py`. The
exercise shows a student one Greek word plus one translator's rendering of the whole stanza it
occurs in, and asks yes/no: does the translation reflect that word? This file is the ground
truth it grades against.

Plain UTF-8 TSV (tab-separated), one header row. Safe to open in LibreOffice Calc / Excel
(import as tab-delimited) or any plain-text editor that preserves tabs exactly.

## Columns

| Column | Editable? | Meaning |
|---|---|---|
| `lemma` | No — generated | Dictionary/citation form of the word, e.g. `ἀνήρ`. |
| `form` | No — generated | The exact inflected surface form as it appears in the poem, e.g. `Ἄνδρα` (accusative singular of `ἀνήρ`). |
| `stanza_ref` | No — generated | Which verse-group this specific occurrence is in, e.g. `I.1–5`. A word used in more than one stanza gets **one row per occurrence** — each independently reviewable, since the same word can be handled differently by a translator in different passages. |
| `translator` | No — generated | Which translator's rendering is being judged: `Жуковский` (1849, verse) or `Вересаев` (1953, prose) — the two literary Russian translations in this lesson. (The подстрочник/word-for-word interlinear gloss is deliberately excluded — "is this word reflected" only makes sense against a real literary translation, not a literal gloss.) |
| `reflected` | **Yes — this is the only field to fill in** | See below. |

## Filling in `reflected`

Exactly one of three values, lowercase, no quotes:

- **`yes`** — the translator's rendering of the *whole stanza* (not just the word's own line —
  translators render verse-block units, not individual lines) conveys this word's meaning, even
  if loosely, paraphrased, or via a different but semantically-connected Russian word.
- **`no`** — the concept is genuinely omitted from that rendering, or substantially changed/
  dropped.
- **blank** (`""`, the starter default) — not yet reviewed. Leave blank if genuinely unsure.
  Blank rows are automatically excluded from the quiz — never silently graded as "no".

**Worked example:** row `ἀνήρ / Ἄνδρα / I.1–5 / Жуковский / (blank)`. Жуковский's rendering of
I.1–5 opens "Муза, скажи мне о том многоопытном **муже**, который...". "муже" reflects
`ἀνήρ`/`Ἄνδρα` → `yes`.

## Regeneration is safe — never overwrites your work

The notebook re-syncs this file on every run (`GreekUtils.sync_translation_presence_tsv`), but
it's an upsert, not an overwrite:

- A row you've already filled in keeps your value, byte-for-byte, on every future regeneration.
- New words or new occurrences (e.g. if the vocab list grows) get appended as new blank rows —
  existing rows are never touched.
- If a word or occurrence stops existing (removed from vocab, or the poem text changes), its row
  is **comment-prefixed** (`lemma` gets a leading `#`) rather than deleted, so your review isn't
  lost if it comes back later. Comment-prefixed rows are automatically excluded from the quiz —
  you don't need to do anything with them, just leave them as-is.

## Current state

176 rows, all reviewed (166 `yes` / 10 `no`) as of 2026-07-11. Content words only (nouns, verbs,
adjectives, adverbs, proper names) — function words (particles, conjunctions, prepositions,
pronouns) are excluded by design, since "is this function word reflected" isn't a meaningful
question for a literary translation. **Confirmed exclusion 2026-07-12:** when `"pronoun"` was
briefly added to `_TP_CONTENT_POS` as part of unrelated pronoun-POS work elsewhere in the
project, `sync_translation_presence_tsv` correctly appended 54 new pronoun rows — reverted on
review, since the design principle above already covers pronouns. Those 54 rows are now
comment-prefixed (`#`) in the TSV, not deleted, per the upsert behavior documented below.
