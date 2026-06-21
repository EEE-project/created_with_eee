# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.23.3",
#     "pandas>=2.0",
#     "eee-project @ git+https://codeberg.org/EEE-project/eee-project.git",
#     "ancient-greek-backend-eee @ git+https://codeberg.org/EEE-project/ancient-greek-backend-eee.git",
# ]
#
# [tool.uv.sources]
# eee-project = { git = "https://codeberg.org/EEE-project/eee-project.git" }
# ancient-greek-backend-eee = { git = "https://codeberg.org/EEE-project/ancient-greek-backend-eee.git" }
# ///

import marimo

__generated_with = "0.23.10"
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
    # Δίδαγμα δ'
    **Palaestra — Древнегреческий язык, начальный уровень — Лето 2026**
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
    | (σύ) | ἐρωτ**ῶ** | ἐρ**ώ**τα |
    | (ὑμεῖς) | ἐρωτ**ᾶ**τε | ἐρωτ**ᾶ**τε |

    Ударение облегчённое на месте стяжения: ἐρ**ώ**τα (σύ), ἐρωτ**ᾶ**τε (ὑμεῖς).
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
    import pandas as _pd_tsv

    def load_tsv(filename):
        return _pd_tsv.read_csv(
            gu.ensure_file(filename, nb_dir=NB_DIR, remote_base=NB_REMOTE),
            sep="\t",
        )

    for _pdf in (
        'заметки_19.06.pdf',
        'κεφ_Ι(0,5)_ἀσκήματα_τέλος.pdf',
        'энклитики+немного_алфавита_и_практики_письма_τέλος.pdf',
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
    write_input_w = gu.diacritics_text(placeholder='греческое слово…')
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
        else:
            _ok = gu._ci(write_input_w.value.strip(), {cv_w()['form']})
            set_score_w({'correct': score_w()['correct'] + int(_ok), 'total': score_w()['total'] + 1})
            set_cv_w(_r[0] if _r else None)
            set_remaining_w(_r[1:] if _r else [])
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
            mo.md('## Упражнение 2 · Написать греческое слово'),
            mo.md('Для ввода используйте **polytonic Greek keyboard** или кнопки диакритики ниже.<br>**Как пользоваться:** нажмите кнопку знака диакритики → введите гласную → знак применится. Нажмите повторно или введите согласную — снимается. Можно **совмещать несколько знаков диакритики** (например, придыхание + ударение перед вводом буквы → ἆ).'),
            mo.md(f'**{_s["total"] + 1}** / {len(VOCAB_WORDS)} — правильно: {_s["correct"]}'),
            _fb,
            write_input_w,
            mo.hstack([check_btn_w, next_btn_w], justify='start'),
        ])
    _out
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
def _():
    import marimo as mo
    import random

    return mo, random


@app.cell(hide_code=True)
def _(cfg, mo):
    from eee_project import GreekUtils, ANCIENT_GREEK
    from eee_project.notebook_utils import eee_footer
    from pathlib import Path as _Path
    gu = GreekUtils(mo_module=mo, config=ANCIENT_GREEK)
    NB_DIR = _Path(__file__).parent
    NB_REMOTE = f"{cfg.raw_base}/2026_06_19"
    eee_footer(mo, lang='ru')
    return NB_DIR, NB_REMOTE, gu


if __name__ == "__main__":
    app.run()
