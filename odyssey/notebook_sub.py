# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "eee-project @ git+https://codeberg.org/EEE-project/eee-project.git",
#     "marimo>=0.23.9",
# ]
#
# [tool.uv.sources]
# eee-project = { git = "https://codeberg.org/EEE-project/eee-project.git" }
# ///

import marimo

__generated_with = "0.23.9"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(lang_sel, mo):
    from eee_project import ConfigStore, eee_topbar
    _ROOT = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main"
    cfg = ConfigStore.from_url(
        f"{_ROOT}/odyssey/lessons.tsv",
        ga=f"{_ROOT}/ga.json",
    )
    _MAIN_URL = ""  # molab URL of created_with_eee/notebook.py — fill after deployment
    eee_topbar(mo, back_url=_MAIN_URL or None, lang=lang_sel.value, titles={
        "ru": "Древнегреческий с Гомером",
        "en": "Ancient Greek with Homer",
        "el": "Αρχαία Ελληνικά με τον Όμηρο",
    }, ga_config=cfg.ga_config())
    return (cfg,)


@app.cell(hide_code=True)
def _(cfg, lang_sel, mo):
    _lang = lang_sel.value
    _LABELS = {"ru": "Пробный урок", "en": "Pilot Lesson", "el": "Δοκιμαστικό Μάθημα"}
    _TITLES = {
        "ru": "Одиссея I.1–21",
        "en": "Odyssey I.1–21",
        "el": "Οδύσσεια Α.1–21",
    }
    _DESCS = {
        "ru": "Чтение Одиссеи с морфологическим анализом, парадигмами и переводом.",
        "en": "Reading the Odyssey with morphological analysis, paradigms, and translation.",
        "el": "Ανάγνωση Οδύσσειας με μορφολογική ανάλυση, παραδείγματα και μετάφραση.",
    }
    _lesson = cfg.lessons()[0]
    _nb_id = _lesson["nb_id"]
    _url = f"https://molab.marimo.io/notebooks/{_nb_id}/app" if _nb_id else None
    if _url:
        _card = f"""<a class="eee-card" href="{_url}">
          <div class="eee-card-header">
            <div class="eee-card-icon">{_lesson['icon']}</div>
            <div>
              <div class="eee-card-label">{_LABELS.get(_lang, _LABELS['en'])}</div>
              <div class="eee-card-title">{_TITLES.get(_lang, _TITLES['en'])}</div>
              <div class="eee-card-greek">{_lesson['greek']}</div>
            </div>
          </div>
          <div class="eee-card-desc">{_DESCS.get(_lang, _DESCS['en'])}</div>
          <div class="eee-card-arrow">◀</div>
        </a>"""
    else:
        _SOON = {"ru": "скоро", "el": "σύντομα", "en": "coming soon"}
        _card = f"""<div class="eee-card eee-card-disabled">
          <div class="eee-card-header">
            <div class="eee-card-icon">{_lesson['icon']}</div>
            <div>
              <div class="eee-card-label">{_LABELS.get(_lang, _LABELS['en'])}</div>
              <div class="eee-card-title">{_TITLES.get(_lang, _TITLES['en'])}</div>
              <div class="eee-card-greek">{_lesson['greek']}</div>
            </div>
          </div>
          <div class="eee-card-desc">{_DESCS.get(_lang, _DESCS['en'])}</div>
          <div class="eee-card-arrow">{_SOON.get(_lang, 'soon')}</div>
        </div>"""

    mo.Html("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Syne:wght@400;700;800&display=swap');
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
    """ + _card)
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
