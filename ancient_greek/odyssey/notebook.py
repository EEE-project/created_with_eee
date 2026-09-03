# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "eee-project>=1.1.0",
#     "marimo>=0.23.14",
# ]
# ///

import marimo

__generated_with = "0.23.14"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    from eee_project import ConfigStore, eee_topbar
    from eee_project.notebook_utils import parent_back_url
    _ROOT = "https://raw.githubusercontent.com/EEE-project/created_with_eee/main"
    cfg = ConfigStore.from_file_or_url(
        __file__,
        f"{_ROOT}/ancient_greek/odyssey/index.tsv",
        ga=f"{_ROOT}/ga.json",
    )
    back_url = parent_back_url(f"{_ROOT}/ancient_greek/index.tsv")
    eee_topbar(mo, back_url=back_url, lang="ru", titles={
        "ru": "Одиссея с Гомером",
    }, parent_titles={
        "ru": "Αρχαία Ελληνικά", "el": "Αρχαία Ελληνικά", "en": "Ancient Greek",
    }, style="index", ga_config=cfg.ga_config(), same_window=True)
    return (cfg,)


@app.cell(hide_code=True)
def _(cfg, mo):
    from eee_project.notebook_utils import eee_card_list
    eee_card_list(mo, cfg, "ru", lang_fallback="ru", same_window=True)
    return


@app.cell(hide_code=True)
def _(mo):
    from eee_project.notebook_utils import eee_footer
    eee_footer(mo, lang="ru")
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
