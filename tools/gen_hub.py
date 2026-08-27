"""Generate static HTML for the 10 hub/index pages (root, ancient_greek,
modern_greek, b1greeklanguageandculture, and the 6 course hubs).

These pages are pure navigation -- a topbar, hero, and card grid rendered
from index.tsv, nothing computational -- so unlike lesson pages they don't
need a Pyodide/WASM boot. Reproduces eee_project.notebook_utils's actual
CSS/markup (_TOPBAR_CSS, _HERO_CSS, _CARD_LIST_CSS, _FOOTER_CSS and the
eee_topbar/eee_hero/eee_card_list/eee_footer render shapes) so these pages
are visually identical to what those functions would render, just static.

Run: python3 tools/gen_hub.py [--out-dir DIR]
"""
import argparse
import csv
import json
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent

LANG_OPTIONS = {"Ελληνικά": "el", "Русский": "ru", "English": "en"}
FOOTER_LABEL = {"ru": "Исходный код:", "en": "Source:", "el": "Πηγαίος κώδικας:"}
CARD_LIST_SOON = {"ru": "скоро", "el": "σύντομα", "en": "coming soon"}

# odyssey/palaestra/b1greeklanguageandculture are split into their own GitLab
# projects (1GB Pages-per-project cap -- see README's GitLab Pages section),
# so a hub card's normal root-relative url (correct on Codeberg/GitHub, where
# these courses are NOT split out) 404s when this same generated page is
# deployed to the unified GitLab project. Resolved client-side, matching how
# eee_footer()'s own "Source" link already detects its host at runtime.
GITLAB_SPLIT_OVERRIDES = {
    "/created_with_eee/ancient_greek/odyssey/": "https://eee-project.gitlab.io/created-with-eee-odyssey/",
    "/created_with_eee/ancient_greek/palaestra/ancient_greek.2026.summer/": "https://eee-project.gitlab.io/created-with-eee-palaestra/",
    "/created_with_eee/modern_greek/b1greeklanguageandculture/": "https://eee-project.gitlab.io/created-with-eee-b1glc/",
}

GITLAB_SPLIT_SCRIPT = """<script>
document.addEventListener('DOMContentLoaded', function() {
  if (location.hostname !== 'eee-project.gitlab.io') return;
  document.querySelectorAll('[data-gitlab-href]').forEach(function(el) {
    el.href = el.getAttribute('data-gitlab-href');
  });
});
</script>"""

