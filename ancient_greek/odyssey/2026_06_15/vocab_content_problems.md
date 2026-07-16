# vocab_IX_19-38.tsv — content problems

Tokens in the poem that don't match any vocab entry (after normalization).

## Two-word form (same pattern as 2723's `πεφυγμένος ἦεν`)

Row 97: `οὔ ποτε	οὔ ποτε	adv	…	никогда`

The phrase is an indivisible adverb meaning "never". Consequence: `ποτε` appears
as an individual poem token (IX.33: `ἐμὸν οὔ ποτε θυμὸν`) but won't be highlighted
because WORDS_COMBINED stores `ου ποτε` as a single string. `οὔ` is covered by
its own separate entry (row 81).

## Content problems

| token in poem | norm | closest vocab form | issue |
|---|---|---|---|
| `δέ` / `δὲ` | `δε` | `δ᾽` (norm: `δ`) | only elided form in vocab; full `δέ`/`δὲ` not covered |
| `μοι` | `μοι` | — | dative of ἐγώ, not in vocab |
| `πολυκηδέ'` | `πολυκηδε` | `πολυκηδέα` (norm: `πολυκηδεα`) | poem has elided form (α dropped); vocab has full acc. form |
| `ἐνί` | `ενι` | `ἐν` (norm: `εν`) | Homeric `ἐνί` (= ἐν + ι) vs standard `ἐν` |
| `ὅν` | `ον` | — | relative/possessive pronoun, not in vocab |
| `Δουλίχιόν` | `Δουλιχιον` | — | island name (IX.22), not in vocab |
| `Ζάκυνθος` | `Ζακυνθος` | — | island name (IX.22), not in vocab |
| `Σάμη` | `Σαμη` | — | island name (IX.22), not in vocab |
| `Ζεύς` | `Ζευς` | — | nom. of Ζεύς (IX.38: `ὅν μοι Ζεὺς ἐφέηκε`), not in vocab |
| `Κίρκη` | `Κιρκη` | — | nom. of Κίρκη (IX.31), not in vocab |
