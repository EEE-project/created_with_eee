# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.23.14",
#     "eee-project>=1.1.0",
#     "ancient-greek-backend-eee>=2.0.0",
#     "unimorph-backend-eee>=1.0.3",
#     "modern-greek-backend-eee>=1.0.0",
# ]
# ///

import marimo

__generated_with = "0.23.13"
app = marimo.App(
    width="medium",
    app_title="Одиссея с Гомером — День 1: Одиссея IX.19–38",
)


@app.cell(hide_code=True)
def _(lang_sel, mo):
    from eee_project import ConfigStore, eee_topbar
    _ROOT = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main"
    cfg = ConfigStore.from_file_or_url(__file__, f"{_ROOT}/ancient_greek/odyssey/index.tsv", ga=f"{_ROOT}/ga.json")
    eee_topbar(mo, back_url=cfg.index_url(), lang=lang_sel.value, titles={
        "ru": "Одиссея с Гомером",
        "en": "Odyssey with Homer",
        "el": "Οδύσσεια με τον Όμηρο",
    }, ga_config=cfg.ga_config(), same_window=True)
    return (cfg,)


@app.cell(hide_code=True)
def _(cfg):
    import pathlib as _pl
    # Course-local lexicon files (moved from greek-inflexion-eee 2026-07-31,
    # see this course's own AGENTS.md) -- Epic-register, Odyssey-course-
    # vocabulary-specific data merged into ag_backend/ag_homer below,
    # alongside homer (same register), not lsj/byzantine (Attic/Koine).
    _odyssey_yamls = [_pl.Path(__file__).parent.parent / f"odyssey_morpheus_{_p}_lexicon.yaml" for _p in ("adjs", "nouns", "verbs")]
    from eee_project import GreekUtils as _GU
    for _y in _odyssey_yamls:
        _GU.ensure_file(_y.name, nb_dir=_y.parent, remote_base=cfg.raw_base)
    ODYSSEY_EXTRA_LEXICONS = [str(_y.resolve()) for _y in _odyssey_yamls]
    return (ODYSSEY_EXTRA_LEXICONS,)


@app.cell(hide_code=True)
def _(eee, lang_sel, mo):
    from pathlib import Path as _Ph
    _TITLES = {
        "ru": ("# Одиссея с Гомером", "## День 1 · Odyss. IX.19–38"),
        "en": ("# Odyssey with Homer", "## Day 1 · Odyss. IX.19–38"),
        "el": ("# Οδύσσεια με τον Όμηρο", "## Ημέρα 1 · Odyss. IX.19–38"),
    }
    _h1, _h2 = _TITLES.get(lang_sel.value, _TITLES["ru"])
    _left = mo.vstack([
        mo.md(_h1),
        mo.md(_h2),
    ])
    _img = eee.magnify_image(mo, _Ph(__file__).parent / "map_ithaca.jpg", raw_base="https://codeberg.org/EEE-project/created_with_eee/raw/branch/main/ancient_greek/odyssey/2026_06_15", width=280)
    mo.hstack([_left, _img], align="start")
    return


@app.cell(hide_code=True)
def _(gu, lang_sel, mo):
    _base = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main/ancient_greek/odyssey/2026_06_15"
    mo.md(
        f"{gu.ui_label('lesson_materials_label', lang_sel.value)} "
        f"[Одиссея 1.pdf]({_base}/Одиссея%201.pdf) · "
        f"[слова день 1.pdf]({_base}/слова%20день%201.pdf) · "
        "[odysseus-unbound.org ↗](https://www.odysseus-unbound.org/mystery/)"
    )
    return


