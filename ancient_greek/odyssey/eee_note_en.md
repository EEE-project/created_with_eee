Built with [EEE](https://telegram.me/eee_greek) — a system for building interactive learning materials.
The morphological-analysis modules build word-form tables from a set of lexicons (stem dictionaries and
attested forms); see the documentation in
[ancient-greek-backend-eee](https://codeberg.org/EEE-project/ancient-greek-backend-eee) and
[eee-project](https://codeberg.org/EEE-project/eee-project) for details:

* **homer** — the Homeric corpus (Iliad, Odyssey): 2322 verb + 15 noun stems
* **morpheus** — forms independently confirmed by the Perseids Morpheus analyzer, for lemmas that the
  dictionary lexicons can't cover (athematic, contract, deponent verbs, etc.):
  46 verb + 62 noun lemmas
* **odyssey_morpheus** — forms from this Odyssey course's own vocabulary, not covered by the other lexicons,
  also confirmed by Perseids Morpheus: 56 verb + 59 noun + 57 adjective lemmas
* **pratt / ltrg** — teaching lexicons (Pratt, LTRG): 22 + 34 verb, 26 noun stems
* **lsj** — from LSJ and Wiktionary: 9 verb + 18 noun stems
* **lxx** — the Septuagint: 1905 verb stems
* **morphgnt** — the Greek New Testament: 1848 verb stems
* **byzantine** — Sophocles' dictionary (1887), Byzantine deviations from Koine/Attic: 61 lemmas

The periods on the timeline of the Greek language are combinations of the lexicons above:

* **Epic** · ~8th c. BCE — homer + morpheus + odyssey_morpheus
* **Classical Attic** · 5th–4th c. BCE — pratt + ltrg + lsj
* **Hellenistic Koine** · 4th–1st c. BCE — lxx
* **Roman Koine** · 1st–3rd c. CE — morphgnt
* **Byzantine** · 4th–15th c. CE — lxx + morphgnt + pratt + ltrg + lsj, with byzantine as a layer of differences on top
* **Modern Greek** · 16th c. – present — [modern-greek-backend-eee](https://codeberg.org/EEE-project/modern-greek-backend-eee), a separate rule-based engine (not a lexicon, full paradigm coverage for any lemma)

Also connected: [unimorph-backend-eee](https://codeberg.org/EEE-project/unimorph-backend-eee) — the
UniMorph database (2224 nouns + 207 adjectives; no verbs; coverage skewed toward New Testament texts).

In the word-form table you can switch between lexicons from different historical periods,
whenever the system has matching data for that word.
