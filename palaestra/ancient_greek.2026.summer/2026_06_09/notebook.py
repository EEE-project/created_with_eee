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
def _():
    import csv as _csv
    import eee_project as eee
    from ancient_greek_backend_eee import AncientGreekBackend
    from pathlib import Path as _Path

    ag = AncientGreekBackend(lexicons=["pratt", "ltrg", "homer", "lxx", "morphgnt"])
    eee.register_backend("grc", ag)
    eee.register_backend("grc", ag, backend="ancient-greek")
    eee.set_chain("grc", ["ancient-greek"])

    _all_vslots = eee.get_slot_templates("grc", "verb", "en") or []
    _sg_slot = next((s for s in _all_vslots if s.tag == "PAD.2S"), None)
    _pl_slot = next((s for s in _all_vslots if s.tag == "PAD.2P"), None)

    with open(_Path(__file__).parent / "verbs.tsv", encoding="utf-8") as _f:
        _rows = list(_csv.DictReader(_f, delimiter="\t"))

    VERBS = []
    for _r in _rows:
        _w = _r["Word"]
        VERBS.append({
            "verb": _w,
            "meaning": _r["Translation"],
            "sg": min(eee.inflect_slot(_w, _sg_slot, "verb", language="grc", backend="ancient-greek"), default="") if _sg_slot else "",
            "pl": min(eee.inflect_slot(_w, _pl_slot, "verb", language="grc", backend="ancient-greek"), default="") if _pl_slot else "",
        })
    return VERBS, eee


@app.cell(hide_code=True)
def _(mo):

    import unicodedata

    def strip_diacritics(s):
        return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

    strict_v = mo.ui.switch(label="Учитывать диакритику", value=False)
    mo.hstack([strict_v], justify="end")
    return strict_v, strip_diacritics


@app.cell(hide_code=True)
def _(mo):

    _clk = lambda v: (v or 0) + 1
    clear_btn_v = mo.ui.button(label="Очистить", on_click=_clk)
    return (clear_btn_v,)


@app.cell(hide_code=True)
def _(VERBS, clear_btn_v, mo):

    _dep = clear_btn_v.value
    _clk = lambda v: (v or 0) + 1
    submit_btn_v = mo.ui.button(label="Проверить ✓", on_click=_clk)
    _verb = [mo.ui.text(placeholder="глагол…") for _ in VERBS]
    _sg   = [mo.ui.text(placeholder="ед. ч.…") for _ in VERBS]
    _pl   = [mo.ui.text(placeholder="мн. ч.…") for _ in VERBS]
    verb_word_v = _verb
    verb_sg_v   = _sg
    verb_pl_v   = _pl
    _rows = [
        mo.hstack([mo.md(f"**{v['meaning']}**"), _verb[i], _sg[i], _pl[i]], justify="start")
        for i, v in enumerate(VERBS)
    ]
    mo.vstack([
        mo.md(r"## Упражнение 1 · Повелительное наклонение"),
        mo.md("Дано: **значение**. Введите: словарную форму глагола, затем повел. ед. и мн. ч."),
        *_rows,
        mo.hstack([clear_btn_v, submit_btn_v], justify="end"),
    ])
    return submit_btn_v, verb_pl_v, verb_sg_v, verb_word_v


@app.cell(hide_code=True)
def _(
    VERBS,
    mo,
    strict_v,
    strip_diacritics,
    submit_btn_v,
    verb_pl_v,
    verb_sg_v,
    verb_word_v,
):

    _feedback = []
    if submit_btn_v.value:
        def _cmp(a, b):
            return (a == b) if strict_v.value else (strip_diacritics(a) == strip_diacritics(b))
        for _i, _v in enumerate(VERBS):
            _w = verb_word_v[_i].value.strip()
            _s = verb_sg_v[_i].value.strip()
            _p = verb_pl_v[_i].value.strip()
            _parts = []
            if _w:
                _ok = _cmp(_w, _v["verb"])
                _parts.append(f"{'✓' if _ok else '✗'} глагол **{_w}**" + (f" ← *{_v['verb']}*" if not _ok else ""))
            if _s:
                _ok = _cmp(_s, _v["sg"])
                _parts.append(f"{'✓' if _ok else '✗'} sg **{_s}**" + (f" ← *{_v['sg']}*" if not _ok else ""))
            if _p:
                _ok = _cmp(_p, _v["pl"])
                _parts.append(f"{'✓' if _ok else '✗'} pl **{_p}**" + (f" ← *{_v['pl']}*" if not _ok else ""))
            if _parts:
                _feedback.append(mo.md(f"*{_v['meaning']}*: " + " · ".join(_parts)))
    mo.vstack(_feedback) if _feedback else mo.md("")
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
def _(eee):
    import csv as _csv
    from pathlib import Path as _Path

    _all_aslots = eee.get_slot_templates("grc", "adjective", "en") or []
    _adv_slot = next((s for s in _all_aslots if s.tag == "ADV"), None)

    with open(_Path(__file__).parent / "adjs.tsv", encoding="utf-8") as _f:
        _rows = list(_csv.DictReader(_f, delimiter="\t"))

    ADJS = []
    for _r in _rows:
        _w = _r["Word"]
        ADJS.append({
            "adj": _w,
            "meaning": _r["Translation"],
            "adv": min(eee.inflect_slot(_w, _adv_slot, "adjective", language="grc", backend="ancient-greek"), default="") if _adv_slot else "",
        })
    return (ADJS,)


@app.cell(hide_code=True)
def _(mo):

    _clk_a = lambda v: (v or 0) + 1
    clear_btn_a = mo.ui.button(label="Очистить", on_click=_clk_a)
    return (clear_btn_a,)


@app.cell(hide_code=True)
def _(ADJS, clear_btn_a, mo):

    _dep = clear_btn_a.value
    _clk_a = lambda v: (v or 0) + 1
    submit_btn_a = mo.ui.button(label="Проверить ✓", on_click=_clk_a)
    _inputs = [
        mo.ui.text(placeholder="наречие…", value="καλῶς" if i == 0 else "")
        for i, _ in enumerate(ADJS)
    ]
    adv_inputs = _inputs
    mo.vstack([
        mo.md(r"## Упражнение 2 · Образование наречий"),
        mo.md(r"**Правило:** замените окончание **-ός** на **-ῶς** (с облегчённым ударением: циркумфлекс)"),
        mo.md(r"*Пример:* καλ**ός** → καλ**ῶς**"),
        *[
            mo.hstack([mo.md(f"**{a['adj']}** — {a['meaning']}"), _inputs[i]], justify="start")
            for i, a in enumerate(ADJS)
        ],
        mo.hstack([clear_btn_a, submit_btn_a], justify="end"),
    ])
    return adv_inputs, submit_btn_a


@app.cell(hide_code=True)
def _(ADJS, adv_inputs, mo, strict_v, strip_diacritics, submit_btn_a):

    _feedback = []
    if submit_btn_a.value:
        def _cmp(a, b):
            return (a == b) if strict_v.value else (strip_diacritics(a) == strip_diacritics(b))
        for _i, _a in enumerate(ADJS):
            _val = adv_inputs[_i].value.strip()
            if _val:
                _ok = _cmp(_val, _a["adv"])
                _feedback.append(mo.md(
                    f"{'✓' if _ok else '✗'} **{_a['adj']}** → **{_val}**" +
                    (f" ← правильно: *{_a['adv']}*" if not _ok else "")
                ))
    mo.vstack(_feedback) if _feedback else mo.md("")
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
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
