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

__generated_with = "0.23.14"
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
    # Δίδαγμα ι' · Κεφάλαιον II
    **Palaestra — Древнегреческий язык, начальный уровень — Лето 2026**

    [![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_s6Zjygc4nNszNDedyFiqCn)
    """)
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, mo):
    mo.md(f"""
    **Материалы занятия:** [κεφΙΙ(2).pdf]({NB_REMOTE}/κεφΙΙ(2).pdf) · [κεφΙΙ(2,5)\\_ἀσκήματα\\_τέλος.pdf]({NB_REMOTE}/κεφΙΙ(2,5)_ἀσκήματα_τέλος.pdf) · [Athenaze\\_2\\_vocabula.pdf]({NB_REMOTE}/Athenaze_2_vocabula.pdf) · [CONSPECTVS GRAMMATICVS II.pdf]({NB_REMOTE}/CONSPECTVS GRAMMATICVS II_graecus.pdf)
    """)
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, mo):
    mo.md(fr"""
    ## Проверка домашнего задания · Κεφ. II(2,5) — ἀσκήματα

    Ответы к упражнениям из «κεφΙΙ(2,5)_ἀσκήματα.pdf» (задано на прошлом занятии):

    [κεφΙΙ(2,5)\_ἀσκήματα\_τέλος.pdf]({NB_REMOTE}/κεφΙΙ(2,5)_ἀσκήματα_τέλος.pdf)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## ἡ θέα · ἡ θεά · ὁ/ἡ θεός

    ἡ θέα, -ας («зрелище, вид») < τὸ θέατρον («театр») < θεάομαι («смотрю, созерцаю»)

    ἡ θεά, -ᾶς — богиня
    **ὁ / ἡ θεός, -οῦ** — «божество», общего рода: ὁ θεός (бог) *или* ἡ θεός (богиня)
    в зависимости от контекста — артикль показывает пол, окончание не меняется.

    **φίλος 3 ↔ ἐχθρός 3** (+ δοτ.) — «друг/дружественный» ↔ «враг/враждебный»:
    > *ἵλεως θεὸς φίλος ἐστὶν τοῖς ἀνθρώποις καὶ ἀεὶ αὐτοῖς συλλαμβάνει.*
    > «Милостивый бог — друг людям и всегда им помогает.»
    > *ὁ δεσπότης χαλεπός ἐστιν πρὸς τὸν δοῦλον· ἐχθρὸς γάρ ἐστιν τοῖς ἀργοῖς.*
    > «Хозяин суров с рабом; ведь он враг ленивым.»

    > *ὦ διδάσκαλε, ἵλεώς μοι ἴσθι!* — «Учитель, будь милостив ко мне!»
    (ἵλεως ἴσθι + dat. — «будь милостив к…»)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## κατάρατος · μάλα → μάλιστα

    **κατάρατος** = μάλιστα κακός — «проклятый» = «наихудший, самый плохой»

    **μάλα** («очень») → **μάλιστα** («более/наиболее всего»), удвоение: μάλα-μάλα
    (усилительная степень наречия — без отдельного сравнительного слова)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Предикативное vs атрибутивное положение прилагательного

    **Предикативное** (без артикля перед прилагательным — прилагательное само
    выступает сказуемым, часто с опущенной связкой):
    > *ὁ ἄνθρωπος ἰσχυρός (ἐστιν).* — «Человек силён.»

    **Атрибутивное** (прилагательное с артиклем, определяет существительное):
    > *ὁ ἰσχυρὸς ἄνθρωπος* = *ὁ ἄνθρωπος ὁ ἰσχυρός* — «сильный человек»

    То же правило работает и с предложными группами вместо прилагательного:
    > *τὸ ἐν τῷ ἀγρῷ δένδρον* — «дерево, которое в поле» (атрибутивно)
    > *τὸ δένδρον ἐν τῷ ἀγρῷ (ἐστιν).* — «Дерево — в поле.» (предикативно)
    > *ἡσυχάζει ὑπὸ τῷ δένδρῳ τῷ ἐν τῷ ἀγρῷ.* — «Он отдыхает под деревом, которое в поле.»
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Субстантивированный инфинитив

    Инфинитив с артиклем **τό** работает как отглагольное существительное:

    > *ὁ πόνος* = *τὸ πονεῖν* — «труд» = «трудиться» (синонимы)
    > *ὁ ἀνὴρ σοφὸς δυνατός ἐστι καλῶς φιλοσοφεῖν.* — «Мудрый муж способен хорошо философствовать.»
    > *μισῶ τὸ ἕωθεν ἀόκνως ἐν τῷ ἀγρῷ σὺν τῷ δούλῳ πονεῖν.*
    > «Я ненавижу с рассвета усердно трудиться в поле вместе с рабом.»
    (τὸ … πονεῖν — вся инфинитивная группа целиком является дополнением μισῶ)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## ἡ μεσημβρία · μετά + время

    **ἡ μεσημβρία, -ας** — полдень: время, когда солнце в середине неба и палит
    сильнее всего (ὅτε ὁ ἥλιος ἐν μέσῳ τῷ οὐρανῷ ἐστιν καὶ μάλιστα φλέγει)

    **μετά + αἰτ.**, когда речь о времени, значит «после» (ср. ἔπειτα):
    > *μετὰ τὴν μεσημβρίαν* — «после полудня»: πρῶτόν ἐστιν ἡ μεσημβρία καὶ ἔπειτα
    > γίγνεταί τι… — «сперва наступает полдень, а затем происходит что-то…»

    Athenaze, стр. 23: «ΜΕΤΑ ΜΕΣΗΜΒΡΙΑΝ» — заголовок сегодняшнего чтения.

    **Напоминание** (из прошлого занятия): ἀροτρεύω ⇒ ἀρότρῳ σκάπτω τὸν ἀγρόν ·
    κεντέω ⇒ κέντρῳ ἐλαύνω τοὺς βοῦς (дательный орудия)
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
        'κεφΙΙ(2).pdf',
        'κεφΙΙ(2,5)_ἀσκήματα_τέλος.pdf',
        'Athenaze_2_vocabula.pdf',
        'CONSPECTVS GRAMMATICVS II_graecus.pdf',
    ):
        gu.ensure_file(_pdf, nb_dir=NB_DIR, remote_base=NB_REMOTE)
    for _f in ('cap2_nouns.tsv', 'cap2_adjectives.tsv', 'nouns.tsv', 'adjectives.tsv'):
        gu.ensure_file(_f, nb_dir=NB_DIR, remote_base=NB_REMOTE)
    return (load_tsv,)