# Each hub: tsv (its own card-list source), parent_tsv (None for root --
# back_url is a fixed self-badge, not a link), out (destination dir),
# titles/parent_titles (topbar), hero (None to reuse palaestra's hand-rolled
# single-language hero instead), default_lang (initial dropdown selection),
# footer_lang (fixed language for RU-only hubs; None for trilingual ones,
# where it tracks the selector).
HUBS = {
    "root": {
        "tsv": "index.tsv", "parent_tsv": None, "out": ".",
        "titles": {"ru": "EEE", "el": "EEE", "en": "EEE"}, "parent_titles": None,
        "hero": {
            "ru": ("Курсы греческого языка", "Интерактивные тетради"),
            "el": ("Μαθήματα ελληνικής γλώσσας", "Διαδραστικά Τετράδια"),
            "en": ("Greek Language Courses", "Interactive Notebooks"),
        },
        "default_lang": "en", "footer_lang": None,
    },
    "ancient_greek": {
        "tsv": "ancient_greek/index.tsv", "parent_tsv": "index.tsv", "out": "ancient_greek",
        "titles": {"ru": "Αρχαία Ελληνικά", "el": "Αρχαία Ελληνικά", "en": "Ancient Greek"},
        "parent_titles": {"ru": "EEE", "el": "EEE", "en": "EEE"},
        "hero": {
            "ru": ("Αρχαία Ελληνικά", "Курсы древнегреческого языка"),
            "el": ("Αρχαία Ελληνικά", "Μαθήματα αρχαίας ελληνικής γλώσσας"),
            "en": ("Ancient Greek", "Ancient Greek language courses"),
        },
        "default_lang": "el", "footer_lang": None,
    },
    "modern_greek": {
        "tsv": "modern_greek/index.tsv", "parent_tsv": "index.tsv", "out": "modern_greek",
        "titles": {"ru": "Νέα Ελληνικά", "el": "Νέα Ελληνικά", "en": "Modern Greek"},
        "parent_titles": {"ru": "EEE", "el": "EEE", "en": "EEE"},
        "hero": {
            "ru": ("Νέα Ελληνικά", "Курсы современного греческого языка"),
            "el": ("Νέα Ελληνικά", "Μαθήματα σύγχρονης ελληνικής γλώσσας"),
            "en": ("Modern Greek", "Modern Greek language courses"),
        },
        "default_lang": "el", "footer_lang": None,
    },
    "b1greeklanguageandculture": {
        "tsv": "modern_greek/b1greeklanguageandculture/index.tsv",
        "parent_tsv": "modern_greek/index.tsv",
        "out": "modern_greek/b1greeklanguageandculture",
        "titles": {"ru": "B1: Греческий язык и культура", "el": "B1: Ελληνική Γλώσσα και Πολιτισμός", "en": "B1: Greek Language and Culture"},
        "parent_titles": {"ru": "Νέα Ελληνικά", "el": "Νέα Ελληνικά", "en": "Modern Greek"},
        "hero": {
            "ru": ("B1: Греческий язык и культура", "Курс по истории и культуре Греции"),
            "el": ("B1: Ελληνική Γλώσσα και Πολιτισμός", "Μάθημα ιστορίας και πολιτισμού της Ελλάδας"),
            "en": ("B1: Greek Language and Culture", "Course on Greek history and culture"),
        },
        "default_lang": "el", "footer_lang": None,
    },
    "odyssey": {
        "tsv": "ancient_greek/odyssey/index.tsv", "parent_tsv": "ancient_greek/index.tsv",
        "out": "ancient_greek/odyssey",
        "titles": {"ru": "Одиссея с Гомером"}, "parent_titles": {"ru": "Αρχαία Ελληνικά", "el": "Αρχαία Ελληνικά", "en": "Ancient Greek"},
        "hero": None, "default_lang": "ru", "footer_lang": "ru",
    },
    "palaestra": {
        "tsv": "ancient_greek/palaestra/ancient_greek.2026.summer/index.tsv",
        "parent_tsv": "ancient_greek/index.tsv",
        "out": "ancient_greek/palaestra/ancient_greek.2026.summer",
        "titles": {"ru": "Palaestra"}, "parent_titles": {"ru": "Αρχαία Ελληνικά", "el": "Αρχαία Ελληνικά", "en": "Ancient Greek"},
        "hero": {"ru": ("Древнегреческий язык, начальный уровень", "Palaestra · Лето 2026")},
        "default_lang": "ru", "footer_lang": "ru",
    },
    "ellinika_b": {
        "tsv": "modern_greek/ellinika_b/index.tsv", "parent_tsv": "modern_greek/index.tsv",
        "out": "modern_greek/ellinika_b",
        "titles": {"ru": "Ελληνικά Β1", "el": "Ελληνικά Β1", "en": "Ελληνικά Β1"},
        "parent_titles": {"ru": "Νέα Ελληνικά", "el": "Νέα Ελληνικά", "en": "Modern Greek"},
        "hero": {
            "ru": ("Ελληνικά Β1 — Интерактивные тетради", "Уроки современного греческого языка"),
            "el": ("Ελληνικά Β1 — Διαδραστικά Τετράδια", "Μαθήματα σύγχρονων ελληνικών"),
            "en": ("Ελληνικά Β1 — Interactive Notebooks", "Modern Greek language lessons"),
        },
        "default_lang": "en", "footer_lang": None,
    },
    "kapodistrias": {
        "tsv": "modern_greek/b1greeklanguageandculture/kapodistrias/index.tsv",
        "parent_tsv": "modern_greek/b1greeklanguageandculture/index.tsv",
        "out": "modern_greek/b1greeklanguageandculture/kapodistrias",
        "titles": {"ru": "Каподистриас", "el": "Καποδίστριας", "en": "Kapodistrias"},
        "parent_titles": {"ru": "B1: Греческий язык и культура", "el": "B1: Ελληνική Γλώσσα και Πολιτισμός", "en": "B1: Greek Language and Culture"},
        "hero": {
            "ru": ("Каподистриас", "B1: Греческий язык и культура"),
            "el": ("Καποδίστριας", "B1: Ελληνική Γλώσσα και Πολιτισμός"),
            "en": ("Kapodistrias", "B1: Greek Language and Culture"),
        },
        "default_lang": "el", "footer_lang": None,
    },
    "kavafis_ithaki": {
        "tsv": "modern_greek/b1greeklanguageandculture/kavafis_ithaki/index.tsv",
        "parent_tsv": "modern_greek/b1greeklanguageandculture/index.tsv",
        "out": "modern_greek/b1greeklanguageandculture/kavafis_ithaki",
        "titles": {"ru": "Καβάφης — Ιθάκη", "el": "Καβάφης — Ιθάκη", "en": "Kavafis — Ithaki"},
        "parent_titles": {"ru": "B1: Греческий язык и культура", "el": "B1: Ελληνική Γλώσσα και Πολιτισμός", "en": "B1: Greek Language and Culture"},
        "hero": {
            "ru": ("Καβάφης — Ιθάκη", "B1: Греческий язык и культура"),
            "el": ("Καβάφης — Ιθάκη", "B1: Ελληνική Γλώσσα και Πολιτισμός"),
            "en": ("Kavafis — Ithaki", "B1: Greek Language and Culture"),
        },
        "default_lang": "el", "footer_lang": None,
    },
    "zorba": {
        "tsv": "modern_greek/b1greeklanguageandculture/zorba/index.tsv",
        "parent_tsv": "modern_greek/b1greeklanguageandculture/index.tsv",
        "out": "modern_greek/b1greeklanguageandculture/zorba",
        "titles": {"ru": "Алексис Зорбас", "el": "Αλέξης Ζορμπάς", "en": "Alexis Zorbas"},
        "parent_titles": {"ru": "B1: Греческий язык и культура", "el": "B1: Ελληνική Γλώσσα και Πολιτισμός", "en": "B1: Greek Language and Culture"},
        "hero": {
            "ru": ("Алексис Зорбас", "B1: Греческий язык и культура"),
            "el": ("Αλέξης Ζορμπάς", "B1: Ελληνική Γλώσσα και Πολιτισμός"),
            "en": ("Alexis Zorbas", "B1: Greek Language and Culture"),
        },
        "default_lang": "el", "footer_lang": None,
    },
}

