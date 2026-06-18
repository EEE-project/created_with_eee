# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "eee-project @ git+https://codeberg.org/EEE-project/eee-project.git",
#     "marimo>=0.23.3",
#     "modern-greek-eee @ git+https://github.com/EEE-project/modern-greek-eee.git",
#     "modern-greek-inflexion-eee @ git+https://github.com/EEE-project/modern-greek-inflexion-eee.git",
#     "pandas",
# ]
#
# [tool.uv.sources]
# eee-project = { git = "https://codeberg.org/EEE-project/eee-project.git" }
# modern-greek-eee = { git = "https://github.com/EEE-project/modern-greek-eee" }
# modern-greek-inflexion-eee = { git = "https://github.com/EEE-project/modern-greek-inflexion-eee" }
# ///

import marimo

__generated_with = "0.23.5"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(language_selector, mo):
    from eee_project import ConfigStore, eee_topbar
    _ROOT = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main"
    _cfg = ConfigStore.from_url(
        f"{_ROOT}/ellinika_b/lessons.tsv",
        ga=f"{_ROOT}/ga.json",
    )
    eee_topbar(mo, back_url=_cfg.index_url(), lang=language_selector.value, titles={
        "ru": "Ελληνικά Β", "el": "Ελληνικά Β", "en": "Ελληνικά Β",
    }, ga_config=_cfg.ga_config())
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Title
    _lang = language_selector.value
    _badge = "[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_XVcePWL2WPvyqykXxBM8mn)"
    if _lang == "ru":
        _sub = "Глава 7 — Образы из прошлого · B1"
        _gl, _tl = "Грамматика", "Тесты"
        _tc = "Существительные · Глаголы · Прилагательные"
    elif _lang == "el":
        _sub = "Ενότητα 7 — Εικόνες από το παρελθόν · B1"
        _gl, _tl = "Γραμματική", "Τεστ"
        _tc = "Ουσιαστικά · Ρήματα · Επίθετα"
    else:
        _sub = "Unit 7 — Images from the Past · B1"
        _gl, _tl = "Grammar", "Tests"
        _tc = "Nouns · Verbs · Adjectives"
    _gc = "Παρατατικός (Α, Β1, Β2, ΑΒ) · Χρονικές συνδέσεις"
    _out = mo.md(f"""# «Θυμάμαι ότι παίζαμε όλη μέρα...» 🏘️
    ## {_sub} {_badge}

    **{_gl}:** {_gc}
    **{_tl}:** {_tc}
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Vocabulary (p. 106)
    _lang = language_selector.value
    if _lang == "ru":
        _heading = "### Словарь и фразы (с. 106)"
        _phrases_heading = "#### Πώς το λένε; — Как сказать?"
        _phrases = """
    | Греческий | Русский |
    |-----------|---------|
    | **Εδώ, τα λέγαμε…** | Ну вот, мы же говорили… |
    | **Μα τι κατάσταση είναι αυτή;** | Что вообще происходит? |
    | **Αμάν πια!** | Ну хватит уже! |
    | **Εμ, βέβαια!** | Ну конечно! |
    | **Ακόμα και…** | Даже… |
    | **Άκουσα ότι…** | Я слышал, что… |
    | **Αλλά με όλα τα προβλήματά του…** | Но со всеми его проблемами… |
    | **Όχι όπως τώρα που…** | Не так, как сейчас, когда… |
    | **Δεν είναι η μέρα σου σήμερα.** | Сегодня не твой день. |
    | **Όλα μαύρα τα βλέπεις.** | Ты всё видишь в чёрном цвете. |
    | **Μήπως σου φτιάξει το κέφι.** | Может, тебе поднимет настроение. |
    | **Τι να σας κεράσουμε;** | Чем вас угостить? |
    """
        _vocab_heading = "#### Λέξεις, λέξεις — Слова, слова..."
        _vocab = """
    | Греческий | Русский |
    |-----------|---------|
    | **πεζοδρόμιο** (το) | тротуар |
    | **πολυκατοικία** (η) | многоквартирный дом |
    | **πράσινο** (το) | зелень / зелёные насаждения |
    | **χωράφι** (το) | поле |
    """
    elif _lang == "el":
        _heading = "### Λεξιλόγιο & Εκφράσεις (σ. 106)"
        _phrases_heading = "#### Πώς το λένε;"
        _phrases = """
    - **Εδώ, τα λέγαμε…**
    - **Μα τι κατάσταση είναι αυτή;**
    - **Αμάν πια!**
    - **Εμ, βέβαια!**
    - **Ακόμα και…**
    - **Άκουσα ότι…**
    - **Αλλά με όλα τα προβλήματά του…**
    - **Όχι όπως τώρα που…**
    - **Δεν είναι η μέρα σου σήμερα.**
    - **Όλα μαύρα τα βλέπεις.**
    - **Μήπως σου φτιάξει το κέφι.**
    - **Τι να σας κεράσουμε;**
    """
        _vocab_heading = "#### Λέξεις, λέξεις"
        _vocab = """
    - **πεζοδρόμιο** (το) — πεζοδρόμιο της πόλης
    - **πολυκατοικία** (η) — κτίριο με πολλά διαμερίσματα
    - **πράσινο** (το) — φυτά και χώροι πρασίνου
    - **χωράφι** (το) — αγροτική έκταση
    """
    else:
        _heading = "### Vocabulary & Phrases (p. 106)"
        _phrases_heading = "#### Πώς το λένε; — How do you say it?"
        _phrases = """
    | Greek | English |
    |-------|---------|
    | **Εδώ, τα λέγαμε…** | Well, we were saying… |
    | **Μα τι κατάσταση είναι αυτή;** | What kind of situation is this? |
    | **Αμάν πια!** | Enough already! |
    | **Εμ, βέβαια!** | Well, of course! |
    | **Ακόμα και…** | Even… |
    | **Άκουσα ότι…** | I heard that… |
    | **Αλλά με όλα τα προβλήματά του…** | But with all its problems… |
    | **Όχι όπως τώρα που…** | Not like now when… |
    | **Δεν είναι η μέρα σου σήμερα.** | Today is not your day. |
    | **Όλα μαύρα τα βλέπεις.** | You see everything in black. |
    | **Μήπως σου φτιάξει το κέφι.** | Maybe it will lift your spirits. |
    | **Τι να σας κεράσουμε;** | What can we treat you to? |
    """
        _vocab_heading = "#### Λέξεις, λέξεις — Words, words..."
        _vocab = """
    | Greek | English |
    |-------|---------|
    | **πεζοδρόμιο** (το) | pavement / sidewalk |
    | **πολυκατοικία** (η) | apartment building |
    | **πράσινο** (το) | greenery / green spaces |
    | **χωράφι** (το) | field |
    """
    mo.md(f"{_heading}\n\n{_phrases_heading}\n{_phrases}\n{_vocab_heading}\n{_vocab}")
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar: Παρατατικός conjugation
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Грамматика: Παρατατικός (Прошедшее продолженное)

    Παρατατικός описывает **длительные или повторяющиеся** действия в прошлом.

    Маркеры времени: *κάθε μέρα* (каждый день), *συχνά* (часто), *όταν ήμουν παιδί* (когда я был ребёнком), *πάντα* (всегда).

    ### Τύπος Α — глаголы на **-ω**

    Окончания: **-α, -ες, -ε, -αμε, -ατε, -αν/ε**

    | Лицо | Ед. ч. | Мн. ч. |
    |------|--------|--------|
    | 1-е | έ**παιζα** | παίζ**αμε** |
    | 2-е | έ**παιζες** | παίζ**ατε** |
    | 3-е | έ**παιζε** | έ**παιζαν** |

    > Двусложные основы добавляют приращение **ε-**: παίζω→**έ**παιζα, γράφω→**έ**γραφα.

    ### Τύπος Β1 — глаголы на **-άω/-ώ** (два варианта)

    | Вариант | 1 ед. | Пример |
    |---------|-------|--------|
    | **-ούσα** | περν**ούσα** | περνούσα, περνούσες, περνούσε, περνούσαμε, περνούσατε, περνούσαν |
    | **-αγα** | πέρν**αγα** | πέρναγα, πέρναγες, πέρναγε, περνάγαμε, περνάγατε, πέρναγαν |

    > Вариант *-αγα*: ударение всегда на 3-м слоге от конца (кроме 1-го и 2-го лица мн. ч.).

    ### Τύπος Β2 — глаголы на **-ώ** (один вариант)

    | Лицо | Пример (μπορώ) |
    |------|----------------|
    | 1 ед. | μπορ**ούσα** |
    | 2 ед. | μπορ**ούσες** |
    | 3 ед. | μπορ**ούσε** |
    | 1 мн. | μπορ**ούσαμε** |
    | 2 мн. | μπορ**ούσατε** |
    | 3 мн. | μπορ**ούσαν** |

    ### Τύπος ΑΒ и исключения

    | Глагол | Παρατατικός |
    |--------|------------|
    | πηγαίνω | **πήγαινα** |
    | ακούω | **άκουγα** |
    | λέω | **έλεγα** |
    | τρώω | **έτρωγα** |
    | θέλω | **ήθελα** |
    | ξέρω | **ήξερα** |
    | υπάρχω | **υπήρχα** |
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Γραμματική: Παρατατικός

    Ο Παρατατικός εκφράζει **διαρκείς ή επαναλαμβανόμενες** πράξεις στο παρελθόν.

    Χρονικοί δείκτες: *κάθε μέρα*, *συχνά*, *όταν ήμουν παιδί*, *πάντα*.

    ### Τύπος Α — ρήματα σε **-ω**

    Καταλήξεις: **-α, -ες, -ε, -αμε, -ατε, -αν/ε**

    | Πρόσωπο | Ενικός | Πληθυντικός |
    |---------|--------|-------------|
    | 1ο | έ**παιζα** | παίζ**αμε** |
    | 2ο | έ**παιζες** | παίζ**ατε** |
    | 3ο | έ**παιζε** | έ**παιζαν** |

    > Μονοσύλλαβες βάσεις παίρνουν αύξηση **ε-**: γράφω→**έ**γραφα.

    ### Τύπος Β1 — ρήματα σε **-άω/-ώ** (δύο τύποι)

    | Τύπος | 1ο εν. | Παράδειγμα |
    |-------|--------|------------|
    | **-ούσα** | περν**ούσα** | περνούσα, -ούσες, -ούσε, -ούσαμε, -ούσατε, -ούσαν |
    | **-αγα** | πέρν**αγα** | πέρναγα, -αγες, -αγε, περνάγαμε, -άγατε, -αγαν |

    ### Τύπος Β2 — ρήματα σε **-ώ** (ένας τύπος)

    μπορ**ούσα**, μπορ**ούσες**, μπορ**ούσε**, μπορ**ούσαμε**, μπορ**ούσατε**, μπορ**ούσαν**

    ### Τύπος ΑΒ και εξαιρέσεις

    | Ρήμα | Παρατατικός |
    |------|------------|
    | πηγαίνω | **πήγαινα** |
    | ακούω | **άκουγα** |
    | λέω | **έλεγα** |
    | τρώω | **έτρωγα** |
    | θέλω | **ήθελα** |
    | ξέρω | **ήξερα** |
    | υπάρχω | **υπήρχα** |
    """)
    else:
        _out = mo.md("""
    ## Grammar: Παρατατικός (Past Imperfect)

    The Παρατατικός describes **ongoing or repeated** actions in the past.

    Time markers: *κάθε μέρα* (every day), *συχνά* (often), *όταν ήμουν παιδί* (when I was a child), *πάντα* (always).

    ### Type A — verbs ending in **-ω**

    Endings: **-α, -ες, -ε, -αμε, -ατε, -αν/ε**

    | Person | Singular | Plural |
    |--------|----------|--------|
    | 1st | έ**παιζα** | παίζ**αμε** |
    | 2nd | έ**παιζες** | παίζ**ατε** |
    | 3rd | έ**παιζε** | έ**παιζαν** |

    > Monosyllabic stems add augment **ε-**: γράφω→**έ**γραφα.

    ### Type B1 — verbs ending in **-άω/-ώ** (two patterns)

    | Pattern | 1st sg. | Example |
    |---------|---------|---------|
    | **-ούσα** | περν**ούσα** | περνούσα, -ούσες, -ούσε, -ούσαμε, -ούσατε, -ούσαν |
    | **-αγα** | πέρν**αγα** | πέρναγα, -αγες, -αγε, περνάγαμε, -άγατε, -αγαν |

    ### Type B2 — verbs ending in **-ώ** (one pattern)

    μπορ**ούσα**, μπορ**ούσες**, μπορ**ούσε**, μπορ**ούσαμε**, μπορ**ούσατε**, μπορ**ούσαν**

    ### Type AB and irregular verbs

    | Verb | Imperfect |
    |------|-----------|
    | πηγαίνω | **πήγαινα** |
    | ακούω | **άκουγα** |
    | λέω | **έλεγα** |
    | τρώω | **έτρωγα** |
    | θέλω | **ήθελα** |
    | ξέρω | **ήξερα** |
    | υπάρχω | **υπήρχα** |
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar: Time connectors
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Грамматика: Синтаксические конструкции с Παρατατικός

    ### Παρατατικός + Παρατατικός — два одновременных длительных действия

    Союзы: **Όταν** (когда), **Ενώ** (в то время как), **Όση ώρα** (пока).

    | Греческий | Русский |
    |-----------|---------|
    | Όταν εσύ **πήγαινες**, εγώ **γύριζα**. | Когда ты шёл, я возвращался. |
    | Ενώ **διάβαζα**, **άκουγα** μουσική. | Пока я учился, я слушал музыку. |

    ### Παρατατικός + Αόριστος — длительное действие прерывается кратким событием

    Союзы: **Ενώ**, **Την ώρα που**, **Καθώς** (в то время как/пока).

    | Греческий | Русский |
    |-----------|---------|
    | Την ώρα που **πήγαινα** στη στάση, **πέρασε** το λεωφορείο. | Пока я шёл на остановку, проехал автобус. |
    | Καθώς **έπαιζα**, **χτύπησε** το τηλέφωνο. | Пока я играл, зазвонил телефон. |

    ### Элизия (Απαλοιφή φωνήεντος)

    | Полная форма | Элизия |
    |-------------|--------|
    | με άκουσε | **μ' άκουσε** |
    | το έφαγα | **τ' έφαγα** |
    | μου είπε | **μου 'πε** |
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Γραμματική: Συντακτικές δομές με Παρατατικό

    ### Παρατατικός + Παρατατικός — δύο ταυτόχρονες διαρκείς πράξεις

    Σύνδεσμοι: **Όταν**, **Ενώ**, **Όση ώρα**.

    | Ελληνικά | Μετάφραση |
    |----------|-----------|
    | Όταν εσύ **πήγαινες**, εγώ **γύριζα**. | When you were going, I was returning. |
    | Ενώ **διάβαζα**, **άκουγα** μουσική. | While I was studying, I was listening to music. |

    ### Παρατατικός + Αόριστος — διαρκής πράξη που διακόπτεται

    Σύνδεσμοι: **Ενώ**, **Την ώρα που**, **Καθώς**.

    | Ελληνικά | Μετάφραση |
    |----------|-----------|
    | Την ώρα που **πήγαινα** στη στάση, **πέρασε** το λεωφορείο. | While I was walking to the stop, the bus passed. |
    | Καθώς **έπαιζα**, **χτύπησε** το τηλέφωνο. | While I was playing, the phone rang. |

    ### Απαλοιφή φωνήεντος (Elision)

    | Πλήρης τύπος | Απαλοιφή |
    |-------------|----------|
    | με άκουσε | **μ' άκουσε** |
    | το έφαγα | **τ' έφαγα** |
    | μου είπε | **μου 'πε** |
    """)
    else:
        _out = mo.md("""
    ## Grammar: Syntax with Παρατατικός

    ### Παρατατικός + Παρατατικός — two simultaneous ongoing actions

    Conjunctions: **Όταν** (when), **Ενώ** (while), **Όση ώρα** (as long as / while).

    | Greek | English |
    |-------|---------|
    | Όταν εσύ **πήγαινες**, εγώ **γύριζα**. | When you were going, I was returning. |
    | Ενώ **διάβαζα**, **άκουγα** μουσική. | While I was studying, I was listening to music. |

    ### Παρατατικός + Aorist — ongoing action interrupted by a brief event

    Conjunctions: **Ενώ**, **Την ώρα που**, **Καθώς** (while / as).

    | Greek | English |
    |-------|---------|
    | Την ώρα που **πήγαινα** στη στάση, **πέρασε** το λεωφορείο. | While I was walking to the stop, the bus passed. |
    | Καθώς **έπαιζα**, **χτύπησε** το τηλέφωνο. | While I was playing, the phone rang. |

    ### Elision (Απαλοιφή φωνήεντος)

    | Full form | Elided |
    |-----------|--------|
    | με άκουσε | **μ' άκουσε** |
    | το έφαγα | **τ' έφαγα** |
    | μου είπε | **μου 'πε** |
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Phonography (p. 111)
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Φωνή-Γραφή — Звук и письмо (с. 111)

    ### Элизия с μ', σ', τ'

    Если **με, σε, το, τα** стоят перед словом на гласную (ο, α), они сокращаются:

    | Полная форма | Краткая форма |
    |-------------|--------------|
    | **με** + гласная | **μ'** — *με άκουγε → μ' άκουγε* |
    | **σε** + гласная | **σ'** — *σε έβλεπε → σ' έβλεπε* |
    | **το** + ο, α | **τ'** — *το όνομα → τ' όνομα* |
    | **τα** + α | **τ'** — *τα άλλα → τ' άλλα* |

    ### Элизия с μου, σου, του, το, τα + [ε-, ι-]

    | Полная форма | Краткая форма |
    |-------------|--------------|
    | μου + έ... | **μου '—** — *μου έλεγε → μου 'λεγε* |
    | σου + έ... | **σου '—** — *σου έστελνε → σου 'στέλνε* |
    | του + έ... | **του '—** — *του έφερνε → του 'φερνε* |
    | το + ή... | **το '—** — *το ήξερε → το 'ξερε* |
    | τα + έ... | **τα '—** — *τα έδινε → τα 'δινε* |
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Φωνή-Γραφή (σ. 111)

    ### Απαλοιφή με μ', σ', τ'

    Τα **με, σε, το, τα** μπροστά από λέξη που αρχίζει με φωνήεν (ο, α):

    | Πλήρης τύπος | Σύντομος τύπος |
    |-------------|----------------|
    | **με** + φωνήεν | **μ'** — *με άκουγε → μ' άκουγε* |
    | **σε** + φωνήεν | **σ'** — *σε έβλεπε → σ' έβλεπε* |
    | **το** + ο, α | **τ'** — *το όνομα → τ' όνομα* |
    | **τα** + α | **τ'** — *τα άλλα → τ' άλλα* |

    ### Απαλοιφή με μου, σου, του, το, τα + [ε-, ι-]

    | Πλήρης τύπος | Σύντομος τύπος |
    |-------------|----------------|
    | μου + έ... | **μου '—** — *μου έλεγε → μου 'λεγε* |
    | σου + έ... | **σου '—** — *σου έστελνε → σου 'στέλνε* |
    | του + έ... | **του '—** — *του έφερνε → του 'φερνε* |
    | το + ή... | **το '—** — *το ήξερε → το 'ξερε* |
    | τα + έ... | **τα '—** — *τα έδινε → τα 'δινε* |
    """)
    else:
        _out = mo.md("""
    ## Φωνή-Γραφή — Sound & Script (p. 111)

    ### Elision with μ', σ', τ'

    **με, σε, το, τα** before a word starting with a vowel (ο, α):

    | Full form | Elided form |
    |-----------|-------------|
    | **με** + vowel | **μ'** — *με άκουγε → μ' άκουγε* |
    | **σε** + vowel | **σ'** — *σε έβλεπε → σ' έβλεπε* |
    | **το** + ο, α | **τ'** — *το όνομα → τ' όνομα* |
    | **τα** + α | **τ'** — *τα άλλα → τ' άλλα* |

    ### Elision with μου, σου, του, το, τα + [ε-, ι-]

    | Full form | Elided form |
    |-----------|-------------|
    | μου + έ... | **μου '—** — *μου έλεγε → μου 'λεγε* |
    | σου + έ... | **σου '—** — *σου έστελνε → σου 'στέλνε* |
    | του + έ... | **του '—** — *του έφερνε → του 'φερνε* |
    | το + ή... | **το '—** — *το ήξερε → το 'ξερε* |
    | τα + έ... | **τα '—** — *τα έδινε → τα 'δινε* |
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Test 1 heading
    mo.md(t_ui("test1_heading", language_selector.value))
    return


@app.cell(hide_code=True)
def _(mo):
    # Noun state
    tbl_sel_n, set_tbl_sel_n = mo.state(None)
    session_total_n, set_session_total_n = mo.state(0)
    return session_total_n, set_session_total_n, set_tbl_sel_n, tbl_sel_n


@app.cell(hide_code=True)
def _(mo):
    # Noun file upload
    file_upload_noun = mo.ui.file(label="Load nouns TSV")
    file_upload_noun
    return (file_upload_noun,)


@app.cell(hide_code=True)
def _(file_upload_noun, gu, notebook_dir, os, pd):
    # Load noun data
    if file_upload_noun.value:
        df_noun = gu.load_data(file_upload_noun, [])
    else:
        try:
            df_noun = pd.read_csv(os.path.join(notebook_dir, 'nouns.tsv'), sep='\t')
        except FileNotFoundError:
            df_noun = None
    return (df_noun,)


@app.cell(hide_code=True)
def _(df_noun, language_selector, mo, t_ui, tbl_sel_n):
    # Noun table
    _lang = language_selector.value
    table_noun = mo.ui.table(df_noun, selection="multi", initial_selection=tbl_sel_n()) if df_noun is not None else None
    _display = table_noun if table_noun is not None else mo.md(
        "_nouns.tsv не найден — загрузите файл._" if _lang == "ru" else
        "_Το αρχείο nouns.tsv δεν βρέθηκε — φόρτωσε αρχείο._" if _lang == "el" else
        "_nouns.tsv not found — upload a file to begin._"
    )
    mo.vstack([mo.md(t_ui("select_nouns", _lang)), _display])
    return (table_noun,)


@app.cell(hide_code=True)
def _(gu, mo, random, session_total_n, set_session_total_n, table_noun):
    # Noun words
    words_noun = gu.get_words(table_noun)
    words4test_noun, set_words4test_noun = mo.state(words_noun.copy() if words_noun else [])
    if words_noun and len(words_noun) > session_total_n():
        set_session_total_n(len(words_noun))
    elif not words_noun:
        set_session_total_n(0)
    noun_msg, set_noun_msg = mo.state("")
    current_noun, set_current_noun = mo.state(None)
    captured_simple, set_captured_simple = mo.state(None)
    captured_article, set_captured_article = mo.state(None)
    _clk = lambda v: (v or 0) + 1
    skip_button_n = mo.ui.button(label="Skip", on_click=_clk)
    clear_button_n = mo.ui.button(label="Clear", on_click=_clk)
    skip_count_n, set_skip_count_n = mo.state(0)
    clear_count_n, set_clear_count_n = mo.state(0)
    submit_count_n, set_submit_count_n = mo.state(0)
    if words_noun and current_noun() is None:
        set_current_noun(random.choice(words_noun))
    return (
        captured_article,
        captured_simple,
        clear_button_n,
        clear_count_n,
        current_noun,
        noun_msg,
        set_captured_article,
        set_captured_simple,
        set_clear_count_n,
        set_current_noun,
        set_noun_msg,
        set_skip_count_n,
        set_submit_count_n,
        set_words4test_noun,
        skip_button_n,
        skip_count_n,
        submit_count_n,
        words4test_noun,
    )


@app.cell(hide_code=True)
def _(clear_count_n, current_noun, gu):
    # Noun simple form
    clear_count_n()
    _nc = current_noun()
    noun_word, noun_trans, noun_form = gu.create_noun_test_ui([_nc] if _nc else [], mode='simple')
    return noun_form, noun_trans, noun_word


@app.cell(hide_code=True)
def _(clear_count_n, current_noun, gu):
    # Noun article form
    clear_count_n()
    _acn = current_noun()
    art_noun_word, art_noun_trans, art_noun_form = gu.create_noun_test_ui([_acn] if _acn else [], mode='article')
    return art_noun_form, art_noun_trans, art_noun_word


@app.cell(hide_code=True)
def _(
    art_noun_form,
    captured_article,
    captured_simple,
    mo,
    noun_form,
    set_submit_count_n,
):
    # Submit button N
    _vals_s = noun_form.value if noun_form is not None else []
    _vals_a = art_noun_form.value if art_noun_form is not None else []
    _snap_s = captured_simple()
    _snap_a = captured_article()
    _has_s = bool(_vals_s and any(v.strip() for v in _vals_s))
    _has_a = bool(_vals_a and any(v.strip() for v in _vals_a))
    _match_s = _snap_s is not None and [v.strip() for v in _vals_s] == [v.strip() for v in (_snap_s.value or [])]
    _match_a = _snap_a is not None and [v.strip() for v in _vals_a] == [v.strip() for v in (_snap_a.value or [])]
    _dirty = (_has_s and not _match_s) or (_has_a and not _match_a)
    _clk = lambda v: (v or 0) + 1
    submit_button_n = mo.ui.button(label="Submit", on_click=_clk, kind="warn" if _dirty else "neutral")
    set_submit_count_n(0)
    return (submit_button_n,)


@app.cell(hide_code=True)
def _(
    captured_simple,
    clear_button_n,
    gu,
    language_selector,
    mo,
    noun_form,
    noun_trans,
    noun_word,
    session_total_n,
    skip_button_n,
    submit_button_n,
    t_ui,
    words4test_noun,
):
    # Noun simple display
    _lang = language_selector.value
    _feedback = mo.md("")
    if words4test_noun() and noun_word:
        _cs = captured_simple()
        if _cs and getattr(_cs, 'test_word', None) == noun_word:
            with mo.capture_stdout() as _buf:
                gu.check_noun_test(noun_word, _cs, mode='simple')
            if _buf.getvalue():
                _feedback = mo.md(_buf.getvalue())
        _view = mo.vstack([
            mo.md(f"{t_ui('simple_noun_heading', _lang)} ({len(words4test_noun())}/{session_total_n()})"),
            mo.md(f"{t_ui('translation_label', _lang)} **{noun_trans}**"),
            noun_form,
            _feedback,
            mo.hstack([skip_button_n, clear_button_n, submit_button_n], justify="end"),
        ])
    else:
        _view = mo.md(t_ui("noun_empty", _lang))
    _view
    return


@app.cell(hide_code=True)
def _(
    art_noun_form,
    art_noun_trans,
    art_noun_word,
    captured_article,
    clear_button_n,
    gu,
    language_selector,
    mo,
    session_total_n,
    skip_button_n,
    submit_button_n,
    t_ui,
    words4test_noun,
):
    # Noun article display
    _lang = language_selector.value
    _feedback_a = mo.md("")
    if words4test_noun() and art_noun_word:
        _ca = captured_article()
        if _ca and getattr(_ca, 'test_word', None) == art_noun_word:
            with mo.capture_stdout() as _buf_a:
                gu.check_noun_test(art_noun_word, _ca, mode='article')
            if _buf_a.getvalue():
                _feedback_a = mo.md(_buf_a.getvalue())
        _view_art = mo.vstack([
            mo.md(f"{t_ui('article_noun_heading', _lang)} ({len(words4test_noun())}/{session_total_n()})"),
            mo.md(f"{t_ui('translation_label', _lang)} **{art_noun_trans}**"),
            art_noun_form,
            _feedback_a,
            mo.hstack([skip_button_n, clear_button_n, submit_button_n], justify="end"),
        ])
    else:
        _view_art = mo.md(t_ui("noun_empty", _lang))
    _view_art
    return


@app.cell(hide_code=True)
def _(mo, noun_msg):
    # Noun message
    mo.md(noun_msg())
    return


@app.cell(hide_code=True)
def _(
    captured_article,
    captured_simple,
    current_noun,
    df_noun,
    gu,
    language_selector,
    random,
    session_total_n,
    set_captured_article,
    set_captured_simple,
    set_current_noun,
    set_noun_msg,
    set_tbl_sel_n,
    set_words4test_noun,
    t_ui,
    words4test_noun,
):
    # Noun pass handler
    _lang = language_selector.value
    _cn = current_noun()
    _cs = captured_simple()
    _ca = captured_article()
    if words4test_noun() and _cn and (_cs or _ca):
        _passed = False
        if _cs and getattr(_cs, 'test_word', None) == _cn['Word']:
            _passed = gu.check_noun_test(_cn['Word'], _cs, mode='simple')
        if not _passed and _ca and getattr(_ca, 'test_word', None) == _cn['Word']:
            _passed = gu.check_noun_test(_cn['Word'], _ca, mode='article')
        if _passed:
            _new = [w for w in words4test_noun() if w['Word'] != _cn['Word']]
            set_words4test_noun(_new)
            if df_noun is not None:
                _rem = {w['Word'] for w in _new}
                set_tbl_sel_n([i for i, w in enumerate(df_noun['Word']) if w in _rem])
            set_noun_msg(t_ui("noun_passed", _lang).format(word=_cn["Word"], remaining=len(_new), total=session_total_n()))
            set_captured_simple(None)
            set_captured_article(None)
            set_current_noun(random.choice(_new) if _new else None)
    return


@app.cell(hide_code=True)
def _(
    art_noun_form,
    art_noun_word,
    gu,
    noun_form,
    noun_word,
    set_captured_article,
    set_captured_simple,
    set_submit_count_n,
    submit_button_n,
    submit_count_n,
):
    # Noun submit handler
    if (submit_button_n.value or 0) > submit_count_n():
        set_submit_count_n(submit_button_n.value)
        if noun_word and noun_form:
            set_captured_simple(gu.make_snapshot(noun_form))
        if art_noun_word and art_noun_form:
            set_captured_article(gu.make_snapshot(art_noun_form))
    return


@app.cell(hide_code=True)
def _(
    current_noun,
    df_noun,
    random,
    set_captured_article,
    set_captured_simple,
    set_current_noun,
    set_skip_count_n,
    set_tbl_sel_n,
    set_words4test_noun,
    skip_button_n,
    skip_count_n,
    words4test_noun,
):
    # Noun skip handler
    if (skip_button_n.value or 0) > skip_count_n():
        set_skip_count_n(skip_button_n.value)
        set_captured_simple(None)
        set_captured_article(None)
        _cn = current_noun()
        _new = [w for w in words4test_noun() if not _cn or w['Word'] != _cn['Word']]
        set_words4test_noun(_new)
        if df_noun is not None:
            _rem = {w['Word'] for w in _new}
            set_tbl_sel_n([i for i, w in enumerate(df_noun['Word']) if w in _rem])
        set_current_noun(random.choice(_new) if _new else None)
    return


@app.cell(hide_code=True)
def _(
    clear_button_n,
    clear_count_n,
    set_captured_article,
    set_captured_simple,
    set_clear_count_n,
):
    # Noun clear handler
    if (clear_button_n.value or 0) > clear_count_n():
        set_clear_count_n(clear_button_n.value)
        set_captured_simple(None)
        set_captured_article(None)
    return


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Test 2 heading
    mo.md(t_ui("test2_heading", language_selector.value))
    return


@app.cell(hide_code=True)
def _(mo):
    # Verb state
    tbl_sel_v, set_tbl_sel_v = mo.state(None)
    session_total_v, set_session_total_v = mo.state(0)
    return session_total_v, set_session_total_v, set_tbl_sel_v, tbl_sel_v


@app.cell(hide_code=True)
def _(mo):
    # Verb file upload
    file_upload_verb = mo.ui.file(label="Load verbs TSV")
    file_upload_verb
    return (file_upload_verb,)


@app.cell(hide_code=True)
def _(file_upload_verb, gu, notebook_dir, os, pd):
    # Load verb data
    if file_upload_verb.value:
        df_verb = gu.load_data(file_upload_verb, [])
    else:
        try:
            df_verb = pd.read_csv(os.path.join(notebook_dir, 'verbs.tsv'), sep='\t')
        except FileNotFoundError:
            df_verb = None
    return (df_verb,)


@app.cell(hide_code=True)
def _(df_verb, language_selector, mo, t_ui, tbl_sel_v):
    # Verb table
    _lang = language_selector.value
    table_verb = mo.ui.table(df_verb, selection="multi", initial_selection=tbl_sel_v()) if df_verb is not None else None
    _display = table_verb if table_verb is not None else mo.md(
        "_verbs.tsv не найден — загрузите файл._" if _lang == "ru" else
        "_Το αρχείο verbs.tsv δεν βρέθηκε — φόρτωσε αρχείο._" if _lang == "el" else
        "_verbs.tsv not found — upload a file to begin._"
    )
    mo.vstack([mo.md(t_ui("select_verbs", _lang)), _display])
    return (table_verb,)


@app.cell(hide_code=True)
def _(gu, language_selector, mo, t_ui):
    # Tense selector
    _lang = language_selector.value
    if _lang == "ru":
        _tense_options = {
            f"{gu.TENSE_LABELS['imperfect']['greek']} (Прошедшее продолженное)": "imperfect",
            f"{gu.TENSE_LABELS['present']['greek']} (Настоящее время)": "present",
        }
        _default = f"{gu.TENSE_LABELS['imperfect']['greek']} (Прошедшее продолженное)"
    elif _lang == "el":
        _tense_options = {
            gu.TENSE_LABELS['imperfect']['greek']: "imperfect",
            gu.TENSE_LABELS['present']['greek']: "present",
        }
        _default = gu.TENSE_LABELS['imperfect']['greek']
    else:
        _tense_options = {
            f"{gu.TENSE_LABELS['imperfect']['greek']} (Past Imperfect)": "imperfect",
            f"{gu.TENSE_LABELS['present']['greek']} (Present)": "present",
        }
        _default = f"{gu.TENSE_LABELS['imperfect']['greek']} (Past Imperfect)"
    tense_selector = mo.ui.dropdown(
        options=_tense_options,
        value=_default,
        label=t_ui("tense_label", _lang),
    )
    tense_selector
    return (tense_selector,)


@app.cell(hide_code=True)
def _(gu, mo, session_total_v, set_session_total_v, table_verb):
    # Verb words
    words_verb = gu.get_words(table_verb)
    words4test_verb, set_words4test_verb = mo.state(words_verb.copy() if words_verb else [])
    if words_verb and len(words_verb) > session_total_v():
        set_session_total_v(len(words_verb))
    elif not words_verb:
        set_session_total_v(0)
    verb_msg, set_verb_msg = mo.state("")
    captured_verb, set_captured_verb = mo.state(None)
    _clk = lambda v: (v or 0) + 1
    skip_button_v = mo.ui.button(label="Skip", on_click=_clk)
    clear_button_v = mo.ui.button(label="Clear", on_click=_clk)
    skip_count_v, set_skip_count_v = mo.state(0)
    clear_count_v, set_clear_count_v = mo.state(0)
    submit_count_v, set_submit_count_v = mo.state(0)
    return (
        captured_verb,
        clear_button_v,
        clear_count_v,
        set_captured_verb,
        set_clear_count_v,
        set_skip_count_v,
        set_submit_count_v,
        set_verb_msg,
        set_words4test_verb,
        skip_button_v,
        skip_count_v,
        submit_count_v,
        verb_msg,
        words4test_verb,
        words_verb,
    )


@app.cell(hide_code=True)
def _(clear_count_v, gu, random, tense_selector, words4test_verb, words_verb):
    # Verb form
    clear_count_v()
    cv_verb = random.choice(words4test_verb()) if words4test_verb() else None
    _tense_key = tense_selector.value
    _ui_label = gu.TENSE_LABELS[_tense_key]['greek'] if _tense_key else "—"
    verb_fields, _ = gu.create_verb_test_ui(_ui_label, words_verb, words4test_verb(), cv_verb)
    return cv_verb, verb_fields


@app.cell(hide_code=True)
def _(captured_verb, mo, set_submit_count_v, tense_selector, verb_fields):
    # Submit button V
    _values = verb_fields.value if verb_fields is not None else []
    _snap = captured_verb()
    _has_input = bool(_values and any(v.strip() for v in _values))
    _matches_snap = (
        _snap is not None
        and getattr(_snap, 'tense', None) == tense_selector.value
        and [v.strip() for v in _values] == [v.strip() for v in (_snap.value or [])]
    )
    _dirty = _has_input and not _matches_snap
    _clk = lambda v: (v or 0) + 1
    submit_button_v = mo.ui.button(label="Submit", on_click=_clk, kind="warn" if _dirty else "neutral")
    set_submit_count_v(0)
    return (submit_button_v,)


@app.cell(hide_code=True)
def _(
    captured_verb,
    clear_button_v,
    cv_verb,
    gu,
    language_selector,
    mo,
    session_total_v,
    skip_button_v,
    submit_button_v,
    t_ui,
    tense_selector,
    verb_fields,
    verb_msg,
    words4test_verb,
):
    # Verb display
    _lang = language_selector.value
    _TENSE_LABELS = {k: gu.TENSE_LABELS[k]['greek'] for k in gu.TENSE_LABELS}
    if not words4test_verb():
        _view_verb = mo.md(t_ui("verb_empty", _lang))
    elif not tense_selector.value:
        _view_verb = mo.md(t_ui("verb_no_tense", _lang))
    else:
        _feedback_v = mo.md("")
        _c = captured_verb()
        if cv_verb and _c and getattr(_c, 'verb_word', None) == cv_verb['Word'] and getattr(_c, 'tense', None) == tense_selector.value:
            _, _msg = gu.check_verb_test(cv_verb['Word'], _c, tense_selector.value)
            _feedback_v = mo.md(_msg)
        _label = _TENSE_LABELS.get(tense_selector.value, tense_selector.value)
        _rem = len(words4test_verb())
        _items = [mo.md(f"{t_ui('verb_heading', _lang)} — {_label} ({_rem}/{session_total_v()})")]
        if verb_msg():
            _items.append(mo.md(verb_msg()))
        _items += [
            mo.md(f"{t_ui('translation_label', _lang)} **{cv_verb['Translation']}**") if cv_verb else mo.md(""),
            verb_fields,
            mo.hstack([skip_button_v, clear_button_v, submit_button_v], justify="end"),
            _feedback_v,
        ]
        _view_verb = mo.vstack(_items)
    _view_verb
    return


@app.cell(hide_code=True)
def _(
    captured_verb,
    cv_verb,
    df_verb,
    gu,
    language_selector,
    session_total_v,
    set_captured_verb,
    set_tbl_sel_v,
    set_verb_msg,
    set_words4test_verb,
    t_ui,
    tense_selector,
    words4test_verb,
):
    # Verb pass handler
    _lang = language_selector.value
    _tense_key = tense_selector.value
    _c = captured_verb()
    if cv_verb and _tense_key and _c and getattr(_c, 'verb_word', None) == cv_verb['Word'] and getattr(_c, 'tense', None) == _tense_key:
        _ok, _ = gu.check_verb_test(cv_verb['Word'], _c, _tense_key)
        if _ok:
            _new = [w for w in words4test_verb() if w['Word'] != cv_verb['Word']]
            set_words4test_verb(_new)
            if df_verb is not None:
                _rem = {w['Word'] for w in _new}
                set_tbl_sel_v([i for i, w in enumerate(df_verb['Word']) if w in _rem])
            set_verb_msg(t_ui("verb_passed", _lang).format(word=cv_verb["Word"], trans=cv_verb["Translation"], remaining=len(_new), total=session_total_v()))
            set_captured_verb(None)
    return


@app.cell(hide_code=True)
def _(
    cv_verb,
    gu,
    set_captured_verb,
    set_submit_count_v,
    submit_button_v,
    submit_count_v,
    tense_selector,
    verb_fields,
):
    # Verb submit handler
    if (submit_button_v.value or 0) > submit_count_v():
        set_submit_count_v(submit_button_v.value)
        if cv_verb and verb_fields:
            set_captured_verb(gu.make_snapshot(verb_fields, verb_word=cv_verb['Word'], tense=tense_selector.value))
    return


@app.cell(hide_code=True)
def _(
    cv_verb,
    df_verb,
    set_captured_verb,
    set_skip_count_v,
    set_tbl_sel_v,
    set_words4test_verb,
    skip_button_v,
    skip_count_v,
    words4test_verb,
):
    # Verb skip handler
    if (skip_button_v.value or 0) > skip_count_v():
        set_skip_count_v(skip_button_v.value)
        set_captured_verb(None)
        if words4test_verb():
            _new = [w for w in words4test_verb() if not cv_verb or w['Word'] != cv_verb['Word']]
            set_words4test_verb(_new)
            if df_verb is not None:
                _rem = {w['Word'] for w in _new}
                set_tbl_sel_v([i for i, w in enumerate(df_verb['Word']) if w in _rem])
    return


@app.cell(hide_code=True)
def _(clear_button_v, clear_count_v, set_captured_verb, set_clear_count_v):
    # Verb clear handler
    if (clear_button_v.value or 0) > clear_count_v():
        set_clear_count_v(clear_button_v.value)
        set_captured_verb(None)
    return


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Test 3 heading
    mo.md(t_ui("test3_heading", language_selector.value))
    return


@app.cell(hide_code=True)
def _(mo):
    # Adj state
    tbl_sel_a, set_tbl_sel_a = mo.state(None)
    session_total_a, set_session_total_a = mo.state(0)
    return session_total_a, set_session_total_a, set_tbl_sel_a, tbl_sel_a


@app.cell(hide_code=True)
def _(mo):
    # Adj file upload
    file_upload_adj = mo.ui.file(label="Load adjectives TSV")
    file_upload_adj
    return (file_upload_adj,)


@app.cell(hide_code=True)
def _(file_upload_adj, gu, notebook_dir, os, pd):
    # Load adj data
    if file_upload_adj.value:
        df_adj = gu.load_data(file_upload_adj, [])
    else:
        try:
            df_adj = pd.read_csv(os.path.join(notebook_dir, 'adjectives.tsv'), sep='\t')
        except FileNotFoundError:
            df_adj = None
    return (df_adj,)


@app.cell(hide_code=True)
def _(df_adj, language_selector, mo, t_ui, tbl_sel_a):
    # Adj table
    _lang = language_selector.value
    table_adj = mo.ui.table(df_adj, selection="multi", initial_selection=tbl_sel_a()) if df_adj is not None else None
    _display = table_adj if table_adj is not None else mo.md(
        "_adjectives.tsv не найден — загрузите файл._" if _lang == "ru" else
        "_Το αρχείο adjectives.tsv δεν βρέθηκε — φόρτωσε αρχείο._" if _lang == "el" else
        "_adjectives.tsv not found — upload a file to begin._"
    )
    mo.vstack([mo.md(t_ui("select_adjs", _lang)), _display])
    return (table_adj,)


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Mode selector
    _lang = language_selector.value
    if _lang == "ru":
        _opts = {"Простой: 3 рода × 2 числа (6 полей)": "simple", "Сложный: все роды, числа и падежи (18 полей)": "complex"}
        _default_mode = "Простой: 3 рода × 2 числа (6 полей)"
    elif _lang == "el":
        _opts = {"Απλό: 3 γένη × 2 αριθμοί (6 πεδία)": "simple", "Σύνθετο: όλα τα γένη, αριθμοί και πτώσεις (18 πεδία)": "complex"}
        _default_mode = "Απλό: 3 γένη × 2 αριθμοί (6 πεδία)"
    else:
        _opts = {"Simple: 3 genders × 2 numbers (6 fields)": "simple", "Complex: all genders, numbers, and cases (18 fields)": "complex"}
        _default_mode = "Simple: 3 genders × 2 numbers (6 fields)"
    mode_selector = mo.ui.radio(options=_opts, value=_default_mode, label=t_ui("mode_label", _lang))
    mo.md(f"{mode_selector}")
    return (mode_selector,)


@app.cell(hide_code=True)
def _(gu, mo, random, session_total_a, set_session_total_a, table_adj):
    # Adj words
    words_adj = gu.get_words(table_adj)
    words4test_adj, set_words4test_adj = mo.state(words_adj.copy() if words_adj else [])
    if words_adj and len(words_adj) > session_total_a():
        set_session_total_a(len(words_adj))
    elif not words_adj:
        set_session_total_a(0)
    adj_last_passed_mesg, set_adj_last_passed_mesg = mo.state("")
    adj_cv, set_adj_cv = mo.state(None)
    captured_adj, set_captured_adj = mo.state(None)
    _clk = lambda v: (v or 0) + 1
    skip_button_a = mo.ui.button(label="Skip", on_click=_clk)
    clear_button_a = mo.ui.button(label="Clear", on_click=_clk)
    skip_count_a, set_skip_count_a = mo.state(0)
    clear_count_a, set_clear_count_a = mo.state(0)
    submit_count_a, set_submit_count_a = mo.state(0)
    if words_adj and adj_cv() is None:
        set_adj_cv(random.choice(words_adj))
    return (
        adj_cv,
        adj_last_passed_mesg,
        captured_adj,
        clear_button_a,
        clear_count_a,
        set_adj_cv,
        set_adj_last_passed_mesg,
        set_captured_adj,
        set_clear_count_a,
        set_skip_count_a,
        set_submit_count_a,
        set_words4test_adj,
        skip_button_a,
        skip_count_a,
        submit_count_a,
        words4test_adj,
    )


@app.cell(hide_code=True)
def _(adj_cv, clear_count_a, gu, mode_selector):
    # Adj form
    clear_count_a()
    _acv = adj_cv()
    _mode = mode_selector.value
    adj_form, _ = gu.create_adjective_test_ui([] if not _acv else [_acv], [], _acv, mode=_mode)
    return (adj_form,)


@app.cell(hide_code=True)
def _(adj_form, captured_adj, mo, set_submit_count_a):
    # Submit button A
    _values = adj_form.value if adj_form else []
    _snap = captured_adj()
    _has_input = bool(_values and any(v.strip() for v in _values))
    _matches_snap = _snap is not None and [v.strip() for v in _values] == [v.strip() for v in (_snap.value or [])]
    _dirty = _has_input and not _matches_snap
    _clk = lambda v: (v or 0) + 1
    submit_button_a = mo.ui.button(label="Submit", on_click=_clk, kind="warn" if _dirty else "neutral")
    set_submit_count_a(0)
    return (submit_button_a,)


@app.cell(hide_code=True)
def _(
    adj_cv,
    adj_form,
    captured_adj,
    clear_button_a,
    gu,
    language_selector,
    mo,
    mode_selector,
    session_total_a,
    skip_button_a,
    submit_button_a,
    t_ui,
    words4test_adj,
):
    # Adj display
    _lang = language_selector.value
    _adj = adj_cv()
    _mode = mode_selector.value
    if words4test_adj() and _adj:
        _feedback_a = mo.md("")
        _c = captured_adj()
        if _c and getattr(_c, 'adj_word', None) == _adj['Word']:
            _, _msg = gu.check_adjective_test(_adj['Word'], _c, mode=_mode)
            if _msg:
                _feedback_a = mo.md(_msg)
        _view_adj = mo.vstack([
            mo.md(f"{t_ui('adj_heading', _lang)} ({len(words4test_adj())}/{session_total_a()})"),
            mo.md(f"{t_ui('translation_label', _lang)} **{_adj['Translation']}**"),
            adj_form,
            _feedback_a,
            mo.hstack([skip_button_a, clear_button_a, submit_button_a], justify="end"),
        ])
    else:
        _view_adj = mo.md(t_ui("adj_empty", _lang))
    _view_adj
    return


@app.cell(hide_code=True)
def _(adj_last_passed_mesg, mo):
    # Adj message
    mo.md(adj_last_passed_mesg())
    return


@app.cell(hide_code=True)
def _(
    adj_cv,
    captured_adj,
    df_adj,
    gu,
    language_selector,
    random,
    session_total_a,
    set_adj_cv,
    set_adj_last_passed_mesg,
    set_captured_adj,
    set_tbl_sel_a,
    set_words4test_adj,
    t_ui,
    words4test_adj,
):
    # Adj pass handler
    _lang = language_selector.value
    _adj = adj_cv()
    _c = captured_adj()
    if words4test_adj() and _adj and _c and getattr(_c, 'adj_word', None) == _adj['Word']:
        adj_ok, _ = gu.check_adjective_test(_adj['Word'], _c)
        if adj_ok:
            _new = [w for w in words4test_adj() if w['Word'] != _adj['Word']]
            set_words4test_adj(_new)
            if df_adj is not None:
                _rem = {w['Word'] for w in _new}
                set_tbl_sel_a([i for i, w in enumerate(df_adj['Word']) if w in _rem])
            set_adj_last_passed_mesg(t_ui("adj_passed", _lang).format(word=_adj["Word"], trans=_adj["Translation"], remaining=len(_new), total=session_total_a()))
            set_adj_cv(random.choice(_new) if _new else None)
            set_captured_adj(None)
    return


@app.cell(hide_code=True)
def _(
    adj_cv,
    adj_form,
    gu,
    set_captured_adj,
    set_submit_count_a,
    submit_button_a,
    submit_count_a,
):
    # Adj submit handler
    if (submit_button_a.value or 0) > submit_count_a():
        set_submit_count_a(submit_button_a.value)
        _acv = adj_cv()
        if _acv and adj_form:
            set_captured_adj(gu.make_snapshot(adj_form))
    return


@app.cell(hide_code=True)
def _(
    adj_cv,
    df_adj,
    random,
    set_adj_cv,
    set_captured_adj,
    set_skip_count_a,
    set_tbl_sel_a,
    set_words4test_adj,
    skip_button_a,
    skip_count_a,
    words4test_adj,
):
    # Adj skip handler
    if (skip_button_a.value or 0) > skip_count_a():
        set_skip_count_a(skip_button_a.value)
        set_captured_adj(None)
        _acv = adj_cv()
        _new = [w for w in words4test_adj() if not _acv or w['Word'] != _acv['Word']]
        set_words4test_adj(_new)
        if df_adj is not None:
            _rem = {w['Word'] for w in _new}
            set_tbl_sel_a([i for i, w in enumerate(df_adj['Word']) if w in _rem])
        set_adj_cv(random.choice(_new) if _new else None)
    return


@app.cell(hide_code=True)
def _(clear_button_a, clear_count_a, set_captured_adj, set_clear_count_a):
    # Adj clear handler
    if (clear_button_a.value or 0) > clear_count_a():
        set_clear_count_a(clear_button_a.value)
        set_captured_adj(None)
    return


@app.cell(hide_code=True)
def _(mo):
    # Language selector
    language_selector = mo.ui.dropdown(
        options={"English": "en", "Русский": "ru", "Ελληνικά": "el"},
        value="English",
        label="🌐",
    )
    mo.Html(f"""
    <div style="position: fixed; top: 60px; right: 10px; z-index: 1000; background: white; padding: 8px 12px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);">
        {language_selector}
    </div>
    """)
    return (language_selector,)


@app.cell(hide_code=True)
def _():
    # UI strings
    _UI_STRINGS = {
        "en": {
            "test1_heading": "## Test 1: Nouns",
            "test2_heading": "## Test 2: Verbs",
            "test3_heading": "## Test 3: Adjectives",
            "select_nouns": "### Select nouns to practice",
            "select_verbs": "### Select verbs to practice",
            "select_adjs": "### Select adjectives to practice",
            "translation_label": "Translation:",
            "simple_noun_heading": "**Simple noun test**",
            "article_noun_heading": "**Noun test with articles**",
            "verb_heading": "**Verb test**",
            "adj_heading": "**Adjective test**",
            "noun_empty": "_Select nouns from the table above to begin._",
            "verb_empty": "_Select verbs from the table above to begin._",
            "verb_no_tense": "_Select a tense above._",
            "adj_empty": "_Select adjectives from the table above to begin._",
            "tense_label": "Select tense:",
            "mode_label": "Test mode:",
            "noun_passed": '<span style="color:green;">Test for <b>"{word}"</b> passed.\n\n{remaining} words remaining out of {total}.</span>',
            "verb_passed": '<span style="color:green;">Test for <b>"{word} — {trans}"</b> passed.\n\n{remaining} words remaining out of {total}.</span>',
            "adj_passed": '<span style="color:green;">Test for <b>"{word} — {trans}"</b> passed.\n\n{remaining} words remaining out of {total}.</span>',
        },
        "ru": {
            "test1_heading": "## Тест 1: Существительные",
            "test2_heading": "## Тест 2: Глаголы",
            "test3_heading": "## Тест 3: Прилагательные",
            "select_nouns": "### Выберите существительные для практики",
            "select_verbs": "### Выберите глаголы для практики",
            "select_adjs": "### Выберите прилагательные для практики",
            "translation_label": "Перевод:",
            "simple_noun_heading": "**Простой тест по существительным**",
            "article_noun_heading": "**Тест по существительным с артиклями**",
            "verb_heading": "**Тест по глаголам**",
            "adj_heading": "**Тест по прилагательным**",
            "noun_empty": "_Выберите существительные из таблицы выше, чтобы начать._",
            "verb_empty": "_Выберите глаголы из таблицы выше, чтобы начать._",
            "verb_no_tense": "_Выберите время выше._",
            "adj_empty": "_Выберите прилагательные из таблицы выше, чтобы начать._",
            "tense_label": "Выбрать время:",
            "mode_label": "Режим теста:",
            "noun_passed": '<span style="color:green;">Тест для <b>"{word}"</b> пройден.\n\n{remaining} слов осталось из {total}.</span>',
            "verb_passed": '<span style="color:green;">Тест для <b>"{word} — {trans}"</b> пройден.\n\n{remaining} слов осталось из {total}.</span>',
            "adj_passed": '<span style="color:green;">Тест для <b>"{word} — {trans}"</b> пройден.\n\n{remaining} слов осталось из {total}.</span>',
        },
        "el": {
            "test1_heading": "## Τεστ 1: Ουσιαστικά",
            "test2_heading": "## Τεστ 2: Ρήματα",
            "test3_heading": "## Τεστ 3: Επίθετα",
            "select_nouns": "### Επιλογή ουσιαστικών για εξάσκηση",
            "select_verbs": "### Επιλογή ρημάτων για εξάσκηση",
            "select_adjs": "### Επιλογή επιθέτων για εξάσκηση",
            "translation_label": "Μετάφραση:",
            "simple_noun_heading": "**Απλό τεστ ουσιαστικών**",
            "article_noun_heading": "**Τεστ ουσιαστικών με άρθρα**",
            "verb_heading": "**Τεστ ρημάτων**",
            "adj_heading": "**Τεστ επιθέτων**",
            "noun_empty": "_Επιλέξτε ουσιαστικά από τον παραπάνω πίνακα για να ξεκινήσετε._",
            "verb_empty": "_Επιλέξτε ρήματα από τον παραπάνω πίνακα για να ξεκινήσετε._",
            "verb_no_tense": "_Επιλέξτε χρόνο παραπάνω._",
            "adj_empty": "_Επιλέξτε επίθετα από τον παραπάνω πίνακα για να ξεκινήσετε._",
            "tense_label": "Επιλογή χρόνου:",
            "mode_label": "Επιλογή τρόπου:",
            "noun_passed": '<span style="color:green;">Τεστ για <b>"{word}"</b> ολοκληρώθηκε.\n\n{remaining} λέξεις απομένουν από {total}.</span>',
            "verb_passed": '<span style="color:green;">Τεστ για <b>"{word} — {trans}"</b> ολοκληρώθηκε.\n\n{remaining} λέξεις απομένουν από {total}.</span>',
            "adj_passed": '<span style="color:green;">Τεστ για <b>"{word} — {trans}"</b> ολοκληρώθηκε.\n\n{remaining} λέξεις απομένουν από {total}.</span>',
        },
    }

    def t_ui(key, lang=None):
        _lang = lang if lang else "en"
        return _UI_STRINGS.get(_lang, _UI_STRINGS["en"]).get(key, _UI_STRINGS["en"].get(key, key))

    return (t_ui,)


@app.cell(hide_code=True)
def _():
    # Imports
    import os
    import random
    import pandas as pd
    import marimo as mo
    from modern_greek_eee import greek_utils as gu
    notebook_dir = os.path.dirname(os.path.abspath(__file__))
    return gu, mo, notebook_dir, os, pd, random


if __name__ == "__main__":
    app.run()
