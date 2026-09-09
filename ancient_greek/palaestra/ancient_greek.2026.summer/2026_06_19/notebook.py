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

__generated_with = "0.23.13"
app = marimo.App(width="medium", app_title="Palaestra — Занятие 4 · 19.06.2026: Средний залог и II склонение")


@app.cell(hide_code=True)
def _(mo):
    from eee_project import ConfigStore, eee_topbar
    _ROOT = "https://raw.githubusercontent.com/EEE-project/created_with_eee/main"
    cfg = ConfigStore.from_file_or_url(
        __file__,
        f"{_ROOT}/ancient_greek/palaestra/ancient_greek.2026.summer/index.tsv",
        ga=f"{_ROOT}/ga.json",
    )
    eee_topbar(mo, back_url=cfg.index_url(), lang="ru", titles="Palaestra",
               ga_config=cfg.ga_config(), same_window=True)
    return (cfg,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Δίδαγμα δ'
    **Palaestra — Древнегреческий язык, начальный уровень — Лето 2026**
    """)
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, mo):
    mo.md(f"""
    **Материалы занятия:** [Κεφ.I(1).pdf]({NB_REMOTE}/Κεφ.I(1).pdf) · [заметки\\_19.06.pdf]({NB_REMOTE}/заметки_19.06.pdf) · [κεφ\\_Ι(0,5)\\_ἀσκήματα\\_τέλος.pdf]({NB_REMOTE}/κεφ_Ι(0,5)_ἀσκήματα_τέλος.pdf) · [энклитики+немного\\_алфавита\\_и\\_практики\\_письма\\_τέλος.pdf]({NB_REMOTE}/энклитики+немного_алфавита_и_практики_письма_τέλος.pdf)
    """)
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, mo):
    mo.md(fr"""
    ## Проверка домашнего задания · τὸ δεύτερον προστεταγμένον

    ### 1. Вопросы о Δικαιόπολις · [κεφ\_Ι(0,5)\_ἀσκήματα\_τέλος.pdf]({NB_REMOTE}/κεφ_Ι(0,5)_ἀσκήματα_τέλος.pdf)

    | Вопрос | Ответ |
    |:-------|:------|
    | Τίς ἐστιν ὁ Δικαιόπολις; | ὁ Δικαιόπολις **αὐτουργός** ἐστιν |
    | Ποδαπός ἐστιν ὁ Δ.; | ὁ Δ. **Ἀθηναῖος** ἐστιν |
    | Ποῦ ὁ Δ. οὐκ οἰκεῖ; Ποῦ οἰκεῖ; | ὁ Δ. οὐκ ἐν ταῖς Ἀθήναις, ἀλλὰ **ἐν τοῖς ἀγροῖς** οἰκεῖ |
    | Διὰ τί οἰκεῖ ἐν τοῖς ἀγροῖς; | αὐτουργὸς **γάρ** ἐστιν |
    | Ἆρα Ῥωμαῖός ἐστιν ὁ Δ.; | οὐδαμῶς — οὐ Ῥωμαῖος, ἀλλὰ **Ἀθηναῖος** ἐστιν |

    ### 2. Энклитики · [энклитики+немного\_алфавита\_и\_практики\_письма\_τέλος.pdf]({NB_REMOTE}/энклитики+немного_алфавита_и_практики_письма_τέλος.pdf)

    Файл с ответами на упражнение 8 и задание на алфавит.
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
    ## ἐρωτῶ · Стяжённый глагол (-άω)

    Глагол **ἐρωτάω** («спрашивать») в настоящем времени стягивает -ά- + окончание:

    | | ὁριστική | προστακτική |
    |:--|:--:|:--:|
    | (σύ) | ἐρωτ**ᾷς** | ἐρ**ώ**τα |
    | (ὑμεῖς) | ἐρωτ**ᾶ**τε | ἐρωτ**ᾶ**τε |

    Ударение при стяжении: ἐρ**ώ**ταε → ἐρ**ώ**τα (σύ) — острое; ἐρωτ**ά**ετε → ἐρωτ**ᾶ**τε (ὑμεῖς) — облегчённое.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## ἀποκρίνομαι · γίγνομαι · Повелительное среднего залога

    Глаголы **среднего залога** оканчиваются на **-μαι**. Их повелительное наклонение:

    | ὁριστική | (σύ) | (ὑμεῖς) |
    |:---------|:----:|:-------:|
    | ἀποκρίνο**μαι** | ἀποκρίν**ου** | ἀποκρίν**εσθε** |
    | γίγνο**μαι** | γίγν**ου** | γίγν**εσθε** |

    > **γίγνεσθε καλοὶ μαθηταί!** — Будьте хорошими учениками!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## ἐν τῇ παλαίστρᾳ · В классе

    | | |
    |:--|:--|
    | διδάσκαλος λέγει: | **ἀποκρίνεσθε, ὦ μαθηταί** |
    | οἱ μαθηταὶ λέγουσιν: | **πρῶτον ἐρώτα, ὦ διδάσκαλε!** |

    | Выражение | Перевод |
    |:----------|:--------|
    | συγνώμην ἔχε! | Извини! / Прости! |
    | σύγνωθι! | Прости! (аорист) |
    | τίς μέμνηται; | Кто помнит? |
    | ἐγὼ μέμνημαι! | Я помню! |
    | τίς οἶδε; | Кто знает? |
    | ἐγὼ οἶδα! | Я знаю! |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## ὁ αὐτουργός · Гражданин и воин

    Афинский αὐτουργός совмещал три роли:

    - **γεωργός** — земледелец (обрабатывал свой κλῆρος — надел)
    - **πολίτης** — участник политических процессов
    - **στρατιώτης** — солдат-гоплит народного ополчения
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## ἡ ἀρετή, -ῆς

    «превосходство, доблесть» (Hom. Il.)

    > **Ил. XIII. 275, 277** (Идоменей — Мериону):
    >
    > *οἶδʼ ἀρετὴν οἷός ἐσσι· τί σε χρὴ ταῦτα λέγεσθαι;*
    > *…ἔνθα μάλιστʼ ἀρετὴ διαείδεται ἀνδρῶν*
    >
    > «Ведаю доблесть твою, и об ней говоришь ты напрасно» —
    > «…в засадах опасных мужей открывается доблесть» (Н. И. Гнедич)
    >
    > «Знаю я доблесть твою. Зачем мне о ней говоришь ты? —
    > …Доблесть мужей ведь всего проявляется больше в засадах» (В. В. Вересаев)

    Словообразовательное гнездо (Beekes, *EDG* p. 128):

    | слово | значение | примечание |
    |:------|:---------|:-----------|
    | **ἀρείων** | «лучше, благороднее, доблестнее» | сравнительная степень (Hom. Il.); микен. *a-rjo-a* /arjoha/ |
    | **ἄριστος** | «наилучший» | превосходная степень |
    | **ἀρός** | «польза, выгода» | ἀρός· ὄφελος (Hesych.) |

    И.-е. корень: предположительно *\*h₂erh₁-*.

    Этимология спорна: связь с **ἀρείων** семантически привлекательна, но формально неясна
    (Beekes p. 128). Nikolaev (2005) реконструирует *\*h₂nr-etéh₂-* — от слова «мужчина, герой».
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## II склонение · ὁ κλῆρος (о-основа)

    | πτῶσις | ἄρθρον | κλῆρος |
    |:-------|:------:|:------:|
    | ὀνομαστική | ὁ | κλῆρ**ος** |
    | γενική | τοῦ | κλήρ**ου** |
    | δοτική | τῷ | κλήρ**ῳ** |
    | αἰτιατική | τόν | κλῆρ**ον** |
    | κλητική | ὦ | κλῆρ**ε** |

    *βλέπω τὸν κλῆρον* — вижу надел (αἰτιατική = прямое дополнение).

    Ударение: перед длинным окончанием (-ου, -ῳ) περισπώμενον → ὀξύ: κλ**ῆ**ρος, но κλ**ή**ρου, κλ**ή**ρῳ.
    """)
    return


@app.cell(hide_code=True)
def _(NB_DIR, NB_REMOTE, gu):
    for _pdf in (
        'Κεφ.I(1).pdf',
        'заметки_19.06.pdf',
        'κεφ_Ι(0,5)_ἀσκήματα_τέλος.pdf',
        'энклитики+немного_алфавита_и_практики_письма_τέλος.pdf',
    ):
        gu.ensure_file(_pdf, nb_dir=NB_DIR, remote_base=NB_REMOTE)
    return


@app.cell(hide_code=True)
def _(NB_DIR, NB_REMOTE, gu, mo):
    _verbs = gu.load_vocab_table("verbs.tsv", nb_dir=NB_DIR, remote_base=NB_REMOTE)
    _nouns = gu.load_vocab_table("nouns.tsv", nb_dir=NB_DIR, remote_base=NB_REMOTE)
    _adj = gu.load_vocab_table("adjectives.tsv", nb_dir=NB_DIR, remote_base=NB_REMOTE)
    mo.vstack([
        mo.md("## Capitulum I · Словарь Athenaze"),
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
    | | πολλάκις — часто (saepe) | ὦ — о! (o!) |
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
    ## τὸ τρίτον προστεταγμένον · Домашнее задание

    **Μελετήματα** (Carmelo Consoli), Capitolo I, стр. 7–8 — упражнения после первого чтения (linee 1–16):

    **1.1.** Дополните предложения, добавив нужные окончания и артикли:

    1. Ὁ Δικαιόπολις αὐτουργ_____ ἐστιν.
    2. _____ αὐτουργὸς ἰσχυρ_____ ἐστιν.
    3. Ὁ ἀγρ_____ μικρ_____ ἐστιν.
    4. _____ πόνος μακρ_____ ἐστιν.
    5. Ὁ αὐτουργὸς πον_____.
    6. Ὁ κλῆρ_____ παρέχ_____ σῖτ_____.
    7. Ὁ κλῆρ_____ μικρ_____ ἐστιν, ἀλλὰ καλ_____.
    8. _____ Δικαιόπολις γεωργ_____ τὸν ἀγρ_____.
    9. Ὁ αὐτουργ_____ φιλ_____ _____ καλ_____ κλῆρ_____.
    10. Οὐ πολ_____ σῖτ_____ ἀλλὰ ἱκαν_____ παρέχει _____ κλῆρ_____.

    **1.2.** Вставьте подходящее слово из списка (форма может меняться):
    *(αὐτουργός, βίος, κλῆρος, σῖτος, ἱκανός, ἰσχυρός, μακρός, γεωργεῖ, οἰκεῖ, πονεῖ, χαίρει)*

    1. Ὁ Δικαιόπολις οὐκ ἐν ταῖς Ἀθήναις _________, ἀλλὰ ἐν τοῖς ἀγροῖς.
    2. Ὁ Δικαιόπολις _________ ἐστιν, οἰκεῖ γάρ ἐν τοῖς ἀγροῖς.
    3. Ὁ αὐτουργὸς _________ τὸν ἀγρόν· καὶ ἐν τοῖς ἀγροῖς _________· _________ ἐστιν ὁ πόνος, ἀλλ' ὁ ἄνθρωπος _________ ἐστιν.
    4. Χαλεπός ἐστιν ὁ _________, ἀλλ' ὁ ἄνθρωπος _________, ἐλεύθερος γάρ ἐστιν.
    5. Ὁ _________ παρέχει _________ οὐ πολὺν ἀλλ' _________.

    **1.3.** Заполните таблицу (ὀνομαστική ↔ αἰτιατική):

    | ὀνομαστική | αἰτιατική |
    |:----------:|:---------:|
    | βίος | |
    | | αὐτουργόν |
    | μικρός | |
    | ἐλεύθερος | |
    | | τόν |
    | | πολύν |
    | κλῆρος | |
    """)
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, mo):
    mo.md(fr"""
    ### [Κεφ.I(1).pdf]({NB_REMOTE}/Κεφ.I(1).pdf)

    ### 1. Τί οὐκ ἔστι τούτου αὐλίου καὶ διὰ τί; · Что лишнее?

    Ἰσχυρός · καλός · ἄοκνος · **σῖτος** · μικρός · πολύς

    ### 2. προσάπτετε τὰς περιόδους (1) · Соедините предложения

    - Μικρὸς μὲν ὁ ἀγρός ἐστιν, ὁ δὲ πόνος ἀπέραντος.
    - ὁ βίος χαλεπός ἐστιν.

    *Выберите подходящую частицу — возможно несколько вариантов.*

    ### 3. Τί ἐστι; · Что это?

    > Μικρὸς μέν ἐστι, σῖτον δὲ παρέχει οὐ πολὺν, ἀλλὰ ἱκανόν.

    ### 4. Γεμίζετε (1) · *ἀεί / οὖν / αὐτουργός / γάρ / δέ*

    Ὁ Δικαιόπολις \_\_\_\_\_\_\_\_\_ ἐστιν· τὸν \_\_\_ κλῆρον \_\_\_ γεωργεῖ·
    μικρὸς μὲν \_\_\_\_\_ ὁ ἀγρός ἐστι, πολὺν \_\_\_ σῖτον παρέχει.

    ### 5. προσάπτετε τὰς περιόδους (2) · Соедините предложения

    - ὁ Δικαιόπολις τὸν οἶκον φιλεῖ.
    - Μικρὸς μέν ἐστι, καλός δέ.

    *Выберите подходящую частицу — возможно несколько вариантов.*

    ### 6. Τί ἐστι; (ἐπίθετον) · Какое прилагательное?

    > ἀεὶ πονεῖ καὶ φιλεῖ τὸν πόνον

    ### 7. Γεμίζετε (2) · *ἀεί / πολλάκις / ἐλεύθερος / ἰσχυρός / χαίρει / πονεῖ*

    Ὁ Δικαιόπολις \_\_\_\_\_\_\_\_ ἐστι καὶ ἐν τοῖς ἀγροῖς ἀεὶ \_\_\_\_\_\_\_\_\_·
    στενάζει δὲ \_\_\_\_\_\_\_\_\_· ὁ γὰρ πόνος μακρὸς καὶ χαλεπός ἐστιν.
    Ἀλλ' \_\_\_\_ ὁ αὐτουργὸς \_\_\_\_\_\_\_\_\_· ἄνθρωπος γὰρ \_\_\_\_\_\_\_\_\_ ἐστιν.
    """)
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(cfg, mo):
    from eee_project import GreekUtils, ANCIENT_GREEK
    from eee_project.notebook_utils import eee_footer
    from pathlib import Path as _Path
    gu = GreekUtils(mo_module=mo, config=ANCIENT_GREEK)
    NB_DIR = _Path(__file__).parent
    NB_REMOTE = cfg.nb_remote("2026_06_19")
    _prev_url, _next_url = cfg.adjacent_urls("2026_06_19/")
    eee_footer(mo, lang='ru', prev_url=_prev_url, next_url=_next_url, same_window=True)
    return NB_DIR, NB_REMOTE, gu


if __name__ == "__main__":
    app.run()
