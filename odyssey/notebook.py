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
def _(mo):
    from eee_project import ConfigStore, eee_topbar
    _ROOT = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main"
    cfg = ConfigStore.from_url(
        f"{_ROOT}/odyssey/lessons.tsv",
        ga=f"{_ROOT}/ga.json",
    )
    eee_topbar(mo, back_url=None, lang="ru", titles={
        "ru": "Одиссея для отважных",
    }, style="index", ga_config=cfg.ga_config())
    return (cfg,)


@app.cell(hide_code=True)
def _(cfg, mo):
    def _make_card(lesson):
        _nb_id = lesson["nb_id"]
        _url = f"https://molab.marimo.io/notebooks/{_nb_id}/app" if _nb_id else None
        if _url:
            return f"""<a class="eee-card" href="{_url}" target="_blank" rel="noopener">
              <div class="eee-card-header">
                <div class="eee-card-icon">{lesson['icon']}</div>
                <div>
                  <div class="eee-card-label">{lesson['label']}</div>
                  <div class="eee-card-title">{lesson['desc']}</div>
                </div>
              </div>
              <div class="eee-card-desc">{lesson['title']}</div>
              <div class="eee-card-arrow">◀</div>
            </a>"""
        return f"""<div class="eee-card eee-card-disabled">
          <div class="eee-card-header">
            <div class="eee-card-icon">{lesson['icon']}</div>
            <div>
              <div class="eee-card-label">{lesson['label']}</div>
              <div class="eee-card-title">{lesson['desc']}</div>
            </div>
          </div>
          <div class="eee-card-desc">{lesson['title']}</div>
          <div class="eee-card-arrow">скоро</div>
        </div>"""

    _cards = "\n".join(_make_card(l) for l in cfg.lessons())

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
    .eee-card-desc { font-size: 13px; color: #666; line-height: 1.5; }
    .eee-card-arrow {
      text-align: right; margin-top: 10px;
      font-family: "DM Mono", monospace; font-size: 11px; color: #5f27cd;
    }
    </style>
    """ + _cards)
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
