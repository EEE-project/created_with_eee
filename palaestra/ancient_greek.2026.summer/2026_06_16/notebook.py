# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.23.3",
#     "pandas>=2.0",
#     "eee-project @ git+https://codeberg.org/EEE-project/eee-project.git",
# ]
#
# [tool.uv.sources]
# eee-project = { git = "https://codeberg.org/EEE-project/eee-project.git" }
# ///

import marimo

__generated_with = "0.23.8"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    from eee_project import ConfigStore, eee_topbar
    _ROOT = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main"
    cfg = ConfigStore.from_url(
        f"{_ROOT}/palaestra/ancient_greek.2026.summer/lessons.tsv",
        ga=f"{_ROOT}/ga.json",
    )
    eee_topbar(mo, back_url=cfg.index_url(), lang="ru", titles="Palaestra",
               ga_config=cfg.ga_config())
    return (cfg,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Δίδαγμα γ'
    **Palaestra — Древнегреческий язык, начальный уровень — Лето 2026**

    [![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_xiJbhAWqwnxiV1SxYvYAdX)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Проверка домашнего задания · τὸ πρῶτον προστεταγμένον

    Файл: [дз+энклитики+заметки.pdf](./дз+энклитики+заметки.pdf)

    **Задания 1–3** — ударения в barytona, oxytona/perispomena, на подчёркнутом слоге.

    **Задания 4–8** — ὁριστική ↔ προστακτική:

    | ὁριστική | (σύ) | (ὑμεῖς) |
    |:---------|:----:|:-------:|
    | ἀναγιγνώσκω | ἀναγίγνωσκε! | ἀναγιγνώσκετε! |
    | ἀκούω | ἄκουε! | ἀκούετε! |
    | παύω | παῦε! | παύετε! |
    | λέγω | λέγε! | λέγετε! |
    | καταλαμβάνω | καταλάμβανε! | καταλαμβάνετε! |

    Ударение рецессивное: краткое окончание → 3-й от конца; долгое → 2-й от конца.

    εὖ / ὀρθῶς / καλῶς λέγεις, ἀναγιγνώσκεις… — хорошо, правильно говоришь, читаешь…

    **Задание 9** — антоним: δῆλόν ἐστιν ↔ **ἄδηλόν ἐστιν**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## αἱ μεταβολαί · Изменения при энклитиках

    Энклитика присоединяется к предыдущему слову; у некоторых типов появляется дополнительное ударение:

    | Тип | + τίς | + ἐστί |
    |:----|:-----:|:------:|
    | ὀξύτονον: ἀγρός | ἀγρός τις | ἀγρός ἐστι |
    | **παροξύτονον**: λίθος | λίθος τις | λίθος **ἐστί** |
    | **προπαροξύτονον**: ἄνθρωπος | ἄνθρωπ**ό**ς τις | ἄνθρωπ**ό**ς ἐστι |
    | περισπώμενον: φῶς | φῶς τι | φῶς ἐστι |
    | **προπερισπώμενον**: οἶκος | οἶκ**ό**ς τις | οἶκ**ό**ς ἐστι |

    Цепочка проклитик и энклитик: εἴ τίς ποτέ μοι εἶπε…

    φῶς = φόος (← φο + ος = 2 моры → περισπώμενον не на 2-м от конца — особый случай)
    """)
    return


@app.cell(hide_code=True)
def _(NB_DIR, NB_REMOTE, gu):
    import pandas as _pd_tsv

    def load_tsv(filename):
        return _pd_tsv.read_csv(
            gu.ensure_file(filename, nb_dir=NB_DIR, remote_base=NB_REMOTE),
            sep="\t",
        )

    for _pdf in (
        'Athenaze_1_vocabula.pdf',
        'κεφ_Ι(0,5)_ἀσκήματα.pdf',
        'энклитики+немного_алфавита_и_практики_письма.pdf',
        'дз+энклитики+заметки.pdf',
    ):
        gu.ensure_file(_pdf, nb_dir=NB_DIR, remote_base=NB_REMOTE)
    return (load_tsv,)


@app.cell(hide_code=True)
def _(load_tsv, mo):
    _verbs = load_tsv("verbs.tsv")
    _nouns = load_tsv("nouns.tsv")
    _adj = load_tsv("adjectives.tsv")
    mo.vstack([
        mo.md("## Capitulum I · Словарь Athenaze"),
        mo.md("Файл: [Athenaze_1_vocabula.pdf](./Athenaze_1_vocabula.pdf)"),
        mo.md("**Verba (глаголы):**"),
        mo.ui.table(_verbs, selection=None),
        mo.md("**Nomina substantiva (существительные, 2-е скл.):**"),
        mo.ui.table(_nouns, selection=None),
        mo.md("**Nomina adjectiva (прилагательные):**"),
        mo.ui.table(_adj, selection=None),
        mo.md(r"""
    **Praepositiones · Adverbia · Coniunctiones:**

    | | | |
    |:--|:--|:--|
    | πρός + acc. — к (ad) | ἀεί — всегда (semper) | ἀλλά — но (sed) |
    | ἐκ + gen. — из (ex) | μάλα — очень (valde) | γάρ — потому что, ведь (nam) |
    | ἐν + dat. — в, где? (in) | οὐ/οὐκ/οὐχ — не (non) | οὖν — поэтому (ergo) |
    | | οὐκέτι — уже не (iam non) | καί — и (et) |
    | | πολλάκις — часто (saepe) | |
    | | τέλος — наконец (tandem) | |

    *Locutiones:* δι'ὀλίγου — спустя недолгое время · ἐν ταῖς Ἀθήναις — в Афинах
        """),
    ])
    return


@app.cell(hide_code=True)
def _(NB_DIR, NB_REMOTE, gu):
    VOCAB_WORDS = gu.load_vocab_tsv(
        'verbs.tsv', 'nouns.tsv', 'adjectives.tsv', 'particles.tsv',
        nb_dir=NB_DIR, remote_base=NB_REMOTE,
    )
    return (VOCAB_WORDS,)


@app.cell(hide_code=True)
def _(mo):
    cv_c, set_cv_c = mo.state(None)
    score_c, set_score_c = mo.state({"correct": 0, "total": 0})
    remaining_c, set_remaining_c = mo.state(None)
    return cv_c, remaining_c, score_c, set_cv_c, set_remaining_c, set_score_c


@app.cell(hide_code=True)
def _(VOCAB_WORDS, random, remaining_c, set_cv_c, set_remaining_c):
    if remaining_c() is None and VOCAB_WORDS:
        _s = random.sample(VOCAB_WORDS, len(VOCAB_WORDS))
        set_cv_c(_s[0])
        set_remaining_c(_s[1:])
    return


@app.cell(hide_code=True)
def _(VOCAB_WORDS, cv_c, gu, mo, random):
    if cv_c() is None:
        answer_radio = mo.ui.radio(options=[''])
    else:
        answer_radio, _ = gu.word_quiz_question(cv_c(), VOCAB_WORDS, 'ru', random)
    return (answer_radio,)


@app.cell(hide_code=True)
def _(
    VOCAB_WORDS,
    answer_radio,
    cv_c,
    mo,
    random,
    remaining_c,
    score_c,
    set_cv_c,
    set_remaining_c,
    set_score_c,
):
    _done = cv_c() is None and remaining_c() is not None and len(remaining_c()) == 0

    def _on_next_c(_):
        if cv_c() is None:
            _shuf = random.sample(VOCAB_WORDS, len(VOCAB_WORDS))
            set_cv_c(_shuf[0])
            set_remaining_c(_shuf[1:])
            set_score_c({'correct': 0, 'total': 0})
        else:
            _ok = answer_radio.value == cv_c()['form']
            set_score_c({'correct': score_c()['correct'] + int(_ok), 'total': score_c()['total'] + 1})
            set_cv_c(remaining_c()[0] if remaining_c() else None)
            set_remaining_c(remaining_c()[1:] if remaining_c() else [])

    _s = score_c()
    if _done:
        _out = mo.vstack([
            mo.callout(mo.md(f"Готово! Правильно: **{_s['correct']}** / **{_s['total']}**"), kind='success'),
            mo.ui.button(label='Пройти снова', on_click=_on_next_c),
        ])
    elif cv_c() is None:
        mo.stop(True, mo.md(''))
    else:
        _next_c = mo.ui.button(label='Следующий', on_click=_on_next_c)
        _fb = mo.md('')
        if answer_radio.value is not None:
            _ok = answer_radio.value == cv_c()['form']
            _color = '#2d9e2d' if _ok else '#d32f2f'
            _mark = '✓' if _ok else '✗'
            _fb = mo.md(f'<span style="color:{_color};font-weight:bold">{_mark} {cv_c()["meaning"]} → {cv_c()["form"]}</span>')
        _out = mo.vstack([
            mo.md(f'## Упражнение 1 · Выбрать слово\n\n**{_s["total"] + 1}** / {len(VOCAB_WORDS)} — правильно: {_s["correct"]}'),
            answer_radio,
            _fb,
            mo.hstack([_next_c], justify='start'),
        ])
    _out
    return


@app.cell(hide_code=True)
def _(mo):
    cv_w, set_cv_w = mo.state(None)
    score_w, set_score_w = mo.state({"correct": 0, "total": 0})
    remaining_w, set_remaining_w = mo.state(None)
    return cv_w, remaining_w, score_w, set_cv_w, set_remaining_w, set_score_w


@app.cell(hide_code=True)
def _(VOCAB_WORDS, random, remaining_w, set_cv_w, set_remaining_w):
    if remaining_w() is None and VOCAB_WORDS:
        _s = random.sample(VOCAB_WORDS, len(VOCAB_WORDS))
        set_cv_w(_s[0])
        set_remaining_w(_s[1:])
    return


@app.cell(hide_code=True)
def _(cv_w, gu, mo):
    _ = cv_w()
    if cv_w() is None:
        write_input_w = mo.ui.text(placeholder='греческое слово…', full_width=True)
    else:
        write_input_w, _ = gu.word_write_question(cv_w(), 'ru')
    check_btn_w = mo.ui.button(label='Проверить', on_click=lambda v: (v or 0) + 1)
    return check_btn_w, write_input_w


@app.cell(hide_code=True)
def _(cv_w, mo, remaining_w):
    _done = cv_w() is None and remaining_w() is not None and len(remaining_w()) == 0
    next_btn_w = mo.ui.button(
        label='Пройти снова' if _done else 'Следующий',
        on_click=lambda v: (v or 0) + 1,
    )
    return (next_btn_w,)


@app.cell(hide_code=True)
def _(
    VOCAB_WORDS,
    cv_w,
    gu,
    next_btn_w,
    random,
    remaining_w,
    score_w,
    set_cv_w,
    set_remaining_w,
    set_score_w,
    write_input_w,
):
    if next_btn_w.value:
        _r = remaining_w()
        if _r is None:
            pass
        elif cv_w() is None:
            _shuf = random.sample(VOCAB_WORDS, len(VOCAB_WORDS))
            set_cv_w(_shuf[0])
            set_remaining_w(_shuf[1:])
            set_score_w({'correct': 0, 'total': 0})
        elif _r:
            _ok = gu._ci(write_input_w.value.strip(), {cv_w()['form']})
            set_score_w({'correct': score_w()['correct'] + int(_ok), 'total': score_w()['total'] + 1})
            set_cv_w(_r[0])
            set_remaining_w(_r[1:])
        else:
            _ok = gu._ci(write_input_w.value.strip(), {cv_w()['form']})
            set_score_w({'correct': score_w()['correct'] + int(_ok), 'total': score_w()['total'] + 1})
            set_cv_w(None)
            set_remaining_w([])
    return


@app.cell(hide_code=True)
def _(
    VOCAB_WORDS,
    check_btn_w,
    cv_w,
    gu,
    mo,
    next_btn_w,
    remaining_w,
    score_w,
    write_input_w,
):
    _done = cv_w() is None and remaining_w() is not None and len(remaining_w()) == 0
    _s = score_w()
    if _done:
        _out = mo.vstack([
            mo.callout(mo.md(f"Готово! Правильно: **{_s['correct']}** / **{_s['total']}**"), kind='success'),
            next_btn_w,
        ])
    else:
        _meaning = cv_w().get('meaning', '') if cv_w() is not None else ''
        _typed = write_input_w.value.strip()
        if check_btn_w.value and _typed and cv_w() is not None:
            _ok = gu._ci(_typed, {cv_w()['form']})
            _color = '#2d9e2d' if _ok else '#d32f2f'
            _mark = '✓' if _ok else '✗'
            _fb = mo.md(f'<span style="color:{_color};font-weight:bold">{_mark} {_meaning} → {cv_w()["form"]}</span>')
        else:
            _fb = mo.md(f'*{_meaning}*') if _meaning else mo.md('')
        _out = mo.vstack([
            mo.md(f'## Упражнение 2 · Написать греческое слово\n\n**{_s["total"] + 1}** / {len(VOCAB_WORDS)} — правильно: {_s["correct"]}'),
            _fb,
            write_input_w,
            mo.hstack([check_btn_w, next_btn_w], justify='start'),
        ])
    _out
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Вопросы и ответы

    **Τίς…; — Кто?** → именительный падеж (ὀνομαστική):

    > Τίς ἐστιν ὁ Ἀνδρέας; — ὁ Ἀνδρέας **διδάσκαλός** ἐστιν.
    > Τίς ἐστιν ὁ Δ.; — ὁ Δ. **αὐτουργός** ἐστιν.

    **Ποδαπός…; — Откуда? Какой национальности?** → именительный:

    > Ποδαπός ἐστιν ὁ Ἀνδρέας; — ὁ Ἀνδρέας **Ῥῶσσός** / **Ἕλλην** / **Ῥωμαῖος** ἐστιν.
    > (Ῥῶσσος ← Ῥωσία, Γερμανός ← Γερμανία, Ἀμερικανός ← Ἀμέρικα…)

    **Ποῦ; — Где?** → **ἐν** + дательный (δοτική):

    > Ποῦ οἰκεῖ ὁ Δ.; — ὁ Δ. **ἐν τοῖς ἀγροῖς** οἰκεῖ.

    **Διὰ τί; — Почему?** → частица **γάρ** на втором месте:

    > Διὰ τί ὁ Δ. ἐν τοῖς ἀγροῖς οἰκεῖ; — αὐτουργὸς **γάρ** ἐστιν.

    **Ἆρα…; — Разве? (да/нет):**

    > Ἆρα Ῥωμαῖός ἐστιν ὁ Δ.;
    > Ναί, αὐτουργός ἐστιν. — Да, он земледелец.
    > Οὐδαμῶς, οὐ Ῥωμαῖός ἐστιν, **ἀλλά** Ἀθηναῖος.

    Частицы стоят **на втором месте** (закон Ваккернагеля): γάρ, ἀλλά, οὖν, καί.

    *ἡ γὰρ σιωπὴ μαρτυρεῖ τὸ μὴ θελεῖν.* — Ибо молчание свидетельствует о нежелании.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## τὸ δεύτερον προστεταγμένον · Домашнее задание

    **1. Вопросы о Δικαιόπολις** — файл: [κεφ\_Ι(0,5)\_ἀσκήματα.pdf](./κεφ_Ι(0,5)_ἀσκήματα.pdf)

    Ответьте на вопросы (и составьте вопросы к ответам):
    - Τίς ἐστιν ὁ Δικαιόπολις;
    - Ποδαπός ἐστιν ὁ Δικαιόπολις;
    - Ποῦ ὁ Δ. οὐκ οἰκεῖ; Ποῦ οἰκεῖ;
    - Διὰ τί οἰκεῖ ὁ Δ. ἐν τοῖς ἀγροῖς;
    - Ἆρα Ῥωμαῖός ἐστιν ὁ Δ.;

    **2. Энклитики** — файл: [энклитики+немного\_алфавита\_и\_практики\_письма.pdf](./энклитики+немного_алфавита_и_практики_письма.pdf)

    Упражнение 8: вставьте энклитику и при необходимости исправьте ударения.
    - A) энклитическую частицу **τε**
    - Б) энклитическую форму глагола **ἐστί**

    Упражнение на алфавит: расположите слова в алфавитном порядке (строчными и заглавными буквами).

    **3. Словарь** — файл: [Athenaze\_1\_vocabula.pdf](./Athenaze_1_vocabula.pdf)

    Выучите слова Capitulum I (verba + nomina substantiva как минимум).
    """)
    return


@app.cell(hide_code=True)
def _(cfg, mo):
    from eee_project import GreekUtils, ANCIENT_GREEK
    from eee_project.notebook_utils import eee_footer
    from pathlib import Path as _Path
    gu = GreekUtils(mo_module=mo, config=ANCIENT_GREEK)
    NB_DIR = _Path(__file__).parent
    NB_REMOTE = cfg.nb_remote(__file__)
    eee_footer(mo, lang='ru')
    return NB_DIR, NB_REMOTE, gu


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import random

    return mo, random


if __name__ == "__main__":
    app.run()
