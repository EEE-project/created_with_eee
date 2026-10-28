# Language files of this folder

`notebook.py` is the source notebook: it holds the text of all languages and a language selector.
`python -m eee_project.split_lesson` made one notebook for each language from it. A language notebook has the same cells in the same order.
It differs from the source in the language selector (fixed to one language), 21 dict values and 0 if-chains: the text of the other languages is empty there.

## Files by language

| Language | Notebook | Other files of this language |
|:--|:--|:--|
| Russian (`ru`) | `notebook_ru.py` | `vocab_IX_152-180_ru.tsv`, `../eee_note_ru.md` |
| Greek (`el`) | `notebook_el.py` | `vocab_IX_152-180_el.tsv`, `../eee_note_el.md` |
| English (`en`) | `notebook_en.py` | `vocab_IX_152-180_en.tsv`, `../eee_note_en.md` |

The list shows the files that were in the folder when the notebooks were made, without the files that git ignores.
The translation texts (`translations_<language>.md`) are downloaded from the knowledge base when a notebook runs. Git ignores them.

## Files for all languages

`notebook.py`, `Od_IX_152-180.pdf`, `Od_IX_152-180_vocabula.pdf`, `greek.md`, `ictus.html`, `meeting7_vase.jpg`, `translation_presence.tsv`

## Rules

- In a language notebook, change only the text of its language.
- To bring the changed texts back into `notebook.py`: run `python -m eee_project.join_lesson notebook.py` (it shows what would change), then `python -m eee_project.join_lesson notebook.py --write`.
- To change any other line: (1) join as above; (2) change `notebook.py`; (3) delete the language notebooks and make them again.