@app.cell(hide_code=True)
def _(eee, lang_sel, mo):
    from pathlib import Path as _Pe
    _etm = _Pe(__file__).parent / "etymologicum_magnum_odysseus.jpg"
    _etimg = eee.magnify_image(mo, _etm, raw_base="https://codeberg.org/EEE-project/created_with_eee/raw/branch/main/ancient_greek/odyssey/2026_06_15", width=460)
    _TXT = {
        "ru": r"""
    ---
    ## Имя героя

    **Ὀδυσσεύς** ← **ὀδύσσομαι** — гневаться, ненавидеть; причинять страдание

    > *πολλοῖσιν γὰρ ἐγώ γε ὀδυσσάμενος* (Od. XIX.407)
    > «ибо многим я причинил страдание»

    Имя означает «тот, кто причиняет / претерпевает страдания». Гомер использует его как этимологический символ судьбы героя.

    [«Μέγα Ἐτυμολογικόν»](https://el.wikipedia.org/wiki/Μέγα_Ετυμολογικόν)
    («Большой этимологический словарь») — крупнейший византийский лексикон,
    составленный неизвестным автором в первой половине XII века на основе
    более ранних словарей; помимо не всегда точных этимологий, он сохранил
    немало фрагментов античных текстов, иначе утраченных
    ([издание Ф. Зильбурга, 1816↗](https://archive.org/details/etymologikontome00etymuoft)),
    объясняет имя иначе — связывая с **ὁδός** «путь, дорога»:

    > **κατὰ τὴν ὁδὸν ὗσεν ὁ Ζεύς**
    > «в пути пролил дождь Зевс»

    Беременная Антиклея, мать Одиссея, шла через гору Нерит на Итаке; Зевс
    пролил сильный дождь, и она от муки и страха упала наземь и родила
    сына — так он получил имя, потому что в пути (ὁδός) Зевс пролил дождь
    (ὗσεν).
    """,
        "en": r"""
    ---
    ## Name of the Hero

    **Ὀδυσσεύς** ← **ὀδύσσομαι** — to be angry, to hate; to cause suffering

    > *πολλοῖσιν γὰρ ἐγώ γε ὀδυσσάμενος* (Od. XIX.407)
    > "for I have caused suffering to many"

    The name means "the one who causes / endures suffering." Homer uses it as an etymological symbol of the hero's fate.

    [«Μέγα Ἐτυμολογικόν»](https://el.wikipedia.org/wiki/Μέγα_Ετυμολογικόν)
    ("The Great Etymological Dictionary") — the largest Byzantine lexicon,
    compiled by an unknown author in the first half of the 12th century from
    earlier dictionaries; alongside not always accurate etymologies, it preserved
    many fragments of ancient texts otherwise lost
    ([F. Sylburg's 1816 edition ↗](https://archive.org/details/etymologikontome00etymuoft)),
    explains the name differently — linking it to **ὁδός** "way, road":

    > **κατὰ τὴν ὁδὸν ὗσεν ὁ Ζεύς**
    > "on the road Zeus rained down"

    Anticleia, Odysseus's mother, was pregnant and walking across Mount Neriton on
    Ithaca; Zeus sent down a heavy rain, and she, from pain and fear, fell to the
    ground and gave birth to her son — so he received his name, because on the
    road (ὁδός) Zeus rained (ὗσεν).
    """,
        "el": r"""
    ---
    ## Το όνομα του ήρωα

    **Ὀδυσσεύς** ← **ὀδύσσομαι** — οργίζομαι, μισώ· προκαλώ πόνο

    > *πολλοῖσιν γὰρ ἐγώ γε ὀδυσσάμενος* (Οδ. XIX.407)
    > «γιατί σε πολλούς προκάλεσα πόνο»

    Το όνομα σημαίνει «αυτός που προκαλεί / υφίσταται πόνο». Ο Όμηρος το χρησιμοποιεί ως ετυμολογικό σύμβολο της μοίρας του ήρωα.

    Το [«Μέγα Ἐτυμολογικόν»](https://el.wikipedia.org/wiki/Μέγα_Ετυμολογικόν)
    — το μεγαλύτερο βυζαντινό λεξικό, συνταγμένο από άγνωστο συγγραφέα στο
    πρώτο μισό του 12ου αιώνα με βάση παλαιότερα λεξικά· εκτός από ετυμολογίες
    όχι πάντα ακριβείς, διέσωσε πολλά αποσπάσματα αρχαίων κειμένων που
    διαφορετικά θα είχαν χαθεί
    ([έκδοση F. Sylburg, 1816 ↗](https://archive.org/details/etymologikontome00etymuoft)),
    εξηγεί το όνομα διαφορετικά — συνδέοντάς το με το **ὁδός** «δρόμος»:

    > **κατὰ τὴν ὁδὸν ὗσεν ὁ Ζεύς**
    > «στον δρόμο έβρεξε ο Δίας»

    Η έγκυος Αντίκλεια, η μητέρα του Οδυσσέα, περπατούσε στο όρος Νήριτον της
    Ιθάκης· ο Δίας έριξε δυνατή βροχή, κι εκείνη από τον πόνο και τον φόβο
    έπεσε καταγής και γέννησε τον γιο της — έτσι πήρε το όνομά του, επειδή
    στον δρόμο (ὁδός) ο Δίας έβρεξε (ὗσεν).
    """,
    }
    mo.vstack([
        mo.md(_TXT.get(lang_sel.value, _TXT["ru"])),
        _etimg,
    ])
    return


@app.cell(hide_code=True)
def _(eee, lang_sel, mo):
    from pathlib import Path as _Pg
    _gen = _Pg(__file__).parent / "genealogy.jpg"
    _gimg = eee.magnify_image(mo, _gen, raw_base="https://codeberg.org/EEE-project/created_with_eee/raw/branch/main/ancient_greek/odyssey/2026_06_15", width=560)
    _TXT = {
        "ru": r"""
    ---
    ## Родословная Одиссея

    Одиссей — не просто хитрец-самоучка: хитроумие у него в крови. По материнской
    линии его дед — **Автолик**, сын Гермеса, славившийся воровским мастерством и
    умением обходить клятвы; от него и досталась внуку слава хитроумнейшего из
    героев. По отцовской линии Одиссей восходит через Аркесия к самому Эолу
    (Айолу). Отец — **Лаэрт**, мать — **Антиклея**, дочь Автолика. Жена —
    **Пенелопа**, дочь Икария; сын — **Телемах**.
    """,
        "en": r"""
    ---
    ## The Genealogy of Odysseus

    Odysseus is no mere self-taught trickster: cunning runs in his blood. On his
    mother's side, his grandfather is **Autolycus**, son of Hermes, famed for his
    skill in thievery and his knack for evading oaths; it is from him that his
    grandson inherited his reputation as the most cunning of heroes. On his
    father's side, Odysseus traces his line through Arcesius back to Aeolus
    himself. His father is **Laertes**, his mother **Anticleia**, daughter of
    Autolycus. His wife is **Penelope**, daughter of Icarius; his son,
    **Telemachus**.
    """,
        "el": r"""
    ---
    ## Η γενεαλογία του Οδυσσέα

    Ο Οδυσσέας δεν είναι απλώς ένας αυτοδίδακτος πονηρός: η πονηριά είναι στο αίμα
    του. Από τη μητρική γραμμή, παππούς του είναι ο **Αυτόλυκος**, γιος του Ερμή,
    φημισμένος για την κλεπτική του δεινότητα και την ικανότητά του να ξεφεύγει
    από όρκους· από εκείνον κληρονόμησε ο εγγονός του τη φήμη του πιο πονηρού
    από τους ήρωες. Από την πατρική γραμμή, ο Οδυσσέας ανάγεται μέσω του Αρκεισίου
    στον ίδιο τον Αίολο. Πατέρας του είναι ο **Λαέρτης**, μητέρα του η
    **Αντίκλεια**, κόρη του Αυτόλυκου. Σύζυγός του η **Πηνελόπη**, κόρη του
    Ικάριου· γιος του, ο **Τηλέμαχος**.
    """,
    }
    mo.vstack([
        mo.md(_TXT.get(lang_sel.value, _TXT["ru"])),
        _gimg,
    ])
    return


