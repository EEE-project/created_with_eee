# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.23.14",
#     "pandas>=2.0",
#     "eee-project>=1.1.0",
#     "ancient-greek-backend-eee>=2.0.0",
# ]
# ///

import marimo

__generated_with = "0.23.10"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    from eee_project import ConfigStore, eee_topbar
    _ROOT = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main"
    cfg = ConfigStore.from_file_or_url(
        __file__,
        f"{_ROOT}/ancient_greek/palaestra/ancient_greek.2026.summer/index.tsv",
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
def _(NB_REMOTE, mo):
    mo.md(f"**Материалы занятия:** [дз+энклитики+заметки.pdf]({NB_REMOTE}/дз+энклитики+заметки.pdf) · [κεφ\\_Ι(0,5)\\_ἀσκήματα.pdf]({NB_REMOTE}/κεφ_Ι(0,5)_ἀσκήματα.pdf) · [энклитики+немного\\_алфавита\\_и\\_практики\\_письма.pdf]({NB_REMOTE}/энклитики+немного_алфавита_и_практики_письма.pdf) · [Athenaze\\_1\\_vocabula.pdf]({NB_REMOTE}/Athenaze_1_vocabula.pdf)")
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, mo):
    mo.md(fr"""
    ## Проверка домашнего задания · τὸ πρῶτον προστεταγμένον

    Файл: [дз+энклитики+заметки.pdf]({NB_REMOTE}/дз+энклитики+заметки.pdf)

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
    ## Ο ΔΙΚΑΙΟΠΟΛΙΣ (α) · Athenaze, Capitolo I, стр. 3

    Δικαιόπολις Ἀθηναῖός ἐστιν· οἰκεῖ δὲ ὁ Δικαιόπολις οὐκ ἐν ταῖς Ἀθήναις ἀλλὰ
    ἐν τοῖς ἀγροῖς· αὐτουργὸς γάρ ἐστιν.

    Γεωργεῖ οὖν τὸν κλῆρον καὶ πονεῖ ἐν τοῖς ἀγροῖς. Χαλεπὸς δέ ἐστιν ὁ βίος· ὁ
    γὰρ κλῆρός ἐστι μικρός, μακρὸς δὲ ὁ πόνος. Ἀεὶ οὖν πονεῖ ὁ Δικαιόπολις καὶ
    πολλάκις στενάζει καὶ λέγει· «Ὦ Ζεῦ, χαλεπὸς ἐστιν ὁ βίος· ἀπέραντος γάρ
    ἐστιν ὁ πόνος, μικρὸς δὲ ὁ κλῆρος καὶ οὐ πολὺν σῖτον παρέχει.»

    Ἀλλὰ ἰσχυρός ἐστιν ὁ ἄνθρωπος καὶ ἄοκνος· πολλάκις οὖν χαίρει· ἐλεύθερος
    γάρ ἐστι καὶ αὐτουργός· φιλεῖ δὲ τὸν οἶκον. Καλὸς γάρ ἐστιν ὁ κλῆρος καὶ
    σῖτον παρέχει οὐ πολὺν ἀλλὰ ἱκανόν.
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
def _(NB_REMOTE, load_tsv, mo):
    _verbs = load_tsv("verbs.tsv")
    _nouns = load_tsv("nouns.tsv")
    _adj = load_tsv("adjectives.tsv")
    mo.vstack([
        mo.md("## Capitulum I · Словарь Athenaze"),
        mo.md(f"Файл: [Athenaze_1_vocabula.pdf]({NB_REMOTE}/Athenaze_1_vocabula.pdf)"),
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
    score_c, set_score_c = mo.state({'correct': 0, 'total': 0})
    remaining_c, set_remaining_c = mo.state(None)
    history_c, set_history_c = mo.state([])
    future_c, set_future_c = mo.state([])
    restore_entry_c, set_restore_entry_c = mo.state(None)
    return (
        cv_c,
        future_c,
        history_c,
        remaining_c,
        restore_entry_c,
        score_c,
        set_cv_c,
        set_future_c,
        set_history_c,
        set_remaining_c,
        set_restore_entry_c,
        set_score_c,
    )


@app.cell(hide_code=True)
def _(VOCAB_WORDS, cv_c, gu, history_c, remaining_c, restore_entry_c):
    _ = cv_c()
    answer_radio, next_btn_c, prev_btn_c = gu.word_quiz_widgets(
        cv=cv_c(),
        remaining=remaining_c(),
        vocab=VOCAB_WORDS,
        restore_entry=restore_entry_c(),
        history_len=len(history_c()),
    )
    return answer_radio, next_btn_c, prev_btn_c


@app.cell(hide_code=True)
def _(
    VOCAB_WORDS,
    answer_radio,
    cv_c,
    future_c,
    gu,
    history_c,
    next_btn_c,
    prev_btn_c,
    remaining_c,
    restore_entry_c,
    score_c,
    set_cv_c,
    set_future_c,
    set_history_c,
    set_remaining_c,
    set_restore_entry_c,
    set_score_c,
):
    gu.word_quiz_form(
        cv_c, set_cv_c, remaining_c, set_remaining_c,
        score_c, set_score_c, restore_entry_c, set_restore_entry_c,
        history_c, set_history_c, future_c, set_future_c,
        answer_radio, next_btn_c, prev_btn_c,
        vocab=VOCAB_WORDS,
        title='## Упражнение 1 · Выбрать слово',
    )
    return


@app.cell(hide_code=True)
def _(mo):
    cv_w, set_cv_w = mo.state(None)
    score_w, set_score_w = mo.state({'correct': 0, 'total': 0})
    remaining_w, set_remaining_w = mo.state(None)
    history_w, set_history_w = mo.state([])
    future_w, set_future_w = mo.state([])
    restore_entry_w, set_restore_entry_w = mo.state(None)
    return (
        cv_w,
        future_w,
        history_w,
        remaining_w,
        restore_entry_w,
        score_w,
        set_cv_w,
        set_future_w,
        set_history_w,
        set_remaining_w,
        set_restore_entry_w,
        set_score_w,
    )


@app.cell(hide_code=True)
def _(cv_w, gu, history_w, remaining_w, restore_entry_w):
    _ = cv_w()
    write_input_w, dia_w, check_btn_w, prev_btn_w, next_btn_w = gu.word_drill_widgets(
        cv=cv_w(),
        remaining=remaining_w(),
        restore_entry=restore_entry_w(),
        history_len=len(history_w()),
    )
    return check_btn_w, dia_w, next_btn_w, prev_btn_w, write_input_w


@app.cell(hide_code=True)
def _(
    VOCAB_WORDS,
    check_btn_w,
    cv_w,
    dia_w,
    future_w,
    gu,
    history_w,
    next_btn_w,
    prev_btn_w,
    remaining_w,
    restore_entry_w,
    score_w,
    set_cv_w,
    set_future_w,
    set_history_w,
    set_remaining_w,
    set_restore_entry_w,
    set_score_w,
    write_input_w,
):
    gu.word_drill_form(
        cv_w, set_cv_w, remaining_w, set_remaining_w,
        score_w, set_score_w, restore_entry_w, set_restore_entry_w,
        history_w, set_history_w, future_w, set_future_w,
        write_input_w, dia_w, check_btn_w, prev_btn_w, next_btn_w,
        vocab=VOCAB_WORDS,
        title='## Упражнение 2 · Написать греческое слово',
        comment='Для ввода используйте **polytonic Greek keyboard** или кнопки диакритики ниже.<br>**Как пользоваться:** нажмите кнопку знака диакритики → введите гласную → знак применится. Нажмите повторно или введите согласную — снимается. Можно **совмещать несколько знаков диакритики** (например, придыхание + ударение перед вводом буквы → ἆ).',
    )
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
def _(NB_REMOTE, mo):
    mo.md(fr"""
    ## τὸ δεύτερον προστεταγμένον · Домашнее задание

    **1. Вопросы о Δικαιόπολις** — файл: [κεφ\_Ι(0,5)\_ἀσκήματα.pdf]({NB_REMOTE}/κεφ_Ι(0,5)_ἀσκήματα.pdf)

    Ответьте на вопросы (и составьте вопросы к ответам):
    - Τίς ἐστιν ὁ Δικαιόπολις;
    - Ποδαπός ἐστιν ὁ Δικαιόπολις;
    - Ποῦ ὁ Δ. οὐκ οἰκεῖ; Ποῦ οἰκεῖ;
    - Διὰ τί οἰκεῖ ὁ Δ. ἐν τοῖς ἀγροῖς;
    - Ἆρα Ῥωμαῖός ἐστιν ὁ Δ.;

    **2. Энклитики** — файл: [энклитики+немного\_алфавита\_и\_практики\_письма.pdf]({NB_REMOTE}/энклитики+немного_алфавита_и_практики_письма.pdf)

    Упражнение 8: вставьте энклитику и при необходимости исправьте ударения.
    - A) энклитическую частицу **τε**
    - Б) энклитическую форму глагола **ἐστί**

    Упражнение на алфавит: расположите слова в алфавитном порядке (строчными и заглавными буквами).

    **3. Словарь** — файл: [Athenaze\_1\_vocabula.pdf]({NB_REMOTE}/Athenaze_1_vocabula.pdf)

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
    NB_REMOTE = cfg.nb_remote("2026_06_16")
    eee_footer(mo, lang='ru')
    return NB_DIR, NB_REMOTE, gu


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
