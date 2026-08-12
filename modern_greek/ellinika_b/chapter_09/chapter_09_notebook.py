# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "eee-project>=1.1.0",
#     "marimo>=0.23.14",
#     "modern-greek-backend-eee>=1.0.0",
#     "pandas",
# ]
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
    }, ga_config=_cfg.ga_config(), same_window=True)
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Title
    _lang = language_selector.value
    _badge = "[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_NK69X9ZtB785PTA971TNSD)"
    if _lang == "ru":
        _out = mo.md(f"""
    # «Αλλάζουμε συνήθειες» ♻️
    ## Глава 9 — Окружающая среда и экологические привычки · B1 {_badge}

    **Грамматика:** Будущее продолженное · Сравнение времён · Косвенные вопросы
    **Тесты:** Существительные · Глаголы · Прилагательные
    """)
    elif _lang == "el":
        _out = mo.md(f"""
    # «Αλλάζουμε συνήθειες» ♻️
    ## Ενότητα 9 — Περιβάλλον και Οικολογικές Συνήθειες · B1 {_badge}

    **Γραμματική:** Συνεχής Μέλλοντας · Σύγκριση χρόνων · Πλάγιες Ερωτηματικές
    **Τεστ:** Ουσιαστικά · Ρήματα · Επίθετα
    """)
    else:
        _out = mo.md(f"""
    # «Αλλάζουμε συνήθειες» ♻️
    ## Unit 9 — Environment & Ecological Habits · B1 {_badge}

    **Grammar:** Continuous Future · Tenses in Context · Indirect Questions
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
    ## Словарь (Λέξεις, λέξεις)

    | Греческий | Русский |
    |:----------|:--------|
    | η ανακύκλωση | переработка (отходов) |
    | το περιβάλλον | окружающая среда |
    | η ρύπανση | загрязнение |
    | η μόλυνση | заражение / загрязнение |
    | ο οικολόγος | эколог |
    | η συνήθεια | привычка |
    | η προστασία | защита |
    | το δάσος | лес |
    | η συσκευή | прибор / устройство |
    | το ρεύμα | электричество / ток |
    | ο λογαριασμός | счёт |
    | το σκουπίδι | мусор |
    | το χαρτί | бумага |
    | το νερό | вода |
    | το φως | свет |
    | το πρόβλημα | проблема |
    | το μέσο | средство |
    | η μεταφορά | транспорт / перевозка |
    | ο Θερμοσίφωνας | водонагреватель / бойлер |
    | ο κάδος | бак / мусорный контейнер |
    | κάνω οικονομία | экономить / беречь деньги |
    | το σκοτάδι | темнота |
    | η συγκοινωνία | общественный транспорт |
    | ανακυκλώνω | перерабатывать |
    | η ευκαιρία | возможность / случай |
    | η νοοτροπία | менталитет / образ мышления |
    | σώζω | спасать |
    | η τεχνολογία | технология |
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Λεξιλόγιο

    | Ελληνικά | Αγγλικά |
    |:---------|:--------|
    | η ανακύκλωση | recycling |
    | το περιβάλλον | environment |
    | η ρύπανση | pollution |
    | η μόλυνση | pollution / infection |
    | ο οικολόγος | ecologist |
    | η συνήθεια | habit |
    | η προστασία | protection |
    | το δάσος | forest |
    | η συσκευή | appliance / device |
    | το ρεύμα | electricity / current |
    | ο λογαριασμός | bill / account |
    | το σκουπίδι | trash / garbage |
    | το χαρτί | paper |
    | το νερό | water |
    | το φως | light |
    | το πρόβλημα | problem |
    | το μέσο | means / medium |
    | η μεταφορά | transport / transfer |
    | ο Θερμοσίφωνας | water heater / boiler |
    | ο κάδος | bin / container |
    | κάνω οικονομία | to save money / to economize |
    | το σκοτάδι | darkness |
    | η συγκοινωνία | public transport |
    | ανακυκλώνω | to recycle |
    | η ευκαιρία | opportunity, chance |
    | η νοοτροπία | mentality, mindset |
    | σώζω | to save, to rescue |
    | η τεχνολογία | technology |
    """)
    else:
        _out = mo.md("""
    ## Vocabulary

    | Greek | English |
    |:------|:--------|
    | η ανακύκλωση | recycling |
    | το περιβάλλον | environment |
    | η ρύπανση | pollution |
    | η μόλυνση | pollution / infection |
    | ο οικολόγος | ecologist |
    | η συνήθεια | habit |
    | η προστασία | protection |
    | το δάσος | forest |
    | η συσκευή | appliance / device |
    | το ρεύμα | electricity / current |
    | ο λογαριασμός | bill / account |
    | το σκουπίδι | trash / garbage |
    | το χαρτί | paper |
    | το νερό | water |
    | το φως | light |
    | το πρόβλημα | problem |
    | το μέσο | means / medium |
    | η μεταφορά | transport / transfer |
    | ο Θερμοσίφωνας | water heater / boiler |
    | ο κάδος | bin / container |
    | κάνω οικονομία | to save money / to economize |
    | το σκοτάδι | darkness |
    | η συγκοινωνία | public transport |
    | ανακυκλώνω | to recycle |
    | η ευκαιρία | opportunity, chance |
    | η νοοτροπία | mentality, mindset |
    | σώζω | to save, to rescue |
    | η τεχνολογία | technology |
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar: Continuous Future
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Грамматика: Будущее продолженное (Συνεχής Μέλλοντας)

    Используется для **повторяющихся, привычных или продолжающихся** действий в будущем.

    **Образование:** θα + Настоящее время (Ενεστώτας)

    | Лицо | ανακυκλώνω (перерабатывать) |
    |:-----|:----------------------------|
    | εγώ | **θα ανακυκλώνω** |
    | εσύ | **θα ανακυκλώνεις** |
    | αυτός/ή/ό | **θα ανακυκλώνει** |
    | εμείς | **θα ανακυκλώνουμε** |
    | εσείς | **θα ανακυκλώνετε** |
    | αυτοί/ές/ά | **θα ανακυκλώνουν** |

    > **Сравнение:** Простое будущее (θα + основа аориста) = одно завершённое действие
    > Будущее продолженное (θα + Настоящее) = повторяющееся / продолжающееся
    >
    > Пример: *Αύριο θα ανακυκλώσω* ("Завтра я сдам это в переработку" — один раз) / *Από τώρα θα ανακυκλώνω κάθε μέρα* ("С этого момента я буду сдавать в переработку каждый день" — привычка)
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Grammar: Continuous Future (Συνεχής Μέλλοντας)

    Used for **repeated, habitual, or ongoing** actions in the future.

    **Formation:** θα + Present tense (Ενεστώτας)

    | Person | ανακυκλώνω (to recycle) |
    |:-------|:------------------------|
    | εγώ | **θα ανακυκλώνω** |
    | εσύ | **θα ανακυκλώνεις** |
    | αυτός/ή/ό | **θα ανακυκλώνει** |
    | εμείς | **θα ανακυκλώνουμε** |
    | εσείς | **θα ανακυκλώνετε** |
    | αυτοί/ές/ά | **θα ανακυκλώνουν** |

    > **Compare:** Simple Future (θα + aorist stem) = one completed action
    > Continuous Future (θα + Present) = repeated / ongoing
    >
    > Example: *Αύριο θα ανακυκλώσω* ("Tomorrow I'll recycle it" — once) / *Από τώρα θα ανακυκλώνω κάθε μέρα* ("From now on I'll recycle every day" — habit)
    """)
    else:
        _out = mo.md("""
    ## Grammar: Continuous Future (Συνεχής Μέλλοντας)

    Used for **repeated, habitual, or ongoing** actions in the future.

    **Formation:** θα + Present tense (Ενεστώτας)

    | Person | ανακυκλώνω (to recycle) |
    |:-------|:------------------------|
    | εγώ | **θα ανακυκλώνω** |
    | εσύ | **θα ανακυκλώνεις** |
    | αυτός/ή/ό | **θα ανακυκλώνει** |
    | εμείς | **θα ανακυκλώνουμε** |
    | εσείς | **θα ανακυκλώνετε** |
    | αυτοί/ές/ά | **θα ανακυκλώνουν** |

    > **Compare:** Simple Future (θα + aorist stem) = one completed action
    > Continuous Future (θα + Present) = repeated / ongoing
    >
    > Example: *Αύριο θα ανακυκλώσω* ("Tomorrow I'll recycle it" — once) / *Από τώρα θα ανακυκλώνω κάθε μέρα* ("From now on I'll recycle every day" — habit)
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar: Tenses in Context (Για δες)
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Грамматика: Сравнение времён (Για δες)

    | | Прошедшее (один раз) | | Прошедшее (длительно / часто) |
    |:--|:--|:--|:--|
    | **Аорист** | Χτες **διάβασα** εφημερίδα. ("Вчера я почитал газету.") | **Имперфект** | Παλιά **διάβαζα** εφημερίδα κάθε μέρα. ("Раньше я читал газету каждый день.") |
    | **Простое будущее** | Αύριο **θα διαβάσω** για το τεστ. ("Завтра я почитаю к тесту.") | **Будущее продолженное** | Από αύριο **θα διαβάζω** τρεις ώρες την ημέρα. ("Начиная с завтра я буду читать по три часа в день.") |

    **Будущее продолженное — выражения времени:**

    | Выражение | Пример |
    |:----------|:-------|
    | Από αύριο ("Начиная с завтра") | θα ανακυκλώνω. ("...я буду сдавать в переработку.") |
    | Από 'δώ και πέρα ("Отныне") | θα αγοράζω βιολογικά τρόφιμα. ("...я буду покупать биопродукты.") |
    | Από 'δώ και στο εξής ("С этого момента и впредь") | θα παίρνω το τραμ. ("...я буду ездить на трамвае.") |
    | Όσον καιρό θα είμαι εκεί ("Пока я буду там") | θα πηγαίνω στη δουλειά με το ποδήλατο. ("...я буду ездить на работу на велосипеде.") |
    | πάντα / συχνά / τακτικά ("всегда / часто / регулярно") | θα παίρνω το αυτοκίνητο. ("...я буду ездить на машине.") |
    | Σπάνια ("Редко") | θα διαβάζω. ("...я буду читать.") |
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Grammar: Tenses in Context (Για δες)

    | | Past (once) | | Past (ongoing / habitual) |
    |:--|:--|:--|:--|
    | **Aorist** | Χτες **διάβασα** εφημερίδα. ("Yesterday I read a newspaper.") | **Imperfect** | Παλιά **διάβαζα** εφημερίδα κάθε μέρα. ("I used to read a newspaper every day.") |
    | **Simple Future** | Αύριο **θα διαβάσω** για το τεστ. ("Tomorrow I'll read for the test.") | **Continuous Future** | Από αύριο **θα διαβάζω** τρεις ώρες την ημέρα. ("Starting tomorrow I'll read three hours a day.") |

    **Continuous Future — time expressions:**

    | Expression | Example |
    |:-----------|:--------|
    | Από αύριο ("Starting tomorrow") | θα ανακυκλώνω. ("...I'll recycle.") |
    | Από 'δώ και πέρα ("From now on") | θα αγοράζω βιολογικά τρόφιμα. ("...I'll buy organic food.") |
    | Από 'δώ και στο εξής ("From this point onward") | θα παίρνω το τραμ. ("...I'll take the tram.") |
    | Όσον καιρό θα είμαι εκεί ("As long as I'm there") | θα πηγαίνω στη δουλειά με το ποδήλατο. ("...I'll go to work by bike.") |
    | πάντα / συχνά / τακτικά ("always / often / regularly") | θα παίρνω το αυτοκίνητο. ("...I'll take the car.") |
    | Σπάνια ("Rarely") | θα διαβάζω. ("...I'll read.") |
    """)
    else:
        _out = mo.md("""
    ## Grammar: Tenses in Context (Για δες)

    | | Past (once) | | Past (ongoing / habitual) |
    |:--|:--|:--|:--|
    | **Aorist** | Χτες **διάβασα** εφημερίδα. ("Yesterday I read a newspaper.") | **Imperfect** | Παλιά **διάβαζα** εφημερίδα κάθε μέρα. ("I used to read a newspaper every day.") |
    | **Simple Future** | Αύριο **θα διαβάσω** για το τεστ. ("Tomorrow I'll read for the test.") | **Continuous Future** | Από αύριο **θα διαβάζω** τρεις ώρες την ημέρα. ("Starting tomorrow I'll read three hours a day.") |

    **Continuous Future — time expressions:**

    | Expression | Example |
    |:-----------|:--------|
    | Από αύριο ("Starting tomorrow") | θα ανακυκλώνω. ("...I'll recycle.") |
    | Από 'δώ και πέρα ("From now on") | θα αγοράζω βιολογικά τρόφιμα. ("...I'll buy organic food.") |
    | Από 'δώ και στο εξής ("From this point onward") | θα παίρνω το τραμ. ("...I'll take the tram.") |
    | Όσον καιρό θα είμαι εκεί ("As long as I'm there") | θα πηγαίνω στη δουλειά με το ποδήλατο. ("...I'll go to work by bike.") |
    | πάντα / συχνά / τακτικά ("always / often / regularly") | θα παίρνω το αυτοκίνητο. ("...I'll take the car.") |
    | Σπάνια ("Rarely") | θα διαβάζω. ("...I'll read.") |
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Phrases: Πώς το λένε;
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Разговорные фразы (Πώς το λένε;)

    | Греческий | Русский |
    |:----------|:--------|
    | Αμάν! | Господи! / Ну хватит! |
    | Πώς είναι δυνατόν; | Как это возможно? |
    | Ξέρω 'γώ; | Откуда мне знать? |
    | Αλλά βέβαια... | Но конечно... |
    | Ε, καλά τώρα. | Ну ладно. / Хорошо. |
    | Όπως και να 'χει... | Как бы то ни было... |
    | Δεν πάει άλλο. | Так больше нельзя. / Хватит. |
    | Δε βγαίνουμε οικονομικά. | Концы с концами не сводим. |
    | Εμένα μου το λες; | Ты мне это говоришь? |
    | Εγώ που χαλάω ένα σωρό λεφτά; | Я, который трачу кучу денег? |
    | Έτσι όπως πάμε... | Если так пойдёт... |
    | Άσε που... | Не говоря уже о том, что... |
    | Σωστό κι αυτό. | Это тоже верно. |
    | Να μη σου πω ότι... | Не говоря уж о том, что... |
    | Μια χαρά! | Отлично! / Замечательно! |
    | Δε μου λες... | Скажи-ка... / Послушай... |
    | Άμα δε σβήνουμε τα φώτα και τις συσκευές... | Если мы не выключаем свет и приборы... |
    | Από εμάς εξαρτάται. | От нас зависит. |
    | Κι όμως. | И всё же. / Тем не менее. |
    | Ωραίο ακούγεται όλο αυτό. | Всё это звучит красиво. |
    | Τι λέτε, ρε παιδιά; | Что скажете, ребята? |
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Πώς το λένε;

    | Ελληνικά | Αγγλικά |
    |:---------|:--------|
    | Αμάν! | For heaven's sake! / Come on! |
    | Πώς είναι δυνατόν; | How is it possible? |
    | Ξέρω 'γώ; | How should I know? |
    | Αλλά βέβαια... | But of course... |
    | Ε, καλά τώρα. | Oh come on. / Alright then. |
    | Όπως και να 'χει... | Be that as it may... / Anyway... |
    | Δεν πάει άλλο. | It's unbearable. / Enough is enough. |
    | Δε βγαίνουμε οικονομικά. | We can't make ends meet. |
    | Εμένα μου το λες; | Are you telling me? / You're preaching to the choir. |
    | Εγώ που χαλάω ένα σωρό λεφτά; | And I who spend a fortune? |
    | Έτσι όπως πάμε... | The way things are going... |
    | Άσε που... | Not to mention... / Let alone... |
    | Σωστό κι αυτό. | That's true too. / Fair point. |
    | Να μη σου πω ότι... | Not to mention that... |
    | Μια χαρά! | Great! / Just fine! |
    | Δε μου λες... | Tell me... / Say... |
    | Άμα δε σβήνουμε τα φώτα και τις συσκευές... | If we don't turn off the lights and appliances... |
    | Από εμάς εξαρτάται. | It's up to us. / It depends on us. |
    | Κι όμως. | And yet. / Nevertheless. |
    | Ωραίο ακούγεται όλο αυτό. | It all sounds nice. |
    | Τι λέτε, ρε παιδιά; | What do you say, guys? |
    """)
    else:
        _out = mo.md("""
    ## Useful Phrases (Πώς το λένε;)

    | Greek | English |
    |:------|:--------|
    | Αμάν! | For heaven's sake! / Come on! |
    | Πώς είναι δυνατόν; | How is it possible? |
    | Ξέρω 'γώ; | How should I know? |
    | Αλλά βέβαια... | But of course... |
    | Ε, καλά τώρα. | Oh come on. / Alright then. |
    | Όπως και να 'χει... | Be that as it may... / Anyway... |
    | Δεν πάει άλλο. | It's unbearable. / Enough is enough. |
    | Δε βγαίνουμε οικονομικά. | We can't make ends meet. |
    | Εμένα μου το λες; | Are you telling me? / You're preaching to the choir. |
    | Εγώ που χαλάω ένα σωρό λεφτά; | And I who spend a fortune? |
    | Έτσι όπως πάμε... | The way things are going... |
    | Άσε που... | Not to mention... / Let alone... |
    | Σωστό κι αυτό. | That's true too. / Fair point. |
    | Να μη σου πω ότι... | Not to mention that... |
    | Μια χαρά! | Great! / Just fine! |
    | Δε μου λες... | Tell me... / Say... |
    | Άμα δε σβήνουμε τα φώτα και τις συσκευές... | If we don't turn off the lights and appliances... |
    | Από εμάς εξαρτάται. | It's up to us. / It depends on us. |
    | Κι όμως. | And yet. / Nevertheless. |
    | Ωραίο ακούγεται όλο αυτό. | It all sounds nice. |
    | Τι λέτε, ρε παιδιά; | What do you say, guys? |
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Grammar: Indirect Questions
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Грамматика: Косвенные вопросы (Πλάγιες Ερωτηματικές)

    Прямые вопросы становятся косвенными придаточными с тем же вопросительным словом:

    | Прямой вопрос | Косвенный (пересказ) |
    |:--------------|:--------------------|
    | **Τι** μπορώ να κάνω για το περιβάλλον; ("**Что** я могу сделать для окружающей среды?") | Η Αρλέτα θέλει να μάθει **τι** μπορεί να κάνει. ("Арлета хочет узнать, **что** она может сделать.") |
    | **Πώς** θα πηγαίνεις στη δουλειά σου; ("**Как** ты будешь добираться до работы?") | Ο Ερβίν ρώτησε **πώς** θα πηγαίνει. ("Эрвин спросил, **как** он будет добираться.") |
    | **Πότε** φεύγεις; ("**Когда** ты уезжаешь?") | Ο Φοίβος ρώτησε **πότε** φεύγει. ("Фивос спросил, **когда** он уезжает.") |
    | **Γιατί** πετάς την εφημερίδα στα σκουπίδια; ("**Почему** ты выбрасываешь газету в мусор?") | Ο Πάμπλο ρώτησε **γιατί** πετάει. ("Пабло спросил, **почему** он её выбрасывает.") |
    | **Πού** υπάρχει κάδος ανακύκλωσης; ("**Где** есть контейнер для переработки?") | Ο Νίκος δεν ξέρει **πού** υπάρχει. ("Никос не знает, **где** он есть.") |
    | Υπάρχει κανένας κάδος; _(да/нет)_ ("Есть ли вообще контейнер?") | Ο Πάμπλο ρώτησε **αν** υπάρχει κάδος. ("Пабло спросил, есть **ли** контейнер.") |
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Grammar: Indirect Questions (Πλάγιες Ερωτηματικές)

    Direct questions become indirect clauses using the same question word:

    | Direct question | Indirect (reported) |
    |:----------------|:--------------------|
    | **Τι** μπορώ να κάνω για το περιβάλλον; ("**What** can I do for the environment?") | Η Αρλέτα θέλει να μάθει **τι** μπορεί να κάνει. ("Arleta wants to find out **what** she can do.") |
    | **Πώς** θα πηγαίνεις στη δουλειά σου; ("**How** will you get to work?") | Ο Ερβίν ρώτησε **πώς** θα πηγαίνει. ("Ervin asked **how** he would get there.") |
    | **Πότε** φεύγεις; ("**When** are you leaving?") | Ο Φοίβος ρώτησε **πότε** φεύγει. ("Phoevos asked **when** he was leaving.") |
    | **Γιατί** πετάς την εφημερίδα στα σκουπίδια; ("**Why** are you throwing the newspaper in the trash?") | Ο Πάμπλο ρώτησε **γιατί** πετάει. ("Pablo asked **why** he was throwing it away.") |
    | **Πού** υπάρχει κάδος ανακύκλωσης; ("**Where** is there a recycling bin?") | Ο Νίκος δεν ξέρει **πού** υπάρχει. ("Nikos doesn't know **where** there is one.") |
    | Υπάρχει κανένας κάδος; _(yes/no)_ ("Is there a bin at all?") | Ο Πάμπλο ρώτησε **αν** υπάρχει κάδος. ("Pablo asked **whether** there was a bin.") |
    """)
    else:
        _out = mo.md("""
    ## Grammar: Indirect Questions (Πλάγιες Ερωτηματικές)

    Direct questions become indirect clauses using the same question word:

    | Direct question | Indirect (reported) |
    |:----------------|:--------------------|
    | **Τι** μπορώ να κάνω για το περιβάλλον; ("**What** can I do for the environment?") | Η Αρλέτα θέλει να μάθει **τι** μπορεί να κάνει. ("Arleta wants to find out **what** she can do.") |
    | **Πώς** θα πηγαίνεις στη δουλειά σου; ("**How** will you get to work?") | Ο Ερβίν ρώτησε **πώς** θα πηγαίνει. ("Ervin asked **how** he would get there.") |
    | **Πότε** φεύγεις; ("**When** are you leaving?") | Ο Φοίβος ρώτησε **πότε** φεύγει. ("Phoevos asked **when** he was leaving.") |
    | **Γιατί** πετάς την εφημερίδα στα σκουπίδια; ("**Why** are you throwing the newspaper in the trash?") | Ο Πάμπλο ρώτησε **γιατί** πετάει. ("Pablo asked **why** he was throwing it away.") |
    | **Πού** υπάρχει κάδος ανακύκλωσης; ("**Where** is there a recycling bin?") | Ο Νίκος δεν ξέρει **πού** υπάρχει. ("Nikos doesn't know **where** there is one.") |
    | Υπάρχει κανένας κάδος; _(yes/no)_ ("Is there a bin at all?") | Ο Πάμπλο ρώτησε **αν** υπάρχει κάδος. ("Pablo asked **whether** there was a bin.") |
    """)
    _out
    return


