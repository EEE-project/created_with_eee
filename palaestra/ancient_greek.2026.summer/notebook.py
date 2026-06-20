# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.23.3",
#     "eee-project @ git+https://codeberg.org/EEE-project/eee-project.git",
# ]
#
# [tool.uv.sources]
# eee-project = { git = "https://codeberg.org/EEE-project/eee-project.git" }
# ///

import marimo

__generated_with = "0.23.9"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    from eee_project import ConfigStore, eee_topbar
    _ROOT = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main"
    cfg = ConfigStore.from_url(
        f"{_ROOT}/palaestra/ancient_greek.2026.summer/lessons.tsv",
        ga=f"{_ROOT}/ga.json",
    )
    eee_topbar(mo, back_url=cfg.index_url(), lang="ru", titles="Palaestra", style="index",
               ga_config=cfg.ga_config())
    return (cfg,)


@app.cell(hide_code=True)
def _(mo):
    mo.Html("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Syne:wght@400;700;800&display=swap');
    .eee-hero { text-align: center; padding: 32px 16px 24px; font-family: Syne, sans-serif; }
    .eee-series {
      font-family: "DM Mono", monospace; font-size: 11px; color: #003d82;
      letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 10px;
    }
    .eee-title {
      font-size: 26px; font-weight: 800; letter-spacing: -0.02em;
      background: linear-gradient(90deg, #003d82, #5f27cd);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
      margin-bottom: 6px;
    }
    .eee-subtitle { font-size: 14px; color: #666; }
    </style>
    <div class="eee-hero">
      <div class="eee-title">Древнегреческий язык, начальный уровень</div>
      <div class="eee-series">Palaestra · Лето 2026</div>
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo, cfg):
    _LESSONS = [
        {
            "icon": _l["icon"],
            "nb": _l["nb_id"],
            "label": _l["label"],
            "title": _l["title"],
            "greek": _l["greek"],
            "desc": _l["desc"],
        }
        for _l in cfg.lessons()
    ]

    _cards = []
    for _l in _LESSONS:
        _url = _l["nb"] if _l["nb"].startswith("http") else f"https://molab.marimo.io/notebooks/{_l['nb']}/app" if _l["nb"] else None
        if _url:
            _inner = f"""<a class="eee-card" href="{_url}" target="_blank">
            <div class="eee-card-header">
              <div class="eee-card-icon">{_l['icon']}</div>
              <div>
                <div class="eee-card-label">{_l['label']}</div>
                <div class="eee-card-title">{_l['title']}</div>
                <div class="eee-card-greek">{_l['greek']}</div>
              </div>
            </div>
            <div class="eee-card-desc">{_l['desc']}</div>
            <div class="eee-card-arrow">◀</div>
          </a>"""
        else:
            _inner = f"""<div class="eee-card eee-card-disabled">
            <div class="eee-card-header">
              <div class="eee-card-icon">{_l['icon']}</div>
              <div>
                <div class="eee-card-label">{_l['label']}</div>
                <div class="eee-card-title">{_l['title']}</div>
                <div class="eee-card-greek">{_l['greek']}</div>
              </div>
            </div>
            <div class="eee-card-desc">{_l['desc']}</div>
            <div class="eee-card-arrow">скоро</div>
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
