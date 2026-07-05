# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "eee-project @ git+https://codeberg.org/EEE-project/eee-project.git",
#     "marimo>=0.23.13",
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
        f"{_ROOT}/ellinika_b/lessons.tsv",
        ga=f"{_ROOT}/ga.json",
    ).ga_config()
    eee_topbar(mo, back_url=None, lang=lang_sel.value, titles={
        "ru": "EEE", "el": "EEE", "en": "EEE",
    }, style="index", ga_config=_ga)
    return


@app.cell(hide_code=True)
def _(lang_sel, mo):
    _HERO = {
        "ru": ("Курсы греческого языка", "Интерактивные тетради"),
        "el": ("Μαθήματα ελληνικής γλώσσας", "Διαδραστικά Τετράδια"),
        "en": ("Greek Language Courses", "Interactive Notebooks"),
    }
    _title, _subtitle = _HERO.get(lang_sel.value, _HERO["en"])
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
def _(lang_sel, mo):
    _lang = lang_sel.value
    _COURSES = [
        {
            "icon": "📖",
            "nb": "nb_WwAH5TcPv1GwasoBu8rM8b",
            "greek": "Ελληνικά Β",
            "label": {"ru": "Современный греческий Б", "el": "Σύγχρονα Ελληνικά Β", "en": "Modern Greek B"},
            "title": {"ru": "Ελληνικά Β — Интерактивные тетради", "el": "Ελληνικά Β — Διαδραστικά Τετράδια", "en": "Ελληνικά Β — Interactive Notebooks"},
            "desc": {
                "ru": "10 интерактивных уроков по главам учебника Ελληνικά Β. Словарь, существительные, глаголы, прилагательные.",
                "el": "10 διαδραστικά μαθήματα βασισμένα στα κεφάλαια του Ελληνικά Β. Λεξιλόγιο, ουσιαστικά, ρήματα, επίθετα.",
                "en": "10 interactive lessons based on chapters from Ελληνικά Β. Vocabulary, nouns, verbs, adjectives.",
            },
        },
        {
            "icon": "🏛️",
            "nb": "nb_DvTBdMDLxtKzYCY5cgTgRb",
            "greek": "Καποδίστριας",
            "label": {"ru": "B1: Греческий язык и культура", "el": "B1: Ελληνική Γλώσσα και Πολιτισμός", "en": "B1: Greek Language and Culture"},
            "title": {"ru": "Серия уроков — Каподистриас", "el": "Σειρά μαθημάτων — Καποδίστριας", "en": "Lesson series — Kapodistrias"},
            "desc": {
                "ru": "Уроки B1 на основе истории Иоанниса Каподистриаса. Словарь, грамматика, культура.",
                "el": "Μαθήματα B1 βασισμένα στην ιστορία του Ιωάννη Καποδίστρια. Λεξιλόγιο, γραμματική, πολιτισμός.",
                "en": "B1 lessons based on the story of Ioannis Kapodistrias. Vocabulary, grammar, culture.",
            },
        },
        {
            "icon": "🏛",
            "nb": "nb_dNfJMtygPUh5dhfXA44AbJ",
            "greek": "Παλαίστρα",
            "label": {"ru": "Древнегреческий язык", "el": "Αρχαία Ελληνικά", "en": "Ancient Greek"},
            "title": {"ru": "Παλαίστρα — Лето 2026", "el": "Παλαίστρα — Καλοκαίρι 2026", "en": "Palaestra — Summer 2026"},
            "desc": {
                "ru": "Введение в древнегреческий язык для начинающих. Алфавит, грамматика, чтение.",
                "el": "Εισαγωγή στα αρχαία ελληνικά για αρχάριους. Αλφάβητο, γραμματική, ανάγνωση.",
                "en": "Introduction to Ancient Greek for beginners. Alphabet, grammar, reading.",
            },
        },
        {
            "icon": "🏺",
            "nb": "nb_kfCNB7ejMPX5EUj3AHTZWV",
            "greek": "Ὀδύσσεια Α.1–21",
            "label": {"ru": "Древнегреческий с Гомером", "el": "Αρχαία Ελληνικά με τον Όμηρο", "en": "Ancient Greek with Homer"},
            "title": {"ru": "Одиссея — Пробный урок", "el": "Οδύσσεια — Δοκιμαστικό Μάθημα", "en": "Odyssey — Pilot Lesson"},
            "desc": {
                "ru": "Чтение Одиссеи I.1–21 с морфологическим анализом, парадигмами и переводом.",
                "el": "Ανάγνωση Οδύσσειας Α.1–21 με μορφολογική ανάλυση, παραδείγματα και μετάφραση.",
                "en": "Reading the Odyssey I.1–21 with morphological analysis, paradigms, and translation.",
            },
        },
    ]

    _SOON = {"ru": "скоро", "el": "σύντομα", "en": "coming soon"}
    _cards = []
    for _c in _COURSES:
        _url = f"https://molab.marimo.io/notebooks/{_c['nb']}/app" if _c["nb"] else None
        _label = _c['label'].get(_lang, _c['label']['en'])
        _title_text = _c['title'].get(_lang, _c['title']['en'])
        _desc_text = _c['desc'].get(_lang, _c['desc']['en'])
        if _url:
            _inner = f"""<a class="eee-card" href="{_url}">
            <div class="eee-card-header">
              <div class="eee-card-icon">{_c['icon']}</div>
              <div>
                <div class="eee-card-label">{_label}</div>
                <div class="eee-card-title">{_title_text}</div>
                <div class="eee-card-greek">{_c['greek']}</div>
              </div>
            </div>
            <div class="eee-card-desc">{_desc_text}</div>
            <div class="eee-card-arrow">◀</div>
          </a>"""
        else:
            _soon = _SOON.get(_lang, "soon")
            _inner = f"""<div class="eee-card eee-card-disabled">
            <div class="eee-card-header">
              <div class="eee-card-icon">{_c['icon']}</div>
              <div>
                <div class="eee-card-label">{_label}</div>
                <div class="eee-card-title">{_title_text}</div>
                <div class="eee-card-greek">{_c['greek']}</div>
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


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
