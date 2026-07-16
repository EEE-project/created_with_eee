# vocab_I_1-21.tsv — content problems

Tokens in the poem that don't match any vocab entry (after normalization fixes and bug fixes).

| token in poem | location | vocab form | issue |
|---|---|---|---|
| `πόντι'` (πόντιος, "sea-nymph") | I.14 | `πότνι᾽` (πότνια, "lady/mistress") | **different words** — poem text and vocab entry disagree on the reading |
| `νόστου` (gen.) | I.13: `νόστου κεχρημένον` | `νόστον` (acc., I.5) | different case of same lemma; second occurrence not covered |
| `ἔνθα` (full form) | I.18: `οὐδ' ἔνθα πεφυγμένος` | `Ἔνθ᾽` (elided, I.11) | same adverb, elided vs full form; second occurrence not covered |
| `πεφυγμένος` / `ἦεν` | I.18 | `πεφυγμένος ἦεν` (two-word form) | vocab intentionally uses the phrase; individual tokens won't be highlighted |
| `Ὀδυσῆι` (dat.) | I.21 | — | proper name, absent from vocab entirely |

## Note: two-word vocab forms

The entry `πεφυγμένος ἦεν` (I.18) is intentionally kept as a phrase in the `form` column,
with the translation "избежал (плюскв.)" covering the whole construction.

Consequence: "все слова" coverage highlighting matches by individual token. A two-word form
is stored as a single string with a space and will never match either `πεφυγμένος` or `ἦεν`
alone. Both tokens will appear unhighlighted in the poem even though the phrase is in the vocab.

This is by design — the phrase is a pluperfect periphrasis (perf. ptcp. + impf. of εἰμί),
and splitting it into two entries would lose the grammatical note and misrepresent the
translation.

## Fixed in this session

- `ἑτάρους` (acc. pl., I.6) — added as separate entry (Homeric contracted form `ἑτάρ-` vs standard `ἑταῖρ-`)