@app.cell(hide_code=True)
def _(eee, lang_sel, mo):
    from pathlib import Path as _Pn
    _ner = _Pn(__file__).parent / "neriton_epithet.jpg"
    _nimg = eee.magnify_image(mo, _ner, raw_base="https://codeberg.org/EEE-project/created_with_eee/raw/branch/main/ancient_greek/odyssey/2026_06_15", width=560)
    _TXT = {
        "ru": r"""
    ---
    ## ἐνοσίχθων и εἰνοσίφυλλος

    **ἐνοσίχθων** («сотрясающий землю») — постоянный эпитет Посейдона:
    *ἐνοσι-* «сотрясение» + *χθών* «земля».

    Тем же корнем образован эпитет горы Нерит на Итаке — **εἰνοσίφυλλος**
    («колышущий листвой», *ἐνοσι-* + *φύλλον* «лист»). Он звучит и в нашем
    тексте (IX.21–22):

    > **Νήριτον εἰνοσίφυλλον, ἀριπρεπές** — «Нерит, колышущий листвой, заметный издалека»

    и в «Илиаде» (Β.631–632), где гора Нерит названа тем же словом.
    """,
        "en": r"""
    ---
    ## ἐνοσίχθων and εἰνοσίφυλλος

    **ἐνοσίχθων** ("earth-shaker") — a standing epithet of Poseidon:
    *ἐνοσι-* "shaking" + *χθών* "earth".

    The same root forms the epithet of Mount Neriton on Ithaca —
    **εἰνοσίφυλλος** ("leaf-shaking", *ἐνοσι-* + *φύλλον* "leaf"). It appears
    in our text too (IX.21–22):

    > **Νήριτον εἰνοσίφυλλον, ἀριπρεπές** — "Neriton, leaf-shaking, conspicuous from afar"

    and in the *Iliad* (Β.631–632), where Mount Neriton is called by the same word.
    """,
        "el": r"""
    ---
    ## ἐνοσίχθων και εἰνοσίφυλλος

    **ἐνοσίχθων** («αυτός που σείει τη γη») — πάγιο επίθετο του Ποσειδώνα:
    *ἐνοσι-* «σεισμός» + *χθών* «γη».

    Από την ίδια ρίζα σχηματίζεται και το επίθετο του όρους Νήριτον στην
    Ιθάκη — **εἰνοσίφυλλος** («αυτό που σείει τα φύλλα», *ἐνοσι-* + *φύλλον*
    «φύλλο»). Απαντά και στο κείμενό μας (IX.21–22):

    > **Νήριτον εἰνοσίφυλλον, ἀριπρεπές** — «το Νήριτον, που σείει τα φύλλα του, ξεχωριστό από μακριά»

    καθώς και στην *Ιλιάδα* (Β.631–632), όπου το όρος Νήριτον ονομάζεται με την ίδια λέξη.
    """,
    }
    mo.vstack([
        mo.md(_TXT.get(lang_sel.value, _TXT["ru"])),
        _nimg,
    ])
    return


@app.cell(hide_code=True)
def _(eee, lang_sel, mo):
    from pathlib import Path as _Pi
    _ith = _Pi(__file__).parent / "ithaca_kefalonia.jpg"
    _iimg = eee.magnify_image(mo, _ith, raw_base="https://codeberg.org/EEE-project/created_with_eee/raw/branch/main/ancient_greek/odyssey/2026_06_15", width=460)
    _TXT = {
        "ru": r"""
    ---
    ## Итака и соседние острова

    Одиссей сам описывает своё окружение (IX.22–24):

    > **ἀμφὶ δὲ νῆσοι πολλαὶ ναιετάουσι μάλα σχεδὸν ἀλλήλῃσι,
    > Δουλίχιόν τε Σάμη τε καὶ ὑλήεσσα Ζάκυνθος.**
    > «а вокруг лежат близко друг к другу многие острова:
    > Дулихий, Сама и лесистый Закинф»

    На фотографии — закат над Ионическим морем; на горизонте подписаны
    Кефалония и, чуть дальше, сама Итака.
    """,
        "en": r"""
    ---
    ## Ithaca and the Neighboring Islands

    Odysseus himself describes his surroundings (IX.22–24):

    > **ἀμφὶ δὲ νῆσοι πολλαὶ ναιετάουσι μάλα σχεδὸν ἀλλήλῃσι,
    > Δουλίχιόν τε Σάμη τε καὶ ὑλήεσσα Ζάκυνθος.**
    > "and around it lie many islands close to one another:
    > Dulichium, Same, and wooded Zacynthus"

    The photograph shows a sunset over the Ionian Sea; on the horizon,
    Cephalonia is labeled and, a little farther, Ithaca itself.
    """,
        "el": r"""
    ---
    ## Η Ιθάκη και τα γειτονικά νησιά

    Ο ίδιος ο Οδυσσέας περιγράφει το περιβάλλον του (IX.22–24):

    > **ἀμφὶ δὲ νῆσοι πολλαὶ ναιετάουσι μάλα σχεδὸν ἀλλήλῃσι,
    > Δουλίχιόν τε Σάμη τε καὶ ὑλήεσσα Ζάκυνθος.**
    > «κι ολόγυρα κατοικούνται πολλά νησιά, πολύ κοντά το ένα στο άλλο:
    > το Δουλίχιο, η Σάμη και η δασωμένη Ζάκυνθος»

    Στη φωτογραφία, ένα ηλιοβασίλεμα πάνω από το Ιόνιο Πέλαγος· στον ορίζοντα
    σημειώνονται η Κεφαλονιά και, λίγο πιο πέρα, η ίδια η Ιθάκη.
    """,
    }
    mo.vstack([
        mo.md(_TXT.get(lang_sel.value, _TXT["ru"])),
        _iimg,
    ])
    return


