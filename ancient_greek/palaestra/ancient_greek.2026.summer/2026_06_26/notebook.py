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
               ga_config=cfg.ga_config(), same_window=True)
    return (cfg,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Δίδαγμα ς'
    **Palaestra — Древнегреческий язык, начальный уровень — Лето 2026**
    """)
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, mo):
    _cap1_remote = NB_REMOTE.replace("/2026_06_26", "/2026_06_16")
    _course_remote = NB_REMOTE.replace("/2026_06_26", "")
    mo.md(f"**Материалы занятия:** [заметки\\_26.06.pdf]({NB_REMOTE}/заметки_26.06.pdf) · [τόνος+κλίσις β'.pdf]({NB_REMOTE}/τόνος+κλίσις β'.pdf) · [κεφ(Ι)\\_ἀσκήματα.pdf]({NB_REMOTE}/κεφ(Ι)_ἀσκήματα.pdf) · [κεφ.I, (3)\\_ἀσκήματα\\_τέλος.pdf]({NB_REMOTE}/κεφ.I, (3)_ἀσκήματα_τέλος.pdf) · [Athenaze\\_1\\_vocabula.pdf]({_cap1_remote}/Athenaze_1_vocabula.pdf) · [CONSPECTVS GRAMMATICVS I\\_graecus.pdf]({_course_remote}/CONSPECTVS GRAMMATICVS I_graecus.pdf)")
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, mo):
    mo.md(fr"""
    ## Проверка домашнего задания · τὸ τέταρτον προστεταγμένον

    [κεφ.I, (3)\_ἀσκήματα\_τέλος.pdf]({NB_REMOTE}/κεφ.I, (3)_ἀσκήματα_τέλος.pdf) — файл с ответами.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## ἡ δευτέρα κλίσις · II склонение (о-основа)

    | ἡ πτῶσις | τὸ ἄρθρον | ὁ ἀγρός | τὰ ἄρθρα | οἱ ἀγροί |
    |:---------|:---------:|:-------:|:--------:|:--------:|
    | ὀνομαστική | ὁ | ἀγρ**ός** | οἱ | ἀγρ**οί** |
    | αἰτιατική *(ποῖ; πρός)* | τόν | ἀγρ**όν** | τούς | ἀγρ**ούς** |
    | γενική *(πόθεν; ἐκ/ἐξ)* | τοῦ | ἀγρ**οῦ** | τῶν | ἀγρ**ῶν** |
    | δοτική *(ποῦ; ἐν + ὑπό)* | τῷ | ἀγρ**ῷ** | τοῖς | ἀγρ**οῖς** |

    > *ὁ Δ. βαδίζει πρὸς τὸν ἀγρόν.* (ποῖ → αἰτιατική)
    > *ὁ δοῦλος μένει πρὸς τῷ ἀγρῷ.* (ποῦ → δοτική)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## πολύς · μέγας · Неправильные формы

    | | ὀνομαστική | αἰτιατική |
    |:--|:--:|:--:|
    | **πολύς** | πολύς | **πολύν** / (ἱκανόν) |
    | **μέγας** | μέγας | **μέγαν** |

    > *φέρει **μέγαν** λίθον ἐκ τοῦ ἀγροῦ* — несёт большой камень с поля.
    > *παρέχει σῖτον οὐ **πολύν**, ἀλλὰ **ἱκανόν*** — даёт зерна не много, но достаточно.

    ## Ποῦ; / Πόθεν; / Ποῖ; · Сводная таблица

    | вопрос | семантика | падеж | предлог |
    |:-------|:----------|:-----:|:-------:|
    | **Ποῦ;** — где? | место (τόπος) | δοτική | ἐν, ὑπό, πρός |
    | **Πόθεν;** — откуда? | происхождение (γένεσις) | γενική | ἐκ, ἀπό |
    | **Ποῖ;** — куда? | движение (κίνησις) | αἰτιατική | πρός, εἰς |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## ὅς, ἥ, ὅ · Относительное местоимение

    Вводит придаточное определительное:

    > *ὁ ἥλιος = σῶμα ἐν τῷ οὐρανῷ, **ὃ** φλέγει καὶ τοὺς γεωργοὺς κατατρίβει.*
    > «Солнце — небесное тело, **которое** жжёт и изнуряет земледельцев.»

    Согласуется с антецедентом в роде и числе, падеж определяется ролью в придаточном.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## μέν · δέ · Противопоставление

    **μέν … δέ** — «с одной стороны … с другой / а»:

    > *ὁ **μὲν** δεσπότης πονεῖ, ὁ **δὲ** δοῦλος ἡσυχάζει.*
    > «Хозяин трудится, а раб отдыхает.»

    > *μικρὸς **μὲν** ὁ ἀγρός ἐστιν, **ἀλλ'** ὁ ἄνθρωπος ἰσχυρός.*

    **Ἥλιος:**

    | | глагол |
    |:--|:--|
    | πρῶτον μέν | **ἀνατέλλει** — восходит |
    | ἔπειτα δέ | **φλέγει καὶ κατατρίβει** — жжёт и изнуряет |
    | τέλος δέ | **καταδύνει** — заходит |

    *ἡ ἀνατολή, -ῆς* (восход, восток) ↔ *ἡ δύσις, -εως* (закат, запад)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Про порядок падежей

    **Откуда порядок Nom–Gen–Dat–Acc–Voc?**
    Александрийская традиция — [Дионисий Фракийский](https://www.academia.edu/52422942/The_Origin_of_the_Opposition_%CF%80%CF%84%CF%89%CE%B9%CF%83%CF%82_%D0%BE%CF%81%CE%B8%CE%AE_%CE%B5%CF%85%CE%B8%CE%B5%CE%AF%CE%B1_%CF%80%CF%84%CF%8E%CF%83%CE%B5%CE%B9%CF%82_%CF%80%CE%BB%CE%AC%CE%B3%CE%B9%CE%B1%CE%B9_i_Casus_Rectus_Casus_Obliqui_i_in_the_Linguistics_of_Ancient_Greece) (II–I вв. до н.э.) кодифицировал его для нужд школы (чтение Гомера). Он унаследовал стоический приоритет генитива, но лишил его философского содержания: порядок стал просто каноном парадигм.

    **Почему стоики ставили генитив первым?**
    Для стоиков падеж — логико-семантическая категория ([λεκτόν](https://www.degruyterbrill.com/document/doi/10.1515/apeiron-2023-0115/html)), не морфологическая. Генитив выражает *отношение* одной вещи к другой (Σωκράτους = Сократ, рассматриваемый через связь), а это согласуется с их учением о взаимосвязи вещей в космосе. Аккузатив выражает объект *действия* — он появляется уже внутри события, потому вторичен.

    **Почему в практике аккузатив?**
    Синтаксически самый частотный: прямое дополнение + большинство предлогов. У Аполлония Дискола (II в. н.э., теория управления глагола) выходит на первый план.

    | Эпоха | Что такое падеж |
    |:---|:---|
    | [Аристотель](https://classics.washington.edu/events/2024-02-22/two-notions-case-aristotle), IV в. до н.э. | πτῶσις = любое отклонение от основной формы (*Поэтика*, гл. 20) |
    | Стоики, III–II вв. до н.э. | логическое отношение предмета (λεκτόν) |
    | Дионисий Фракийский, II–I вв. до н.э. | морфологическая парадигма для школы |
    | Аполлоний Дискол, II в. н.э. | синтаксическое управление |
    | Византия, V–XV вв. → сегодня | школьный канон |
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

    _course_remote = NB_REMOTE.replace("/2026_06_26", "")
    _cap1_remote = NB_REMOTE.replace("/2026_06_26", "/2026_06_16")
    gu.ensure_file('CONSPECTVS GRAMMATICVS I_graecus.pdf', nb_dir=NB_DIR, remote_base=_course_remote)
    gu.ensure_file('Athenaze_1_vocabula.pdf', nb_dir=NB_DIR, remote_base=_cap1_remote)
    for _pdf in (
        'заметки_26.06.pdf',
        'τόνος+κλίσις β\'.pdf',
        'κεφ(Ι)_ἀσκήματα.pdf',
        'κεφ.I, (3)_ἀσκήματα_τέλος.pdf',
    ):
        gu.ensure_file(_pdf, nb_dir=NB_DIR, remote_base=NB_REMOTE)
    for _f in ('cap1_verbs.tsv', 'cap1_nouns.tsv', 'cap1_adjectives.tsv', 'cap1_particles.tsv'):
        gu.ensure_file(_f, nb_dir=NB_DIR, remote_base=NB_REMOTE)
    return (load_tsv,)


@app.cell(hide_code=True)
def _(load_tsv, mo):
    _verbs = load_tsv("verbs.tsv")
    _nouns = load_tsv("nouns.tsv")
    mo.vstack([
        mo.md("## Νέαι λέξεις · Новые слова"),
        mo.md("**Verba (глаголы):**"),
        mo.ui.table(_verbs, selection=None),
        mo.md("**Nomina substantiva (существительные):**"),
        mo.ui.table(_nouns, selection=None),
    ])
    return


@app.cell(hide_code=True)
def _(NB_DIR, NB_REMOTE, gu):
    VOCAB_WORDS = gu.load_vocab_tsv(
        'verbs.tsv', 'nouns.tsv',
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
        comment='Для ввода используйте **polytonic Greek keyboard** или кнопки диакритики ниже.<br>**Как пользоваться:** нажмите кнопку знака диакритики → введите гласную → знак применится. Нажмите повторно или введите согласную — снимается.',
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Склонение существительных · II-е склонение (о-основа)
    """)
    return


@app.cell(hide_code=True)
def _(NB_DIR, NB_REMOTE, gu):
    WORDS_NOUN_N3 = [
        {"Word": w["form"], "Translation": w["meaning"]}
        for w in gu.load_vocab_tsv('cap1_nouns.tsv', nb_dir=NB_DIR, remote_base=NB_REMOTE)
    ]
    return (WORDS_NOUN_N3,)


@app.cell(hide_code=True)
def _(WORDS_NOUN_N3, mo):
    w4t_n3, set_w4t_n3 = mo.state(list(WORDS_NOUN_N3))
    hist_n3, set_hist_n3 = mo.state([])
    msg_n3, set_msg_n3 = mo.state("")
    cap_n3, set_cap_n3 = mo.state(None)
    entered_n3, set_entered_n3 = mo.state({})
    sub_cnt_n3, set_sub_cnt_n3 = mo.state(0)
    prev_cnt_n3, set_prev_cnt_n3 = mo.state(0)
    nxt_cnt_n3, set_nxt_cnt_n3 = mo.state(0)
    restart_cnt_n3, set_restart_cnt_n3 = mo.state(0)
    entercnt_n3, set_entercnt_n3 = mo.state(0)
    errors_n3, set_errors_n3 = mo.state({})
    retry_cnt_n3, set_retry_cnt_n3 = mo.state(0)
    return (
        cap_n3,
        entercnt_n3,
        entered_n3,
        errors_n3,
        hist_n3,
        msg_n3,
        nxt_cnt_n3,
        prev_cnt_n3,
        restart_cnt_n3,
        retry_cnt_n3,
        set_cap_n3,
        set_entercnt_n3,
        set_entered_n3,
        set_errors_n3,
        set_hist_n3,
        set_msg_n3,
        set_nxt_cnt_n3,
        set_prev_cnt_n3,
        set_restart_cnt_n3,
        set_retry_cnt_n3,
        set_sub_cnt_n3,
        set_w4t_n3,
        sub_cnt_n3,
        w4t_n3,
    )


@app.cell(hide_code=True)
def _(
    entered_n3,
    gu,
    hist_n3,
    set_entercnt_n3,
    set_nxt_cnt_n3,
    set_prev_cnt_n3,
    w4t_n3,
):
    cv_n3 = w4t_n3()[0] if w4t_n3() else None
    _, _, noun_meta_n3 = gu.create_noun_test_ui([cv_n3] if cv_n3 else [])
    _ac_n3 = getattr(noun_meta_n3, "active_cases", [])
    _entered_form_n3 = entered_n3().get(cv_n3["Word"]) if cv_n3 else None
    noun_form_n3, prev_btn_n3, nxt_btn_n3, restart_btn_n3 = gu.paradigm_drill_widgets(
        labels=[f"{n} {c}:" for n, c in _ac_n3],
        values=_entered_form_n3,
        history_len=len(hist_n3()),
        remaining_len=len(w4t_n3()),
        next_label="Следующее",
        prev_label="Предыдущее",
    )
    set_prev_cnt_n3(0)
    set_nxt_cnt_n3(0)
    set_entercnt_n3(0)
    return (
        cv_n3,
        noun_form_n3,
        noun_meta_n3,
        nxt_btn_n3,
        prev_btn_n3,
        restart_btn_n3,
    )


@app.cell(hide_code=True)
def _(
    WORDS_NOUN_N3,
    cap_n3,
    check_btn_n3,
    cv_n3,
    entercnt_n3,
    entered_n3,
    errors_n3,
    gu,
    hist_n3,
    msg_n3,
    noun_form_n3,
    noun_meta_n3,
    nxt_btn_n3,
    nxt_cnt_n3,
    prev_btn_n3,
    prev_cnt_n3,
    restart_btn_n3,
    restart_cnt_n3,
    retry_btn_n3,
    retry_cnt_n3,
    set_cap_n3,
    set_entercnt_n3,
    set_entered_n3,
    set_errors_n3,
    set_hist_n3,
    set_msg_n3,
    set_nxt_cnt_n3,
    set_prev_cnt_n3,
    set_restart_cnt_n3,
    set_retry_cnt_n3,
    set_sub_cnt_n3,
    set_w4t_n3,
    sub_cnt_n3,
    w4t_n3,
):
    gu.noun_paradigm_drill_form(
        w4t_n3, set_w4t_n3, hist_n3, set_hist_n3, msg_n3, set_msg_n3,
        cap_n3, set_cap_n3, entered_n3, set_entered_n3,
        sub_cnt_n3, set_sub_cnt_n3, prev_cnt_n3, set_prev_cnt_n3,
        nxt_cnt_n3, set_nxt_cnt_n3, entercnt_n3, set_entercnt_n3,
        restart_cnt_n3, set_restart_cnt_n3,
        cv_n3, noun_form_n3, check_btn_n3, prev_btn_n3, nxt_btn_n3, restart_btn_n3,
        vocab=WORDS_NOUN_N3,
        noun_meta=noun_meta_n3,
        word_key="Word",
        meaning_key="Translation",
        meaning_label="Перевод",
        title="## Упражнение 3 · Склонение существительных",
        done_message="✅ Все существительные пройдены!",
        get_errors=errors_n3, set_errors=set_errors_n3,
        get_retry_cnt=retry_cnt_n3, set_retry_cnt=set_retry_cnt_n3,
        retry_btn=retry_btn_n3,
    )
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, mo):
    mo.md(f"""
    ## τὸ πέμπτον προστεταγμένον · Домашнее задание

    1. **αὖθις ἀναγιγνώσκετε ὅλον τὸ πρῶτον κεφάλαιον** — ещё раз перечитайте всю первую главу.

    2. **ἀσκήματα ποιεῖτε** из [κεφ(Ι)\\_ἀσκήματα.pdf]({NB_REMOTE}/κεφ(Ι)_ἀσκήματα.pdf).
    """)
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, mo):
    _cap1_remote = NB_REMOTE.replace("/2026_06_26", "/2026_06_16")
    mo.md(f"""## Весь словарь Athenaze I · [Athenaze\\_1\\_vocabula.pdf]({_cap1_remote}/Athenaze_1_vocabula.pdf)""")
    return


@app.cell(hide_code=True)
def _(NB_DIR, NB_REMOTE, gu):
    VOCAB_ALL = gu.load_vocab_tsv(
        'cap1_verbs.tsv', 'cap1_nouns.tsv', 'cap1_adjectives.tsv', 'cap1_particles.tsv',
        nb_dir=NB_DIR, remote_base=NB_REMOTE,
    )
    return (VOCAB_ALL,)


@app.cell(hide_code=True)
def _(mo):
    cv_a, set_cv_a = mo.state(None)
    score_a, set_score_a = mo.state({'correct': 0, 'total': 0})
    remaining_a, set_remaining_a = mo.state(None)
    history_a, set_history_a = mo.state([])
    future_a, set_future_a = mo.state([])
    restore_entry_a, set_restore_entry_a = mo.state(None)
    return (
        cv_a,
        future_a,
        history_a,
        remaining_a,
        restore_entry_a,
        score_a,
        set_cv_a,
        set_future_a,
        set_history_a,
        set_remaining_a,
        set_restore_entry_a,
        set_score_a,
    )


@app.cell(hide_code=True)
def _(VOCAB_ALL, cv_a, gu, history_a, remaining_a, restore_entry_a):
    _ = cv_a()
    answer_radio_a, next_btn_a, prev_btn_a = gu.word_quiz_widgets(
        cv=cv_a(),
        remaining=remaining_a(),
        vocab=VOCAB_ALL,
        restore_entry=restore_entry_a(),
        history_len=len(history_a()),
    )
    return answer_radio_a, next_btn_a, prev_btn_a


@app.cell(hide_code=True)
def _(
    VOCAB_ALL,
    answer_radio_a,
    cv_a,
    future_a,
    gu,
    history_a,
    next_btn_a,
    prev_btn_a,
    remaining_a,
    restore_entry_a,
    score_a,
    set_cv_a,
    set_future_a,
    set_history_a,
    set_remaining_a,
    set_restore_entry_a,
    set_score_a,
):
    gu.word_quiz_form(
        cv_a, set_cv_a, remaining_a, set_remaining_a,
        score_a, set_score_a, restore_entry_a, set_restore_entry_a,
        history_a, set_history_a, future_a, set_future_a,
        answer_radio_a, next_btn_a, prev_btn_a,
        vocab=VOCAB_ALL,
        title='## Упражнение 4 · Выбрать слово',
    )
    return


@app.cell(hide_code=True)
def _(mo):
    cv_aw, set_cv_aw = mo.state(None)
    score_aw, set_score_aw = mo.state({'correct': 0, 'total': 0})
    remaining_aw, set_remaining_aw = mo.state(None)
    history_aw, set_history_aw = mo.state([])
    future_aw, set_future_aw = mo.state([])
    restore_entry_aw, set_restore_entry_aw = mo.state(None)
    return (
        cv_aw,
        future_aw,
        history_aw,
        remaining_aw,
        restore_entry_aw,
        score_aw,
        set_cv_aw,
        set_future_aw,
        set_history_aw,
        set_remaining_aw,
        set_restore_entry_aw,
        set_score_aw,
    )


@app.cell(hide_code=True)
def _(cv_aw, gu, history_aw, remaining_aw, restore_entry_aw):
    _ = cv_aw()
    write_input_aw, dia_aw, check_btn_aw, prev_btn_aw, next_btn_aw = gu.word_drill_widgets(
        cv=cv_aw(),
        remaining=remaining_aw(),
        restore_entry=restore_entry_aw(),
        history_len=len(history_aw()),
    )
    return check_btn_aw, dia_aw, next_btn_aw, prev_btn_aw, write_input_aw


@app.cell(hide_code=True)
def _(
    VOCAB_ALL,
    check_btn_aw,
    cv_aw,
    dia_aw,
    future_aw,
    gu,
    history_aw,
    next_btn_aw,
    prev_btn_aw,
    remaining_aw,
    restore_entry_aw,
    score_aw,
    set_cv_aw,
    set_future_aw,
    set_history_aw,
    set_remaining_aw,
    set_restore_entry_aw,
    set_score_aw,
    write_input_aw,
):
    gu.word_drill_form(
        cv_aw, set_cv_aw, remaining_aw, set_remaining_aw,
        score_aw, set_score_aw, restore_entry_aw, set_restore_entry_aw,
        history_aw, set_history_aw, future_aw, set_future_aw,
        write_input_aw, dia_aw, check_btn_aw, prev_btn_aw, next_btn_aw,
        vocab=VOCAB_ALL,
        title='## Упражнение 5 · Написать греческое слово',
        comment='Для ввода используйте **polytonic Greek keyboard** или кнопки диакритики ниже.<br>**Как пользоваться:** нажмите кнопку знака диакритики → введите гласную → знак применится. Нажмите повторно или введите согласную — снимается.',
    )
    return


@app.cell(hide_code=True)
def _(VOCAB_WORDS):
    _REQUIRED = {"form", "meaning"}
    assert VOCAB_WORDS, "load_vocab_tsv returned empty list"
    assert all(_REQUIRED <= set(w) for w in VOCAB_WORDS), f"word missing keys: {VOCAB_WORDS}"
    assert all(w["form"] and w["meaning"] for w in VOCAB_WORDS), "word has empty form or meaning"
    del _REQUIRED
    return


@app.cell(hide_code=True)
def _(VOCAB_ALL):
    _REQUIRED = {"form", "meaning"}
    assert VOCAB_ALL, "load_vocab_tsv returned empty list (cap1)"
    assert all(_REQUIRED <= set(w) for w in VOCAB_ALL), f"cap1 word missing keys: {VOCAB_ALL}"
    assert all(w["form"] and w["meaning"] for w in VOCAB_ALL), "cap1 word has empty form or meaning"
    del _REQUIRED
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
async def _(cfg, mo):
    import eee_project as eee
    from ancient_greek_backend_eee import AncientGreekBackend
    from eee_project import GreekUtils, ANCIENT_GREEK, setup_ancient_greek
    from eee_project.notebook_utils import eee_footer
    from pathlib import Path as _Path
    NB_DIR = _Path(__file__).parent
    NB_REMOTE = cfg.nb_remote("2026_06_26")
    _noun_yaml = NB_DIR.parent / "athenaze_cap1_nouns.yaml"
    _verb_yaml = NB_DIR.parent / "athenaze_cap1_verbs.yaml"
    await GreekUtils.ensure_files(
        _noun_yaml.name, _verb_yaml.name, nb_dir=NB_DIR.parent, remote_base=cfg.raw_base,
    )
    ag = AncientGreekBackend(lexicons=["pratt", "ltrg", str(_verb_yaml.resolve()), str(_noun_yaml.resolve())])
    setup_ancient_greek(ag)
    gu = GreekUtils(ag, mo, eee_module=eee, config=ANCIENT_GREEK)
    _prev_url, _next_url = cfg.adjacent_urls("2026_06_26/")
    eee_footer(mo, lang='ru', prev_url=_prev_url, next_url=_next_url, same_window=True)
    return NB_DIR, NB_REMOTE, gu


@app.cell(hide_code=True)
def _(cap_n3, cv_n3, gu, noun_form_n3, set_sub_cnt_n3):
    check_btn_n3 = gu.dirty_check_button(
        noun_form_n3, cap_n3, cv_n3, "test_word", word_key="Word", label="Проверить"
    )
    set_sub_cnt_n3(0)
    return (check_btn_n3,)


@app.cell(hide_code=True)
def _(errors_n3, gu):
    # Noun retry-mistakes button
    retry_btn_n3 = gu.retry_mistakes_button(errors_n3())
    return (retry_btn_n3,)


if __name__ == "__main__":
    app.run()
