# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.23.14",
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
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    from eee_project import ConfigStore, eee_topbar
    _ROOT = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main"
    cfg = ConfigStore.from_file_or_url(
        __file__,
        f"{_ROOT}/ancient_greek/palaestra/ancient_greek.2026.summer/lessons.tsv",
        ga=f"{_ROOT}/ga.json",
    )
    eee_topbar(mo, back_url=cfg.index_url(), lang="ru", titles="Palaestra",
               ga_config=cfg.ga_config())
    return (cfg,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Δίδαγμα α'
    **Palaestra — Древнегреческий язык, начальный уровень — Лето 2026**

    [![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_6yCT2rFgPRPqBPNKo3g3uj)
    """)
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, mo):
    mo.md(f"**Материалы занятия:** [Δίδαγμα α'.pdf]({NB_REMOTE}/Δίδαγμα%20α'.pdf) · [ΣΤΟΙΧΕΙΑ.pdf]({NB_REMOTE}/ΣΤΟΙΧΕΙΑ.pdf) · [ΤΟ ΠΡΟΛΕΓΟΜΕΝΟΝ ΔΙΔΑΓΜΑ (2).pdf]({NB_REMOTE}/ΤΟ%20ΠΡΟΛΕΓΟΜΕΝΟΝ%20ΔΙΔΑΓΜΑ%20(2).pdf) · [πρῶτον προστεταγμένον.pdf]({NB_REMOTE}/πρῶτον%20προστεταγμένον.pdf)")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## τὰ στοιχεῖα — τὰ γράμματα · Алфавит

    | № | Прописн. | Строчн. | Греческое | Русское | Произнош. (Эразм) | Лат. |
    |---|:--------:|:-------:|-----------|---------|:-----------------:|:----:|
    | 1 | Α | α | ἄλφα | альфа | a | ā |
    | 2 | Β | β | βῆτα | бета | б | b |
    | 3 | Γ | γ | γάμμα | гамма | г | g |
    | 4 | Δ | δ | δέλτα | дельта | д | d |
    | 5 | Ε | ε | ἔ ψιλόν | эпсилон | э *(кратк.)* | ĕ |
    | 6 | Ζ | ζ | ζῆτα | дзета | дз | dz |
    | 7 | Η | η | ἦτα | эта | э *(долг.)* | ē |
    | 8 | Θ | θ | θῆτα | тета | тх | th |
    | 9 | Ι | ι | ἰῶτα | иота | и | ī |
    | 10 | Κ | κ | κάππα | каппа | к | k |
    | 11 | Λ | λ | λάμβδα | ламбда | л | l |
    | 12 | Μ | μ | μῦ | мю | м | m |
    | 13 | Ν | ν | νῦ | ню | н | n |
    | 14 | Ξ | ξ | ξεῖ | кси | кс | x |
    | 15 | Ο | ο | ὄ μικρόν | омикрон | о *(кратк.)* | ŏ |
    | 16 | Π | π | πεῖ | пи | п | p |
    | 17 | Ρ | ρ | ῥῶ | ро | р | r, rh |
    | 18 | Σ | σ/ς | σίγμα | сигма | с | s |
    | 19 | Τ | τ | ταῦ | тау | т | t |
    | 20 | Υ | υ | ὖ ψιλόν | юпсилон | ю | ȳ |
    | 21 | Φ | φ | φεῖ | фи | ф | ph |
    | 22 | Χ | χ | χεῖ | хи | х | ch |
    | 23 | Ψ | ψ | ψεῖ | пси | пс | ps |
    | 24 | Ω | ω | ὦ μέγα | омега | о *(долг.)* | ō |

    *ε, ο — всегда краткие; η, ω — всегда долгие.
    σ — в начале и середине слова; ς — в конце слова.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Три традиции произношения

    В истории изучения древнегреческого сложились три основные системы:

    **Эразмовское** (*Erasmian*, XVI в., Эразм Роттердамский) — реконструкция классической аттической фонетики, принятая в западной академической традиции.
    η ≈ долгое **ē** [ɛː], ω ≈ долгое **ō** [ɔː], υ ≈ нем. **ü** [y], β = **b**.
    Ударение считается тональным (музыкальным) → в практике просто ударный слог.
    Θ = придыхательный **t** (смычный + выдох, как санскр. *th*), δ = **d** (звонкий смычный).
    Придыхание ῾ = **h**. Именно эту систему мы используем на курсе.

    **Кóйне / Лукианово** (*Koine*, I в. до н. э. — II в. н. э.) — реконструкция разговорного греческого эпохи Нового Завета и Римской империи.
    К этому периоду η и ι слились в **и**, υ сблизился с ι (уже ≈ **и** во многих диалектах), придыхание ослабевало.
    Θ → фрикативный **th** (как англ. *thin*), δ → **ð** (как англ. *this*), β → **в**.

    **Рейхлиново** (*Reuchlinian*, XVI в., Иоганн Рейхлин) — традиция, основанная на византийском и новогреческом произношении.
    η = ι = υ = ει = οι = **и**, β = **в**, γ = звонкий фрикатив [**ɣ**] (как новогреч. γ), придыхание исчезло.
    Θ = **th** (англ. *thin*), δ = **ð** (англ. *this*).
    Используется в Греции при преподавании древнегреческого и в греческой церковной традиции.

    ---

    ### Диакритические знаки и их произношение

    | Кнопка | Название | Произношение | Применение |
    |:------:|:---------|:-------------|:-----------|
    | ά | οξεῖα — острое ударение | высокий тон слога (→ ударение) | любой гласный |
    | ὰ | βαρεῖα — тупое ударение | понижение тона (перед следующим словом) | любой гласный |
    | ᾶ | περισπωμένη — облечённое | восходяще-нисходящий тон на долгом слоге | только долгие: α η ι υ ω |
    | ἁ | δασεῖα — густое придыхание | звук **h** перед гласным (ἁ = *ha*) | любой гласный |
    | ἀ | ψιλή — тонкое придыхание | нет придыхания (ἀ = *a*) | любой гласный |
    | ᾳ | ὑπογεγραμμένη — йота подписная | в класс. период: дифтонг (ᾳ = *ai*); у эразмистов обычно не произносится | только α η ω |
    | ϊ | διαίρεσις — диереза | два слога, не дифтонг: ναΐ = *na-i*, не *nai* | только ι υ |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## τὸ ποίημα · Стихотворение с алфавитом

    <div style="border-left:3px solid #ccc;padding:.6em 1.2em;font-size:1.1em;line-height:2.2">
    ἔστ' <strong>ἄλφα</strong>, <strong>βῆτα</strong>, <strong>γάμμα</strong>, <strong>δέλτα</strong>, καὶ τὸ <strong>εἶ</strong>,<br>
    <strong>ζῆτ'</strong>, <strong>ἦτα</strong>, <strong>θῆτ'</strong>, <strong>ἰῶτα</strong>, <strong>κάππα</strong>, <strong>λάμβδα</strong>, <strong>μῦ</strong>,<br>
    <strong>νῦ</strong>, <strong>ξῖ</strong>, τὸ <strong>οὖ</strong>, <strong>πῖ</strong>, <strong>ῥῶ</strong>, τὸ <strong>σῖγμα</strong>, <strong>ταῦ</strong>, τὸ <strong>ῦ</strong>,<br>
    <strong>φῖ</strong>, <strong>χῖ</strong> τε καὶ <strong>ψῖ</strong> καὶ τὸ <strong>ὦ</strong>.
    </div>

    *Домашнее задание: выучить наизусть.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## χρήσιμαι λέξεις · Полезные слова

    ### Глаголы — ἡ προστακτική (повелительное наклонение)

    | Глагол | Значение | Sg (ед. ч.) | Pl (мн. ч.) |
    |:-------|:---------|:-----------:|:-----------:|
    | λέγω | говорить, читать вслух | **λέγε!** | **λέγετε!** |
    | ἀκούω | слушать | **ἄκουε!** | **ἀκούετε!** |
    | ἀναγιγνώσκω | читать | **ἀναγίγνωσκε!** | **ἀναγιγνώσκετε!** |
    | παύω | останавливать(ся) | **παῦε!** | **παύετε!** |

    ### Выражения (φράσεις)

    | Греческий | Перевод |
    |:----------|:--------|
    | καταλαμβάνω | я понимаю |
    | οὐ καταλαμβάνω | я не понимаю |
    | ὦ διδάσκαλε, παῦε, οὐ καταλαμβάνω... αὖθις λέγε | Учитель, остановись, я не понимаю... скажи ещё раз |
    | δῆλόν ἐστιν ↔ ἄδηλόν ἐστιν | это ясно ↔ это неясно |
    | ἆρα δῆλόν ἐστιν; | это ясно? |
    | ναί, μάλιστα ↔ οὐδαμῶς, ἥκιστα | да, конечно ↔ нет, нисколько |
    | χαῖρε! · εἰς αὖθις | здравствуй! · до следующего раза |
    | χάριν σοι / χάριν ὑμῖν | спасибо (тебе / вам) |
    """)
    return


@app.cell(hide_code=True)
def _(cfg, mo):
    import eee_project as eee
    from ancient_greek_backend_eee import AncientGreekBackend
    from eee_project import GreekUtils, ANCIENT_GREEK, setup_ancient_greek
    from pathlib import Path as _Path

    ag = AncientGreekBackend(lexicons=["pratt", "ltrg", "homer", "lxx", "morphgnt"])
    setup_ancient_greek(ag)

    gu = GreekUtils(ag, mo, eee_module=eee, config=ANCIENT_GREEK)

    NB_REMOTE = f"{cfg.raw_base}/2026_06_09"
    for _pdf in (
        "Δίδαγμα α'.pdf",
        "ΣΤΟΙΧΕΙΑ.pdf",
        "ΤΟ ΠΡΟΛΕΓΟΜΕΝΟΝ ΔΙΔΑΓΜΑ (2).pdf",
        "πρῶτον προστεταγμένον.pdf",
    ):
        gu.ensure_file(_pdf, nb_dir=_Path(__file__).parent, remote_base=NB_REMOTE)
    _IMP = {"VerbForm": "Fin", "Tense": "Pres", "Voice": "Act", "Mood": "Imp"}
    VERBS = gu.load_slot_drill(
        gu.ensure_file("verbs.tsv", nb_dir=_Path(__file__).parent, remote_base=NB_REMOTE),
        {"verb": None, "sg": {**_IMP, "Person": "2", "Number": "Sing"},
                       "pl": {**_IMP, "Person": "2", "Number": "Plur"}},
        pos="verb",
    )
    _FIELDS_V = [('verb', 'словарная форма'), ('sg', 'повел. ед. ч.'), ('pl', 'повел. мн. ч.')]
    VERB_ENTRIES = [
        {"meaning": f"{v['meaning']} ({lbl})", "form": v[key]}
        for v in VERBS
        for key, lbl in _FIELDS_V
    ]

    return NB_REMOTE, VERB_ENTRIES, eee, gu


@app.cell(hide_code=True)
def _(mo):
    cv_v, set_cv_v = mo.state(None)
    remaining_v, set_remaining_v = mo.state(None)
    score_v, set_score_v = mo.state({'correct': 0, 'total': 0})
    history_v, set_history_v = mo.state([])
    future_v, set_future_v = mo.state([])
    restore_entry_v, set_restore_entry_v = mo.state(None)

    return (
        cv_v,
        future_v,
        history_v,
        remaining_v,
        restore_entry_v,
        score_v,
        set_cv_v,
        set_future_v,
        set_history_v,
        set_remaining_v,
        set_restore_entry_v,
        set_score_v,
    )


@app.cell(hide_code=True)
def _(cv_v, gu, history_v, remaining_v, restore_entry_v):
    _ = cv_v()
    write_input_v, dia_v, check_btn_v, prev_btn_v, next_btn_v = gu.word_drill_widgets(
        cv=cv_v(),
        remaining=remaining_v(),
        restore_entry=restore_entry_v(),
        history_len=len(history_v()),
    )

    return check_btn_v, dia_v, next_btn_v, prev_btn_v, write_input_v


@app.cell(hide_code=True)
def _(
    VERB_ENTRIES,
    check_btn_v,
    cv_v,
    dia_v,
    future_v,
    gu,
    history_v,
    next_btn_v,
    prev_btn_v,
    remaining_v,
    restore_entry_v,
    score_v,
    set_cv_v,
    set_future_v,
    set_history_v,
    set_remaining_v,
    set_restore_entry_v,
    set_score_v,
    write_input_v,
):
    gu.word_drill_form(
        cv_v, set_cv_v, remaining_v, set_remaining_v,
        score_v, set_score_v, restore_entry_v, set_restore_entry_v,
        history_v, set_history_v, future_v, set_future_v,
        write_input_v, dia_v, check_btn_v, prev_btn_v, next_btn_v,
        vocab=VERB_ENTRIES,
        title='## Упражнение 1 · Повелительное наклонение',
        comment='Для ввода используйте **polytonic Greek keyboard** или кнопки диакритики ниже.<br>**Как пользоваться:** нажмите кнопку знака диакритики → введите гласную → знак применится. Нажмите повторно или введите согласную — снимается. Можно **совмещать несколько знаков диакритики** (например, придыхание + ударение перед вводом буквы → ἆ).',
        form_key='form',
    )

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## ἀναγιγνώσκετε! · Слова для чтения

    Слова оканчиваются на **-μα** (средний род, 3-е склонение):

    | | | | |
    |---|---|---|---|
    | 1. αἴνιγμα | 11. δόγμα | 21. μάθημα | 31. πρόβλημα |
    | 2. ἀξίωμα | 12. δρᾶμα | 22. μίασμα | 32. ῥεῦμα |
    | 3. ἄρωμα | 13. ἔμβλημα | 23. νόμισμα | 33. στίγμα |
    | 4. ἄσθμα | 14. ζεῦγμα | 24. ὄνομα | 34. σύμπτωμα |
    | 5. γράμμα | 15. θέμα | 25. πάθημα | 35. σύστημα |
    | 6. δέρμα | 16. θεώρημα | 26. πλάσμα | 36. σχῆμα |
    | 7. διάδημα | 17. ἰδίωμα | 27. πνεῦμα | 37. σχίσμα |
    | 8. διάφραγμα | 18. κίνημα | 28. πρᾶγμα | 38. σῶμα |
    | 9. δίλημμα | 19. κλίμα | 29. ποίημα | 39. φλέγμα |
    | 10. δίπλωμα | 20. κόμμα | 30. πρίσμα | 40. χρῶμα |
    """)
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, eee, gu):
    import csv as _csv
    from pathlib import Path as _Path

    _all_aslots = eee.get_slot_templates("grc", "adjective", "en") or []
    _adv_slot = next((s for s in _all_aslots if s.tag == "ADV"), None)

    _adjs_path = gu.ensure_file("adjs.tsv", nb_dir=_Path(__file__).parent, remote_base=NB_REMOTE)
    with open(_adjs_path, encoding="utf-8") as _f:
        _rows = list(_csv.DictReader(_f, delimiter="\t"))

    ADJS = []
    for _r in _rows:
        _w = _r["Word"]
        ADJS.append({
            "adj": _w,
            "meaning": _r["Translation"],
            "adv": min(eee.inflect_slot(_w, _adv_slot, "adjective", language="grc", backend="ancient-greek"), default="") if _adv_slot else "",
            "label": f"{_w} — {_r['Translation']}",
                "prompt": f"{_w} ({_r['Translation']})",
        })
    return (ADJS,)


@app.cell(hide_code=True)
def _(ADJS, mo):
    import random as _rand
    _shuf_a = _rand.sample(ADJS, len(ADJS))
    cv_a, set_cv_a = mo.state(_shuf_a[0])
    remaining_a, set_remaining_a = mo.state(_shuf_a[1:])
    score_a, set_score_a = mo.state({'correct': 0, 'total': 0})
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
def _(cv_a, gu, history_a, remaining_a, restore_entry_a):
    _ = cv_a()
    write_input_a, dia_a, check_btn_a, prev_btn_a, next_btn_a = gu.word_drill_widgets(
        cv=cv_a(),
        remaining=remaining_a(),
        restore_entry=restore_entry_a(),
        history_len=len(history_a()),
        placeholder='наречие…',
    )
    return check_btn_a, dia_a, next_btn_a, prev_btn_a, write_input_a


@app.cell(hide_code=True)
def _(
    ADJS,
    check_btn_a,
    cv_a,
    dia_a,
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
    write_input_a,
):
    gu.word_drill_form(
        cv_a, set_cv_a, remaining_a, set_remaining_a,
        score_a, set_score_a, restore_entry_a, set_restore_entry_a,
        history_a, set_history_a, future_a, set_future_a,
        write_input_a, dia_a, check_btn_a, prev_btn_a, next_btn_a,
        vocab=ADJS,
        title='## Упражнение 2 · Образование наречий\n\n**Правило:** замените окончание **-ός** на **-ῶς**\n\n*Пример:* καλός (красивый) → καλῶς',
        meaning_key='prompt',
        form_key='adv',
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## τὸ πρῶτον προστεταγμένον · Домашнее задание

    1. Повторите алфавит и постарайтесь выучить стихотворение.
    2. Выучите основные глаголы и выражения (χρήσιμαι λέξεις).
    3. Прочитайте слова на последнем слайде (αἴνιγμα... χρῶμα).
    4. Образуйте наречия (упражнение 2 выше).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    from eee_project.notebook_utils import eee_footer
    eee_footer(mo, lang="ru")
    return


if __name__ == "__main__":
    app.run()
