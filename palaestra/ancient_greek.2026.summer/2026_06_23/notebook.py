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

__generated_with = "0.23.11"
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
    # Δίδαγμα ε'
    **Palaestra — Древнегреческий язык, начальный уровень — Лето 2026**
    """)
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, mo):
    _cap1_remote = NB_REMOTE.replace("/2026_06_23", "/2026_06_16")
    mo.md(f"**Материалы занятия:** [заметки\\_23.06.pdf]({NB_REMOTE}/заметки_23.06.pdf) · [I(1,5).pdf]({NB_REMOTE}/I(1,5).pdf) · [κεφ.I, (3)\\_ἀσκήματα.pdf]({NB_REMOTE}/κεφ.I, (3)_ἀσκήματα.pdf) · [Athenaze\\_1\\_vocabula.pdf]({_cap1_remote}/Athenaze_1_vocabula.pdf)")
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, mo):
    mo.md(fr"""
    ## Проверка домашнего задания · τὸ τρίτον προστεταγμένον

    ### Μελετήματα · упражнения 1.4, 1.5, 1.6, 1.8

    [κεφ.I, (3)\_ἀσκήματα\_τέλος.pdf]({NB_REMOTE}/κεφ.I, (3)_ἀσκήματα_τέλος.pdf) — файл с ответами.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## ὀνόματα γραμματικά · Грамматические термины

    | ὄνομα | значение | пример |
    |:------|:---------|:-------|
    | τὸ **ῥῆμα** | глагол (verbum) | λέγω, ἀκούω, παύω, ἀναγιγνώσκω, κτλ. |
    | τὸ **οὐσιαστικόν** [ὄνομα] | существительное | ὁ ἄνθρωπος, ἡ κόρη, τὸ πρόβλημα, κτλ. |
    | τὸ **ἐπίθετον** [ὄνομα] | прилагательное | καλός, ἀγαθός, κακός, μικρός, κτλ. |
    | τὸ **ἐπίρρημα** | наречие (ad-verbium) | καλῶς, ἀγαθῶς, ὀρθῶς, κτλ. |

    *Полезные сокращения:* **κτλ.** = καὶ τὰ λοιπά = etc. · **π.χ.** = παραδείγματος χάριν = н-р · **διό** = ergo
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## ἡ συζυγία · Спряжение в настоящем времени

    ### εἶναι

    | | ὁ ἑνικὸς ἀριθμός | ὁ πληθυντικὸς ἀριθμός |
    |:--|:--:|:--:|
    | Πρῶτον πρόσωπον | ἐγώ **εἰμι** | ἡμεῖς **ἐσμεν** |
    | Δεύτερον πρόσωπον | σὺ **εἶ** | ὑμεῖς **ἐστε** |
    | Τρίτον πρόσωπον | ὁ γεωργός **ἐστι(ν)** | οἱ γεωργοί **εἰσι(ν)** |

    > *Τίς εἰμι ἐγώ;* — σὺ **διδάσκαλος** εἶ.
    > *Τίνες ὑμεῖς ἐστε;* — ἡμεῖς **μαθηταί** ἐσμεν.

    ### λέγ-ειν · ἀκού-ειν (thematic verbs)

    | | ἑνικός | πληθυντικός |
    |:--|:--:|:--:|
    | 1 | λέγ**-ω** / ἀκού**-ω** | λέγ**-ομεν** / ἀκού**-ομεν** |
    | 2 | λέγ**-εις** / ἀκού**-εις** | λέγ**-ετε** / ἀκού**-ετε** |
    | 3 | λέγ**-ει** / ἀκού**-ει** | λέγ**-ουσι(ν)** / ἀκού**-ουσι(ν)** |

    ### φιλ-εῖν (ε-contract)

    | | ἑνικός | πληθυντικός |
    |:--|:--:|:--:|
    | 1 | ἐγὼ φιλ**ῶ** (φιλέ**-ω**) | ἡμεῖς φιλ**οῦμεν** (φιλέ**-ομεν**) |
    | 2 | σὺ φιλ**εῖς** (φιλέ**-εις**) | ὑμεῖς φιλ**εῖτε** (φιλέ**-ετε**) |
    | 3 | φιλ**εῖ** (φιλέ**-ει**) | φιλ**οῦσι(ν)** (φιλέ**-ουσι**) |

    > *Ἆρα φιλεῖς τὴν ἑλληνικὴν γλῶτταν;* — **φιλέω** ↔ **μισέω**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## ἡ αἰτιατικὴ πτῶσις · Винительный падеж

    Прямое дополнение глагола (отвечает на вопрос *τίνα; / τί;*):

    | ὀνομαστική | αἰτιατική |
    |:----------:|:---------:|
    | ὁ οἶκος | ἔχω τ**ὸν** οἶκ**ον** |
    | ὁ ἀγρός | ἔχω τ**ὸν** ἀγρ**όν** |
    | ὁ κλῆρος | γεωργεῖ τ**ὸν** κλῆρ**ον** |

    > *Τί σκάπτει ὁ Δικαιόπολις;* — ὁ Δ. σκάπτει **τὸν ἀγρόν**.
    > *Τίνα φιλεῖ ὁ Ἀνδρέας;* — ὁ Ἀνδρέας φιλεῖ **τὸν γεωργόν**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ποῦ; / Πόθεν; / Ποῖ; · Вопросы о месте

    | вопрос | падеж | предлог | пример |
    |:-------|:-----:|:-------:|:-------|
    | **Ποῦ;** — где? | δοτική | ἐν | ἐν τῷ ἀγρ**ῷ** |
    | **Πόθεν;** — откуда? | γενική | ἐκ | ἐκ τοῦ ἀγρ**οῦ** |
    | **Ποῖ;** — куда? | αἰτιατική | πρός | πρὸς τὸν ἀγρ**όν** |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Заметки

    - **ν подвижное ([ν ἐφελκυστικόν](https://en.wiktionary.org/wiki/ephelcystic_nu)):** ἐστι(ν) может принимать конечное **ν** перед гласным и в конце предложения.
    - **[εἰμί](https://mysite.du.edu/~etuttle/classics/nugreek/lesson6.htm):** большинство форм настоящего времени — энклитические (кроме εἶ).
    - **[Стяжение](https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D1%8F%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5) (συναίρεσις):** слияние двух соседних гласных в один долгий гласный или дифтонг ([φιλέω](https://www.greek-language.gr/digitalResources/ancient_greek/tools/liddel-scott/search.html?lq=%CF%86%CE%B9%CE%BB%CE%B5%CF%89) → φιλῶ, ε + ω → ω). [См. про класс стяжённых глаголов, где сама основа заканчивается на гласную, и происходит стяжение гласного с начальным (тематическим) гласным окончаний.](http://www.languagreek.ru/glagoly.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ἄσκησις α' · Γεμίζετε

    **Слова для вставки:** ὁ ἀγρός (2×) · μέγας · πολύς · τὸ δένδρον (2×) · τὸ ἕρμα

    > Ὁ Δικαιόπολις ἐν τῷ **ἀγρῷ** πονεῖ· αἴρει γάρ **μέγαν** λίθον καὶ ἐκ **τοῦ ἀγροῦ** ἐκφέρει
    > πρὸς **τὸ ἕρμα**. κάμνει οὖν καὶ πρὸς **τὸ δένδρον** βαδίζει καὶ ὑπὸ **τῷ δένδρῳ** καθίζει
    > καὶ ἡσυχάζει, ἀλλὰ δι᾿ ὀλίγου ἐπαίρει ἑαυτὸν καὶ **τὸν ἀγρόν** σκάπτει.
    > Ὁ οὖν μικρὸς κλῆρος οὐ **πολὺν** σῖτον παρέχει, ἀλλὰ ἱκανόν.

    ## Ἄσκησις β' · Γεμίζετε

    **Слова для вставки:** καθίζει · ἡσυχάζει · δι᾿ ὀλίγου · κάμνει · δένδρον · κατατρίβει

    > Ὁ μὲν Δικαιόπολις ἰσχυρός ἐστι, πονεῖ δὲ πολὺν χρόνον καὶ ὁ ἥλιος αὐτὸν **κατατρίβει**.
    > ὁ οὖν αὐτουργὸς μάλα **κάμνει**. βαδίζει οὖν καὶ **καθίζει** ὑπὸ **δένδρῳ**,
    > ἀλλὰ **δι᾿ ὀλίγου** ἐπαίρει ἑαυτὸν καὶ βαδίζει πρὸς τὸν ἀγρόν. τέλος δὲ ἐν τῷ οἴκῳ **ἡσυχάζει**.
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

    _cap1_remote = NB_REMOTE.replace("/2026_06_23", "/2026_06_16")
    gu.ensure_file('Athenaze_1_vocabula.pdf', nb_dir=NB_DIR, remote_base=_cap1_remote)
    for _pdf in (
        'заметки_23.06.pdf',
        'I(1,5).pdf',
        'κεφ.I, (3)_ἀσκήματα.pdf',
    ):
        gu.ensure_file(_pdf, nb_dir=NB_DIR, remote_base=NB_REMOTE)
    for _f in ('cap1_verbs.tsv', 'cap1_nouns.tsv', 'cap1_adjectives.tsv', 'cap1_particles.tsv'):
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
        mo.md("**Nomina adjectiva (прилагательные):**"),
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
        vocab=VOCAB_WORDS,
        restore_entry=restore_entry_c(),
        done=cv_c() is None and remaining_c() is not None and len(remaining_c()) == 0,
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
        restore_entry=restore_entry_w(),
        done=cv_w() is None and remaining_w() is not None and len(remaining_w()) == 0,
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
    ## Спряжение глаголов · Present Active Indicative
    """)
    return


@app.cell(hide_code=True)
def _():
    from eee_project import make_paradigm_form

    return (make_paradigm_form,)


@app.cell(hide_code=True)
def _(NB_DIR, NB_REMOTE, gu):
    _PAI = {"VerbForm": "Fin", "Tense": "Pres", "Voice": "Act", "Mood": "Ind"}
    _raw_v3 = gu.load_slot_drill(
        gu.ensure_file("cap1_verbs.tsv", nb_dir=NB_DIR, remote_base=NB_REMOTE),
        {
            "verb": None,
            "1sg": {**_PAI, "Person": "1", "Number": "Sing"},
            "2sg": {**_PAI, "Person": "2", "Number": "Sing"},
            "3sg": {**_PAI, "Person": "3", "Number": "Sing"},
            "1pl": {**_PAI, "Person": "1", "Number": "Plur"},
            "2pl": {**_PAI, "Person": "2", "Number": "Plur"},
            "3pl": {**_PAI, "Person": "3", "Number": "Plur"},
        },
        pos="verb",
    )
    WORDS_VERB_V3 = [
        {"Word": v["verb"], "Translation": v["meaning"]}
        for v in _raw_v3
        if all(v.get(k) for k in ["1sg", "2sg", "3sg", "1pl", "2pl", "3pl"])
    ]
    return (WORDS_VERB_V3,)


@app.cell(hide_code=True)
def _(WORDS_VERB_V3, mo):
    w4t_v3, set_w4t_v3 = mo.state(list(WORDS_VERB_V3))
    hist_v3, set_hist_v3 = mo.state([])
    msg_v3, set_msg_v3 = mo.state("")
    cap_v3, set_cap_v3 = mo.state(None)
    sub_cnt_v3, set_sub_cnt_v3 = mo.state(0)
    prev_cnt_v3, set_prev_cnt_v3 = mo.state(0)
    nxt_cnt_v3, set_nxt_cnt_v3 = mo.state(0)
    prev_btn_v3 = mo.ui.button(label="Предыдущее", on_click=lambda v: (v or 0) + 1)
    nxt_btn_v3 = mo.ui.button(label="Следующее", on_click=lambda v: (v or 0) + 1)
    return (
        cap_v3,
        hist_v3,
        msg_v3,
        nxt_btn_v3,
        nxt_cnt_v3,
        prev_btn_v3,
        prev_cnt_v3,
        set_cap_v3,
        set_hist_v3,
        set_msg_v3,
        set_nxt_cnt_v3,
        set_prev_cnt_v3,
        set_sub_cnt_v3,
        set_w4t_v3,
        sub_cnt_v3,
        w4t_v3,
    )


@app.cell(hide_code=True)
def _(make_paradigm_form, mo, set_sub_cnt_v3, w4t_v3):
    cv_v3 = w4t_v3()[0] if w4t_v3() else None
    verb_form_v3 = make_paradigm_form(mo, ["1 sg:", "2 sg:", "3 sg:", "1 pl:", "2 pl:", "3 pl:"])
    check_btn_v3 = mo.ui.button(label="Проверить", on_click=lambda v: (v or 0) + 1)
    set_sub_cnt_v3(0)
    return check_btn_v3, cv_v3, verb_form_v3


@app.cell(hide_code=True)
def _(
    WORDS_VERB_V3,
    check_btn_v3,
    cv_v3,
    mo,
    msg_v3,
    nxt_btn_v3,
    prev_btn_v3,
    verb_fb_v3,
    verb_form_v3,
    w4t_v3,
):
    if not w4t_v3():
        _out_v3 = mo.md("**✅ Все глаголы пройдены!**")
    else:
        _fback_v3 = mo.md(verb_fb_v3) if verb_fb_v3 else mo.md("")
        _done = len(WORDS_VERB_V3) - len(w4t_v3())
        _total = len(WORDS_VERB_V3)
        _items = [mo.md(f"## Упражнение 3 · Спряжение в настоящем времени ({_done + 1}/{_total})")]
        if msg_v3():
            _items.append(mo.md(msg_v3()))
        _items += [
            mo.md(f"Перевод: **{cv_v3['Translation']}**") if cv_v3 else mo.md(""),
            verb_form_v3,
            mo.hstack([check_btn_v3, prev_btn_v3, nxt_btn_v3], justify="end"),
            _fback_v3,
        ]
        _out_v3 = mo.vstack(_items)
    _out_v3
    return


@app.cell(hide_code=True)
def _(
    check_btn_v3,
    cv_v3,
    set_cap_v3,
    set_sub_cnt_v3,
    sub_cnt_v3,
    verb_form_v3,
):
    import types as _tv3
    if (check_btn_v3.value or 0) > sub_cnt_v3():
        set_sub_cnt_v3(check_btn_v3.value)
        if cv_v3:
            _snap_v3 = _tv3.SimpleNamespace(
                verb_word=cv_v3["Word"],
                tense="present",
                value=list(verb_form_v3.widget.values),
            )
            set_cap_v3(_snap_v3)
    return


@app.cell(hide_code=True)
def _(
    cv_v3,
    hist_v3,
    set_cap_v3,
    set_hist_v3,
    set_msg_v3,
    set_w4t_v3,
    verb_ok_v3,
    w4t_v3,
):
    if verb_ok_v3:
        set_hist_v3(hist_v3() + [cv_v3])
        set_w4t_v3([w for w in w4t_v3() if w["Word"] != cv_v3["Word"]])
        set_msg_v3(f"✅ {cv_v3['Word']} — {cv_v3['Translation']}")
        set_cap_v3(None)
    return


@app.cell(hide_code=True)
def _(
    cv_v3,
    hist_v3,
    nxt_btn_v3,
    nxt_cnt_v3,
    prev_btn_v3,
    prev_cnt_v3,
    set_cap_v3,
    set_hist_v3,
    set_nxt_cnt_v3,
    set_prev_cnt_v3,
    set_sub_cnt_v3,
    set_w4t_v3,
    w4t_v3,
):
    if (nxt_btn_v3.value or 0) > nxt_cnt_v3():
        set_nxt_cnt_v3(nxt_btn_v3.value)
        set_cap_v3(None)
        set_sub_cnt_v3(0)
        if w4t_v3() and cv_v3:
            set_hist_v3(hist_v3() + [cv_v3])
            set_w4t_v3([w for w in w4t_v3() if w["Word"] != cv_v3["Word"]])

    if (prev_btn_v3.value or 0) > prev_cnt_v3():
        set_prev_cnt_v3(prev_btn_v3.value)
        set_cap_v3(None)
        set_sub_cnt_v3(0)
        if hist_v3():
            _prev_v3 = hist_v3()[-1]
            set_hist_v3(hist_v3()[:-1])
            set_w4t_v3([_prev_v3] + [w for w in w4t_v3() if w["Word"] != _prev_v3["Word"]])
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, mo):
    mo.md(fr"""
    ## τὸ τέταρτον προστεταγμένον · Домашнее задание

    1. **ἀναγιγνώσκετε ὅλον τὸ πρῶτον κεφάλαιον** — перечитайте всю первую главу.

    2. **Μελετήματα** (Carmelo Consoli), упражнения к первому уроку:
       - **1.4 + 1.5** — напишите правильные формы существительных и глаголов
       - **1.6** — заполните пропуски
       - **1.8** — напишите правильные формы существительных

    3. **ἀσκήματα ποιεῖτε** — [κεφ.I, (3)\_ἀσκήματα.pdf]({NB_REMOTE}/κεφ.I, (3)_ἀσκήματα.pdf)
    """)
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, mo):
    _cap1_remote = NB_REMOTE.replace("/2026_06_23", "/2026_06_16")
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
        vocab=VOCAB_ALL,
        restore_entry=restore_entry_a(),
        done=cv_a() is None and remaining_a() is not None and len(remaining_a()) == 0,
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
        restore_entry=restore_entry_aw(),
        done=cv_aw() is None and remaining_aw() is not None and len(remaining_aw()) == 0,
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
    _REQUIRED = {"form", "meaning", "lemma", "context"}
    assert VOCAB_WORDS, "load_vocab_tsv returned empty list"
    assert all(_REQUIRED <= set(w) for w in VOCAB_WORDS), f"word missing keys: {VOCAB_WORDS}"
    assert all(w["form"] and w["meaning"] for w in VOCAB_WORDS), "word has empty form or meaning"
    del _REQUIRED
    return


@app.cell(hide_code=True)
def _(VOCAB_ALL):
    _REQUIRED = {"form", "meaning", "lemma", "context"}
    assert VOCAB_ALL, "load_vocab_tsv returned empty list (cap1)"
    assert all(_REQUIRED <= set(w) for w in VOCAB_ALL), f"cap1 word missing keys: {VOCAB_ALL}"
    assert all(w["form"] and w["meaning"] for w in VOCAB_ALL), "cap1 word has empty form or meaning"
    del _REQUIRED
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import random

    return (mo,)


@app.cell(hide_code=True)
def _(cfg, mo):
    import eee_project as eee
    from ancient_greek_backend_eee import AncientGreekBackend
    from eee_project import GreekUtils, ANCIENT_GREEK
    from eee_project.notebook_utils import eee_footer
    from pathlib import Path as _Path
    NB_DIR = _Path(__file__).parent
    NB_REMOTE = f"{cfg.raw_base}/2026_06_23"
    _verb_yaml = NB_DIR.parent / "athenaze_cap1_verbs.yaml"
    if not _verb_yaml.exists():
        import urllib.request as _ur
        _ur.urlretrieve(f"{cfg.raw_base}/athenaze_cap1_verbs.yaml", str(_verb_yaml))
    ag = AncientGreekBackend(lexicons=["pratt", "ltrg", str(_verb_yaml)])
    eee.register_backend("grc", ag)
    eee.register_backend("grc", ag, backend="ancient-greek")
    eee.set_chain("grc", ["ancient-greek"])
    gu = GreekUtils(ag, mo, eee_module=eee, config=ANCIENT_GREEK)
    eee_footer(mo, lang='ru')
    return NB_DIR, NB_REMOTE, gu


@app.cell(hide_code=True)
def _(cap_v3, cv_v3, gu):
    _c = cap_v3()
    verb_ok_v3 = False
    verb_fb_v3 = ""
    if cv_v3 and _c and getattr(_c, "verb_word", None) == cv_v3["Word"]:
        verb_ok_v3, verb_fb_v3 = gu.check_verb_test(cv_v3["Word"], _c, "present")
    return verb_fb_v3, verb_ok_v3


if __name__ == "__main__":
    app.run()