# ═══════════════════════════════ CSS, verbatim from eee_project.notebook_utils ══

TOPBAR_CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Syne:wght@400;700;800&display=swap');
#eee-topbar {
  position: sticky; top: 0; z-index: 100;
  height: 48px; background: #f5f5f5;
  border-bottom: 2px solid #003d82;
  display: flex; align-items: center;
  padding: 0 12px; gap: 10px;
  font-family: Syne, sans-serif;
}
#eee-topbar .tb-back {
  font-size: 15px; font-weight: 700; letter-spacing: 0.02em;
  color: #003d82; text-decoration: none;
  padding: 4px 6px; flex: 1;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
#eee-topbar .tb-badge {
  font-family: "DM Mono", monospace; font-size: 12px; font-weight: 700;
  color: #003d82; background: rgba(0,61,130,0.08);
  border: 1px solid rgba(0,61,130,0.3); border-radius: 4px;
  padding: 4px 8px; letter-spacing: 0.1em; text-decoration: none; flex-shrink: 0;
}
</style>"""

BADGE = '<a class="tb-badge" href="https://telegram.me/+VuocC5la3ZwyNDky" target="_blank">EEE Community</a>'

HERO_CSS = """<style>
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
</style>"""

CARD_LIST_CSS = """<style>
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
</style>"""

FOOTER_CSS = """<style>
#eee-footer {
  height: 40px; background: #f5f5f5; border-top: 1px solid #e0e0e0;
  display: flex; align-items: center; justify-content: center; gap: 6px;
  font-family: "DM Mono", monospace;
}
#eee-footer .footer-label { font-size: 10px; color: #1a1a1a; }
#eee-footer a { font-size: 11px; color: #003d82; text-decoration: none; }
</style>"""

PAGE_CSS = """<style>
* { box-sizing: border-box; }
body { margin: 0; font-family: Syne, sans-serif; }
.eee-page { max-width: 640px; margin: 0 auto; padding: 0 16px 16px; }
#lang-picker {
  position: fixed; top: 56px; right: 12px; z-index: 1000;
  background: white; padding: 6px 10px; border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,.12); font-family: Syne, sans-serif; font-size: 13px;
}
#lang-picker select { font-family: inherit; font-size: inherit; border: none; background: none; }
</style>"""


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def js_str(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


def read_tsv_rows(path: Path) -> "list[dict]":
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def read_self_index_url(path: Path) -> str:
    rows = read_tsv_rows(path)
    return rows[0]["index_url"]


def render_topbar(cfg: dict, langs: "list[str]", back_url: "str | None") -> str:
    """Matches eee_topbar's style="index" branch: self-badge when no back_url,
    else a "◀ {parent_title}" link. Trilingual pages render one <span>/<a> per
    language with data-lang, toggled by JS; RU-only pages render a single one."""
    parts = [TOPBAR_CSS, '<div id="eee-topbar">']
    for lang in langs:
        display = "" if lang == langs[0] else 'style="display:none"'
        if back_url:
            parent_title = cfg["parent_titles"][lang]
            parts.append(f'<a class="tb-back" data-lang="{lang}" {display} href="{esc(back_url)}">◀ {esc(parent_title)}</a>')
        else:
            title = cfg["titles"][lang]
            parts.append(f'<span class="tb-back" data-lang="{lang}" {display}>● {esc(title)}</span>')
    parts.append(BADGE)
    parts.append("</div>")
    return "\n".join(parts)


def render_hero(hero: "dict[str, tuple[str, str]]", langs: "list[str]") -> str:
    parts = [HERO_CSS, '<div class="eee-hero">']
    for lang in langs:
        title, subtitle = hero[lang]
        display = "" if lang == langs[0] else "display:none"
        parts.append(f'<div data-lang="{lang}" style="{display}">'
                     f'<div class="eee-title">{esc(title)}</div>'
                     f'<div class="eee-series">{esc(subtitle)}</div></div>')
    parts.append("</div>")
    return "\n".join(parts)


def render_cards(rows: "list[dict]", langs: "list[str]") -> str:
    cards = []
    used_gitlab_override = False
    for row in rows:
        url = row["url"] or None
        header = f"""<div class="eee-card-header">
          <div class="eee-card-icon">{row['icon']}</div>
          <div>"""
        for lang in langs:
            display = "" if lang == langs[0] else "display:none"
            label = row.get(f"label_{lang}", "")
            title = row.get(f"title_{lang}", "")
            header += (f'<div data-lang="{lang}" style="{display}">'
                       f'<div class="eee-card-label">{esc(label)}</div>'
                       f'<div class="eee-card-title">{esc(title)}</div></div>')
        header += f'<div class="eee-card-greek">{esc(row["greek"])}</div></div></div>'
        desc_block = ""
        for lang in langs:
            display = "" if lang == langs[0] else "display:none"
            desc = row.get(f"desc_{lang}", "")
            desc_block += f'<div class="eee-card-desc" data-lang="{lang}" style="{display}">{esc(desc)}</div>'
        arrow_block = ""
        for lang in langs:
            display = "" if lang == langs[0] else "display:none"
            soon = CARD_LIST_SOON[lang]
            arrow_block += f'<div class="eee-card-arrow" data-lang="{lang}" style="{display}">{"◀" if url else esc(soon)}</div>'
        inner = header + desc_block + arrow_block
        if url:
            gitlab_href = GITLAB_SPLIT_OVERRIDES.get(url)
            if gitlab_href:
                used_gitlab_override = True
                cards.append(f'<a class="eee-card" href="{esc(url)}" data-gitlab-href="{esc(gitlab_href)}">{inner}</a>')
            else:
                cards.append(f'<a class="eee-card" href="{esc(url)}">{inner}</a>')
        else:
            cards.append(f'<div class="eee-card eee-card-disabled">{inner}</div>')
    result = CARD_LIST_CSS + "\n".join(cards)
    if used_gitlab_override:
        result += GITLAB_SPLIT_SCRIPT
    return result


def render_footer(langs: "list[str]") -> str:
    parts = [FOOTER_CSS, '<div id="eee-footer">']
    for lang in langs:
        display = "" if lang == langs[0] else "display:none"
        parts.append(f'<span class="footer-label" data-lang="{lang}" style="{display}">{esc(FOOTER_LABEL[lang])}</span>')
    parts.append('<a href="https://codeberg.org/EEE-project" target="_blank">codeberg.org/EEE-project</a>')
    parts.append("</div>")
    return "\n".join(parts)


def render_lang_picker(default_lang: str) -> str:
    opts = "\n".join(
        f'<option value="{code}"{" selected" if code == default_lang else ""}>{esc(name)}</option>'
        for name, code in LANG_OPTIONS.items()
    )
    return f"""<div id="lang-picker">🌐 <select onchange="setLang(this.value)">{opts}</select></div>