@app.cell(hide_code=True)
def _(lang_sel, mo):
    _TXT = {
        "ru": r"""
    ---
    ## Загадка гомеровской Итаки

    Сам Одиссей описывает свой остров дальше в поэме (IX.25-28):

    > **αὐτὴ δὲ χθαμαλὴ πανυπερτάτη εἰν ἁλὶ κεῖται
    > πρὸς ζόφον, αἱ δέ τ᾽ ἄνευθε πρὸς ἠῶ τ᾽ ἠέλιόν τε**
    > «она сама, невысокая, лежит самой крайней в море
    > к западу, а прочие острова - поодаль, к заре и солнцу»

    Но современная Итака гористая и не самая западная среди соседних островов -
    описанию Гомера это не соответствует. Ионические острова лежат на активной
    тектонической границе африканской и евразийской плит и часто страдают от
    землетрясений (катастрофическое - в 1953 году; в 2014-м суша у залива
    Ливади поднялась на 20 см). Гипотеза в том, что сейсмическая активность
    могла изменить очертания архипелага со времён Гомера - и что описанная им
    Итака лежала не там, где сегодняшняя. Подробнее:
    [odysseus-unbound.org ↗](https://www.odysseus-unbound.org/mystery/).
    """,
        "en": r"""
    ---
    ## The Riddle of Homeric Ithaca

    Odysseus himself describes his island further on in the poem (IX.25-28):

    > **αὐτὴ δὲ χθαμαλὴ πανυπερτάτη εἰν ἁλὶ κεῖται
    > πρὸς ζόφον, αἱ δέ τ᾽ ἄνευθε πρὸς ἠῶ τ᾽ ἠέλιόν τε**
    > "it itself, low-lying, lies furthest out to sea
    > toward the west, while the others lie apart, toward the dawn and the sun"

    But modern Ithaca is mountainous and not the westernmost among its
    neighboring islands — this doesn't match Homer's description. The Ionian
    Islands sit on an active tectonic boundary between the African and Eurasian
    plates and often suffer earthquakes (a catastrophic one in 1953; in 2014 the
    land near Livadi bay rose by 20 cm). The hypothesis is that seismic activity
    could have changed the shape of the archipelago since Homer's time — and
    that the Ithaca he described did not lie where today's Ithaca does. More at:
    [odysseus-unbound.org ↗](https://www.odysseus-unbound.org/mystery/).
    """,
        "el": r"""
    ---
    ## Το αίνιγμα της ομηρικής Ιθάκης

    Ο ίδιος ο Οδυσσέας περιγράφει το νησί του παρακάτω στο ποίημα (IX.25-28):

    > **αὐτὴ δὲ χθαμαλὴ πανυπερτάτη εἰν ἁλὶ κεῖται
    > πρὸς ζόφον, αἱ δέ τ᾽ ἄνευθε πρὸς ἠῶ τ᾽ ἠέλιόν τε**
    > «αυτή, χαμηλή, βρίσκεται η πιο ακρινή μέσα στη θάλασσα
    > προς τη δύση, ενώ τα άλλα βρίσκονται πιο πέρα, προς την αυγή και τον ήλιο»

    Όμως η σημερινή Ιθάκη είναι ορεινή και όχι η πιο δυτική ανάμεσα στα γειτονικά
    νησιά — αυτό δεν ταιριάζει με την περιγραφή του Ομήρου. Τα Ιόνια Νησιά
    βρίσκονται πάνω σε ενεργό τεκτονικό όριο μεταξύ της αφρικανικής και της
    ευρασιατικής πλάκας και συχνά πλήττονται από σεισμούς (καταστροφικός το
    1953· το 2014 η ξηρά κοντά στον κόλπο Λιβάδι ανυψώθηκε κατά 20 εκ.). Η
    υπόθεση είναι ότι η σεισμική δραστηριότητα μπορεί να άλλαξε το σχήμα του
    αρχιπελάγους από την εποχή του Ομήρου — και ότι η Ιθάκη που περιέγραψε δεν
    βρισκόταν εκεί όπου βρίσκεται η σημερινή. Περισσότερα:
    [odysseus-unbound.org ↗](https://www.odysseus-unbound.org/mystery/).
    """,
    }
    mo.md(_TXT.get(lang_sel.value, _TXT["ru"]))
    return


@app.cell(hide_code=True)
def _(lang_sel, mo):
    _TXT = {
        "ru": r"""
    ---
    ## Грамматическая памятка для начинающих моряков

    - **ἐνίσπω** — форма аориста конъюнктива 1 л. ед. ч. от ἐνέπω (не
      настоящее время, несмотря на окончание **-ω**)
    - **οὐρανὸν** — окончание **-ν** характерно для винительного падежа ед. числа
    - **νῆσος** – **νῆσοι** — остров-острова, именительный падеж ед. и мн. числа
    - **αὐτός** – **αὐτή** — сам-сама, мужской и женский род (часто обозначаются
      окончаниями **-ος** и **-η**)
    """,
        "en": r"""
    ---
    ## Grammar Notes for Beginning Sailors

    - **ἐνίσπω** — aorist subjunctive, 1st person singular, of ἐνέπω (not
      present tense, despite the **-ω** ending)
    - **οὐρανὸν** — the **-ν** ending is typical of the accusative singular
    - **νῆσος** – **νῆσοι** — island–islands, nominative singular and plural
    - **αὐτός** – **αὐτή** — himself–herself, masculine and feminine (often
      marked by the endings **-ος** and **-η**)
    """,
        "el": r"""
    ---
    ## Γραμματική υπενθύμιση για αρχάριους ναυτικούς

    - **ἐνίσπω** — τύπος υποτακτικής αορίστου, 1ο πρόσωπο ενικού, του ἐνέπω
      (όχι ενεστώτας, παρά την κατάληξη **-ω**)
    - **οὐρανὸν** — η κατάληξη **-ν** είναι χαρακτηριστική της αιτιατικής ενικού
    - **νῆσος** – **νῆσοι** — νησί–νησιά, ονομαστική ενικού και πληθυντικού
    - **αὐτός** – **αὐτή** — ο ίδιος–η ίδια, αρσενικό και θηλυκό γένος (συχνά
      δηλώνονται με τις καταλήξεις **-ος** και **-η**)
    """,
    }
    mo.md(_TXT.get(lang_sel.value, _TXT["ru"]))
    return


@app.cell(hide_code=True)
def _(gu, lang_sel, mo):
    mo.md(f"""
    ---
    {gu.ui_label('poem_section_heading', lang_sel.value)}
    """)
    return


@app.cell(hide_code=True)
def _(TRANS_DESC: dict, gu, lang_sel, mo, trans_selector):
    _desc_map = {"подстрочник": gu.ui_label('interlinear_description', lang_sel.value), **TRANS_DESC}
    mo.md(_desc_map.get(trans_selector.value, ""))
    return


