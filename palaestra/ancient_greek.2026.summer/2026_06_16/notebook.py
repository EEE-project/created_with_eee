# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.23.3",
#     "eee-project @ git+https://codeberg.org/EEE-project/eee-project.git",
#     "ancient-greek-backend-eee @ git+https://codeberg.org/EEE-project/ancient-greek-backend-eee.git",
# ]
#
# [tool.uv.sources]
# eee-project = { git = "https://codeberg.org/EEE-project/eee-project.git" }
# ancient-greek-backend-eee = { git = "https://codeberg.org/EEE-project/ancient-greek-backend-eee.git" }
# ///

import marimo

__generated_with = "0.23.9"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    from eee_project import ConfigStore, eee_topbar
    _ROOT = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main"
    _cfg = ConfigStore.from_url(
        f"{_ROOT}/palaestra/ancient_greek.2026.summer/lessons.tsv",
        ga=f"{_ROOT}/ga.json",
    )
    eee_topbar(mo, back_url=_cfg.index_url(), lang="ru", titles="Palaestra",
               ga_config=_cfg.ga_config())


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Δίδαγμα γ'
    **Palaestra — Древнегреческий язык, начальный уровень — Лето 2026**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Проверка домашнего задания · τὸ δεύτερον προστεταγμένον

    Файл: [дз+энклитики+заметки.pdf](./дз+энклитики+заметки.pdf)

    **Задания 1–3** — ударения в barytona, oxytona / perispomena, на подчёркнутом слоге.
    Правило: ударение *может быть* острым или облегчённым (по количеству мор); *должно быть* — то, которое определяется реальной формой слова.

    **Задания 4–8** — ὁριστική ↔ προστακτική:

    | ὁριστική | (σύ) | (ὑμεῖς) |
    |:---------|:----:|:-------:|
    | ἀναγιγνώσκω | ἀναγίγνωσκε! | ἀναγιγνώσκετε! |
    | ἀκούω | ἄκουε! | ἀκούετε! |
    | παύω | παῦε! | παύετε! |
    | λέγω | λέγε! | λέγετε! |
    | καταλαμβάνω | καταλάμβανε! | καταλαμβάνετε! |

    **Задание 9** — антоним: δῆλόν ἐστιν ↔ **ἄδηλόν ἐστιν**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Рецессивное ударение · τόνος ἐν ῥήμασι

    Ударение в глаголах **рецессивное** — стоит как можно дальше от конца:

    | Конечный гласный | Позиция ударения | Пример |
    |:-----------------|:----------------:|:------:|
    | Краткий (-ε, -ο) | 3-й от конца | ἀκούω → **ἄ**κουε! |
    | Долгий (-η, -ω, дифтонг) | 2-й от конца | ἀκούω → ἀκού**ετε**! |

    εὖ / ὀρθῶς / καλῶς λέγεις, ἀναγιγνώσκεις… — *хорошо, правильно говоришь, читаешь…*

    | Греческий | Перевод |
    |:----------|:--------|
    | δῆλόν ἐστιν | это ясно |
    | ἄδηλόν ἐστιν | это неясно |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    import eee_project as eee
    from ancient_greek_backend_eee import AncientGreekBackend
    from eee_project import GreekUtils, ANCIENT_GREEK
    from pathlib import Path as _Path

    ag = AncientGreekBackend(lexicons=["pratt", "ltrg", "homer", "lxx", "morphgnt"])
    eee.register_backend("grc", ag)
    eee.register_backend("grc", ag, backend="ancient-greek")
    eee.set_chain("grc", ["ancient-greek"])

    gu = GreekUtils(ag, mo, eee_module=eee, config=ANCIENT_GREEK)

    _IMP = {"VerbForm": "Fin", "Tense": "Pres", "Voice": "Act", "Mood": "Imp"}
    VERBS = gu.load_slot_drill(
        _Path(__file__).parent / "verbs.tsv",
        {"verb": None, "sg": {**_IMP, "Person": "2", "Number": "Sing"},
                       "pl": {**_IMP, "Person": "2", "Number": "Plur"}},
        pos="verb",
    )
    return VERBS, eee, gu


@app.cell(hide_code=True)
def _(mo):
    strict_v = mo.ui.switch(label="Учитывать диакритику", value=False)
    mo.hstack([strict_v], justify="end")
    return (strict_v,)


@app.cell(hide_code=True)
def _(mo):
    _clk = lambda v: (v or 0) + 1
    clear_btn_v = mo.ui.button(label="Очистить", on_click=_clk)
    return (clear_btn_v,)