@app.cell(hide_code=True)
def _(language_selector, mo):
    # Φωνή-γραφή: elision
    _lang = language_selector.value
    if _lang == "ru":
        _out = mo.md("""
    ## Произношение и правописание (Φωνή-γραφή)

    ### Стр. 143 — усечение (Αποκοπή)

    Слова, начинающиеся с гласной, могут терять начальный звук после слова, оканчивающегося на гласную:

    | Полная форма | Краткая форма | Пример |
    |:-------------|:--------------|:-------|
    | εγώ | 'γώ | Ξέρω **'γώ**; ("Откуда мне знать?") |
    | εδώ | 'δώ | Από **'δώ** και πέρα ("Отныне") |
    | εκεί | 'κεί | Από **'κεί** ("Оттуда") |

    ### Стр. 150 — Επιτονισμός (интонация и логическое ударение)

    **Обычная интонация** (одни и те же слова, разный смысл в зависимости от интонации):
    - Η Μελέκ είναι φοιτήτρια. ("Мелек — студентка.") (= я это точно знаю)
    - Η Μελέκ είναι φοιτήτρια; ("Мелек — студентка?") (= скажи мне, я вообще не знаю)
    - Η Μελέκ είναι φοιτήτρια! ("Мелек — студентка!") (= правда? Вот это сюрприз!)

    **Логическое (контрастное) ударение:**
    - Ο Νίκος θα έρθει με το ποδήλατο. ("Никос приедет на велосипеде.") (нейтральное утверждение)
    - – Ο Πάμπλο θα έρθει με το ποδήλατο; – **Ο ΝΙΚΟΣ** θα έρθει με το ποδήλατο. ("— Памбло приедет на велосипеде? — НИКОС приедет на велосипеде.") (= а не Памбло)
    - – Ο Νίκος θα έρθει με το αυτοκίνητο; – Ο Νίκος θα έρθει με το **ΠΟΔΗΛΑΤΟ**. ("— Никос приедет на машине? — Никос приедет на ВЕЛОСИПЕДЕ.") (= а не на машине)
    - – Ο Νίκος δε θα έρθει με το ποδήλατο; – **ΘΑ** έρθει με το ποδήλατο. ("— Никос ведь не приедет на велосипеде? — ПРИЕДЕТ он на велосипеде.") (опровержение отрицания)
    - Η δασκάλα **σας** περιμένει. ("Ваша учительница ждёт.") (безударное σας = «ваша», притяжательное) vs. Η δασκάλα **σάς** περιμένει. ("Учительница ждёт вас.") (ударное σάς = «вас», дополнение) — пара слов, различающихся только ударением.
    """)
    elif _lang == "el":
        _out = mo.md("""
    ## Pronunciation & Spelling (Φωνή-γραφή)

    ### p. 143 — Elision (Αποκοπή)

    Words beginning with a vowel can drop it after a word ending in a vowel:

    | Full form | Short form | Example |
    |:----------|:-----------|:--------|
    | εγώ | 'γώ | Ξέρω **'γώ**; ("How should I know?") |
    | εδώ | 'δώ | Από **'δώ** και πέρα ("From now on") |
    | εκεί | 'κεί | Από **'κεί** ("From there") |

    ### p. 150 — Επιτονισμός (Intonation and stress)

    **Plain intonation** (same words, three meanings by intonation alone):
    - Η Μελέκ είναι φοιτήτρια. ("Melek is a student.") (= I know this for a fact, it's certain)
    - Η Μελέκ είναι φοιτήτρια; ("Melek is a student?") (= tell me, I have no idea)
    - Η Μελέκ είναι φοιτήτρια! ("Melek is a student!") (= really? What a surprise!)

    **Emphatic/contrastive stress:**
    - Ο Νίκος θα έρθει με το ποδήλατο. ("Nikos will come by bike.") (neutral statement)
    - – Ο Πάμπλο θα έρθει με το ποδήλατο; – **Ο ΝΙΚΟΣ** θα έρθει με το ποδήλατο. ("— Will Pablo come by bike? — NIKOS will come by bike.") (= not Pablo)
    - – Ο Νίκος θα έρθει με το αυτοκίνητο; – Ο Νίκος θα έρθει με το **ΠΟΔΗΛΑΤΟ**. ("— Will Nikos come by car? — Nikos will come by BIKE.") (= not by car)
    - – Ο Νίκος δε θα έρθει με το ποδήλατο; – **ΘΑ** έρθει με το ποδήλατο. ("— Won't Nikos come by bike? — He WILL come by bike.") (contradicting a negative assumption)
    - Η δασκάλα **σας** περιμένει. ("Your teacher is waiting.") (unstressed σας = "your," possessive) vs. Η δασκάλα **σάς** περιμένει. ("The teacher is waiting for you.") (stressed σάς = "you," object) — a weak-vs-strong pronoun pair distinguished only by stress.
    """)
    else:
        _out = mo.md("""
    ## Pronunciation & Spelling (Φωνή-γραφή)

    ### p. 143 — Elision (Αποκοπή)

    Words beginning with a vowel can drop it after a word ending in a vowel:

    | Full form | Short form | Example |
    |:----------|:-----------|:--------|
    | εγώ | 'γώ | Ξέρω **'γώ**; / Ξέρω εγώ; ("How should I know?") |
    | εδώ | 'δώ | Από **'δώ** και πέρα / Από εδώ και πέρα ("From now on") |
    | εκεί | 'κεί | Από **'κεί** / Από εκεί ("From there") |

    ### p. 150 — Επιτονισμός (Intonation and stress)

    **Plain intonation** (same words, three meanings by intonation alone):
    - Η Μελέκ είναι φοιτήτρια. ("Melek is a student.") (= I know this for a fact, it's certain)
    - Η Μελέκ είναι φοιτήτρια; ("Melek is a student?") (= tell me, I have no idea)
    - Η Μελέκ είναι φοιτήτρια! ("Melek is a student!") (= really? What a surprise!)

    **Emphatic/contrastive stress:**
    - Ο Νίκος θα έρθει με το ποδήλατο. ("Nikos will come by bike.") (neutral statement)
    - – Ο Πάμπλο θα έρθει με το ποδήλατο; – **Ο ΝΙΚΟΣ** θα έρθει με το ποδήλατο. ("— Will Pablo come by bike? — NIKOS will come by bike.") (= not Pablo)
    - – Ο Νίκος θα έρθει με το αυτοκίνητο; – Ο Νίκος θα έρθει με το **ΠΟΔΗΛΑΤΟ**. ("— Will Nikos come by car? — Nikos will come by BIKE.") (= not by car)
    - – Ο Νίκος δε θα έρθει με το ποδήλατο; – **ΘΑ** έρθει με το ποδήλατο. ("— Won't Nikos come by bike? — He WILL come by bike.") (contradicting a negative assumption)
    - Η δασκάλα **σας** περιμένει. ("Your teacher is waiting.") (unstressed σας = "your," possessive) vs. Η δασκάλα **σάς** περιμένει. ("The teacher is waiting for you.") (stressed σάς = "you," object) — a weak-vs-strong pronoun pair distinguished only by stress.
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
    _default_tense = "future_continuous"
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
    _entered_verb_form = entered_verb().get(cv_verb["Word"]) if cv_verb else None
    verb_meta = gu2.verb_drill_meta(cv_verb["Word"], tense_selector.value) if cv_verb and tense_selector.value else None
    verb_form, prev_btn_v, next_btn_v, restart_btn_v = gu2.paradigm_drill_widgets(
        labels=gu2.verb_slot_labels(verb_meta.active_slots if verb_meta else None),
        values=_entered_verb_form,
        history_len=len(hist_verb()),
        remaining_len=len(words4test_verb()),
        lang=language_selector.value,
    )
    set_prev_count_v(0)
    set_next_count_v(0)
    set_enter_count_v(0)
    return cv_verb, next_btn_v, prev_btn_v, restart_btn_v, verb_form, verb_meta


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
    verb_meta,
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
            verb_meta=verb_meta,
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
def _(language_selector, mo):
    from eee_project import ConfigStore as _ConfigStore
    from eee_project.notebook_utils import eee_footer
    _ROOT = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main"
    _cfg = _ConfigStore.from_file_or_url(
        __file__,
        f"{_ROOT}/modern_greek/ellinika_b/index.tsv",
    )
    _prev_url, _next_url = _cfg.adjacent_urls("chapter_09/")
    eee_footer(mo, lang=language_selector.value, prev_url=_prev_url, next_url=_next_url, same_window=True)
    return


@app.cell(hide_code=True)
def _():
    # Imports
    import os
    import random
    import pandas as pd
    import marimo as mo
    notebook_dir = os.path.dirname(os.path.abspath(__file__))
    RAW_BASE = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main/modern_greek/ellinika_b/chapter_09"
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