@app.cell(hide_code=True)
def _(cfg, gu, lang_sel, mo):
    from pathlib import Path as _P
    SHOW_ICTUS = mo.ui.switch(value=True)
    SHOW_HOMER = mo.ui.switch(value=True)

    # Shared across all 6 lessons. Fetched via ensure_file, not a bare local
    # read: molab only bundles files that live in the notebook's own directory,
    # so a parent-directory file like this one is missing there unless we
    # download it ourselves (matches the pattern already used for materials PDFs).
    _eee_note_path = gu.ensure_file(
        "eee_note.md", nb_dir=_P(__file__).parent.parent, remote_base=cfg.raw_base,
    )
    EEE_NOTE = _eee_note_path.read_text(encoding="utf-8") if _eee_note_path else (
        gu.ui_label('eee_note_load_error', lang_sel.value)
    )

    _ICTUS_COLOR_NAME = {"ru": "красным", "en": "red", "el": "κόκκινο"}
    gu.ictus_toggle_panel(SHOW_ICTUS, SHOW_HOMER, EEE_NOTE,
                           ictus_color="#980000",
                           ictus_color_name=_ICTUS_COLOR_NAME.get(lang_sel.value, "красным"),
                           lang=lang_sel.value)
    return EEE_NOTE, SHOW_HOMER, SHOW_ICTUS


@app.cell(hide_code=True)
def _(
    CLICKABLE_FORMS,
    HOMER_WORDS,
    RHYTHM_HTML,
    SHOW_HOMER,
    SHOW_ICTUS,
    STANZAS,
    eee,
    mo,
    stanza_selector,
    trans_selector,
):
    _st_map = {s["ref"]: s for s in STANZAS}
    _stanza = _st_map[stanza_selector.value]

    text_widget = eee.interactive_text(
        mo,
        lines=_stanza["lines"],
        clickable=CLICKABLE_FORMS,
        homer_words=HOMER_WORDS if SHOW_HOMER.value else set(),
        ictus_html=RHYTHM_HTML,
        show_ictus=SHOW_ICTUS.value,
    )

    _txt_lines = _stanza["translations"].get(trans_selector.value, "—").split("\n")

    _line_divs = "".join(
        f'<div>{line.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")}</div>'
        for line in _txt_lines
    )
    _right = mo.Html(
        '<div style="font-size:1.0em;display:flex;flex-direction:column;'
        'justify-content:space-between;border-left:3px solid #ccc;padding-left:0.8em">'
        + _line_divs + "</div>"
    )

    mo.vstack([
        mo.hstack([stanza_selector, trans_selector], justify="space-between"),
        mo.hstack([text_widget, _right], justify="start", align="stretch", gap=1.5),
    ])
    return (text_widget,)


@app.cell(hide_code=True)
def _(QUIZ_WORDS_RAW, build_lexicon_tabs, gu, lang_sel, text_widget):
    gu.render_gloss_panel(QUIZ_WORDS_RAW, text_widget.widget.selected_word, build_lexicon_tabs, lang=lang_sel.value)
    return


@app.cell(hide_code=True)
def _(EEE_NOTE, gu, lang_sel, mo):
    mo.accordion({gu.ui_label('form_check_accordion_label', lang_sel.value): EEE_NOTE})
    return


@app.cell(hide_code=True)
def _(gu, lang_sel, mo):
    mo.md(f"""
    ---
    {gu.ui_label('exercises_section_heading', lang_sel.value)}
    """)
    return


@app.cell(hide_code=True)
def _():
    # Shared per-lesson default: how many items each exercise below draws per
    # session. Change this one value to affect every exercise at once, or
    # override a single exercise by editing its own n=SESSION_SIZE argument.
    SESSION_SIZE = 10
    return (SESSION_SIZE,)


@app.cell(hide_code=True)
def _(gu, lang_sel):
    quiz_renew_btn = gu.make_renew_button(lang=lang_sel.value)
    return (quiz_renew_btn,)


@app.cell(hide_code=True)
def _(QUIZ_WORDS, cv, gu, history, lang_sel, remaining, restore_entry):
    _ = cv()
    answer_radio, next_btn, prev_btn = gu.word_quiz_widgets(
        cv=cv(),
        remaining=remaining(),
        vocab=QUIZ_WORDS,
        restore_entry=restore_entry(),
        history_len=len(history()),
        lang=lang_sel.value,
    )
    return answer_radio, next_btn, prev_btn


@app.cell(hide_code=True)
def _(
    QUIZ_WORDS,
    answer_radio,
    cv,
    future,
    gu,
    history,
    lang_sel,
    next_btn,
    prev_btn,
    quiz_renew_btn,
    remaining,
    restore_entry,
    score,
    set_cv,
    set_future,
    set_history,
    set_remaining,
    set_restore_entry,
    set_score,
):
    gu.word_quiz_form(
        cv, set_cv, remaining, set_remaining,
        score, set_score, restore_entry, set_restore_entry,
        history, set_history, future, set_future,
        answer_radio, next_btn, prev_btn,
        vocab=QUIZ_WORDS,
        title=gu.ui_label('word_find_exercise_heading', lang_sel.value),
        meaning_key='_label',
        form_key='form',
        lang=lang_sel.value,
        renew_btn=quiz_renew_btn,
    )
    return


@app.cell(hide_code=True)
def _(gu, lang_sel, mo):
    mo.md(gu.ui_label('stanza_match_section_heading', lang_sel.value))
    return


@app.cell(hide_code=True)
def _(gu, lang_sel, mo):
    _DIRECTION_OPTS = {
        gu.ui_label('stanza_match_toggle_grc_to_tr', lang_sel.value): "grc_to_tr",
        gu.ui_label('stanza_match_toggle_tr_to_grc', lang_sel.value): "tr_to_grc",
    }
    sm_direction = mo.ui.radio(
        options=_DIRECTION_OPTS,
        value=list(_DIRECTION_OPTS.keys())[0],
        label=gu.ui_label('stanza_match_direction_label', lang_sel.value),
        inline=True,
    )
    sm_direction
    return (sm_direction,)


@app.cell(hide_code=True)
def _(mo):
    sm_cv, sm_set_cv = mo.state(None)
    sm_score, sm_set_score = mo.state({"correct": 0, "total": 0})
    sm_remaining, sm_set_remaining = mo.state(None)
    sm_history, sm_set_history = mo.state([])
    sm_future, sm_set_future = mo.state([])
    sm_restore_entry, sm_set_restore_entry = mo.state(None)
    return (
        sm_cv,
        sm_future,
        sm_history,
        sm_remaining,
        sm_restore_entry,
        sm_score,
        sm_set_cv,
        sm_set_future,
        sm_set_history,
        sm_set_remaining,
        sm_set_restore_entry,
        sm_set_score,
    )


