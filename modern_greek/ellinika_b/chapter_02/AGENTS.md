# Chapter 2 — Σπίτι μου σπιτάκι μου
## Agent & Integration Notes

**Textbook:** Ελληνικά Β' | **Level:** B1 | **Theme:** Housing and residence

---

## Grammar Focus

### 1. Articles (Άρθρα)
Definite (ο/η/το) and indefinite (ένας/μία/ένα) across all three genders, singular and plural.

### 2. Indirect Object Pronouns
Weak (clitic) and strong (emphatic) forms of genitive-case pronouns used as indirect objects:
- Weak: μου, σου, του/της, μας, σας, τους
- Strong: εμένα, εσένα, αυτού/αυτής, εμάς, εσάς, αυτών

### 3. Genitive Case for Possession
Used to express ownership. Question word: ποιανού / τίνος (whose).

### 4. Possessive Pronouns (δικός μου)
Pattern: [Article] + δικός/δική/δικό + [Weak Pronoun]. Used for emphasis or to distinguish ownership.

---

## Test Types

| Type | File | Count | Modes |
|------|------|-------|-------|
| NOUNS | `nouns.tsv` | 37 | Simple (Nom/Acc/Gen Sg+Pl), Article (Def+Ind) |
| VERBS | `verbs.tsv` | 16 | Present, Imperfect, Simple Past, Simple Future, Continuous Future |
| ADJECTIVES | `adjectives.tsv` | 14 | Simple (6 fields), Complex (18 fields) |

---

## Vocabulary Categories

- **Housing types:** κατοικία, σπίτι, διαμέρισμα, γκαρσονιέρα, δυάρι, τριάρι
- **Tenancy:** ιδιοκτήτης, ενοικιαστής, ενοικίαση, ενοίκιο, συμβόλαιο, εγγύηση, κοινόχρηστα
- **Rooms:** δωμάτιο, υπνοδωμάτιο, κουζίνα, μπάνιο, σαλόνι, καθιστικό, τραπεζαρία
- **Parts of house:** πάτωμα, τοίχος, ταβάνι, καλοριφέρ, θέρμανση, σωλήνας
- **Moving/maintenance:** μετακόμιση, συγκατοίκηση, συγκάτοικος, ζημιά, επισκευή, έπιπλο, μάστορας
- **Verbs:** νοικιάζω, μετακομίζω, επισκευάζω, τακτοποιώ, μοιράζομαι, παραπονιέμαι, υπογράφω, συμφωνώ
- **Adjectives:** επιπλωμένος, ευρύχωρος, λογικός, κατάλληλος, καινούριος, παλιός

---

## EEE Integration

- **Library:** modern-greek-eee (Codeberg development branch)
- **Noun test:** `create_noun_test_ui` / `process_noun_test` — two modes (simple + article)
- **Verb test:** `create_verb_test_ui` / `check_verb_test` — manual state management
- **Adjective test:** `create_adjective_test_ui` / `check_adjective_test` / `process_adjective_completion`
- **TSV format:** `Word\tTranslation` (English headers, Greek words)
