#!/usr/bin/env python3
"""Generate a course hub index.html from its index.tsv + this file's hero-text config.

index.tsv already owns each lesson's icon/greek/label/title/desc/url -- the
generator reads it directly rather than having that content re-typed by hand
into the hub HTML too. Course-level text that isn't in index.tsv (hero
title/subtitle, page <title>, the "back" link target) lives in COURSES below.

A course's cards are trilingual (id attributes + TRANSLATIONS entries) only
when its index.tsv has label_en/label_el columns; Russian-only TSVs (no
verified EN/EL source text) get Russian-only cards, matching the existing
odyssey/palaestra pages.

Usage:
    python3 tools/gen_hub.py <course-key> [<course-key> ...]
    python3 tools/gen_hub.py --all
    python3 tools/gen_hub.py --all --out-dir /some/other/dir   # default: pages_generated/
"""
import csv
import io
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
TEMPLATE = (ROOT / "tools" / "hub_template.html").read_text(encoding="utf-8")

COURSES = {
    "odyssey": {
        "tsv": "ancient_greek/odyssey/index.tsv",
        "out": "odyssey/index.html",
        "back_href": "../index.html",
        "title": "Created with EEE — Ancient Greek with Homer",
        "hero": {
            "en": ("ANCIENT GREEK — HOMER'S ODYSSEY", "Ancient Greek with Homer",
                   "Interactive exercises on vocabulary and forms from Homer's Odyssey."),
            "ru": ("ДРЕВНЕГРЕЧЕСКИЙ — ГОМЕРОВСКАЯ ОДИССЕЯ", "Древнегреческий с Гомером",
                   "Интерактивные упражнения по лексике и формам из Одиссеи Гомера."),
            "el": ("ΑΡΧΑΙΑ ΕΛΛΗΝΙΚΑ — ΟΜΗΡΙΚΗ ΟΔΥΣΣΕΙΑ", "Αρχαία Ελληνικά με τον Όμηρο",
                   "Διαδραστικές ασκήσεις λεξιλογίου και τύπων από την Οδύσσεια του Ομήρου."),
        },
    },
    "palaestra": {
        "tsv": "ancient_greek/palaestra/ancient_greek.2026.summer/index.tsv",
        "out": "palaestra/ancient_greek.2026.summer/index.html",
        "back_href": "../../index.html",
        "title": "Created with EEE — Ancient Greek: Palaestra",
        "hero": {
            "en": ("ANCIENT GREEK — PALAESTRA", "Ancient Greek: Palaestra",
                   "Summer 2026 beginners course, based on Athenaze — grammar, forms, and reading practice."),
            "ru": ("ДРЕВНЕГРЕЧЕСКИЙ — ПАЛЕСТРА", "Древнегреческий: Палестра",
                   "Летний курс 2026 для начинающих по учебнику Athenaze — грамматика, формы, чтение."),
            "el": ("ΑΡΧΑΙΑ ΕΛΛΗΝΙΚΑ — ΠΑΛΑΙΣΤΡΑ", "Αρχαία Ελληνικά: Παλαίστρα",
                   "Θερινό μάθημα 2026 για αρχάριους βάσει του Athenaze — γραμματική, τύποι, ανάγνωση."),
        },
    },
    "kapodistrias": {
        "tsv": "modern_greek/b1greeklanguageandculture/kapodistrias/index.tsv",
        "out": "kapodistrias/index.html",
        "back_href": "../index.html",
        "title": "Created with EEE — Kapodistrias",
        "hero": {
            "en": ("MODERN GREEK — HISTORY & CULTURE", "Kapodistrias",
                   "Nouns, verbs, and adjectives through the life of Ioannis Kapodistrias."),
            "ru": ("НОВОГРЕЧЕСКИЙ — ИСТОРИЯ И КУЛЬТУРА", "Каподистриас",
                   "Существительные, глаголы и прилагательные через жизнь Иоанниса Каподистриаса."),
            "el": ("ΝΕΑ ΕΛΛΗΝΙΚΑ — ΙΣΤΟΡΙΑ & ΠΟΛΙΤΙΣΜΟΣ", "Καποδίστριας",
                   "Ουσιαστικά, ρήματα και επίθετα μέσα από τη ζωή του Ιωάννη Καποδίστρια."),
        },
    },
    "ellinika_b": {
        "tsv": "modern_greek/ellinika_b/index.tsv",
        "out": "ellinika_b/index.html",
        "back_href": "../index.html",
        "title": "Created with EEE — Ελληνικά Β",
        "hero": {
            "en": ("MODERN GREEK — B1", "Ελληνικά Β",
                   "Nouns, verbs, and adjectives — vocabulary and grammar drills for each chapter."),
            "ru": ("НОВОГРЕЧЕСКИЙ — B1", "Ελληνικά Β",
                   "Существительные, глаголы и прилагательные — лексика и грамматика по главам."),
            "el": ("ΝΕΑ ΕΛΛΗΝΙΚΑ — Β1", "Ελληνικά Β",
                   "Ουσιαστικά, ρήματα και επίθετα — λεξιλόγιο και γραμματική ανά ενότητα."),
        },
    },
}


def read_tsv_rows(path: Path) -> "list[dict]":
    text = path.read_text(encoding="utf-8")
    reader = csv.DictReader(io.StringIO(text), delimiter="\t")
    return [row for row in reader if row.get("url")]