@app.cell(hide_code=True)
def _(sm_direction, sm_set_cv, sm_set_remaining):
    _ = sm_direction.value
    sm_set_cv(None)
    sm_set_remaining(None)
    return


@app.cell(hide_code=True)
def _(
    SESSION_SIZE,
    STANZAS,
    gu,
    sm_renew_btn,
    sm_set_cv,
    sm_set_future,
    sm_set_history,
    sm_set_remaining,
    sm_set_restore_entry,
    sm_set_score,
):
    SM_STANZAS = gu.sample_session_items(STANZAS, n=SESSION_SIZE)
    gu.reset_quiz_state(sm_renew_btn, sm_set_cv, sm_set_remaining, sm_set_score,
                         sm_set_history, sm_set_future, sm_set_restore_entry)
    return (SM_STANZAS,)


@app.cell(hide_code=True)
def _(gu, lang_sel):
    sm_renew_btn = gu.make_renew_button(lang=lang_sel.value)
    return (sm_renew_btn,)


@app.cell(hide_code=True)
def _(
    SM_STANZAS,
    gu,
    lang_sel,
    sm_cv,
    sm_direction,
    sm_history,
    sm_remaining,
    sm_restore_entry,
):
    _ = sm_cv()
    sm_choice_radio, sm_next_btn, sm_prev_btn = gu.stanza_match_widgets(
        cv=sm_cv(),
        remaining=sm_remaining(),
        stanzas=SM_STANZAS,
        direction=sm_direction.value,
        restore_entry=sm_restore_entry(),
        history_len=len(sm_history()),
        lang=lang_sel.value,
    )
    return sm_choice_radio, sm_next_btn, sm_prev_btn


@app.cell(hide_code=True)
def _(
    SM_STANZAS,
    gu,
    lang_sel,
    sm_choice_radio,
    sm_cv,
    sm_direction,
    sm_future,
    sm_history,
    sm_next_btn,
    sm_prev_btn,
    sm_remaining,
    sm_renew_btn,
    sm_restore_entry,
    sm_score,
    sm_set_cv,
    sm_set_future,
    sm_set_history,
    sm_set_remaining,
    sm_set_restore_entry,
    sm_set_score,
):
    gu.stanza_match_form(
        sm_cv, sm_set_cv, sm_remaining, sm_set_remaining,
        sm_score, sm_set_score, sm_restore_entry, sm_set_restore_entry,
        sm_history, sm_set_history, sm_future, sm_set_future,
        sm_choice_radio, sm_next_btn, sm_prev_btn,
        stanzas=SM_STANZAS,
        direction=sm_direction.value,
        lang=lang_sel.value,
        renew_btn=sm_renew_btn,
    )
    return


@app.cell(hide_code=True)
def _(gu, lang_sel, mo):
    mo.md(gu.ui_label('presence_exercise_heading', lang_sel.value))
    return


@app.cell(hide_code=True)
def _(
    QUIZ_WORDS_RAW,
    SESSION_SIZE,
    STANZAS,
    eee,
    gu,
    tp_renew_btn,
    tp_set_cv,
    tp_set_future,
    tp_set_history,
    tp_set_remaining,
    tp_set_restore_entry,
    tp_set_score,
):
    from pathlib import Path as _P

    LITERARY_TRANSLATORS = ["Жуковский", "Вересаев"]
    _tp_vocab = [w for w in QUIZ_WORDS_RAW if w.get("pos") in eee.TRANSLATION_PRESENCE_CONTENT_POS]
    _tp_path = _P(__file__).parent / "translation_presence.tsv"
    gu.sync_translation_presence_tsv(_tp_vocab, LITERARY_TRANSLATORS, STANZAS, _tp_path)
    TP_ITEMS = gu.balance_presence_items(gu.build_translation_presence_items(
        gu.read_translation_presence_tsv(_tp_path), QUIZ_WORDS_RAW, STANZAS
    ), n=SESSION_SIZE)
    gu.reset_quiz_state(tp_renew_btn, tp_set_cv, tp_set_remaining, tp_set_score,
                         tp_set_history, tp_set_future, tp_set_restore_entry)
    return (TP_ITEMS,)


@app.cell(hide_code=True)
def _(mo):
    tp_cv, tp_set_cv = mo.state(None)
    tp_score, tp_set_score = mo.state({"correct": 0, "total": 0})
    tp_remaining, tp_set_remaining = mo.state(None)
    tp_history, tp_set_history = mo.state([])
    tp_future, tp_set_future = mo.state([])
    tp_restore_entry, tp_set_restore_entry = mo.state(None)
    return (
        tp_cv,
        tp_future,
        tp_history,
        tp_remaining,
        tp_restore_entry,
        tp_score,
        tp_set_cv,
        tp_set_future,
        tp_set_history,
        tp_set_remaining,
        tp_set_restore_entry,
        tp_set_score,
    )


@app.cell(hide_code=True)
def _(gu, lang_sel):
    tp_renew_btn = gu.make_renew_button(lang=lang_sel.value)
    return (tp_renew_btn,)


@app.cell(hide_code=True)
def _(
    TP_ITEMS,
    gu,
    lang_sel,
    tp_cv,
    tp_history,
    tp_remaining,
    tp_restore_entry,
):
    _ = tp_cv()
    tp_choice_radio, tp_next_btn, tp_prev_btn, tp_source_switch = gu.translation_presence_widgets(
        cv=tp_cv(),
        remaining=tp_remaining(),
        items=TP_ITEMS,
        restore_entry=tp_restore_entry(),
        history_len=len(tp_history()),
        lang=lang_sel.value,
    )
    return tp_choice_radio, tp_next_btn, tp_prev_btn, tp_source_switch


