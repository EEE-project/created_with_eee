# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.23.14",
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
               ga_config=cfg.ga_config())
    return (cfg,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Δίδαγμα ζ' · Κεφάλαιον II
    **Palaestra — Древнегреческий язык, начальный уровень — Лето 2026**

    [![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_HYFBzXtFTD58CYSxNQFJ1G)
    """)
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, mo):
    mo.md(f"""
    **Материалы занятия:** [κεφΙΙ(0,5).pdf]({NB_REMOTE}/κεφΙΙ(0,5).pdf) · [Κεφ.II(1)\\_μετάφρασις.pdf]({NB_REMOTE}/Κεφ.II(1)_μετάφρασις.pdf) · [Athenaze\\_2\\_vocabula.pdf]({NB_REMOTE}/Athenaze_2_vocabula.pdf) · [CONSPECTVS GRAMMATICVS II.pdf]({NB_REMOTE}/CONSPECTVS GRAMMATICVS II_graecus.pdf)
    """)
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, mo):
    mo.md(fr"""
    ## Проверка домашнего задания · Κεφ. I — τέλος

    Завершение упражнений по I главе (Μελετήματα) — ответы в файле:

    [κεφ(Ι)\_ἀσκήματα(τέλος).pdf]({NB_REMOTE}/κεφ(Ι)_ἀσκήματα(τέλος).pdf)
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
    | Πρῶτον πρόσωπον | ἐγώ **εἰμί** | ἡμεῖς **ἐσμέν** |
    | Δεύτερον πρόσωπον | σὺ **εἶ** | ὑμεῖς **ἐστέ** |
    | Τρίτον πρόσωπον | ὁ γεωργός **ἐστί(ν)** | οἱ γεωργοί **εἰσί(ν)** |

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
    ## ἡ προστακτική · Повелительное наклонение (императив)

    <!-- ⚠ draft из конспекта κεφΙΙ(0,5) — проверить -->
    Приказ или просьба. Настоящее время, 2-е лицо:

    | | ἑνικός (ты) | πληθυντικός (вы) |
    |:--|:--:|:--:|
    | тематические | λέγ**-ε** · ἄκου**-ε** | λέγ**-ετε** · ἀκού**-ετε** |
    | ε-слитные | φίλ**-ει** (φίλε-ε) | φιλ**-εῖτε** |

    > *Запрет* — с частицей **μή**: **μὴ** λέγε! · **μὴ** οὕτω ἀργὸς ἴσθι!

    Особые формы: **ἐλθέ / ἔλθετε** (приди! — от ἔρχομαι), **ἴσθι / ἔστε** (будь! — от εἰμί).

    ## πάρ-ειμι · присутствовать (εἰμί + приставка)

    | | ἑνικός | πληθυντικός |
    |:--|:--:|:--:|
    | 1 | ἐγὼ **πάρειμι** | ἡμεῖς **πάρεσμεν** |
    | 2 | σὺ **πάρει** | ὑμεῖς **πάρεστε** |
    | 3 | αὐτὸς **πάρεστι(ν)** | αὐτοὶ **πάρεισι(ν)** |

    ## εἰ / εἰ μή · Условие (ἡ πρότασις)

    > **εἰ μὴ** πάρεστιν ὁ δεσπότης, ὁ δοῦλος οὐ πονεῖ. — *Если хозяина нет, раб не работает.*

    В придаточном отрицание — **μή** (= οὐ).
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
        'κεφΙΙ(0,5).pdf',
        'Κεφ.II(1)_μετάφρασις.pdf',
        'κεφ(Ι)_ἀσκήματα(τέλος).pdf',
        'Athenaze_2_vocabula.pdf',
        'CONSPECTVS GRAMMATICVS II_graecus.pdf',
    ):
        gu.ensure_file(_pdf, nb_dir=NB_DIR, remote_base=NB_REMOTE)
    for _f in ('cap2_verbs.tsv', 'nouns.tsv', 'adjectives.tsv'):
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
    ## Спряжение глаголов · Present Active Indicative
    """)
    return


@app.cell(hide_code=True)
def _(NB_DIR, NB_REMOTE, gu):
    _PAI = {"VerbForm": "Fin", "Tense": "Pres", "Voice": "Act", "Mood": "Ind"}
    _raw_v3 = gu.load_slot_drill(
        gu.ensure_file("cap2_verbs.tsv", nb_dir=NB_DIR, remote_base=NB_REMOTE),
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
    entered_v3, set_entered_v3 = mo.state({})
    sub_cnt_v3, set_sub_cnt_v3 = mo.state(0)
    prev_cnt_v3, set_prev_cnt_v3 = mo.state(0)
    nxt_cnt_v3, set_nxt_cnt_v3 = mo.state(0)
    restart_cnt_v3, set_restart_cnt_v3 = mo.state(0)
    entercnt_v3, set_entercnt_v3 = mo.state(0)
    return (
        cap_v3,
        entercnt_v3,
        entered_v3,
        hist_v3,
        msg_v3,
        nxt_cnt_v3,
        prev_cnt_v3,
        restart_cnt_v3,
        set_cap_v3,
        set_entercnt_v3,
        set_entered_v3,
        set_hist_v3,
        set_msg_v3,
        set_nxt_cnt_v3,
        set_prev_cnt_v3,
        set_restart_cnt_v3,
        set_sub_cnt_v3,
        set_w4t_v3,
        sub_cnt_v3,
        w4t_v3,
    )


@app.cell(hide_code=True)
def _(
    entered_v3,
    gu,
    hist_v3,
    set_entercnt_v3,
    set_nxt_cnt_v3,
    set_prev_cnt_v3,
    w4t_v3,
):
    cv_v3 = w4t_v3()[0] if w4t_v3() else None
    _entered_form_v3 = entered_v3().get(cv_v3["Word"]) if cv_v3 else None
    verb_form_v3, prev_btn_v3, nxt_btn_v3, restart_btn_v3 = gu.paradigm_drill_widgets(
        labels=["1 sg:", "2 sg:", "3 sg:", "1 pl:", "2 pl:", "3 pl:"],
        values=_entered_form_v3,
        history_len=len(hist_v3()),
        remaining_len=len(w4t_v3()),
        next_label="Следующее",
        prev_label="Предыдущее",
    )
    set_prev_cnt_v3(0)
    set_nxt_cnt_v3(0)
    set_entercnt_v3(0)
    return cv_v3, nxt_btn_v3, prev_btn_v3, restart_btn_v3, verb_form_v3


@app.cell(hide_code=True)
def _(
    WORDS_VERB_V3,
    cap_v3,
    check_btn_v3,
    cv_v3,
    entercnt_v3,
    entered_v3,
    gu,
    hist_v3,
    msg_v3,
    nxt_btn_v3,
    nxt_cnt_v3,
    prev_btn_v3,
    prev_cnt_v3,
    restart_btn_v3,
    restart_cnt_v3,
    set_cap_v3,
    set_entercnt_v3,
    set_entered_v3,
    set_hist_v3,
    set_msg_v3,
    set_nxt_cnt_v3,
    set_prev_cnt_v3,
    set_restart_cnt_v3,
    set_sub_cnt_v3,
    set_w4t_v3,
    sub_cnt_v3,
    verb_form_v3,
    w4t_v3,
):
    gu.verb_paradigm_drill_form(
        w4t_v3, set_w4t_v3, hist_v3, set_hist_v3, msg_v3, set_msg_v3,
        cap_v3, set_cap_v3, entered_v3, set_entered_v3,
        sub_cnt_v3, set_sub_cnt_v3, prev_cnt_v3, set_prev_cnt_v3,
        nxt_cnt_v3, set_nxt_cnt_v3, entercnt_v3, set_entercnt_v3,
        restart_cnt_v3, set_restart_cnt_v3,
        cv_v3, verb_form_v3, check_btn_v3, prev_btn_v3, nxt_btn_v3, restart_btn_v3,
        vocab=WORDS_VERB_V3,
        tense="present",
        word_key="Word",
        meaning_key="Translation",
        meaning_label="Перевод",
        title="## Упражнение 3 · Спряжение в настоящем времени",
        done_message="✅ Все глаголы пройдены!",
    )
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, mo):
    mo.md(fr"""
    ## τὸ προστεταγμένον · Домашнее задание

    1. **αὖθις ἀναγιγνώσκετε** — перечитайте прочитанную на занятии часть второй главы (Κεφ. II).

    2. **Μελετήματα** (Carmelo Consoli), упражнения ко второму уроку:
       - **2.2** — впишите подходящие по смыслу слова в нужной форме (до 8-го предложения включительно)
       - **2.3 + 2.4** — впишите правильные окончания (склонение и спряжение)

    3. **μεταφράζετε ἑλληνιστί** — переведите предложения из файла [Κεφ.II(1)\_μετάφρασις.pdf]({NB_REMOTE}/Κεφ.II(1)_μετάφρασις.pdf)
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
        'cap2_verbs.tsv', 'nouns.tsv', 'adjectives.tsv',
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
def _(cfg, mo):
    import eee_project as eee
    from ancient_greek_backend_eee import AncientGreekBackend
    from eee_project import GreekUtils, ANCIENT_GREEK, setup_ancient_greek
    from eee_project.notebook_utils import eee_footer
    from pathlib import Path as _Path
    NB_DIR = _Path(__file__).parent
    NB_REMOTE = f"{cfg.raw_base}/2026_07_01"
    _yamls = [NB_DIR.parent / f"athenaze_{_c}_verbs.yaml" for _c in ("cap1", "cap2")]
    for _y in _yamls:
        GreekUtils.ensure_file(_y.name, nb_dir=_y.parent, remote_base=cfg.raw_base)
    ag = AncientGreekBackend(lexicons=["pratt", "ltrg", *[str(_y) for _y in _yamls]])
    setup_ancient_greek(ag)
    gu = GreekUtils(ag, mo, eee_module=eee, config=ANCIENT_GREEK)
    eee_footer(mo, lang='ru')
    return NB_DIR, NB_REMOTE, gu


@app.cell(hide_code=True)
def _(cap_v3, cv_v3, gu, set_sub_cnt_v3, verb_form_v3):
    check_btn_v3 = gu.dirty_check_button(
        verb_form_v3, cap_v3, cv_v3, "verb_word", word_key="Word", label="Проверить"
    )
    set_sub_cnt_v3(0)
    return (check_btn_v3,)


if __name__ == "__main__":
    app.run()