def esc_html(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def js_str(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


def gen_course(key: str, cfg: dict, out_dir: Path) -> None:
    rows = read_tsv_rows(ROOT / cfg["tsv"])
    if not rows:
        raise ValueError(f"{cfg['tsv']}: no rows with a url column")
    trilingual = "label_en" in rows[0] and "label_el" in rows[0]

    cards_html = []
    trans = {"en": [], "ru": [], "el": []}

    for n, row in enumerate(rows, start=1):
        url, icon, greek = row["url"], row["icon"], row["greek"]
        if trilingual:
            label = {lang: row[f"label_{lang}"] for lang in ("en", "ru", "el")}
            title = {lang: row[f"title_{lang}"] for lang in ("en", "ru", "el")}
            desc = {lang: row[f"desc_{lang}"] for lang in ("en", "ru", "el")}
            cards_html.append(
                f'      <a class="card" href="{esc_html(url)}">\n'
                f'        <div class="card-header">\n'
                f'          <div class="card-icon">{icon}</div>\n'
                f'          <div>\n'
                f'            <div class="card-label" id="card-l{n}-label">{esc_html(label["en"])}</div>\n'
                f'            <div class="card-title" id="card-l{n}-title">{esc_html(title["en"])}</div>\n'
                f'            <div class="card-greek">{esc_html(greek)}</div>\n'
                f'          </div>\n'
                f'        </div>\n'
                f'        <div class="card-desc" id="card-l{n}-desc">{esc_html(desc["en"])}</div>\n'
                f'        <div class="card-arrow">◀</div>\n'
                f'      </a>'
            )
            for lang in ("en", "ru", "el"):
                trans[lang].append(
                    f"        l{n}Label: {js_str(label[lang])}, "
                    f"l{n}Title: {js_str(title[lang])}, "
                    f"l{n}Desc: {js_str(desc[lang])}"
                )
        else:
            cards_html.append(
                f'      <a class="card" href="{esc_html(url)}">\n'
                f'        <div class="card-header">\n'
                f'          <div class="card-icon">{icon}</div>\n'
                f'          <div>\n'
                f'            <div class="card-label">{esc_html(row["label_ru"])}</div>\n'
                f'            <div class="card-title">{esc_html(row["title_ru"])}</div>\n'
                f'            <div class="card-greek">{esc_html(greek)}</div>\n'
                f'          </div>\n'
                f'        </div>\n'
                f'        <div class="card-desc">{esc_html(row["desc_ru"])}</div>\n'
                f'        <div class="card-arrow">◀</div>\n'
                f'      </a>'
            )

    els_js = (
        f"    for (let i = 1; i <= {len(rows)}; i++) {{\n"
        f"      ELS['l' + i + 'Label'] = document.getElementById('card-l' + i + '-label');\n"
        f"      ELS['l' + i + 'Title'] = document.getElementById('card-l' + i + '-title');\n"
        f"      ELS['l' + i + 'Desc']  = document.getElementById('card-l' + i + '-desc');\n"
        f"    }}"
    ) if trilingual else ""

    hero = cfg["hero"]
    out = TEMPLATE
    out = out.replace("{{TITLE}}", esc_html(cfg["title"]))
    out = out.replace("{{BACK_HREF}}", cfg["back_href"])
    out = out.replace("{{HERO_SERIES_EN}}", esc_html(hero["en"][0]))
    out = out.replace("{{HERO_TITLE_EN}}", esc_html(hero["en"][1]))
    out = out.replace("{{HERO_SUBTITLE_EN}}", esc_html(hero["en"][2]))
    for lang in ("en", "ru", "el"):
        out = out.replace(f"{{{{HERO_SERIES_{lang.upper()}_JS}}}}", js_str(hero[lang][0]))
        out = out.replace(f"{{{{HERO_TITLE_{lang.upper()}_JS}}}}", js_str(hero[lang][1]))
        out = out.replace(f"{{{{HERO_SUBTITLE_{lang.upper()}_JS}}}}", js_str(hero[lang][2]))
        out = out.replace(
            f"{{{{CARDS_TRANSLATIONS_{lang.upper()}}}}}",
            (",\n" + ",\n".join(trans[lang])) if trans[lang] else "",
        )
    out = out.replace("{{CARDS_HTML}}", "\n".join(cards_html))
    out = out.replace("{{CARDS_ELS_JS}}", els_js)

    out_path = out_dir / cfg["out"]
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(out, encoding="utf-8")
    print(f"wrote {out_path} ({len(rows)} cards, trilingual={trilingual})")


def main() -> None:
    args = sys.argv[1:]
    out_dir = ROOT / "pages_generated"
    if "--out-dir" in args:
        i = args.index("--out-dir")
        out_dir = Path(args[i + 1])
        del args[i:i + 2]

    keys = list(COURSES) if "--all" in args else [a for a in args if not a.startswith("--")]
    if not keys:
        print(__doc__)
        raise SystemExit(1)

    for key in keys:
        if key not in COURSES:
            raise SystemExit(f"unknown course {key!r} -- choices: {', '.join(COURSES)}")
        gen_course(key, COURSES[key], out_dir)


if __name__ == "__main__":
    main()
