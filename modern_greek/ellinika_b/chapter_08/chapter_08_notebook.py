# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "eee-project @ git+https://codeberg.org/EEE-project/eee-project.git",
#     "marimo>=0.23.14",
#     "modern-greek-backend-eee @ git+https://codeberg.org/EEE-project/modern-greek-backend-eee.git",
#     "pandas",
# ]
#
# [tool.uv.sources]
# eee-project = { git = "https://codeberg.org/EEE-project/eee-project.git" }
# modern-greek-backend-eee = { git = "https://codeberg.org/EEE-project/modern-greek-backend-eee.git" }
# ///

import marimo

__generated_with = "0.23.14"
app = marimo.App(width="medium", html_head_file="head.html")


@app.cell(hide_code=True)
def _(language_selector, mo):
    from eee_project import ConfigStore, eee_topbar
    _ROOT = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main"
    _cfg = ConfigStore.from_file_or_url(
        __file__,
        f"{_ROOT}/modern_greek/ellinika_b/index.tsv",
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
    _badge = "[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_ALxQFbGS9Jq8phLPQbGrru)"
    if _lang == "ru":
        _out = mo.md(f"""
    # «Έχει ο καιρός γυρίσματα» 🌤️
    ## Глава 8 — Погода переменчива · B1 {_badge}

    **Грамматика:** Απλός Μέλλοντας · Условные предложения (Αν…) · Прилагательные на -ης/-α/-ικο
    **Тесты:** Существительные · Глаголы · Прилагательные
    """)
    elif _lang == "el":
        _out = mo.md(f"""
    # «Έχει ο καιρός γυρίσματα» 🌤️
    ## Ενότητα 8 — Ο καιρός είναι άστατος · B1 {_badge}

    **Γραμματική:** Απλός Μέλλοντας · Υποθετικές προτάσεις (Αν…) · Επίθετα σε -ης/-α/-ικο
    **Τεστ:** Ουσιαστικά · Ρήματα · Επίθετα
    """)
    else:
        _out = mo.md(f"""
    # «Έχει ο καιρός γυρίσματα» 🌤️
    ## Unit 8 — Weather is Changeable · B1 {_badge}

    **Grammar:** Απλός Μέλλοντας · Conditional sentences (Αν…) · Adjectives in -ης/-α/-ικο
    **Tests:** Nouns · Verbs · Adjectives
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Vocabulary: Λέξεις, λέξεις
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Словарь

    | Греческий | Русский |
    |:---------|:--------|
    | δελτίο καιρού (το) | прогноз погоды |
    | η θερμοκρασία πέφτει / ανεβαίνει | температура падает / поднимается |
    | κακοκαιρία (η) | плохая погода |
    | οργανώνω | организовывать |
    | πεζοπορία (η) | пеший туризм / поход |
    | περπάτημα (το) | ходьба / прогулка |
    | φύση (η) | природа |
    | λιακάδα (η) | солнечная погода / просветление |
    | ο καιρός χειροτερεύει | погода ухудшается |
    | παραπονιάρης, -α, -ικο | нытик, склонный к жалобам |
    | πεισματάρης, -α, -ικο | упрямый |
    | τεμπέλης, -α, -ικο | ленивый |
    | υπομονή (η) | терпение |
    | υψηλή (για την εποχή) θερμοκρασία | высокая (для сезона) температура |
    | ψιχαλίζει — ψιχάλα (η) | моросит — морось |
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Λεξιλόγιο

    | Ελληνικά | Αγγλικά |
    |:---------|:--------|
    | δελτίο καιρού (το) | weather forecast |
    | η θερμοκρασία πέφτει / ανεβαίνει | the temperature drops / rises |
    | κακοκαιρία (η) | bad weather |
    | οργανώνω | to organize |
    | πεζοπορία (η) | hiking |
    | περπάτημα (το) | walking |
    | φύση (η) | nature |
    | λιακάδα (η) | sunny spell / sunshine |
    | ο καιρός χειροτερεύει | the weather gets worse |
    | παραπονιάρης, -α, -ικο | whiny, complaining |
    | πεισματάρης, -α, -ικο | stubborn |
    | τεμπέλης, -α, -ικο | lazy |
    | υπομονή (η) | patience |
    | υψηλή (για την εποχή) θερμοκρασία | high (for the season) temperature |
    | ψιχαλίζει — ψιχάλα (η) | it drizzles — drizzle |
    """)
    else:
        _out = mo.md("""
    ## Vocabulary

    | Greek | English |
    |:------|:--------|
    | δελτίο καιρού (το) | weather forecast |
    | η θερμοκρασία πέφτει / ανεβαίνει | the temperature drops / rises |
    | κακοκαιρία (η) | bad weather |
    | οργανώνω | to organize |
    | πεζοπορία (η) | hiking |
    | περπάτημα (το) | walking |
    | φύση (η) | nature |
    | λιακάδα (η) | sunny spell / sunshine |
    | ο καιρός χειροτερεύει | the weather gets worse |
    | παραπονιάρης, -α, -ικο | whiny, complaining |
    | πεισματάρης, -α, -ικο | stubborn |
    | τεμπέλης, -α, -ικο | lazy |
    | υπομονή (η) | patience |
    | υψηλή (για την εποχή) θερμοκρασία | high (for the season) temperature |
    | ψιχαλίζει — ψιχάλα (η) | it drizzles — drizzle |
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Phrases: Πώς το λένε;
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Полезные фразы

    | Греческий | Русский |
    |:---------|:--------|
    | Έχεις κανένα σχέδιο; | У тебя есть какие-то планы? |
    | Πώς σου ΄ρθε; | Как тебе пришло в голову? |
    | Θα είμαστε καλή παρέα. | Мы будем хорошей компанией. |
    | Έλα τώρα... | Ну ладно... |
    | Καλό θα μας κάνει το πρωινό περπάτημα στη φύση. | Утренняя прогулка на природе пойдёт нам на пользу. |
    | Δεν είναι κακή ιδέα. | Неплохая идея. |
    | Νιώθω χάλια. | Я чувствую себя ужасно. |
    | Άντε, ρε! | Ну давай! / Да ладно! |
    | Η θερμοκρασία θα πέσει πολύ. | Температура упадёт сильно. |
    | Ελπίζω ο καιρός να μας κάνει τη χάρη. | Надеюсь, погода нас не подведёт. |
    | Πώς κάνεις έτσι; | Как ты можешь так делать? |
    | Τι παραπονιάρης που είσαι... | Ну и нытик же ты... |
    | Ελάτε, παιδιά! | Давайте, ребята! |
    | Μη μαλώνετε! | Не ругайтесь! |
    | Επιτέλους! | Наконец-то! |
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Χρήσιμες εκφράσεις

    | Ελληνικά | Αγγλικά |
    |:---------|:--------|
    | Έχεις κανένα σχέδιο; | Do you have any plans? |
    | Πώς σου ΄ρθε; | How did you come up with this? |
    | Θα είμαστε καλή παρέα. | We'll be good company. |
    | Έλα τώρα... | Come on now... |
    | Καλό θα μας κάνει το πρωινό περπάτημα στη φύση. | The morning walk in nature will do us good. |
    | Δεν είναι κακή ιδέα. | It's not a bad idea. |
    | Νιώθω χάλια. | I feel awful. |
    | Άντε, ρε! | Come on! / Give me a break! |
    | Η θερμοκρασία θα πέσει πολύ. | The temperature will drop a lot. |
    | Ελπίζω ο καιρός να μας κάνει τη χάρη. | I hope the weather will do us the favor. |
    | Πώς κάνεις έτσι; | How can you do this? |
    | Τι παραπονιάρης που είσαι... | What a whiner you are... |
    | Ελάτε, παιδιά! | Come on, kids! |
    | Μη μαλώνετε! | Don't argue! |
    | Επιτέλους! | Finally! / At last! |
    """)
    else:
        _out = mo.md("""
    ## Useful Phrases

    | Greek | English |
    |:------|:--------|
    | Έχεις κανένα σχέδιο; | Do you have any plans? |
    | Πώς σου ΄ρθε; | How did you come up with this? |
    | Θα είμαστε καλή παρέα. | We'll be good company. |
    | Έλα τώρα... | Come on now... |
    | Καλό θα μας κάνει το πρωινό περπάτημα στη φύση. | The morning walk in nature will do us good. |
    | Δεν είναι κακή ιδέα. | It's not a bad idea. |
    | Νιώθω χάλια. | I feel awful. |
    | Άντε, ρε! | Come on! / Give me a break! |
    | Η θερμοκρασία θα πέσει πολύ. | The temperature will drop a lot. |
    | Ελπίζω ο καιρός να μας κάνει τη χάρη. | I hope the weather will do us the favor. |
    | Πώς κάνεις έτσι; | How can you do this? |
    | Τι παραπονιάρης που είσαι... | What a whiner you are... |
    | Ελάτε, παιδιά! | Come on, kids! |
    | Μη μαλώνετε! | Don't argue! |
    | Επιτέλους! | Finally! / At last! |
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Weather forecast
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Прогноз погоды

    ### Стр. 123 — как говорить о погоде

    | Конструкция | Варианты |
    |:------------|:---------|
    | **Θα κάνει / Θα έχει** … | ζέστη (жара) · καύσωνα (зной) · κρύο (холод) · ψύχρα (прохлада) · δροσιά (свежесть) · παγωνιά (мороз) · καλό/ωραίο καιρό · κακό/άσχημο καιρό · κακοκαιρία · παλιόκαιρο |
    | **Θα έχει** … | ήλιο · λιακάδα · αέρα · άνεμο · συννεφιά · σύννεφα · βροχή · καταιγίδα · χιόνι · χιονόνερο · χαλάζι · ομίχλη · υγρασία |
    | **Ο καιρός θα είναι** … | ήπιος · καλός/κακός · ωραίος/άσχημος · βροχερός |
    | **Ο καιρός** … | θα φτιάξει / θα χαλάσει |
    | **Η θερμοκρασία** … | θα ανέβει / θα πέσει / θα φτάσει τους 18°C |

    **Τι καιρό κάνει τώρα εκεί;** Βρέχει. Ψιλοβρέχει. Ψιχαλίζει. Χιονίζει. Ρίχνει χιόνι. Ρίχνει χαλάζι. Φυσάει. Έχει αστραπές και βροντές/μπουμπουνητά. Αστράφτει. Βροντάει/Μπουμπουνίζει.

    **Τι καιρό είχατε χτες;** Έβρεχε συνέχεια. Ο δρόμος μπροστά στο σπίτι έγινε ποτάμι και η αποθήκη μας πλημμύρισε. Όλη τη νύχτα δεν μπορέσαμε να ησυχάσουμε από τις αστραπές και τις βροντές. Ένας κεραυνός έπεσε σε ένα δέντρο δίπλα στο σπίτι μας και το έκαψε.

    ### Стр. 124 — официальный прогноз погоды

    | Конструкция | Варианты |
    |:------------|:---------|
    | **Ο καιρός αύριο θα είναι** … | ήπιος (мягкий) · αίθριος (ясный) · άστατος (переменный) |
    | **Θα έχει** … | υψηλές/χαμηλές θερμοκρασίες · ηλιοφάνεια · ήλιο με αραιή συννεφιά · νεφώσεις (облачно) · βροχές και καταιγίδες · δυνατούς ανέμους |
    | **Θα έχουμε** … | άνοδο / πτώση της θερμοκρασίας |

    **Направления ветра:** βοριάς (С) · νοτιάς (Ю) · ανατολικός (В) · δυτικός (З)
    **Бофорт:** ανέμους 5 μποφόρ · ισχυρούς βόρειους ανέμους έντασης 9 μποφόρ
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Δελτίο καιρού

    ### Σ. 123 — πώς μιλάμε για τον καιρό

    | Δομή | Επιλογές |
    |:-----|:---------|
    | **Θα κάνει / Θα έχει** … | ζέστη · καύσωνα · κρύο · ψύχρα · δροσιά · παγωνιά · καλό/ωραίο καιρό · κακό/άσχημο καιρό · κακοκαιρία · παλιόκαιρο |
    | **Θα έχει** … | ήλιο · λιακάδα · αέρα · άνεμο · συννεφιά · σύννεφα · βροχή · καταιγίδα · χιόνι · χιονόνερο · χαλάζι · ομίχλη · υγρασία |
    | **Ο καιρός θα είναι** … | ήπιος · καλός/κακός · ωραίος/άσχημος · βροχερός |
    | **Ο καιρός** … | θα φτιάξει / θα χαλάσει |
    | **Η θερμοκρασία** … | θα ανέβει / θα πέσει / θα φτάσει τους 18°C |

    **Τι καιρό κάνει τώρα εκεί;** Βρέχει. Ψιλοβρέχει. Ψιχαλίζει. Χιονίζει. Ρίχνει χιόνι. Ρίχνει χαλάζι. Φυσάει. Έχει αστραπές και βροντές/μπουμπουνητά. Αστράφτει. Βροντάει/Μπουμπουνίζει.

    **Τι καιρό είχατε χτες;** Έβρεχε συνέχεια. Ο δρόμος μπροστά στο σπίτι έγινε ποτάμι και η αποθήκη μας πλημμύρισε. Όλη τη νύχτα δεν μπορέσαμε να ησυχάσουμε από τις αστραπές και τις βροντές. Ένας κεραυνός έπεσε σε ένα δέντρο δίπλα στο σπίτι μας και το έκαψε.

    ### Σ. 124 — επίσημο δελτίο καιρού

    | Δομή | Επιλογές |
    |:-----|:---------|
    | **Ο καιρός αύριο θα είναι** … | ήπιος · αίθριος · άστατος |
    | **Θα έχει** … | υψηλές/χαμηλές θερμοκρασίες · ηλιοφάνεια · ήλιο με αραιή συννεφιά · νεφώσεις · βροχές και καταιγίδες · δυνατούς ανέμους |
    | **Θα έχουμε** … | άνοδο / πτώση της θερμοκρασίας |

    **Κατευθύνσεις ανέμου:** βοριάς (Β) · νοτιάς (Ν) · ανατολικός (Α) · δυτικός (Δ)
    **Μποφόρ:** ανέμους 5 μποφόρ · ισχυρούς βόρειους ανέμους έντασης 9 μποφόρ
    """)
    else:
        _out = mo.md("""
    ## Weather Forecast

    ### p. 123 — talking about the weather

    | Pattern | Options |
    |:--------|:--------|
    | **Θα κάνει / Θα έχει** … | ζέστη (heat) · καύσωνα (heatwave) · κρύο (cold) · ψύχρα (chill) · δροσιά (coolness) · παγωνιά (frost) · καλό/ωραίο καιρό · κακό/άσχημο καιρό · κακοκαιρία · παλιόκαιρο |
    | **Θα έχει** … | ήλιο · λιακάδα · αέρα · άνεμο · συννεφιά · σύννεφα · βροχή · καταιγίδα · χιόνι · χιονόνερο · χαλάζι · ομίχλη · υγρασία |
    | **Ο καιρός θα είναι** … | ήπιος · καλός/κακός · ωραίος/άσχημος · βροχερός |
    | **Ο καιρός** … | θα φτιάξει / θα χαλάσει |
    | **Η θερμοκρασία** … | θα ανέβει / θα πέσει / θα φτάσει τους 18°C |

    **What's the weather like there right now?** Βρέχει (raining). Ψιλοβρέχει (light rain). Ψιχαλίζει (drizzling). Χιονίζει (snowing). Ρίχνει χιόνι. Ρίχνει χαλάζι (hailing). Φυσάει (windy). Έχει αστραπές και βροντές/μπουμπουνητά (lightning and thunder). Αστράφτει. Βροντάει/Μπουμπουνίζει.

    **What was the weather like yesterday?** Έβρεχε συνέχεια. Ο δρόμος μπροστά στο σπίτι έγινε ποτάμι και η αποθήκη μας πλημμύρισε. Όλη τη νύχτα δεν μπορέσαμε να ησυχάσουμε από τις αστραπές και τις βροντές. Ένας κεραυνός έπεσε σε ένα δέντρο δίπλα στο σπίτι μας και το έκαψε. — _It kept raining nonstop. The street in front of our house became a river and our storage room flooded. All night we couldn't get any peace from the lightning and thunder. A lightning bolt struck a tree next to our house and burned it._

    ### p. 124 — official weather report

    | Pattern | Options |
    |:--------|:--------|
    | **Ο καιρός αύριο θα είναι** … | ήπιος (mild) · αίθριος (clear) · άστατος (changeable) |
    | **Θα έχει** … | υψηλές/χαμηλές θερμοκρασίες · ηλιοφάνεια · ήλιο με αραιή συννεφιά · νεφώσεις (cloudy) · βροχές και καταιγίδες · δυνατούς ανέμους |
    | **Θα έχουμε** … | άνοδο / πτώση της θερμοκρασίας |

    **Wind directions:** βοριάς (N) · νοτιάς (S) · ανατολικός (E) · δυτικός (W)
    **Beaufort:** ανέμους 5 μποφόρ · ισχυρούς βόρειους ανέμους έντασης 9 μποφόρ
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar: Απλός Μέλλοντας
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Грамматика: Απλός Μέλλοντας (Простое будущее)

    Используется для **однократного, завершённого** действия в будущем.
    Образуется с частицей **θα** + основа аориста.

    | Тип | Настоящее | Простое будущее | Изменение основы |
    |:----|:----------|:----------------|:-----------------|
    | A | γράφω | **θα γράψω** | γραφ → γραψ |
    | A | αγοράζω | **θα αγοράσω** | αγοραζ → αγορας |
    | A | πετάω | **θα πετάξω** | πετα → πεταξ |
    | A/B | λέω | **θα πω** | неправильный |
    | A/B | τρώω | **θα φάω** | неправильный |
    | B1 | μιλάω | **θα μιλήσω** | μιλα → μιλης |
    | — | πηγαίνω | **θα πάω** | неправильный |

    ### Спряжение: αγοράζω → θα αγοράσω

    | Лицо | Форма |
    |:-----|:------|
    | εγώ | **θα αγοράσω** |
    | εσύ | **θα αγοράσεις** |
    | αυτός/ή/ό | **θα αγοράσει** |
    | εμείς | **θα αγοράσουμε** |
    | εσείς | **θα αγοράσετε** |
    | αυτοί/ές/ά | **θα αγοράσουν** |

    > **Ср. Συνεχής Μέλλοντας** (θα + настоящее): *θα αγοράζω* = буду покупать (многократно).
    > **Απλός** = один раз; **Συνεχής** = повторно / продолжительно.
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Γραμματική: Απλός Μέλλοντας

    Χρησιμοποιείται για **μία, ολοκληρωμένη** πράξη στο μέλλον.
    Σχηματίζεται με το μόριο **θα** + αοριστόθεμα.

    | Τύπος | Ενεστώτας | Απλός Μέλλοντας | Αλλαγή θέματος |
    |:------|:----------|:----------------|:---------------|
    | A | γράφω | **θα γράψω** | γραφ → γραψ |
    | A | αγοράζω | **θα αγοράσω** | αγοραζ → αγορας |
    | A | πετάω | **θα πετάξω** | πετα → πεταξ |
    | A/B | λέω | **θα πω** | ανώμαλο |
    | A/B | τρώω | **θα φάω** | ανώμαλο |
    | B1 | μιλάω | **θα μιλήσω** | μιλα → μιλης |
    | — | πηγαίνω | **θα πάω** | ανώμαλο |

    ### Παράδειγμα κλίσης — αγοράζω → θα αγοράσω

    | Πρόσωπο | Τύπος |
    |:--------|:------|
    | εγώ | **θα αγοράσω** |
    | εσύ | **θα αγοράσεις** |
    | αυτός/ή/ό | **θα αγοράσει** |
    | εμείς | **θα αγοράσουμε** |
    | εσείς | **θα αγοράσετε** |
    | αυτοί/ές/ά | **θα αγοράσουν** |

    > **Σε αντίθεση με τον Συνεχή Μέλλοντα** (θα + Ενεστώτας): *θα αγοράζω* = θα συνεχίζω να αγοράζω.
    > **Απλός** = μία φορά· **Συνεχής** = επαναλαμβανόμενο / συνεχιζόμενο.
    """)
    else:
        _out = mo.md("""
    ## Grammar: Απλός Μέλλοντας (Simple Future)

    Used for a **single, completed** action in the future.
    Formed with particle **θα** + aorist stem.

    | Type | Present | Simple Future | Stem change |
    |:-----|:--------|:--------------|:------------|
    | A | γράφω | **θα γράψω** | γραφ → γραψ |
    | A | αγοράζω | **θα αγοράσω** | αγοραζ → αγορας |
    | A | πετάω | **θα πετάξω** | πετα → πεταξ |
    | A/B | λέω | **θα πω** | irregular |
    | A/B | τρώω | **θα φάω** | irregular |
    | B1 | μιλάω | **θα μιλήσω** | μιλα → μιλης |
    | — | πηγαίνω | **θα πάω** | irregular |

    ### Example conjugation — αγοράζω → θα αγοράσω

    | Person | Form |
    |:-------|:-----|
    | εγώ | **θα αγοράσω** |
    | εσύ | **θα αγοράσεις** |
    | αυτός/ή/ό | **θα αγοράσει** |
    | εμείς | **θα αγοράσουμε** |
    | εσείς | **θα αγοράσετε** |
    | αυτοί/ές/ά | **θα αγοράσουν** |

    > **Vs. Συνεχής Μέλλοντας** (θα + Present): *θα αγοράζω* = I will keep buying (repeatedly).
    > **Απλός** = one time; **Συνεχής** = repeated/ongoing.
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Stem formation by ending class; Type A = consonant stems, B1/B2 = vowel stems (-άω/-ώ)
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Образование основы — Простое будущее

    | Окончание | Примеры |
    |:----------|:--------|
    | **— Α —** |   |
    | -νω, -ζω, -θω → **-σω** | πληρώ**νω** · θα πληρώ**σω**, αγορά**ζω** · θα αγορά**σω**, νιώ**θω** · θα νιώ**σω** |
    | -ζω, -γω, -χω, -χνω, -κω, -σκω → **-ξω** | κοιτά**ζω** · θα κοιτά**ξω**, ανοί**γω** · θα ανοί**ξω**, τρέ**χω** · θα τρέ**ξω**, φτιά**χνω** · θα φτιά**ξω**, μπλέ**κω** · θα μπλέ**ξω**, διδά**σκω** · θα διδά**ξω** |
    | -εύω, -πω, -φω, -βω, -πτω → **-ψω** | δουλε**ύω** · θα δουλέ**ψω**, λεί**πω** · θα λεί**ψω**, γρά**φω** · θα γρά**ψω**, ανά**βω** · θα ανά**ψω**, βλά**πτω** · θα βλά**ψω** |
    | **— Β1 / Β2 —** |   |
    | **-ήσω** | μιλάω – θα μιλ**ήσω** · τηλεφωνώ – θα τηλεφων**ήσω** · ζω – θα ζ**ήσω** |
    | **-άσω** | γελάω – θα γελ**άσω** · διψάω – θα διψ**άσω** · ξεχνάω – θα ξεχ**άσω** |
    | **-έσω** | φοράω – θα φορ**έσω** · καλώ – θα καλ**έσω** · μπορώ – θα μπορ**έσω** |
    | **-ήξω** | πηδάω – θα πηδ**ήξω** · τραβάω – θα τραβ**ήξω** · φυσάω – θα φυσ**ήξω** · βουτάω – θα βουτ**ήξω** |
    | **-άξω** | κοιτάω – θα κοιτ**άξω** · πετάω – θα πετ**άξω** · φυλάω – θα φυλ**άξω** |

    ### Нерегулярные глаголы

    | Настоящее | Простое будущее |
    |:----------|:----------------|
    | ανεβαίνω | θα ανέβω / θα ανεβώ |
    | αρρωσταίνω | θα αρρωστήσω |
    | βάζω | θα βάλω |
    | βγάζω | θα βγάλω |
    | βγαίνω | θα βγω |
    | βλέπω | θα δω |
    | βρίσκω | θα βρω |
    | δίνω | θα δώσω |
    | είμαι | θα είμαι |
    | έχω | θα έχω |
    | θέλω | θα θελήσω |
    | καίω | θα κάψω |
    | κάνω | θα κάνω |
    | καταλαβαίνω | θα καταλάβω |
    | κατεβαίνω | θα κατέβω / θα κατεβώ |
    | κλαίω | θα κλάψω |
    | λέω | θα πω |
    | μαθαίνω | θα μάθω |
    | μένω | θα μείνω |
    | μεθάω | θα μεθύσω |
    | ξέρω | θα ξέρω |
    | μπαίνω | θα μπω |
    | παθαίνω | θα πάθω |
    | παίρνω | θα πάρω |
    | πεθαίνω | θα πεθάνω |
    | περιμένω | θα περιμένω |
    | πέφτω | θα πέσω |
    | πηγαίνω (πάω) | θα πάω |
    | πίνω | θα πιω |
    | πλένω | θα πλύνω |
    | στέλνω | θα στείλω |
    | τρώω | θα φάω |
    | φέρνω | θα φέρω |
    | φεύγω | θα φύγω |
    | γίνομαι | θα γίνω |
    | έρχομαι | θα έρθω |
    | κάθομαι | θα καθίσω / θα κάτσω |
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Σχηματισμός με βάση την κατάληξη — Απλός Μέλλοντας

    | Κατάληξη | Παραδείγματα |
    |:---------|:-------------|
    | **— Α —** |   |
    | -νω, -ζω, -θω → **-σω** | πληρώ**νω** · θα πληρώ**σω**, αγορά**ζω** · θα αγορά**σω**, νιώ**θω** · θα νιώ**σω** |
    | -ζω, -γω, -χω, -χνω, -κω, -σκω → **-ξω** | κοιτά**ζω** · θα κοιτά**ξω**, ανοί**γω** · θα ανοί**ξω**, τρέ**χω** · θα τρέ**ξω**, φτιά**χνω** · θα φτιά**ξω**, μπλέ**κω** · θα μπλέ**ξω**, διδά**σκω** · θα διδά**ξω** |
    | -εύω, -πω, -φω, -βω, -πτω → **-ψω** | δουλε**ύω** · θα δουλέ**ψω**, λεί**πω** · θα λεί**ψω**, γρά**φω** · θα γρά**ψω**, ανά**βω** · θα ανά**ψω**, βλά**πτω** · θα βλά**ψω** |
    | **— Β1 / Β2 —** |   |
    | **-ήσω** | μιλάω – θα μιλ**ήσω** · τηλεφωνώ – θα τηλεφων**ήσω** · ζω – θα ζ**ήσω** |
    | **-άσω** | γελάω – θα γελ**άσω** · διψάω – θα διψ**άσω** · ξεχνάω – θα ξεχ**άσω** |
    | **-έσω** | φοράω – θα φορ**έσω** · καλώ – θα καλ**έσω** · μπορώ – θα μπορ**έσω** |
    | **-ήξω** | πηδάω – θα πηδ**ήξω** · τραβάω – θα τραβ**ήξω** · φυσάω – θα φυσ**ήξω** · βουτάω – θα βουτ**ήξω** |
    | **-άξω** | κοιτάω – θα κοιτ**άξω** · πετάω – θα πετ**άξω** · φυλάω – θα φυλ**άξω** |

    ### Ανώμαλα ρήματα

    | Ενεστώτας | Απλός Μέλλοντας |
    |:----------|:----------------|
    | ανεβαίνω | θα ανέβω / θα ανεβώ |
    | αρρωσταίνω | θα αρρωστήσω |
    | βάζω | θα βάλω |
    | βγάζω | θα βγάλω |
    | βγαίνω | θα βγω |
    | βλέπω | θα δω |
    | βρίσκω | θα βρω |
    | δίνω | θα δώσω |
    | είμαι | θα είμαι |
    | έχω | θα έχω |
    | θέλω | θα θελήσω |
    | καίω | θα κάψω |
    | κάνω | θα κάνω |
    | καταλαβαίνω | θα καταλάβω |
    | κατεβαίνω | θα κατέβω / θα κατεβώ |
    | κλαίω | θα κλάψω |
    | λέω | θα πω |
    | μαθαίνω | θα μάθω |
    | μένω | θα μείνω |
    | μεθάω | θα μεθύσω |
    | ξέρω | θα ξέρω |
    | μπαίνω | θα μπω |
    | παθαίνω | θα πάθω |
    | παίρνω | θα πάρω |
    | πεθαίνω | θα πεθάνω |
    | περιμένω | θα περιμένω |
    | πέφτω | θα πέσω |
    | πηγαίνω (πάω) | θα πάω |
    | πίνω | θα πιω |
    | πλένω | θα πλύνω |
    | στέλνω | θα στείλω |
    | τρώω | θα φάω |
    | φέρνω | θα φέρω |
    | φεύγω | θα φύγω |
    | γίνομαι | θα γίνω |
    | έρχομαι | θα έρθω |
    | κάθομαι | θα καθίσω / θα κάτσω |
    """)
    else:
        _out = mo.md("""
    ## Stem Formation — Simple Future

    | Ending | Examples |
    |:-------|:---------|
    | **— Α —** |   |
    | -νω, -ζω, -θω → **-σω** | πληρώ**νω** · θα πληρώ**σω**, αγορά**ζω** · θα αγορά**σω**, νιώ**θω** · θα νιώ**σω** |
    | -ζω, -γω, -χω, -χνω, -κω, -σκω → **-ξω** | κοιτά**ζω** · θα κοιτά**ξω**, ανοί**γω** · θα ανοί**ξω**, τρέ**χω** · θα τρέ**ξω**, φτιά**χνω** · θα φτιά**ξω**, μπλέ**κω** · θα μπλέ**ξω**, διδά**σκω** · θα διδά**ξω** |
    | -εύω, -πω, -φω, -βω, -πτω → **-ψω** | δουλε**ύω** · θα δουλέ**ψω**, λεί**πω** · θα λεί**ψω**, γρά**φω** · θα γρά**ψω**, ανά**βω** · θα ανά**ψω**, βλά**πτω** · θα βλά**ψω** |
    | **— Β1 / Β2 —** |   |
    | **-ήσω** | μιλάω – θα μιλ**ήσω** · τηλεφωνώ – θα τηλεφων**ήσω** · ζω – θα ζ**ήσω** |
    | **-άσω** | γελάω – θα γελ**άσω** · διψάω – θα διψ**άσω** · ξεχνάω – θα ξεχ**άσω** |
    | **-έσω** | φοράω – θα φορ**έσω** · καλώ – θα καλ**έσω** · μπορώ – θα μπορ**έσω** |
    | **-ήξω** | πηδάω – θα πηδ**ήξω** · τραβάω – θα τραβ**ήξω** · φυσάω – θα φυσ**ήξω** · βουτάω – θα βουτ**ήξω** |
    | **-άξω** | κοιτάω – θα κοιτ**άξω** · πετάω – θα πετ**άξω** · φυλάω – θα φυλ**άξω** |

    ### Irregular Verbs

    | Present | Simple Future |
    |:--------|:--------------|
    | ανεβαίνω | θα ανέβω / θα ανεβώ |
    | αρρωσταίνω | θα αρρωστήσω |
    | βάζω | θα βάλω |
    | βγάζω | θα βγάλω |
    | βγαίνω | θα βγω |
    | βλέπω | θα δω |
    | βρίσκω | θα βρω |
    | δίνω | θα δώσω |
    | είμαι | θα είμαι |
    | έχω | θα έχω |
    | θέλω | θα θελήσω |
    | καίω | θα κάψω |
    | κάνω | θα κάνω |
    | καταλαβαίνω | θα καταλάβω |
    | κατεβαίνω | θα κατέβω / θα κατεβώ |
    | κλαίω | θα κλάψω |
    | λέω | θα πω |
    | μαθαίνω | θα μάθω |
    | μένω | θα μείνω |
    | μεθάω | θα μεθύσω |
    | ξέρω | θα ξέρω |
    | μπαίνω | θα μπω |
    | παθαίνω | θα πάθω |
    | παίρνω | θα πάρω |
    | πεθαίνω | θα πεθάνω |
    | περιμένω | θα περιμένω |
    | πέφτω | θα πέσω |
    | πηγαίνω (πάω) | θα πάω |
    | πίνω | θα πιω |
    | πλένω | θα πλύνω |
    | στέλνω | θα στείλω |
    | τρώω | θα φάω |
    | φέρνω | θα φέρω |
    | φεύγω | θα φύγω |
    | γίνομαι | θα γίνω |
    | έρχομαι | θα έρθω |
    | κάθομαι | θα καθίσω / θα κάτσω |
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar: Conditional sentences
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Грамматика: Условные предложения — Тип 1 (Υποθετικές προτάσεις, Τύπος Α) (стр. 130)

    **Αν** + Простое будущее (без **θα**) → **θα** + Простое будущее

    Придаточное с **Αν** использует ту же основу/окончания, что и Простое будущее, но без частицы θα.

    | Греческий | Русский |
    |:---------|:--------|
    | Αν **βρέξει** αύριο, δε **θα πάμε** για περπάτημα στο βουνό. | Если завтра пойдёт дождь, мы не пойдём гулять в горы. |
    | Αν **αρχίσεις** γυμναστική, **θα νιώσεις** πολύ καλύτερα. | Если ты начнёшь заниматься спортом, почувствуешь себя намного лучше. |
    | Αν **έρθεις**, **θα φάμε** μαζί το μεσημέρι. | Если ты придёшь, мы вместе пообедаем. |
    | Αν **διαβάσεις** περισσότερο, **θα περάσεις** στις εξετάσεις. | Если ты будешь больше заниматься, сдашь экзамены. |
    | Αν του **τηλεφωνήσεις** τώρα, **θα τον βρεις**. | Если ты позвонишь ему сейчас, застанешь его. |
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Γραμματική: Υποθετικές προτάσεις — Τύπος Α (σ. 130)

    **Αν** + Απλός Μέλλοντας (χωρίς το **θα**) → **θα** + Απλός Μέλλοντας

    Η πρόταση με **Αν** χρησιμοποιεί το ίδιο θέμα/τις ίδιες καταλήξεις με τον Απλό Μέλλοντα, αλλά χωρίς το θα.

    | Ελληνικά | Μετάφραση |
    |:---------|:----------|
    | Αν **βρέξει** αύριο, δε **θα πάμε** για περπάτημα στο βουνό. | If it rains tomorrow, we won't go for a walk in the mountains. |
    | Αν **αρχίσεις** γυμναστική, **θα νιώσεις** πολύ καλύτερα. | If you start exercising, you'll feel much better. |
    | Αν **έρθεις**, **θα φάμε** μαζί το μεσημέρι. | If you come, we'll have lunch together. |
    | Αν **διαβάσεις** περισσότερο, **θα περάσεις** στις εξετάσεις. | If you study more, you'll pass the exams. |
    | Αν του **τηλεφωνήσεις** τώρα, **θα τον βρεις**. | If you call him now, you'll catch him. |
    """)
    else:
        _out = mo.md("""
    ## Grammar: Conditional Sentences — Type 1 (Υποθετικές προτάσεις, Τύπος Α) (p. 130)

    **Αν** + Simple Future (without **θα**) → **θα** + Simple Future

    The **Αν**-clause uses the same stem/endings as the Simple Future, just without the particle θα.

    | Greek | English |
    |:------|:--------|
    | Αν **βρέξει** αύριο, δε **θα πάμε** για περπάτημα στο βουνό. | If it rains tomorrow, we won't go for a walk in the mountains. |
    | Αν **αρχίσεις** γυμναστική, **θα νιώσεις** πολύ καλύτερα. | If you start exercising, you'll feel much better. |
    | Αν **έρθεις**, **θα φάμε** μαζί το μεσημέρι. | If you come, we'll have lunch together. |
    | Αν **διαβάσεις** περισσότερο, **θα περάσεις** στις εξετάσεις. | If you study more, you'll pass the exams. |
    | Αν του **τηλεφωνήσεις** τώρα, **θα τον βρεις**. | If you call him now, you'll catch him. |
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar: Adjectives -ης/-α/-ικο
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Грамматика: Прилагательные на **-ης, -α, -ικο**

    Описывают **черты характера** (часто разговорные, с эмоциональной окраской).

    | Мужской (-ης) | Женский (-α) | Средний (-ικο) | Значение |
    |:--------------|:-------------|:---------------|:---------|
    | τεμπέλης | τεμπέλα | τεμπέλικο | ленивый |
    | γκρινιάρης | γκρινιάρα | γκρινιάρικο | брюзгливый |
    | ζηλιάρης | ζηλιάρα | ζηλιάρικο | ревнивый |
    | πεισματάρης | πεισματάρα | πεισματάρικο | упрямый |
    | ξεχασιάρης | ξεχασιάρα | ξεχασιάρικο | забывчивый |
    | παραπονιάρης | παραπονιάρα | παραπονιάρικο | нытик |

    **Склонение τεμπέλης:**

    | Падеж | М. р. (ед./мн.) | Ж. р. (ед./мн.) | Ср. р. (ед./мн.) |
    |:------|:----------------|:----------------|:-----------------|
    | Им. | τεμπέλης / τεμπέληδες | τεμπέλα / τεμπέλες | τεμπέλικο / τεμπέλικα |
    | Рд. | τεμπέλη / τεμπέληδων | τεμπέλας / τεμπέλων | τεμπέλικου / τεμπέλικων |
    | Вн. | τεμπέλη / τεμπέληδες | τεμπέλα / τεμπέλες | τεμπέλικο / τεμπέλικα |

    **Склонение γκρινιάρης** (пример из учебника):

    | Падеж | М. р. | Ж. р. | Ср. р. |
    |:------|:------|:------|:------|
    | Им. ед. | ο γκρινιάρης | η γκρινιάρα | το γκρινιάρικο |
    | Рд. ед. | του γκρινιάρη | της γκρινιάρας | του γκρινιάρικου |
    | Вн. ед. | τον γκρινιάρη | την γκρινιάρα | το γκρινιάρικο |
    | Им. мн. | οι γκρινιάρηδες | οι γκρινιάρες | τα γκρινιάρικα |
    | Рд. мн. | των γκρινιάρηδων | — | των γκρινιάρικων |
    | Вн. мн. | τους γκρινιάρηδες | τις γκρινιάρες | τα γκρινιάρικα |

    **Другие прилагательные этого типа:**
    πενηντάρης · κοκκινομάλλης · γαλανομάτης · μικρούλης · γκρινιάρης · ζηλιάρης · ναζιάρης · ξεχασιάρης · κουτσομπόλης · τσιγκούνης · φοβητσιάρης · παιχνιδιάρης
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Γραμματική: Επίθετα σε **-ης, -α, -ικο**

    Χρησιμοποιούνται για να περιγράψουν **χαρακτηριστικά προσωπικότητας** (συχνά καθομιλουμένα).

    | Αρσενικό (-ης) | Θηλυκό (-α) | Ουδέτερο (-ικο) | Σημασία |
    |:---------------|:------------|:----------------|:--------|
    | τεμπέλης | τεμπέλα | τεμπέλικο | lazy |
    | γκρινιάρης | γκρινιάρα | γκρινιάρικο | grumpy |
    | ζηλιάρης | ζηλιάρα | ζηλιάρικο | jealous |
    | πεισματάρης | πεισματάρα | πεισματάρικο | stubborn |
    | ξεχασιάρης | ξεχασιάρα | ξεχασιάρικο | forgetful |
    | παραπονιάρης | παραπονιάρα | παραπονιάρικο | whiny |

    **Κλίση του τεμπέλης:**

    | Πτώση | Αρσ. (εν./πλ.) | Θηλ. (εν./πλ.) | Ουδ. (εν./πλ.) |
    |:------|:---------------|:---------------|:---------------|
    | Ονομ. | τεμπέλης / τεμπέληδες | τεμπέλα / τεμπέλες | τεμπέλικο / τεμπέλικα |
    | Γεν. | τεμπέλη / τεμπέληδων | τεμπέλας / τεμπέλων | τεμπέλικου / τεμπέλικων |
    | Αιτ. | τεμπέλη / τεμπέληδες | τεμπέλα / τεμπέλες | τεμπέλικο / τεμπέλικα |

    **Κλίση του γκρινιάρης** (παράδειγμα από το βιβλίο):

    | Πτώση | Αρσ. | Θηλ. | Ουδ. |
    |:------|:-----|:-----|:-----|
    | Ονομ. εν. | ο γκρινιάρης | η γκρινιάρα | το γκρινιάρικο |
    | Γεν. εν. | του γκρινιάρη | της γκρινιάρας | του γκρινιάρικου |
    | Αιτ. εν. | τον γκρινιάρη | την γκρινιάρα | το γκρινιάρικο |
    | Ονομ. πλ. | οι γκρινιάρηδες | οι γκρινιάρες | τα γκρινιάρικα |
    | Γεν. πλ. | των γκρινιάρηδων | — | των γκρινιάρικων |
    | Αιτ. πλ. | τους γκρινιάρηδες | τις γκρινιάρες | τα γκρινιάρικα |

    **Άλλα επίθετα αυτού του τύπου:**
    πενηντάρης · κοκκινομάλλης · γαλανομάτης · μικρούλης · γκρινιάρης · ζηλιάρης · ναζιάρης · ξεχασιάρης · κουτσομπόλης · τσιγκούνης · φοβητσιάρης · παιχνιδιάρης
    """)
    else:
        _out = mo.md("""
    ## Grammar: Adjectives in **-ης, -α, -ικο**

    Used to describe **personality traits** (often colloquial, with emotional nuance).

    | Masculine (-ης) | Feminine (-α) | Neuter (-ικο) | Meaning |
    |:----------------|:--------------|:--------------|:--------|
    | τεμπέλης | τεμπέλα | τεμπέλικο | lazy |
    | γκρινιάρης | γκρινιάρα | γκρινιάρικο | grumpy |
    | ζηλιάρης | ζηλιάρα | ζηλιάρικο | jealous |
    | πεισματάρης | πεισματάρα | πεισματάρικο | stubborn |
    | ξεχασιάρης | ξεχασιάρα | ξεχασιάρικο | forgetful |
    | παραπονιάρης | παραπονιάρα | παραπονιάρικο | whiny |

    **Declension of τεμπέλης:**

    | Case | Masc. (sg/pl) | Fem. (sg/pl) | Neut. (sg/pl) |
    |:-----|:--------------|:-------------|:--------------|
    | Nom. | τεμπέλης / τεμπέληδες | τεμπέλα / τεμπέλες | τεμπέλικο / τεμπέλικα |
    | Gen. | τεμπέλη / τεμπέληδων | τεμπέλας / τεμπέλων | τεμπέλικου / τεμπέλικων |
    | Acc. | τεμπέλη / τεμπέληδες | τεμπέλα / τεμπέλες | τεμπέλικο / τεμπέλικα |

    **Declension of γκρινιάρης** (textbook example):

    | Case | Masc. | Fem. | Neut. |
    |:-----|:------|:-----|:------|
    | Nom. sg | ο γκρινιάρης | η γκρινιάρα | το γκρινιάρικο |
    | Gen. sg | του γκρινιάρη | της γκρινιάρας | του γκρινιάρικου |
    | Acc. sg | τον γκρινιάρη | την γκρινιάρα | το γκρινιάρικο |
    | Nom. pl | οι γκρινιάρηδες | οι γκρινιάρες | τα γκρινιάρικα |
    | Gen. pl | των γκρινιάρηδων | — | των γκρινιάρικων |
    | Acc. pl | τους γκρινιάρηδες | τις γκρινιάρες | τα γκρινιάρικα |

    **More adjectives of this type:**
    πενηντάρης · κοκκινομάλλης · γαλανομάτης · μικρούλης · γκρινιάρης · ζηλιάρης · ναζιάρης · ξεχασιάρης · κουτσομπόλης · τσιγκούνης · φοβητσιάρης · παιχνιδιάρης
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
    # Noun file upload
    file_upload_noun = mo.ui.file(label="Load nouns TSV")
    file_upload_noun
    return (file_upload_noun,)


@app.cell(hide_code=True)
def _(RAW_BASE, file_upload_noun, gu2, language_selector, notebook_dir, pd):
    # Load noun data
    if file_upload_noun.value:
        df_noun = gu2.load_data(file_upload_noun)
    else:
        _noun_fname = 'nouns_ru.tsv' if language_selector.value == 'ru' else 'nouns.tsv'
        _noun_path = gu2.ensure_file(_noun_fname, nb_dir=notebook_dir, remote_base=RAW_BASE) or gu2.ensure_file("nouns.tsv", nb_dir=notebook_dir, remote_base=RAW_BASE)
        df_noun = pd.read_csv(_noun_path, sep='\t') if _noun_path else None
    return (df_noun,)


@app.cell(hide_code=True)
def _(df_noun, language_selector, mo, t_ui):
    # Noun table
    _lang = language_selector.value
    table_noun = mo.ui.table(df_noun, selection="multi", initial_selection=None) if df_noun is not None else None
    _display = table_noun if table_noun is not None else mo.md(t_ui("nouns_not_found", _lang))
    mo.vstack([mo.md(t_ui("select_nouns", _lang)), _display])
    return (table_noun,)


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Noun mode selector
    _lang = language_selector.value
    if _lang == 'ru':
        _opts_n = {"без артикля": "simple", "с артиклем": "article"}
        _default_mode_n = "без артикля"
    elif _lang == 'el':
        _opts_n = {"χωρίς άρθρο": "simple", "με άρθρο": "article"}
        _default_mode_n = "χωρίς άρθρο"
    else:
        _opts_n = {"no article": "simple", "with article": "article"}
        _default_mode_n = "no article"
    mode_selector_n = mo.ui.radio(options=_opts_n, value=_default_mode_n, label=t_ui("mode_label", _lang))
    mo.md(f"{mode_selector_n}")
    return (mode_selector_n,)


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Noun indefinite-article toggle (creation only -- no dependency on
    # mode_selector_n, so switching modes doesn't reset it back to False)
    indefinite_toggle_n = mo.ui.switch(label=t_ui("indefinite_label", language_selector.value), value=False)
    return (indefinite_toggle_n,)


@app.cell(hide_code=True)
def _(indefinite_toggle_n, mo, mode_selector_n):
    # Noun indefinite-article toggle (conditional display: only meaningful
    # once the article itself is being tested)
    indefinite_toggle_n if mode_selector_n.value == "article" else mo.md("")
    return


@app.cell(hide_code=True)
def _(gu2, random, table_noun):
    # Noun words + state
    words_noun = gu2.get_words(table_noun)
    (words4test_noun, set_words4test_noun, hist_noun, set_hist_noun, noun_msg, set_noun_msg,
     captured_noun, set_captured_noun, entered_noun, set_entered_noun,
     submit_count_n, set_submit_count_n, prev_count_n, set_prev_count_n,
     next_count_n, set_next_count_n, enter_count_n, set_enter_count_n,
     restart_count_n, set_restart_count_n) = gu2.make_paradigm_drill_state(
        random.sample(words_noun, len(words_noun)) if words_noun else []
    )
    return (
        captured_noun,
        enter_count_n,
        entered_noun,
        hist_noun,
        next_count_n,
        noun_msg,
        prev_count_n,
        restart_count_n,
        set_captured_noun,
        set_enter_count_n,
        set_entered_noun,
        set_hist_noun,
        set_next_count_n,
        set_noun_msg,
        set_prev_count_n,
        set_restart_count_n,
        set_submit_count_n,
        set_words4test_noun,
        submit_count_n,
        words4test_noun,
        words_noun,
    )


@app.cell(hide_code=True)
def _(
    entered_noun,
    gu2,
    hist_noun,
    indefinite_toggle_n,
    language_selector,
    mode_selector_n,
    set_enter_count_n,
    set_next_count_n,
    set_prev_count_n,
    t_ui,
    words4test_noun,
):
    # Noun form
    cv_noun = words4test_noun()[0] if words4test_noun() else None
    noun_meta = gu2.noun_drill_meta(cv_noun["Word"]) if cv_noun else None
    _ac_noun = getattr(noun_meta, "active_cases", [])
    _entered_noun_form = entered_noun().get(cv_noun["Word"]) if cv_noun else None
    _lang_n = language_selector.value
    _article_n = mode_selector_n.value == "article"
    _indef_n = indefinite_toggle_n.value and _article_n
    _labels_noun = gu2.noun_slot_labels(_ac_noun, lang=_lang_n)
    if _article_n:
        _def_prefix = t_ui("def_prefix", _lang_n)
        _labels_noun = [f"{_def_prefix} {_l}" for _l in _labels_noun]
    if _indef_n:
        _indef_prefix = t_ui("indef_prefix", _lang_n)
        _labels_noun = _labels_noun + [f"{_indef_prefix} {_l}" for _l in gu2.noun_slot_labels(gu2.noun_indef_cells(_ac_noun), lang=_lang_n)]
    noun_form, prev_btn_n, next_btn_n, restart_btn_n = gu2.paradigm_drill_widgets(
        labels=_labels_noun,
        values=_entered_noun_form,
        history_len=len(hist_noun()),
        remaining_len=len(words4test_noun()),
        lang=_lang_n,
    )
    set_prev_count_n(0)
    set_next_count_n(0)
    set_enter_count_n(0)
    return cv_noun, next_btn_n, noun_form, noun_meta, prev_btn_n, restart_btn_n


@app.cell(hide_code=True)
def _(
    captured_noun,
    cv_noun,
    gu2,
    language_selector,
    noun_form,
    set_submit_count_n,
    t_ui,
):
    # Noun check button
    check_btn_n = gu2.dirty_check_button(
        noun_form, captured_noun, cv_noun, "test_word", word_key="Word",
        label=t_ui("check_label", language_selector.value),
    )
    set_submit_count_n(0)
    return (check_btn_n,)


@app.cell(hide_code=True)
def _(
    captured_noun,
    check_btn_n,
    cv_noun,
    enter_count_n,
    entered_noun,
    gu2,
    hist_noun,
    indefinite_toggle_n,
    language_selector,
    mo,
    mode_selector_n,
    next_btn_n,
    next_count_n,
    noun_form,
    noun_meta,
    noun_msg,
    prev_btn_n,
    prev_count_n,
    restart_btn_n,
    restart_count_n,
    set_captured_noun,
    set_enter_count_n,
    set_entered_noun,
    set_hist_noun,
    set_next_count_n,
    set_noun_msg,
    set_prev_count_n,
    set_restart_count_n,
    set_submit_count_n,
    set_words4test_noun,
    submit_count_n,
    t_ui,
    words4test_noun,
    words_noun,
):
    # Noun drill
    _lang = language_selector.value
    _article = mode_selector_n.value == "article"
    _indef_n = indefinite_toggle_n.value and _article
    _title = t_ui("article_noun_heading", _lang) if _article else t_ui("simple_noun_heading", _lang)
    gu2.noun_paradigm_drill_form(
        words4test_noun, set_words4test_noun, hist_noun, set_hist_noun, noun_msg, set_noun_msg,
        captured_noun, set_captured_noun, entered_noun, set_entered_noun,
        submit_count_n, set_submit_count_n, prev_count_n, set_prev_count_n,
        next_count_n, set_next_count_n, enter_count_n, set_enter_count_n,
        restart_count_n, set_restart_count_n,
        cv_noun, noun_form, check_btn_n, prev_btn_n, next_btn_n, restart_btn_n,
        vocab=words_noun,
        noun_meta=noun_meta,
        article=_article,
        indefinite=_indef_n,
        word_key="Word",
        meaning_key="Translation",
        meaning_label=t_ui("translation_label", _lang).rstrip(":"),
        title=_title,
        done_message=t_ui("test1_done", _lang),
    ) if words_noun else mo.md(t_ui("noun_empty", _lang))
    return


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Test 2 heading
    mo.md(t_ui("test2_heading", language_selector.value))
    return


@app.cell(hide_code=True)
def _(mo):
    # Verb file upload
    file_upload_verb = mo.ui.file(label="Load verbs TSV")
    file_upload_verb
    return (file_upload_verb,)


@app.cell(hide_code=True)
def _(RAW_BASE, file_upload_verb, gu2, language_selector, notebook_dir, pd):
    # Load verb data
    if file_upload_verb.value:
        df_verb = gu2.load_data(file_upload_verb)
    else:
        _verb_fname = 'verbs_ru.tsv' if language_selector.value == 'ru' else 'verbs.tsv'
        _verb_path = gu2.ensure_file(_verb_fname, nb_dir=notebook_dir, remote_base=RAW_BASE) or gu2.ensure_file("verbs.tsv", nb_dir=notebook_dir, remote_base=RAW_BASE)
        df_verb = pd.read_csv(_verb_path, sep='\t') if _verb_path else None
    return (df_verb,)


@app.cell(hide_code=True)
def _(df_verb, language_selector, mo, t_ui):
    # Verb table
    _lang = language_selector.value
    table_verb = mo.ui.table(df_verb, selection="multi", initial_selection=None) if df_verb is not None else None
    _display = table_verb if table_verb is not None else mo.md(t_ui("verbs_not_found", _lang))
    mo.vstack([mo.md(t_ui("select_verbs", _lang)), _display])
    return (table_verb,)


@app.cell(hide_code=True)
def _(gu2, language_selector, mo, t_ui):
    # Tense selector
    _lang = language_selector.value
    _tense_options = gu2.tense_dropdown_options(lang=_lang)
    _default_tense = "future"
    _default_key = next((k for k, v in _tense_options.items() if v == _default_tense), next(iter(_tense_options)))
    tense_selector = mo.ui.dropdown(
        options=_tense_options,
        value=_default_key,
        label=t_ui("tense_label", _lang),
    )
    tense_selector
    return (tense_selector,)


@app.cell(hide_code=True)
def _(gu2, random, table_verb):
    # Verb words + state
    words_verb = gu2.get_words(table_verb)
    (words4test_verb, set_words4test_verb, hist_verb, set_hist_verb, verb_msg, set_verb_msg,
     captured_verb, set_captured_verb, entered_verb, set_entered_verb,
     submit_count_v, set_submit_count_v, prev_count_v, set_prev_count_v,
     next_count_v, set_next_count_v, enter_count_v, set_enter_count_v,
     restart_count_v, set_restart_count_v) = gu2.make_paradigm_drill_state(
        random.sample(words_verb, len(words_verb)) if words_verb else []
    )
    return (
        captured_verb,
        enter_count_v,
        entered_verb,
        hist_verb,
        next_count_v,
        prev_count_v,
        restart_count_v,
        set_captured_verb,
        set_enter_count_v,
        set_entered_verb,
        set_hist_verb,
        set_next_count_v,
        set_prev_count_v,
        set_restart_count_v,
        set_submit_count_v,
        set_verb_msg,
        set_words4test_verb,
        submit_count_v,
        verb_msg,
        words4test_verb,
        words_verb,
    )


@app.cell(hide_code=True)
def _(
    entered_verb,
    gu2,
    hist_verb,
    language_selector,
    set_enter_count_v,
    set_next_count_v,
    set_prev_count_v,
    tense_selector,
    words4test_verb,
):
    # Verb form
    cv_verb = words4test_verb()[0] if words4test_verb() else None
    _ = tense_selector.value  # rebuild the form (clear stale input) when the tense changes
    _entered_verb_form = entered_verb().get(cv_verb["Word"]) if cv_verb else None
    verb_form, prev_btn_v, next_btn_v, restart_btn_v = gu2.paradigm_drill_widgets(
        labels=gu2.verb_slot_labels(),
        values=_entered_verb_form,
        history_len=len(hist_verb()),
        remaining_len=len(words4test_verb()),
        lang=language_selector.value,
    )
    set_prev_count_v(0)
    set_next_count_v(0)
    set_enter_count_v(0)
    return cv_verb, next_btn_v, prev_btn_v, restart_btn_v, verb_form


@app.cell(hide_code=True)
def _(
    captured_verb,
    cv_verb,
    gu2,
    language_selector,
    set_submit_count_v,
    t_ui,
    verb_form,
):
    # Verb check button
    check_btn_v = gu2.dirty_check_button(
        verb_form, captured_verb, cv_verb, "verb_word", word_key="Word",
        label=t_ui("check_label", language_selector.value),
    )
    set_submit_count_v(0)
    return (check_btn_v,)


@app.cell(hide_code=True)
def _(
    captured_verb,
    check_btn_v,
    cv_verb,
    enter_count_v,
    entered_verb,
    gu2,
    hist_verb,
    language_selector,
    mo,
    next_btn_v,
    next_count_v,
    prev_btn_v,
    prev_count_v,
    restart_btn_v,
    restart_count_v,
    set_captured_verb,
    set_enter_count_v,
    set_entered_verb,
    set_hist_verb,
    set_next_count_v,
    set_prev_count_v,
    set_restart_count_v,
    set_submit_count_v,
    set_verb_msg,
    set_words4test_verb,
    submit_count_v,
    t_ui,
    tense_selector,
    verb_form,
    verb_msg,
    words4test_verb,
    words_verb,
):
    # Verb drill
    _lang = language_selector.value
    _tense_key = tense_selector.value
    if words_verb and _tense_key:
        _tlabel = gu2.TENSE_LABELS[_tense_key]["greek"]
        _output = gu2.verb_paradigm_drill_form(
            words4test_verb, set_words4test_verb, hist_verb, set_hist_verb, verb_msg, set_verb_msg,
            captured_verb, set_captured_verb, entered_verb, set_entered_verb,
            submit_count_v, set_submit_count_v, prev_count_v, set_prev_count_v,
            next_count_v, set_next_count_v, enter_count_v, set_enter_count_v,
            restart_count_v, set_restart_count_v,
            cv_verb, verb_form, check_btn_v, prev_btn_v, next_btn_v, restart_btn_v,
            vocab=words_verb,
            tense=_tense_key,
            word_key="Word",
            meaning_key="Translation",
            meaning_label=t_ui("translation_label", _lang).rstrip(":"),
            title=f"{t_ui('verb_heading', _lang)} — {_tlabel}",
            done_message=t_ui("test2_done", _lang),
        )
    elif not words_verb:
        _output = mo.md(t_ui("verb_empty", _lang))
    else:
        _output = mo.md(t_ui("verb_no_tense", _lang))
    _output
    return


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Test 3 heading
    mo.md(t_ui("test3_heading", language_selector.value))
    return


@app.cell(hide_code=True)
def _(mo):
    # Adj file upload
    file_upload_adj = mo.ui.file(label="Load adjectives TSV")
    file_upload_adj
    return (file_upload_adj,)


@app.cell(hide_code=True)
def _(RAW_BASE, file_upload_adj, gu2, language_selector, notebook_dir, pd):
    # Load adj data
    if file_upload_adj.value:
        df_adj = gu2.load_data(file_upload_adj)
    else:
        _adj_fname = 'adjectives_ru.tsv' if language_selector.value == 'ru' else 'adjectives.tsv'
        _adj_path = gu2.ensure_file(_adj_fname, nb_dir=notebook_dir, remote_base=RAW_BASE) or gu2.ensure_file("adjectives.tsv", nb_dir=notebook_dir, remote_base=RAW_BASE)
        df_adj = pd.read_csv(_adj_path, sep='\t') if _adj_path else None
    return (df_adj,)


@app.cell(hide_code=True)
def _(df_adj, language_selector, mo, t_ui):
    # Adj table
    _lang = language_selector.value
    table_adj = mo.ui.table(df_adj, selection="multi", initial_selection=None) if df_adj is not None else None
    _display = table_adj if table_adj is not None else mo.md(t_ui("adjs_not_found", _lang))
    mo.vstack([mo.md(t_ui("select_adjs", _lang)), _display])
    return (table_adj,)


@app.cell(hide_code=True)
def _(language_selector, mo, t_ui):
    # Mode selector — language-dependent
    _lang = language_selector.value
    if _lang == "ru":
        _opts = {
            "Простой: 3 рода × 2 числа (6 полей)": "simple",
            "Полный: все роды, числа и падежи (18 полей)": "complex",
        }
        _default_mode = "Простой: 3 рода × 2 числа (6 полей)"
    elif _lang == "el":
        _opts = {
            "Απλό: 3 γένη × 2 αριθμοί (6 πεδία)": "simple",
            "Πλήρες: όλα τα γένη, αριθμοί και πτώσεις (18 πεδία)": "complex",
        }
        _default_mode = "Απλό: 3 γένη × 2 αριθμοί (6 πεδία)"
    else:
        _opts = {
            "Simple: 3 genders × 2 numbers (6 fields)": "simple",
            "Complex: all genders, numbers, and cases (18 fields)": "complex",
        }
        _default_mode = "Simple: 3 genders × 2 numbers (6 fields)"
    mode_selector = mo.ui.radio(options=_opts, value=_default_mode, label=t_ui("mode_label", _lang))
    mo.md(f"{mode_selector}")
    return (mode_selector,)


@app.cell(hide_code=True)
def _(gu2, random, table_adj):
    # Adjective words + state
    words_adj = gu2.get_words(table_adj)
    (words4test_adj, set_words4test_adj, hist_adj, set_hist_adj, adj_msg, set_adj_msg,
     captured_adj, set_captured_adj, entered_adj, set_entered_adj,
     submit_count_a, set_submit_count_a, prev_count_a, set_prev_count_a,
     next_count_a, set_next_count_a, enter_count_a, set_enter_count_a,
     restart_count_a, set_restart_count_a) = gu2.make_paradigm_drill_state(
        random.sample(words_adj, len(words_adj)) if words_adj else []
    )
    return (
        adj_msg,
        captured_adj,
        enter_count_a,
        entered_adj,
        hist_adj,
        next_count_a,
        prev_count_a,
        restart_count_a,
        set_adj_msg,
        set_captured_adj,
        set_enter_count_a,
        set_entered_adj,
        set_hist_adj,
        set_next_count_a,
        set_prev_count_a,
        set_restart_count_a,
        set_submit_count_a,
        set_words4test_adj,
        submit_count_a,
        words4test_adj,
        words_adj,
    )


@app.cell(hide_code=True)
def _(
    entered_adj,
    gu2,
    hist_adj,
    language_selector,
    mode_selector,
    set_enter_count_a,
    set_next_count_a,
    set_prev_count_a,
    words4test_adj,
):
    # Adjective form
    cv_adj = words4test_adj()[0] if words4test_adj() else None
    _mode = mode_selector.value
    _entered_adj_form = entered_adj().get(cv_adj["Word"]) if cv_adj else None
    adj_form, prev_btn_a, next_btn_a, restart_btn_a = gu2.paradigm_drill_widgets(
        labels=gu2.adjective_slot_labels(_mode, lang=language_selector.value),
        values=_entered_adj_form,
        history_len=len(hist_adj()),
        remaining_len=len(words4test_adj()),
        lang=language_selector.value,
    )
    set_prev_count_a(0)
    set_next_count_a(0)
    set_enter_count_a(0)
    return adj_form, cv_adj, next_btn_a, prev_btn_a, restart_btn_a


@app.cell(hide_code=True)
def _(
    adj_form,
    captured_adj,
    cv_adj,
    gu2,
    language_selector,
    set_submit_count_a,
    t_ui,
):
    # Adjective check button
    check_btn_a = gu2.dirty_check_button(
        adj_form, captured_adj, cv_adj, "adj_word", word_key="Word",
        label=t_ui("check_label", language_selector.value),
    )
    set_submit_count_a(0)
    return (check_btn_a,)


@app.cell(hide_code=True)
def _(
    adj_form,
    adj_msg,
    captured_adj,
    check_btn_a,
    cv_adj,
    enter_count_a,
    entered_adj,
    gu2,
    hist_adj,
    language_selector,
    mo,
    mode_selector,
    next_btn_a,
    next_count_a,
    prev_btn_a,
    prev_count_a,
    restart_btn_a,
    restart_count_a,
    set_adj_msg,
    set_captured_adj,
    set_enter_count_a,
    set_entered_adj,
    set_hist_adj,
    set_next_count_a,
    set_prev_count_a,
    set_restart_count_a,
    set_submit_count_a,
    set_words4test_adj,
    submit_count_a,
    t_ui,
    words4test_adj,
    words_adj,
):
    # Adjective drill
    _lang = language_selector.value
    _mode = mode_selector.value
    gu2.adjective_paradigm_drill_form(
        words4test_adj, set_words4test_adj, hist_adj, set_hist_adj, adj_msg, set_adj_msg,
        captured_adj, set_captured_adj, entered_adj, set_entered_adj,
        submit_count_a, set_submit_count_a, prev_count_a, set_prev_count_a,
        next_count_a, set_next_count_a, enter_count_a, set_enter_count_a,
        restart_count_a, set_restart_count_a,
        cv_adj, adj_form, check_btn_a, prev_btn_a, next_btn_a, restart_btn_a,
        vocab=words_adj,
        mode=_mode,
        word_key="Word",
        meaning_key="Translation",
        meaning_label=t_ui("translation_label", _lang).rstrip(":"),
        title=t_ui("adj_heading", _lang),
        done_message=t_ui("test3_done", _lang),
    ) if words_adj else mo.md(t_ui("adj_empty", _lang))
    return


@app.cell(hide_code=True)
def _(gu2):
    t_ui = gu2.ui_label
    return (t_ui,)


@app.cell(hide_code=True)
def _(mo):
    # Language selector — fixed-position overlay
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
    # Imports
    import os
    import random
    import pandas as pd
    import marimo as mo
    notebook_dir = os.path.dirname(os.path.abspath(__file__))
    RAW_BASE = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main/modern_greek/ellinika_b/chapter_08"
    return RAW_BASE, mo, notebook_dir, pd, random


@app.cell(hide_code=True)
def _():
    # Modern Greek eee_project: imports
    import eee_project as eee
    from eee_project import GreekUtils, MODERN_GREEK
    from modern_greek_backend_eee import ModernGreekBackend


    return GreekUtils, MODERN_GREEK, ModernGreekBackend, eee


@app.cell(hide_code=True)
def _(GreekUtils, MODERN_GREEK, ModernGreekBackend, eee, mo, pd):
    # Modern Greek eee_project: backend setup
    _mg_backend = ModernGreekBackend()
    eee.register_backend("el", _mg_backend, backend="modern-greek")
    eee.set_chain("el", ["modern-greek"])
    gu2 = GreekUtils(_mg_backend, mo, pd, eee_module=eee, config=MODERN_GREEK)
    return (gu2,)


if __name__ == "__main__":
    app.run()