@app.cell(hide_code=True)
def _(load_tsv, mo):
    _nouns = load_tsv("nouns.tsv")
    _adj = load_tsv("adjectives.tsv")
    mo.vstack([
        mo.md("## Νέαι λέξεις · Новые слова"),
        mo.md("**Nomina substantiva (существительные):**"),
        mo.ui.table(_nouns, selection=None),
        mo.md("**Nomina adiectiva (прилагательные):**"),
        mo.ui.table(_adj, selection=None),
    ])
    return


@app.cell(hide_code=True)
def _(NB_DIR, NB_REMOTE, gu):
    VOCAB_WORDS = gu.load_vocab_tsv(
        'nouns.tsv', 'adjectives.tsv',
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
        for w in gu.load_vocab_tsv('cap2_nouns.tsv', nb_dir=NB_DIR, remote_base=NB_REMOTE)
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
    return (
        cap_n3,
        entercnt_n3,
        entered_n3,
        hist_n3,
        msg_n3,
        nxt_cnt_n3,
        prev_cnt_n3,
        restart_cnt_n3,
        set_cap_n3,
        set_entercnt_n3,
        set_entered_n3,
        set_hist_n3,
        set_msg_n3,
        set_nxt_cnt_n3,
        set_prev_cnt_n3,
        set_restart_cnt_n3,
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
    set_cap_n3,
    set_entercnt_n3,
    set_entered_n3,
    set_hist_n3,
    set_msg_n3,
    set_nxt_cnt_n3,
    set_prev_cnt_n3,
    set_restart_cnt_n3,
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
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Склонение прилагательных
    """)
    return


@app.cell(hide_code=True)
def _(NB_DIR, NB_REMOTE, gu):
    WORDS_ADJ_ADJ6 = [
        {"Word": w["form"], "Translation": w["meaning"]}
        for w in gu.load_vocab_tsv('cap2_adjectives.tsv', nb_dir=NB_DIR, remote_base=NB_REMOTE)
    ]
    return (WORDS_ADJ_ADJ6,)


@app.cell(hide_code=True)
def _(WORDS_ADJ_ADJ6, mo):
    w4t_adj6, set_w4t_adj6 = mo.state(list(WORDS_ADJ_ADJ6))
    hist_adj6, set_hist_adj6 = mo.state([])
    msg_adj6, set_msg_adj6 = mo.state("")
    cap_adj6, set_cap_adj6 = mo.state(None)
    entered_adj6, set_entered_adj6 = mo.state({})
    sub_cnt_adj6, set_sub_cnt_adj6 = mo.state(0)
    prev_cnt_adj6, set_prev_cnt_adj6 = mo.state(0)
    nxt_cnt_adj6, set_nxt_cnt_adj6 = mo.state(0)
    restart_cnt_adj6, set_restart_cnt_adj6 = mo.state(0)
    entercnt_adj6, set_entercnt_adj6 = mo.state(0)
    return (
        cap_adj6,
        entercnt_adj6,
        entered_adj6,
        hist_adj6,
        msg_adj6,
        nxt_cnt_adj6,
        prev_cnt_adj6,
        restart_cnt_adj6,
        set_cap_adj6,
        set_entercnt_adj6,
        set_entered_adj6,
        set_hist_adj6,
        set_msg_adj6,
        set_nxt_cnt_adj6,
        set_prev_cnt_adj6,
        set_restart_cnt_adj6,
        set_sub_cnt_adj6,
        set_w4t_adj6,
        sub_cnt_adj6,
        w4t_adj6,
    )


@app.cell(hide_code=True)
def _(
    entered_adj6,
    gu,
    hist_adj6,
    set_entercnt_adj6,
    set_nxt_cnt_adj6,
    set_prev_cnt_adj6,
    w4t_adj6,
):
    cv_adj6 = w4t_adj6()[0] if w4t_adj6() else None
    _adj_labels_adj6 = gu.adjective_slot_labels("simple", lang="ru")
    _entered_form_adj6 = entered_adj6().get(cv_adj6["Word"]) if cv_adj6 else None
    adj_form_adj6, prev_btn_adj6, nxt_btn_adj6, restart_btn_adj6 = gu.paradigm_drill_widgets(
        labels=_adj_labels_adj6,
        values=_entered_form_adj6,
        history_len=len(hist_adj6()),
        remaining_len=len(w4t_adj6()),
        next_label="Следующее",
        prev_label="Предыдущее",
    )
    set_prev_cnt_adj6(0)
    set_nxt_cnt_adj6(0)
    set_entercnt_adj6(0)
    return (
        adj_form_adj6,
        cv_adj6,
        nxt_btn_adj6,
        prev_btn_adj6,
        restart_btn_adj6,
    )


@app.cell(hide_code=True)
def _(
    WORDS_ADJ_ADJ6,
    adj_form_adj6,
    cap_adj6,
    check_btn_adj6,
    cv_adj6,
    entercnt_adj6,
    entered_adj6,
    gu,
    hist_adj6,
    msg_adj6,
    nxt_btn_adj6,
    nxt_cnt_adj6,
    prev_btn_adj6,
    prev_cnt_adj6,
    restart_btn_adj6,
    restart_cnt_adj6,
    set_cap_adj6,
    set_entercnt_adj6,
    set_entered_adj6,
    set_hist_adj6,
    set_msg_adj6,
    set_nxt_cnt_adj6,
    set_prev_cnt_adj6,
    set_restart_cnt_adj6,
    set_sub_cnt_adj6,
    set_w4t_adj6,
    sub_cnt_adj6,
    w4t_adj6,
):
    gu.adjective_paradigm_drill_form(
        w4t_adj6, set_w4t_adj6, hist_adj6, set_hist_adj6, msg_adj6, set_msg_adj6,
        cap_adj6, set_cap_adj6, entered_adj6, set_entered_adj6,
        sub_cnt_adj6, set_sub_cnt_adj6, prev_cnt_adj6, set_prev_cnt_adj6,
        nxt_cnt_adj6, set_nxt_cnt_adj6, entercnt_adj6, set_entercnt_adj6,
        restart_cnt_adj6, set_restart_cnt_adj6,
        cv_adj6, adj_form_adj6, check_btn_adj6, prev_btn_adj6, nxt_btn_adj6, restart_btn_adj6,
        vocab=WORDS_ADJ_ADJ6,
        mode="simple",
        word_key="Word",
        meaning_key="Translation",
        meaning_label="Перевод",
        title="## Упражнение 4 · Склонение прилагательных",
        done_message="✅ Все прилагательные пройдены!",
    )
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, mo):
    mo.md(f"""
    ## τὸ προστεταγμένον · Домашнее задание

    1. **αὖθις ἀναγιγνώσκετε** — ещё раз перечитайте начало второй главы (Κεφ. II).

    2. **Μελετήματα** (Carmelo Consoli), упражнения ко второму уроку:
       - **2.1 + 2.2** — заполните (γεμίζετε)
       - **2.3 + 2.4** — впишите правильные окончания (склонение и спряжение)

    3. **ἀσκήματα ποιεῖτε** из файла [Κεφ.II(2)\\_μετάφρασις.pdf]({NB_REMOTE}/Κεφ.II(2)_μετάφρασις.pdf)
    """)
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, mo):
    mo.md(f"""
    ## Весь словарь Athenaze II · [Athenaze\\_2\\_vocabula.pdf]({NB_REMOTE}/Athenaze_2_vocabula.pdf)
    """)
    return


@app.cell(hide_code=True)
def _(NB_DIR, NB_REMOTE, gu):
    VOCAB_ALL = gu.load_vocab_tsv(
        'nouns.tsv', 'adjectives.tsv',
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
        title='## Упражнение 5 · Выбрать слово',
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
        title='## Упражнение 6 · Написать греческое слово',
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
def _(cfg, mo):
    import eee_project as eee
    from ancient_greek_backend_eee import AncientGreekBackend
    from eee_project import GreekUtils, ANCIENT_GREEK, setup_ancient_greek
    from eee_project.notebook_utils import eee_footer
    from pathlib import Path as _Path
    NB_DIR = _Path(__file__).parent
    NB_REMOTE = cfg.nb_remote("2026_07_10")
    _yamls = [NB_DIR.parent / f"athenaze_{_c}_nouns.yaml" for _c in ("cap1", "cap2")]
    _yamls.append(NB_DIR.parent / "athenaze_cap2_adjs.yaml")
    for _y in _yamls:
        GreekUtils.ensure_file(_y.name, nb_dir=_y.parent, remote_base=cfg.raw_base)
    ag = AncientGreekBackend(lexicons=["pratt", "ltrg", *[str(_y.resolve()) for _y in _yamls]])
    setup_ancient_greek(ag)
    gu = GreekUtils(ag, mo, eee_module=eee, config=ANCIENT_GREEK)
    eee_footer(mo, lang='ru')
    return NB_DIR, NB_REMOTE, gu


@app.cell(hide_code=True)
def _(cap_n3, cv_n3, gu, noun_form_n3, set_sub_cnt_n3):
    check_btn_n3 = gu.dirty_check_button(
        noun_form_n3, cap_n3, cv_n3, "test_word", word_key="Word", label="Проверить"
    )
    set_sub_cnt_n3(0)
    return (check_btn_n3,)


@app.cell(hide_code=True)
def _(adj_form_adj6, cap_adj6, cv_adj6, gu, set_sub_cnt_adj6):
    check_btn_adj6 = gu.dirty_check_button(
        adj_form_adj6, cap_adj6, cv_adj6, "adj_word", word_key="Word", label="Проверить"
    )
    set_sub_cnt_adj6(0)
    return (check_btn_adj6,)


if __name__ == "__main__":
    app.run()