@app.cell(hide_code=True)
def _(
    TP_ITEMS,
    gu,
    lang_sel,
    tp_choice_radio,
    tp_cv,
    tp_future,
    tp_history,
    tp_next_btn,
    tp_prev_btn,
    tp_remaining,
    tp_renew_btn,
    tp_restore_entry,
    tp_score,
    tp_set_cv,
    tp_set_future,
    tp_set_history,
    tp_set_remaining,
    tp_set_restore_entry,
    tp_set_score,
    tp_source_switch,
):
    gu.translation_presence_form(
        tp_cv, tp_set_cv, tp_remaining, tp_set_remaining,
        tp_score, tp_set_score, tp_restore_entry, tp_set_restore_entry,
        tp_history, tp_set_history, tp_future, tp_set_future,
        tp_choice_radio, tp_next_btn, tp_prev_btn, tp_source_switch,
        items=TP_ITEMS,
        lang=lang_sel.value,
        renew_btn=tp_renew_btn,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    cv, set_cv = mo.state(None)
    score, set_score = mo.state({"correct": 0, "total": 0})
    remaining, set_remaining = mo.state(None)
    history, set_history = mo.state([])
    future, set_future = mo.state([])
    restore_entry, set_restore_entry = mo.state(None)
    return (
        cv,
        future,
        history,
        remaining,
        restore_entry,
        score,
        set_cv,
        set_future,
        set_history,
        set_remaining,
        set_restore_entry,
        set_score,
    )


@app.cell(hide_code=True)
def _(STANZAS, gu, lang_sel, mo):
    stanza_selector = mo.ui.dropdown(
        options=[s["ref"] for s in STANZAS],
        value=STANZAS[0]["ref"],
        label=gu.ui_label('stanza_label', lang_sel.value),
    )
    return (stanza_selector,)


@app.cell(hide_code=True)
def _(gu, lang_sel, mo):
    _TRANS_BY_LANG = {
        "ru": ["подстрочник", "Жуковский", "Вересаев"],
        "en": ["подстрочник", "Pope", "Murray"],
        "el": ["подстрочник", "Πολυλάς"],
    }
    _DEFAULT_BY_LANG = {"ru": "Жуковский", "en": "Pope", "el": "Πολυλάς"}
    _ALL_OPTIONS = {
        gu.ui_label('interlinear_label', lang_sel.value): "подстрочник",
        "Жуковский (1849)":    "Жуковский",
        "Вересаев (1953)":     "Вересаев",
        "Pope (1725)":          "Pope",
        "Murray (1919)":        "Murray",
        "Πολυλάς (1875/1877)":  "Πολυλάς",
    }
    _valid = _TRANS_BY_LANG.get(lang_sel.value, _TRANS_BY_LANG["ru"])
    _opts = {k: v for k, v in _ALL_OPTIONS.items() if v in _valid}
    _default_v = _DEFAULT_BY_LANG.get(lang_sel.value, "Жуковский")
    _default_k = next((k for k, v in _opts.items() if v == _default_v), list(_opts.keys())[0])
    trans_selector = mo.ui.dropdown(
        options=_opts,
        value=_default_k,
        label=gu.ui_label('trans_selector_label', lang_sel.value),
    )
    return (trans_selector,)


@app.cell(hide_code=True)
async def _(cfg, eee):
    from pathlib import Path as _P
    from eee_project import GreekUtils as _GU

    _root = _P(__file__).parent
    _session_remote = cfg.nb_remote("2026_06_15")
    _fetched = await _GU.ensure_files(
        "greek.md", "ictus.html",
        nb_dir=_root, remote_base=_session_remote,
    )
    _greek_md = _fetched["greek.md"]
    _ictus_html = _fetched["ictus.html"]

    _gke_remote = "https://codeberg.org/EEE-project/greek-knowledge-eee/raw/branch/main/texts/odyssey"
    _trans_fetched = await _GU.ensure_files(
        "translations_ru.md", "translations_en.md", "translations_el.md",
        nb_dir=_root, remote_base=_gke_remote,
    )
    if _greek_md is None or _ictus_html is None or any(v is None for v in _trans_fetched.values()):
        raise FileNotFoundError(
            "greek.md/ictus.html/translations_{ru,en,el}.md: one or more "
            "required session files could not be fetched (see ensure_file "
            "diagnostics above)"
        )
    _greek = eee.parse_stanza_text(_greek_md.read_text(encoding="utf-8"), ref_prefix="### Odyss. ")

    _translations: dict = {}
    TRANS_DESC: dict = {}
    for _fname in ("translations_ru.md", "translations_en.md", "translations_el.md"):
        _tr, _desc = eee.parse_stanza_translations(
            _trans_fetched[_fname].read_text(encoding="utf-8"), ref_prefix="### Odyss. "
        )
        _translations.update(_tr)
        TRANS_DESC.update(_desc)

    STANZAS = [
        {
            "ref": ref,
            "lines": lines,
            "translations": {tr: d.get(ref, "—") for tr, d in _translations.items()},
        }
        for ref, lines in _greek.items()
    ]

    # ictus (rhythm) markup: one marked-up line per plain line, in the same
    # reading order as greek.md -- zipped by position, not re-keyed, so a plain
    # line's own accents/punctuation never need to match the markup exactly.
    _ictus_lines = _ictus_html.read_text(encoding="utf-8").splitlines()
    _all_plain_lines = [line for lines in _greek.values() for line in lines]
    RHYTHM_HTML = dict(zip(_all_plain_lines, _ictus_lines))
    return RHYTHM_HTML, STANZAS, TRANS_DESC


@app.cell(hide_code=True)
def _(ag_backend, cfg, eee, grc_lexicons, gu, lang_sel):
    from pathlib import Path

    QUIZ_WORDS_RAW = gu.resolve_word_grammar(
        gu.load_inflected_vocab_tsv("vocab_IX_19-38.tsv", nb_dir=Path(__file__).parent, remote_base=cfg.nb_remote("2026_06_15")),
        ag_backend, lang_sel.value
    )

    def _lexicon_tag(w):
        sources = eee.grc_lexicon_sources(w, lexicons=grc_lexicons)
        if not sources:
            return ""
        lexicons = ", ".join(f'"{s}"' for s in sources)
        return f"ancient-greek[{lexicons}]"

    for _w in QUIZ_WORDS_RAW:
        _tag = _lexicon_tag(_w)
        if _tag:
            _w["lexicon_tag"] = _tag
    return (QUIZ_WORDS_RAW,)


@app.cell(hide_code=True)
def _(
    QUIZ_WORDS_RAW,
    SESSION_SIZE,
    build_paradigm_table,
    eee,
    grc_lexicons,
    gu,
    quiz_renew_btn,
    set_cv,
    set_future,
    set_history,
    set_remaining,
    set_restore_entry,
    set_score,
):
    QUIZ_WORDS = gu.sample_session_items(eee.filter_grc_quiz_words(
        QUIZ_WORDS_RAW, "none",
        build_paradigm_table=build_paradigm_table, lexicons=grc_lexicons,
    ), n=SESSION_SIZE)

    eee.add_labels(QUIZ_WORDS)

    gu.reset_quiz_state(quiz_renew_btn, set_cv, set_remaining, set_score,
                         set_history, set_future, set_restore_entry)
    return (QUIZ_WORDS,)


@app.cell(hide_code=True)
def _(QUIZ_WORDS_RAW, build_paradigm_table, eee, grc_lexicons):
    CLICKABLE_FORMS = eee.grc_coverage_words(
        QUIZ_WORDS_RAW, "none",
        build_paradigm_table=build_paradigm_table, lexicons=grc_lexicons,
    )
    # words whose exact attested surface form is confirmed by the Homeric
    # corpus lexicon specifically -- highlighted (background) in the clickable
    # text so a reader can tell "Homer himself confirms this form" apart from
    # "some later-period lexicon in the combined engine reaches it".
    HOMER_WORDS = eee.grc_coverage_words(
        QUIZ_WORDS_RAW, "homer",
        build_paradigm_table=build_paradigm_table, lexicons=grc_lexicons,
    )
    return CLICKABLE_FORMS, HOMER_WORDS


@app.cell(hide_code=True)
def _(ag_backend, eee, grc_lexicons, lang_sel, mg, um_backend):
    build_paradigm_table = eee.build_grc_paradigm_table(ag_backend, um_backend, lang=lang_sel.value)
    build_lexicon_tabs = eee.build_grc_lexicon_tabs(
        ag_backend, um_backend,
        lexicons=grc_lexicons,
        el_backend=mg,
        require_lexicon="homer",
        lang=lang_sel.value,
    )
    return build_lexicon_tabs, build_paradigm_table


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(ODYSSEY_EXTRA_LEXICONS, mo):
    import sys as _sys
    import pathlib as _pl
    for _pth in _pl.Path(_sys.prefix).glob("lib/python*/site-packages/_editable_impl_*.pth"):
        _src = _pth.read_text().strip()
        if _src not in _sys.path:
            _sys.path.insert(0, _src)

    import eee_project as eee
    from ancient_greek_backend_eee import AncientGreekBackend
    from unimorph_backend_eee import UniMorphBackend
    from modern_greek_backend_eee import ModernGreekBackend

    # union recognizer for coverage + quiz — all diachronic rungs, incl. Classical Attic (pratt + ltrg + lsj)
    ag_backend = AncientGreekBackend.for_period("epic", "attic", "hellenistic_koine", "roman_koine", extra_lexicons=ODYSSEY_EXTRA_LEXICONS)
    # odyssey_morpheus is Epic-register, Odyssey-course-vocabulary-specific --
    # merged alongside homer (same register), not lsj/byzantine (Attic/Koine).
    ag_homer = AncientGreekBackend.for_period("epic", extra_lexicons=ODYSSEY_EXTRA_LEXICONS)
    ag_lsj = AncientGreekBackend.for_period("attic")
    ag_lxx = AncientGreekBackend.for_period("hellenistic_koine")
    ag_morphgnt = AncientGreekBackend.for_period("roman_koine")
    # byzantine is a sparse exceptions layer, not a standalone engine -- merge
    # onto the same Koine/Attic base the other rungs use so it inherits their
    # lemma coverage and only overrides the specific cells it documents.
    ag_byzantine = AncientGreekBackend.for_period("byzantine")
    grc_lexicons = {"homer": ag_homer, "lsj": ag_lsj, "lxx": ag_lxx, "morphgnt": ag_morphgnt, "byzantine": ag_byzantine}
    um_backend = UniMorphBackend(language="grc")
    mg = ModernGreekBackend()   # Modern-Greek rung of the diachronic dropdown
    eee.register_backend("grc", ag_backend, backend="ancient-greek")
    eee.register_backend("grc", ag_homer, backend="ag-homer")
    eee.register_backend("grc", um_backend, backend="unimorph")
    eee.set_chain("grc", ["ancient-greek", "unimorph"])
    gu = eee.GreekUtils(mo_module=mo)
    return ag_backend, eee, grc_lexicons, gu, mg, um_backend


@app.cell(hide_code=True)
def _(cfg, mo):
    from eee_project.notebook_utils import eee_footer
    _prev_url, _next_url = cfg.adjacent_urls("2026_06_15/")
    eee_footer(mo, lang="ru", prev_url=_prev_url, next_url=_next_url, same_window=True)
    return


@app.cell(hide_code=True)
def _(cfg, gu):
    from pathlib import Path as _P
    NB_DIR = _P(__file__).parent
    NB_REMOTE = cfg.nb_remote("2026_06_15")
    for _f in (
        'Одиссея 1.pdf',
        'слова день 1.pdf',
        'map_ithaca.jpg',
        'genealogy.jpg',
        'neriton_epithet.jpg',
        'ithaca_kefalonia.jpg',
    ):
        gu.ensure_file(_f, nb_dir=NB_DIR, remote_base=NB_REMOTE)
    return


@app.cell(hide_code=True)
def _(mo):
    lang_sel = mo.ui.dropdown(
        options={"English": "en", "Русский": "ru", "Ελληνικά": "el"},
        value="English",
        label="🌐",
    )
    mo.Html(f"""
    <div style="position:fixed;top:56px;right:12px;z-index:1000;
                background:white;padding:6px 10px;border-radius:8px;
                box-shadow:0 2px 8px rgba(0,0,0,.12);">
      {lang_sel}
    </div>
    """)
    return (lang_sel,)


if __name__ == "__main__":
    app.run()
