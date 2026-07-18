# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "eee-project @ git+https://codeberg.org/EEE-project/eee-project.git",
#     "marimo>=0.23.14",
# ]
#
# [tool.uv.sources]
# eee-project = { git = "https://codeberg.org/EEE-project/eee-project.git" }
# ///

import marimo

__generated_with = "0.23.13"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(lang_sel, mo):
    from eee_project import ConfigStore, eee_topbar
    from eee_project.notebook_utils import parent_back_url
    _ROOT = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main"
    cfg = ConfigStore.from_file_or_url(
        __file__,
        f"{_ROOT}/modern_greek/lessons.tsv",
        ga=f"{_ROOT}/ga.json",
    )
    back_url = parent_back_url(f"{_ROOT}/lessons.tsv")
    eee_topbar(mo, back_url=back_url, lang=lang_sel.value, titles={
        "ru": "Σύγχρονα Ελληνικά", "el": "Σύγχρονα Ελληνικά", "en": "Modern Greek",
    }, parent_titles={
        "ru": "EEE", "el": "EEE", "en": "EEE",
    }, style="index", ga_config=cfg.ga_config())
    return (cfg,)


@app.cell(hide_code=True)
def _(lang_sel, mo):
    from eee_project.notebook_utils import eee_hero
    eee_hero(mo, lang_sel.value, {
        "ru": ("Σύγχρονα Ελληνικά", "Курсы современного греческого языка"),
        "el": ("Σύγχρονα Ελληνικά", "Μαθήματα σύγχρονης ελληνικής γλώσσας"),
        "en": ("Modern Greek", "Modern Greek language courses"),
    })
    return


@app.cell(hide_code=True)
def _(cfg, lang_sel, mo):
    from eee_project.notebook_utils import eee_card_list
    eee_card_list(mo, cfg, lang_sel.value)
    return


@app.cell(hide_code=True)
def _(lang_sel, mo):
    from eee_project.notebook_utils import eee_footer
    eee_footer(mo, lang=lang_sel.value)
    return


@app.cell(hide_code=True)
def _(mo):
    lang_sel = mo.ui.dropdown(
        options={"Ελληνικά": "el", "Русский": "ru", "English": "en"},
        value="Ελληνικά",
        label="🌐",
    )
    mo.Html(f"""
    <div style="position:fixed;top:56px;right:12px;z-index:1000;
                background:white;padding:6px 10px;border-radius:8px;
                box-shadow:0 2px 8px rgba(0,0,0,.12);">
      {lang_sel}
    </div>
    """)
    return (lang_sel,)


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
