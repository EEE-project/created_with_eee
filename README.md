# Interactive learning materials created with EEE

Examples of interactive Greek-language course materials in notebook form,
built on the [EEE](https://github.com/EEE-project/eee-project) morphology
framework. No installation required — open directly in your browser:

1. **product** — [GitHub Pages](https://eee-project.github.io/created_with_eee/)
2. **mirror** — [GitLab Pages](https://eee-project.gitlab.io/created_with_eee/)
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

## EEE (Ελληνικά Εκπαιδευτικά Εργαλεία — Greek Language Educational Tools)

🔓 Open source:
- prod — https://github.com/EEE-project/
- prod mirror — https://gitlab.com/EEE-project/
- dev — https://codeberg.org/EEE-project/

💬 Community: https://telegram.me/eee_greek
