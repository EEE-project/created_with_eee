# created_with_eee

Interactive Greek-language courses and notebooks built on the
[EEE](https://github.com/EEE-project/eee-project) morphology framework. No
installation required, open directly in your Telegram messenger:

https://telegram.me/eee_project_greek_bot/created_with_eee

or web-browser:

https://molab.marimo.io/notebooks/nb_n9Es7EWQdEkMKCLcKwpTjg/app

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

**Αρχαία Ελληνικά — Ancient Greek**
- **Odyssey** (`ancient_greek/odyssey/`) — reading course through Homer's
  *Odyssey* Book IX, one lesson per lecture: Greek text with clickable
  word-by-word glosses, rhythm (ictus) markup, multiple literary translations
  side by side, and paradigm/vocabulary drills.
- **Palaestra** (`ancient_greek/palaestra/`) — Ancient Greek for beginners.

**Σύγχρονα Ελληνικά — Modern Greek**
- **Ελληνικά Β** (`modern_greek/ellinika_b/`) — chaptered course following the
  Ελληνικά Β textbook.
- **B1: Ελληνική Γλώσσα και Πολιτισμός** (`modern_greek/b1greeklanguageandculture/`)
  — Greek language and culture, including lessons about the Kapodistrias,
  Zorba, and Kavafis' Ithaki.

Every course shares the same underlying drill/quiz machinery from
[eee-project](https://github.com/EEE-project/eee-project); each course
directory has its own `AGENTS.md` documenting its structure and content
sources.

## EEE (Ελληνικά Εκπαιδευτικά Εργαλεία — Greek Language Educational Tools)

🔓 Open source:
- prod — https://github.com/EEE-project/
- prod mirror — https://gitlab.com/EEE-project/
- dev — https://codeberg.org/EEE-project/

💬 Community: https://telegram.me/eee_greek