@app.cell(hide_code=True)
def _(VERBS, clear_btn_v, gu, mo):
    _dep = clear_btn_v.value
    _clk = lambda v: (v or 0) + 1
    submit_btn_v = mo.ui.button(label="Проверить ✓", on_click=_clk)
    verb_inputs_v, _rows = gu.make_item_drill_rows(
        VERBS, ["verb", "sg", "pl"],
        meaning_key="meaning",
        placeholders=["глагол…", "ед. ч.…", "мн. ч.…"],
    )
    mo.vstack([
        mo.md(r"## Упражнение · Повелительное наклонение"),
        mo.md("Дано: **значение**. Введите: словарную форму глагола, затем повел. ед. и мн. ч."),
        *_rows,
        mo.hstack([clear_btn_v, submit_btn_v], justify="end"),
    ])
    return submit_btn_v, verb_inputs_v


@app.cell(hide_code=True)
def _(VERBS, gu, mo, strict_v, submit_btn_v, verb_inputs_v):
    _fb = gu.check_item_drill(
        VERBS, verb_inputs_v, ["verb", "sg", "pl"],
        field_labels=["глагол", "sg", "pl"],
        strict=strict_v.value,
    ) if submit_btn_v.value else []
    mo.vstack(_fb) if _fb else mo.md("")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ἡ εἰσαγωγή · Введение в Athenaze

    Новые слова:

    | Греческий | Часть речи | Перевод |
    |:----------|:-----------|:--------|
    | ὁ **οἶκος** | ὄνομα οὐσιαστικόν | дом |
    | ὁ **ἀγρός** | ὄνομα οὐσιαστικόν | поле |
    | ὁ **αὐτουργός** | ὄνομα οὐσιαστικόν | земледелец, работающий своими руками (αὐτός + ἔργον) |
    | ὁ **διδάσκαλος** | ὄνομα οὐσιαστικόν | учитель |
    | **Ἀθηναῖος** | ὄνομα ἐπίθετον | афинский |
    | **οἰκεῖ** | ῥῆμα | живёт, обитает |
    | **ἐστι(ν)** | ῥῆμα | есть, является |

    Порядок слов: английский / русский — **S V O**; древнегреческий — **S O V** (дополнение перед глаголом).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Вопросы и ответы

    **Τίς…; — Кто?** → именительный падеж (ὀνομαστική):

    > Τίς ἐστιν ὁ Ἀνδρέας; — Кто такой Андрей?
    > ὁ Ἀνδρέας **διδάσκαλός** ἐστιν. — Андрей — учитель.
    >
    > Τίς ἐστιν ὁ Δ.;
    > ὁ Δ. **αὐτουργός** ἐστιν.

    **Ποῦ; — Где?** → **ἐν** + дательный падеж (δοτική):

    > Ποῦ οἰκεῖ ὁ Δ.;
    > ὁ Δ. **ἐν τοῖς ἀγροῖς** οἰκεῖ.

    **Διὰ τί; — Почему?** → частица **γάρ** (ведь, ибо) на втором месте:

    > Διὰ τί ὁ Δ. ἐν τοῖς ἀγροῖς οἰκεῖ;
    > αὐτουργὸς **γάρ** ἐστιν. — Ведь он земледелец.
    > ὁ **γὰρ** Δ. αὐτουργός ἐστιν.

    Частицы в древнегреческом стоят **на втором месте** (закон Ваккернагеля).

    **ἆρα** — вопрос, ожидающий «да» / «нет»:

    > ἆρα ὁ Δ. αὐτουργός ἐστιν;
    > Ναί, αὐτουργός ἐστιν.

    *Ср. латынь: Est-ne Iulius agricola? — Ita / sic, agricola est.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    *ἡ γὰρ σιωπὴ μαρτυρεῖ τὸ μὴ θελεῖν.* — Ибо молчание свидетельствует о нежелании.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## τὸ τρίτον προστεταγμένον · Домашнее задание

    1. Повторите парадигму повелительного наклонения пяти глаголов (упражнение выше).
    2. Выучите новые слова: οἶκος, ἀγρός, αὐτουργός, διδάσκαλος.
    3. Составьте 2–3 предложения по образцу:
       - *Τίς ἐστιν ὁ …; — ὁ … … ἐστιν.*
       - *Ποῦ οἰκεῖ ὁ …; — ὁ … ἐν … οἰκεῖ.*
       - *Διὰ τί …; — … γάρ ἐστιν.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    from eee_project.notebook_utils import eee_footer
    eee_footer(mo, lang="ru")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