<script>
function setLang(lang) {{
  document.querySelectorAll('[data-lang]').forEach(el => {{
    el.style.display = (el.getAttribute('data-lang') === lang) ? '' : 'none';
  }});
  localStorage.setItem('eee_lang', lang);
}}
document.addEventListener('DOMContentLoaded', function() {{
  var stored = localStorage.getItem('eee_lang');
  if (stored) {{
    var sel = document.querySelector('#lang-picker select');
    if (sel) sel.value = stored;
    setLang(stored);
  }}
}});
</script>"""


def gen_hub(key: str, cfg: dict, out_root: Path) -> None:
    tsv_path = REPO_ROOT / cfg["tsv"]
    rows = read_tsv_rows(tsv_path)
    back_url = read_self_index_url(REPO_ROOT / cfg["parent_tsv"]) if cfg["parent_tsv"] else None

    is_multilingual = len(cfg["titles"]) > 1
    langs = ["el", "ru", "en"] if is_multilingual else ["ru"]
    default_lang = cfg["default_lang"]
    if default_lang in langs:
        langs = [default_lang] + [lang for lang in langs if lang != default_lang]

    if cfg["hero"] is not None:
        hero_html = render_hero(cfg["hero"], langs)
    else:
        hero_html = ""  # odyssey: no hero, matches its own notebook.py

    body = [
        PAGE_CSS,
        render_topbar(cfg, langs, back_url),
        render_lang_picker(default_lang) if is_multilingual else "",
        '<div class="eee-page">',
        hero_html,
        render_cards(rows, langs),
        render_footer(langs if is_multilingual else ["ru"]) if is_multilingual else render_footer(["ru"]),
        "</div>",
    ]

    title_text = cfg["titles"].get("en", next(iter(cfg["titles"].values())))
    html = f"""<!doctype html>
<html lang="{default_lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title_text)}</title>
</head>
<body>
{chr(10).join(body)}
</body>
</html>"""

    out_dir = out_root / cfg["out"]
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "index.html").write_text(html, encoding="utf-8")
    print(f"{key}: wrote {out_dir / 'index.html'} ({len(rows)} cards)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("hubs", nargs="*", help="hub keys to generate (default: all)")
    ap.add_argument("--out-dir", default=None, help="output root (default: repo root)")
    args = ap.parse_args()

    out_root = Path(args.out_dir) if args.out_dir else REPO_ROOT
    keys = args.hubs if args.hubs else list(HUBS.keys())
    for key in keys:
        gen_hub(key, HUBS[key], out_root)


if __name__ == "__main__":
    main()
