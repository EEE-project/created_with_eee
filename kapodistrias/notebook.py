# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "eee-project @ git+https://codeberg.org/EEE-project/eee-project.git",
#     "marimo>=0.23.13",
#     "pandas==3.0.2",
# ]
#
# [tool.uv.sources]
# eee-project = { git = "https://codeberg.org/EEE-project/eee-project.git" }
# ///

import marimo

__generated_with = "0.23.10"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(lang_sel, mo):
    from eee_project import ConfigStore, eee_topbar
    _ROOT = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main"
    _ga = ConfigStore.from_url(
        f"{_ROOT}/kapodistrias/lessons.tsv",
        ga=f"{_ROOT}/ga.json",
    ).ga_config()
    eee_topbar(mo, back_url=None, lang=lang_sel.value, titles={
        "ru": "Каподистриас", "el": "Καποδίστριας", "en": "Kapodistrias",
    }, style="index", ga_config=_ga)
    return


@app.cell(hide_code=True)
def _(lang_sel, mo):
    _TITLES = {
        "ru": ("B1: Греческий язык и культура", "Серия уроков — Каподистриас"),
        "el": ("B1: Ελληνική Γλώσσα και Πολιτισμός", "Σειρά μαθημάτων — Καποδίστριας"),
        "en": ("B1: Greek Language and Culture", "Lesson series — Kapodistrias"),
    }
    _title, _subtitle = _TITLES.get(lang_sel.value, _TITLES["el"])
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
      <div class="eee-series">{_subtitle}</div>
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(lang_sel, mo, pd):
    _lang = lang_sel.value
    _ROOT = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main"
    _lessons_df = pd.read_csv(f"{_ROOT}/kapodistrias/lessons.tsv", sep="\t", keep_default_na=False)
    _LESSONS = [
        {
            "icon": _row["icon"],
            "nb": _row["nb_id"],
            "label": {"ru": _row["label_ru"], "el": _row["label_el"], "en": _row["label_en"]},
            "title": {"ru": _row["title_ru"], "el": _row["title_el"], "en": _row["title_en"]},
            "greek": _row["greek"],
            "desc": {"ru": _row["desc_ru"], "el": _row["desc_el"], "en": _row["desc_en"]},
        }
        for _, _row in _lessons_df.iterrows()
    ]

    _SOON = {"ru": "скоро", "el": "σύντομα", "en": "coming soon"}

    _cards = []
    for _l in _LESSONS:
        _url = _l["nb"] if _l["nb"].startswith("http") else f"https://molab.marimo.io/notebooks/{_l['nb']}/app" if _l["nb"] else None
        _label = _l['label'].get(_lang, _l['label']['el'])
        _title_text = _l['title'].get(_lang, _l['title']['el'])
        _desc_text = _l['desc'].get(_lang, _l['desc']['el'])
        if _url:
            _inner = f"""<a class="eee-card" href="{_url}">
            <div class="eee-card-header">
              <div class="eee-card-icon">{_l['icon']}</div>
              <div>
                <div class="eee-card-label">{_label}</div>
                <div class="eee-card-title">{_title_text}</div>
                <div class="eee-card-greek">{_l['greek']}</div>
              </div>
            </div>
            <div class="eee-card-desc">{_desc_text}</div>
            <div class="eee-card-arrow">◀</div>
          </a>"""
        else:
            _soon = _SOON.get(_lang, "soon")
            _inner = f"""<div class="eee-card eee-card-disabled">
            <div class="eee-card-header">
              <div class="eee-card-icon">{_l['icon']}</div>
              <div>
                <div class="eee-card-label">{_label}</div>
                <div class="eee-card-title">{_title_text}</div>
                <div class="eee-card-greek">{_l['greek']}</div>
              </div>
            </div>
            <div class="eee-card-desc">{_desc_text}</div>
            <div class="eee-card-arrow">{_soon}</div>
          </div>"""
        _cards.append(_inner)

    _html = """
    <style>
    .eee-card, .eee-card-disabled {
      display: block; text-decoration: none; color: #1a1a1a;
      background: #f8f9fa; border: 1px solid #e0e0e0;
      border-radius: 12px; padding: 20px; margin-bottom: 14px;
      font-family: Syne, sans-serif;
      transition: border-color 0.2s, box-shadow 0.2s;
    }
    .eee-card:hover { border-color: rgba(0,61,130,.25); box-shadow: 0 0 18px rgba(0,61,130,.07); }
    .eee-card-disabled { opacity: 0.55; }
    .eee-card-header { display: flex; align-items: center; gap: 12px; margin-bottom: 8px; }
    .eee-card-icon {
      font-size: 26px; width: 46px; height: 46px; flex-shrink: 0;
      display: flex; align-items: center; justify-content: center;
      background: rgba(0,61,130,.06); border-radius: 10px;
    }
    .eee-card-label {
      font-family: "DM Mono", monospace; font-size: 10px; color: #003d82;
      letter-spacing: .12em; text-transform: uppercase; margin-bottom: 2px;
    }
    .eee-card-title { font-size: 16px; font-weight: 700; }
    .eee-card-greek { font-family: "DM Mono", monospace; font-size: 12px; color: #5f27cd; margin-top: 1px; }
    .eee-card-desc { font-size: 13px; color: #666; line-height: 1.5; }
    .eee-card-arrow {
      text-align: right; margin-top: 10px;
      font-family: "DM Mono", monospace; font-size: 11px; color: #5f27cd;
    }
    </style>
    """ + "\n".join(_cards)

    mo.Html(_html)
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
    import pandas as pd
    return mo, pd


if __name__ == "__main__":
    app.run()
