# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.23.14",
#     "eee-project>=1.1.0",
# ]
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
        f"{_ROOT}/ancient_greek/palaestra/ancient_greek.2026.summer/index.tsv",
        ga=f"{_ROOT}/ga.json",
    )
    back_url = parent_back_url(f"{_ROOT}/ancient_greek/index.tsv")
    eee_topbar(mo, back_url=back_url, lang=lang_sel.value, titles={
        "ru": "Палестра",
        "en": "Palaestra",
        "el": "Παλαίστρα",
    }, parent_titles={
        "ru": "Αρχαία Ελληνικά", "el": "Αρχαία Ελληνικά", "en": "Ancient Greek",
    }, style="index", ga_config=cfg.ga_config(), same_window=True)
    return (cfg,)


@app.cell(hide_code=True)
def _(lang_sel, mo):
    _TXT = {
        "ru": ("Древнегреческий язык, начальный уровень", "Palaestra · Лето 2026"),
        "en": ("Ancient Greek, Beginner Level", "Palaestra · Summer 2026"),
        "el": ("Αρχαία Ελληνικά, Επίπεδο Αρχαρίων", "Παλαίστρα · Καλοκαίρι 2026"),
    }
    _title, _series = _TXT.get(lang_sel.value, _TXT["ru"])
    mo.Html(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Syne:wght@400;700;800&display=swap');
    .eee-hero {{ text-align: center; padding: 32px 16px 24px; font-family: Syne, sans-serif; }}
    .eee-series {{
      font-family: "DM Mono", monospace; font-size: 11px; color: #003d82;
      letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 10px;
    }}
    .eee-title {{
      font-size: 26px; font-weight: 800; letter-spacing: -0.02em;
      background: linear-gradient(90deg, #003d82, #5f27cd);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
      margin-bottom: 6px;
    }}
    .eee-subtitle {{ font-size: 14px; color: #666; }}
    </style>
    <div class="eee-hero">
      <div class="eee-title">{_title}</div>
      <div class="eee-series">{_series}</div>
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(cfg, lang_sel, mo):
    from eee_project.notebook_utils import eee_card_list
    eee_card_list(mo, cfg, lang_sel.value, lang_fallback="ru", same_window=True)
    return


@app.cell(hide_code=True)
def _(lang_sel, mo):
    from eee_project.notebook_utils import eee_footer
    eee_footer(mo, lang=lang_sel.value)
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    lang_sel = mo.ui.dropdown(
        options={"English": "en", "Русский": "ru", "Ελληνικά": "el"},
        value="English",
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


if __name__ == "__main__":
    app.run()
