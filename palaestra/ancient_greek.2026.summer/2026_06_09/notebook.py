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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Δίδαγμα α'
    **Palaestra — Древнегреческий язык, начальный уровень — Лето 2026**

    [![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_6yCT2rFgPRPqBPNKo3g3uj)
    """)
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
    from eee_project import GreekUtils, ANCIENT_GREEK
    from pathlib import Path as _Path

    ag = AncientGreekBackend(lexicons=["pratt", "ltrg", "homer", "lxx", "morphgnt"])
    eee.register_backend("grc", ag)
    eee.register_backend("grc", ag, backend="ancient-greek")
    eee.set_chain("grc", ["ancient-greek"])

    gu = GreekUtils(ag, mo, eee_module=eee, config=ANCIENT_GREEK)

    NB_REMOTE = cfg.nb_remote("2026_06_09")
    _IMP = {"VerbForm": "Fin", "Tense": "Pres", "Voice": "Act", "Mood": "Imp"}
    VERBS = gu.load_slot_drill(
        gu.ensure_file("verbs.tsv", nb_dir=_Path(__file__).parent, remote_base=NB_REMOTE),
        {"verb": None, "sg": {**_IMP, "Person": "2", "Number": "Sing"},
                       "pl": {**_IMP, "Person": "2", "Number": "Plur"}},
        pos="verb",
    )
    return VERBS, NB_REMOTE, eee, gu


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
        mo.md(r"## Упражнение 1 · Повелительное наклонение"),
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
        })
    return (ADJS,)


@app.cell(hide_code=True)
def _(mo):

    _clk_a = lambda v: (v or 0) + 1
    clear_btn_a = mo.ui.button(label="Очистить", on_click=_clk_a)
    return (clear_btn_a,)


@app.cell(hide_code=True)
def _(ADJS, clear_btn_a, gu, mo):

    _dep = clear_btn_a.value
    _clk_a = lambda v: (v or 0) + 1
    submit_btn_a = mo.ui.button(label="Проверить ✓", on_click=_clk_a)
    adv_inputs_v, _rows = gu.make_item_drill_rows(
        ADJS, ["adv"],
        meaning_key="label",
        placeholders=["наречие…"],
    )
    mo.vstack([
        mo.md(r"## Упражнение 2 · Образование наречий"),
        mo.md(r"**Правило:** замените окончание **-ός** на **-ῶς** (с облегчённым ударением: циркумфлекс)"),
        mo.md(r"*Пример:* καλ**ός** → καλ**ῶς**"),
        *_rows,
        mo.hstack([clear_btn_a, submit_btn_a], justify="end"),
    ])
    return adv_inputs_v, submit_btn_a


@app.cell(hide_code=True)
def _(ADJS, adv_inputs_v, gu, mo, strict_v, submit_btn_a):

    _fb = gu.check_item_drill(
        ADJS, adv_inputs_v, ["adv"],
        meaning_key="label",
        field_labels=["нар."],
        strict=strict_v.value,
    ) if submit_btn_a.value else []
    mo.vstack(_fb) if _fb else mo.md("")
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


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)
