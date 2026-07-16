# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "eee-project @ git+https://codeberg.org/EEE-project/eee-project.git",
#     "marimo>=0.23.14",
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
app = marimo.App(width="medium", html_head_file="head.html")


@app.cell(hide_code=True)
def _(language_selector, mo):
    from eee_project import ConfigStore, eee_topbar
    _ROOT = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main"
    _cfg = ConfigStore.from_file_or_url(
        __file__,
        f"{_ROOT}/modern_greek/ellinika_b/lessons.tsv",
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
    _badge = "[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/notebooks/nb_MD5SVJUXZ8KnENdvHZN7mV)"
    if _lang == "ru":
        _out = mo.md(f"""
# «Αλλάζουμε συνήθειες» ♻️
## Глава 9 — Окружающая среда и экологические привычки · B1 {_badge}

**Грамматика:** Длительное будущее · Сравнение времён · Косвенные вопросы
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
## Грамматика: Длительное будущее (Συνεχής Μέλλοντας)

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
> Длительное будущее (θα + Настоящее) = повторяющееся / продолжающееся
""")
    elif _lang == "el":
        _out = mo.md("""
## Γραμματική: Συνεχής Μέλλοντας

Χρησιμοποιείται για **επαναλαμβανόμενες, συνήθεις ή συνεχιζόμενες** πράξεις στο μέλλον.

**Σχηματισμός:** θα + Ενεστώτας

| Πρόσωπο | ανακυκλώνω |
|:--------|:-----------|
| εγώ | **θα ανακυκλώνω** |
| εσύ | **θα ανακυκλώνεις** |
| αυτός/ή/ό | **θα ανακυκλώνει** |
| εμείς | **θα ανακυκλώνουμε** |
| εσείς | **θα ανακυκλώνετε** |
| αυτοί/ές/ά | **θα ανακυκλώνουν** |

> **Σύγκριση:** *Απλός Μέλλοντας* (θα + αοριστόθεμα) = μία ολοκληρωμένη πράξη
> *Συνεχής Μέλλοντας* (θα + Ενεστώτας) = επαναλαμβανόμενο / συνεχιζόμενο
>
> Παράδειγμα: *Αύριο θα ανακυκλώσω* (μια φορά) / *Από τώρα θα ανακυκλώνω κάθε μέρα* (συνήθεια)
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
> Example: *Αύριο θα ανακυκλώσω* (once) / *Από τώρα θα ανακυκλώνω κάθε μέρα* (habit)
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
| **Аорист** | Χτες **διάβασα** εφημερίδα. | **Имперфект** | Παλιά **διάβαζα** εφημερίδα κάθε μέρα. |
| **Простое будущее** | Αύριο **θα διαβάσω** για το τεστ. | **Длительное будущее** | Από αύριο **θα διαβάζω** τρεις ώρες την ημέρα. |

**Длительное будущее — выражения времени:**

| Выражение | Пример |
|:----------|:-------|
| Από αύριο | θα ανακυκλώνω. |
| Από 'δώ και πέρα | θα αγοράζω βιολογικά τρόφιμα. |
| Από 'δώ και στο εξής | θα παίρνω το τραμ. |
| Όσον καιρό θα είμαι εκεί | θα πηγαίνω στη δουλειά με το ποδήλατο. |
| πάντα / συχνά / τακτικά | θα παίρνω το αυτοκίνητο. |
| Σπάνια | θα διαβάζω. |
""")
    elif _lang == "el":
        _out = mo.md("""
## Γραμματική: Σύγκριση χρόνων (Για δες)

| | Παρελθόν (μία φορά) | | Παρελθόν (διάρκεια / συχνά) |
|:--|:--|:--|:--|
| **Αόριστος** | Χτες **διάβασα** εφημερίδα. | **Παρατατικός** | Παλιά **διάβαζα** εφημερίδα κάθε μέρα. |
| **Απλός Μέλλοντας** | Αύριο **θα διαβάσω** για το τεστ. | **Συνεχής Μέλλοντας** | Από αύριο **θα διαβάζω** τρεις ώρες την ημέρα. |

**Συνεχής Μέλλοντας — εκφράσεις χρόνου:**

| Έκφραση | Παράδειγμα |
|:--------|:-----------|
| Από αύριο | θα ανακυκλώνω. |
| Από 'δώ και πέρα | θα αγοράζω βιολογικά τρόφιμα. |
| Από 'δώ και στο εξής | θα παίρνω το τραμ. |
| Όσον καιρό θα είμαι εκεί | θα πηγαίνω με το ποδήλατο. |
| πάντα / συχνά / τακτικά | θα παίρνω το αυτοκίνητο. |
| Σπάνια | θα διαβάζω. |
""")
    else:
        _out = mo.md("""
## Grammar: Tenses in Context (Για δες)

| | Past (once) | | Past (ongoing / habitual) |
|:--|:--|:--|:--|
| **Aorist** | Χτες **διάβασα** εφημερίδα. | **Imperfect** | Παλιά **διάβαζα** εφημερίδα κάθε μέρα. |
| **Simple Future** | Αύριο **θα διαβάσω** για το τεστ. | **Continuous Future** | Από αύριο **θα διαβάζω** τρεις ώρες την ημέρα. |

**Continuous Future — time expressions:**

| Expression | Example |
|:-----------|:--------|
| Από αύριο | θα ανακυκλώνω. |
| Από 'δώ και πέρα | θα αγοράζω βιολογικά τρόφιμα. |
| Από 'δώ και στο εξής | θα παίρνω το τραμ. |
| Όσον καιρό θα είμαι εκεί | θα πηγαίνω στη δουλειά με το ποδήλατο. |
| πάντα / συχνά / τακτικά | θα παίρνω το αυτοκίνητο. |
| Σπάνια | θα διαβάζω. |
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

| Φράση |
|:------|
| Αμάν! |
| Πώς είναι δυνατόν; |
| Ξέρω 'γώ; |
| Αλλά βέβαια... |
| Ε, καλά τώρα. |
| Όπως και να 'χει... |
| Δεν πάει άλλο. |
| Δε βγαίνουμε οικονομικά. |
| Εμένα μου το λες; |
| Εγώ που χαλάω ένα σωρό λεφτά; |
| Έτσι όπως πάμε... |
| Άσε που... |
| Σωστό κι αυτό. |
| Να μη σου πω ότι... |
| Μια χαρά! |
| Δε μου λες... |
| Άμα δε σβήνουμε τα φώτα και τις συσκευές... |
| Από εμάς εξαρτάται. |
| Κι όμως. |
| Ωραίο ακούγεται όλο αυτό. |
| Τι λέτε, ρε παιδιά; |
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
| **Τι** μπορώ να κάνω για το περιβάλλον; | Η Αρλέτα θέλει να μάθει **τι** μπορεί να κάνει. |
| **Πώς** θα πηγαίνεις στη δουλειά σου; | Ο Ερβίν ρώτησε **πώς** θα πηγαίνει. |
| **Πότε** φεύγεις; | Ο Φοίβος ρώτησε **πότε** φεύγει. |
| **Γιατί** πετάς την εφημερίδα στα σκουπίδια; | Ο Πάμπλο ρώτησε **γιατί** πετάει. |
| **Πού** υπάρχει κάδος ανακύκλωσης; | Ο Νίκος δεν ξέρει **πού** υπάρχει. |
| Υπάρχει κανένας κάδος; _(да/нет)_ | Ο Πάμπλο ρώτησε **αν** υπάρχει κάδος. |
""")
    elif _lang == "el":
        _out = mo.md("""
## Πλάγιες Ερωτηματικές Προτάσεις (Για δες)

| Ευθεία ερώτηση | Πλάγια ερωτηματική |
|:---------------|:-------------------|
| **Τι** μπορώ να κάνω για το περιβάλλον; | Η Αρλέτα θέλει να μάθει **τι** μπορεί να κάνει. |
| **Πώς** θα πηγαίνεις στη δουλειά σου; | Ο Ερβίν ρώτησε **πώς** θα πηγαίνει. |
| **Πότε** φεύγεις; | Ο Φοίβος ρώτησε **πότε** φεύγει. |
| **Γιατί** πετάς την εφημερίδα στα σκουπίδια; | Ο Πάμπλο ρώτησε **γιατί** πετάει. |
| **Πού** υπάρχει κάδος ανακύκλωσης; | Ο Νίκος δεν ξέρει **πού** υπάρχει. |
| Υπάρχει κανένας κάδος; _(ναι/όχι)_ | Ο Πάμπλο ρώτησε **αν** υπάρχει κάδος. |
""")
    else:
        _out = mo.md("""
## Grammar: Indirect Questions (Πλάγιες Ερωτηματικές)

Direct questions become indirect clauses using the same question word:

| Direct question | Indirect (reported) |
|:----------------|:--------------------|
| **Τι** μπορώ να κάνω για το περιβάλλον; | Η Αρλέτα θέλει να μάθει **τι** μπορεί να κάνει. |
| **Πώς** θα πηγαίνεις στη δουλειά σου; | Ο Ερβίν ρώτησε **πώς** θα πηγαίνει. |
| **Πότε** φεύγεις; | Ο Φοίβος ρώτησε **πότε** φεύγει. |
| **Γιατί** πετάς την εφημερίδα στα σκουπίδια; | Ο Πάμπλο ρώτησε **γιατί** πετάει. |
| **Πού** υπάρχει κάδος ανακύκλωσης; | Ο Νίκος δεν ξέρει **πού** υπάρχει. |
| Υπάρχει κανένας κάδος; _(yes/no)_ | Ο Πάμπλο ρώτησε **αν** υπάρχει κάδος. |
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

Слова, начинающиеся с гласной, могут терять начальный звук после слова, оканчивающегося на гласную:

| Полная форма | Краткая форма | Пример |
|:-------------|:--------------|:-------|
| εγώ | 'γώ | Ξέρω **'γώ**; |
| εδώ | 'δώ | Από **'δώ** και πέρα |
| εκεί | 'κεί | Από **'κεί** |
""")
    elif _lang == "el":
        _out = mo.md("""
## Φωνή-γραφή: Αποκοπή

Λέξεις που αρχίζουν με φωνήεν μπορούν να χάσουν το αρχικό φωνήεν μετά από λέξη που τελειώνει σε φωνήεν:

| Πλήρης τύπος | Αποκοπή | Παράδειγμα |
|:-------------|:--------|:-----------|
| εγώ | 'γώ | Ξέρω **'γώ**; |
| εδώ | 'δώ | Από **'δώ** και πέρα |
| εκεί | 'κεί | Από **'κεί** |
""")
    else:
        _out = mo.md("""
## Pronunciation & Spelling (Φωνή-γραφή)

Words beginning with a vowel can drop it after a word ending in a vowel:

| Full form | Short form | Example |
|:----------|:-----------|:--------|
| εγώ | 'γώ | Ξέρω **'γώ**; / Ξέρω εγώ; |
| εδώ | 'δώ | Από **'δώ** και πέρα / Από εδώ και πέρα |
| εκεί | 'κεί | Από **'κεί** / Από εκεί |
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
    _cn = current_noun()
    _cs = captured_simple()
    _ca = captured_article()
    _lang = language_selector.value
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
def _(clear_button_n, clear_count_n, set_captured_article, set_captured_simple, set_clear_count_n):
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
    # Tense selector — language-dependent
    _lang = language_selector.value
    if _lang == "ru":
        _opts = {
            f"{gu.TENSE_LABELS['future_continuous']['greek']} (Длительное будущее)": "future_continuous",
            f"{gu.TENSE_LABELS['present']['greek']} (Настоящее)": "present",
            f"{gu.TENSE_LABELS['imperfect']['greek']} (Имперфект)": "imperfect",
            f"{gu.TENSE_LABELS['aorist']['greek']} (Аорист)": "aorist",
            f"{gu.TENSE_LABELS['future']['greek']} (Простое будущее)": "future",
        }
        _default = f"{gu.TENSE_LABELS['future_continuous']['greek']} (Длительное будущее)"
    elif _lang == "el":
        _opts = {
            f"{gu.TENSE_LABELS['future_continuous']['greek']} (Συνεχής Μέλλοντας)": "future_continuous",
            f"{gu.TENSE_LABELS['present']['greek']} (Ενεστώτας)": "present",
            f"{gu.TENSE_LABELS['imperfect']['greek']} (Παρατατικός)": "imperfect",
            f"{gu.TENSE_LABELS['aorist']['greek']} (Αόριστος)": "aorist",
            f"{gu.TENSE_LABELS['future']['greek']} (Απλός Μέλλοντας)": "future",
        }
        _default = f"{gu.TENSE_LABELS['future_continuous']['greek']} (Συνεχής Μέλλοντας)"
    else:
        _opts = {
            f"{gu.TENSE_LABELS['future_continuous']['greek']} (Continuous Future)": "future_continuous",
            f"{gu.TENSE_LABELS['present']['greek']} (Present)": "present",
            f"{gu.TENSE_LABELS['imperfect']['greek']} (Imperfect)": "imperfect",
            f"{gu.TENSE_LABELS['aorist']['greek']} (Aorist)": "aorist",
            f"{gu.TENSE_LABELS['future']['greek']} (Simple Future)": "future",
        }
        _default = f"{gu.TENSE_LABELS['future_continuous']['greek']} (Continuous Future)"
    tense_selector = mo.ui.dropdown(options=_opts, value=_default, label=t_ui("tense_label", _lang))
    tense_selector
    return (tense_selector,)


@app.cell(hide_code=True)
def _(gu, mo, random, session_total_v, set_session_total_v, table_verb):
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
    cv_verb, set_cv_verb = mo.state(None)
    if words_verb and cv_verb() is None:
        set_cv_verb(random.choice(words_verb))
    return (
        captured_verb,
        clear_button_v,
        clear_count_v,
        cv_verb,
        set_captured_verb,
        set_clear_count_v,
        set_cv_verb,
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
def _(clear_count_v, cv_verb, gu, tense_selector, words4test_verb, words_verb):
    # Verb form
    clear_count_v()
    _cv = cv_verb()
    _tense_key = tense_selector.value
    _ui_label = gu.TENSE_LABELS[_tense_key]['greek'] if _tense_key else "—"
    verb_fields, _ = gu.create_verb_test_ui(_ui_label, words_verb, words4test_verb(), _cv)
    return (verb_fields,)


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
        _cv = cv_verb()
        _c = captured_verb()
        if _cv and _c and getattr(_c, 'verb_word', None) == _cv['Word'] and getattr(_c, 'tense', None) == tense_selector.value:
            _, _msg = gu.check_verb_test(_cv['Word'], _c, tense_selector.value)
            _feedback_v = mo.md(_msg)
        _label = _TENSE_LABELS.get(tense_selector.value, tense_selector.value)
        _rem = len(words4test_verb())
        _items = [mo.md(f"{t_ui('verb_heading', _lang)} — {_label} ({_rem}/{session_total_v()})")]
        if verb_msg():
            _items.append(mo.md(verb_msg()))
        _items += [
            mo.md(f"{t_ui('translation_label', _lang)} **{_cv['Translation']}**") if _cv else mo.md(""),
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
    random,
    session_total_v,
    set_captured_verb,
    set_cv_verb,
    set_tbl_sel_v,
    set_verb_msg,
    set_words4test_verb,
    t_ui,
    tense_selector,
    words4test_verb,
):
    # Verb pass handler
    _tense_key = tense_selector.value
    _c = captured_verb()
    _cv = cv_verb()
    _lang = language_selector.value
    if _cv and _tense_key and _c and getattr(_c, 'verb_word', None) == _cv['Word'] and getattr(_c, 'tense', None) == _tense_key:
        _ok, _ = gu.check_verb_test(_cv['Word'], _c, _tense_key)
        if _ok:
            _new = [w for w in words4test_verb() if w['Word'] != _cv['Word']]
            set_words4test_verb(_new)
            if df_verb is not None:
                _rem = {w['Word'] for w in _new}
                set_tbl_sel_v([i for i, w in enumerate(df_verb['Word']) if w in _rem])
            set_verb_msg(t_ui("verb_passed", _lang).format(word=_cv["Word"], trans=_cv["Translation"], remaining=len(_new), total=session_total_v()))
            set_captured_verb(None)
            set_cv_verb(random.choice(_new) if _new else None)
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
        _cv = cv_verb()
        if _cv and verb_fields:
            set_captured_verb(gu.make_snapshot(verb_fields, verb_word=_cv['Word'], tense=tense_selector.value))
    return


@app.cell(hide_code=True)
def _(
    cv_verb,
    df_verb,
    random,
    set_captured_verb,
    set_cv_verb,
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
        _cv = cv_verb()
        if words4test_verb():
            _new = [w for w in words4test_verb() if not _cv or w['Word'] != _cv['Word']]
            set_words4test_verb(_new)
            if df_verb is not None:
                _rem = {w['Word'] for w in _new}
                set_tbl_sel_v([i for i, w in enumerate(df_verb['Word']) if w in _rem])
            set_cv_verb(random.choice(_new) if _new else None)
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
    adj_form, _ = gu.create_adjective_test_ui([] if not _acv else [_acv], [], _acv, mode=mode_selector.value)
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
    if words4test_adj() and _adj:
        _feedback_a = mo.md("")
        _c = captured_adj()
        if _c and getattr(_c, 'adj_word', None) == _adj['Word']:
            _, _msg = gu.check_adjective_test(_adj['Word'], _c, mode=mode_selector.value)
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
    _adj = adj_cv()
    _c = captured_adj()
    _lang = language_selector.value
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
def _():
    # UI strings — static dict, no language_selector dependency to avoid cascading resets
    UI_STRINGS = {
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
            "adj_passed":  '<span style="color:green;">Test for <b>"{word} — {trans}"</b> passed.\n\n{remaining} words remaining out of {total}.</span>',
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
            "adj_passed":  '<span style="color:green;">Тест для <b>"{word} — {trans}"</b> пройден.\n\n{remaining} слов осталось из {total}.</span>',
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
            "adj_passed":  '<span style="color:green;">Τεστ για <b>"{word} — {trans}"</b> ολοκληρώθηκε.\n\n{remaining} λέξεις απομένουν από {total}.</span>',
        },
    }

    def t_ui(key, lang=None):
        _lang = lang if lang else "en"
        return UI_STRINGS.get(_lang, UI_STRINGS["en"]).get(key, UI_STRINGS["en"].get(key, key))

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
    from modern_greek_eee import greek_utils as gu
    notebook_dir = os.path.dirname(os.path.abspath(__file__))
    return gu, mo, notebook_dir, os, pd, random


if __name__ == "__main__":
    app.run()
