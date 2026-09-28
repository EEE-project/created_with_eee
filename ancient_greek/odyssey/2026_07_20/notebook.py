# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.23.14",
#     "eee-project>=1.19.0",
#     "ancient-greek-backend-eee>=2.0.0",
#     "unimorph-backend-eee>=1.0.3",
#     "modern-greek-backend-eee>=1.0.0",
# ]
# ///

import marimo

__generated_with = "0.23.14"
app = marimo.App(width="medium", app_title="Одиссея с Гомером — День 6: Одиссея IX.130–151")


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
    from pathlib import Path as _Path
    _TITLES = {
        "ru": ("# Одиссея с Гомером", "## День 6 · Odyss. IX.130–151"),
        "en": ("# Odyssey with Homer", "## Day 6 · Odyss. IX.130–151"),
        "el": ("# Οδύσσεια με τον Όμηρο", "## Ημέρα 6 · Odyss. IX.130–151"),
    }
    _h1, _h2 = _TITLES.get(lang_sel.value, _TITLES["ru"])
    _thumb_path = _Path(__file__).parent / "meeting_vase.jpg"
    _left = mo.vstack([
        mo.md(_h1),
        mo.md(_h2),
    ])
    _img = eee.magnify_image(mo, _thumb_path, raw_base="https://codeberg.org/EEE-project/created_with_eee/raw/branch/main/ancient_greek/odyssey/2026_07_20", width=280)
    _right = mo.vstack([_img], align="center")
    mo.hstack([_left, _right], align="start")
    return


@app.cell(hide_code=True)
def _(NB_REMOTE, gu, lang_sel, mo):
    _txt = (
        f"{gu.ui_label('lesson_materials_label', lang_sel.value)} "
        f"[Od_IX_130-151.pdf]({NB_REMOTE}/Od_IX_130-151.pdf) · "
        f"[Od_IX_130-151_vocabula.docx]({NB_REMOTE}/Od_IX_130-151_vocabula.docx)"
    )
    mo.md(_txt)
    return


@app.cell(hide_code=True)
def _(eee, lang_sel, mo):
    from pathlib import Path as _Path
    _vase_path = _Path(__file__).parent / "kleos_aphthiton_vase.jpg"
    _vine_path = _Path(__file__).parent / "aphthitoi_ampeloi_vineyard.jpg"
    _raw = "https://codeberg.org/EEE-project/created_with_eee/raw/branch/main/ancient_greek/odyssey/2026_07_20"
    _vase = mo.vstack([
        eee.magnify_image(mo, _vase_path, raw_base=_raw, width=220),
        mo.md("<div style='text-align:center'>κλέος ἄφθιτον</div>"),
    ], align="center")
    _vine = mo.vstack([
        eee.magnify_image(mo, _vine_path, raw_base=_raw, width=280),
        mo.md("<div style='text-align:center'>ἄφθιτοι ἄμπελοι</div>"),
    ], align="center")
    _TXT = {
        "ru": r"""
        ---
        ## Ἄφθιτος — «неувядающий»

        В IX.133 остров описывается так, что на нём **ἄφθιτοι ἄμπελοι εἶεν** —
        «были бы неувядающие виноградники». То же прилагательное **ἄφθιτος**
        входит в знаменитую гомеровскую формулу **κλέος ἄφθιτον** — «немеркнущая,
        неувядающая слава» — то, ради чего герой идёт на смерть в бою (ср. Ахилл,
        Il. IX.413).
        """,
        "en": r"""
        ---
        ## Ἄφθιτος — "unfading"

        In IX.133, the island is described such that on it **ἄφθιτοι ἄμπελοι
        εἶεν** — "there would be unfading vineyards." The same adjective
        **ἄφθιτος** appears in the famous Homeric formula **κλέος ἄφθιτον** —
        "undying, unfading fame" — the thing for which a hero goes to his
        death in battle (cf. Achilles, Il. IX.413).
        """,
        "el": r"""
        ---
        ## Ἄφθιτος — «αμάραντος»

        Στο IX.133, το νησί περιγράφεται έτσι ώστε σε αυτό **ἄφθιτοι ἄμπελοι
        εἶεν** — «θα υπήρχαν αμάραντοι αμπελώνες». Το ίδιο επίθετο
        **ἄφθιτος** εμφανίζεται στην περίφημη ομηρική έκφραση **κλέος
        ἄφθιτον** — «αμάραντη, αθάνατη δόξα» — αυτό για το οποίο ο ήρωας
        πηγαίνει στον θάνατο στη μάχη (πρβλ. Αχιλλέας, Il. IX.413).
        """,
    }
    mo.vstack([
        mo.md(_TXT.get(lang_sel.value, _TXT["ru"])),
        mo.hstack([_vase, _vine], justify="center", gap=2),
    ])
    return


@app.cell(hide_code=True)
def _(lang_sel, mo):
    _TXT = {
        "ru": r"""
    ---
    ## Αἴγειροι — тополя у Гомера

    В нашем отрывке тополя (**αἴγειροι**, IX.141) растут у источника —
    примета плодородия и пресной воды. Но в другом месте у Гомера тополя
    отмечают совсем иной порог: в X песни Кирка описывает Одиссею путь к
    дому Аида (Od. X.509–510):

    > **ἔνθα δὲ Περσεφόνης ἄλσος καὶ δενδρήεντα,
    > μακραί τ᾽ αἴγειροι καὶ ἰτέαι ὠλεσίκαρποι·**
    > там роща Персефоны и тенистые деревья,
    > высокие тополя и ивы, теряющие плод

    Возможно, оба образа не противоречат друг другу: тополя у Гомера
    связаны и с пресной водой (как в нашем отрывке), и с царством мёртвых
    — здесь эти два смысла, похоже, наложены один на другой.
    [Текст на ancientrome.ru](https://ancientrome.ru/antlitr/t.htm?a=1344030010#:~:text=Берег%20там%20низ%C2%ADкий,шаг%20свой%20напра%C2%ADвишь.)
    """,
        "en": r"""
    ---
    ## Αἴγειροι — Homer's poplars

    In our passage, poplars (**αἴγειροι**, IX.141) grow by a spring — a
    sign of fertility and fresh water. But elsewhere in Homer, poplars mark
    a very different threshold: in Book X, Circe describes to Odysseus the
    way to the house of Hades (Od. X.509–510):

    > **ἔνθα δὲ Περσεφόνης ἄλσος καὶ δενδρήεντα,
    > μακραί τ᾽ αἴγειροι καὶ ἰτέαι ὠλεσίκαρποι·**
    > there is the grove of Persephone and shady trees,
    > tall poplars and willows that shed their fruit

    Perhaps the two images do not contradict each other: in Homer, poplars
    are linked both to fresh water (as in our passage) and to the realm of
    the dead — here these two meanings seem to be layered one over the
    other.
    [Text at ancientrome.ru](https://ancientrome.ru/antlitr/t.htm?a=1344030010#:~:text=Берег%20там%20низ%C2%ADкий,шаг%20свой%20напра%C2%ADвишь.)
    """,
        "el": r"""
    ---
    ## Αἴγειροι — οι λεύκες του Ομήρου

    Στο δικό μας απόσπασμα, οι λεύκες (**αἴγειροι**, IX.141) φυτρώνουν
    κοντά σε μια πηγή — σημάδι γονιμότητας και γλυκού νερού. Αλλού όμως
    στον Όμηρο, οι λεύκες σηματοδοτούν ένα εντελώς διαφορετικό κατώφλι:
    στη ραψωδία Κ η Κίρκη περιγράφει στον Οδυσσέα τον δρόμο προς το σπίτι
    του Άδη (Od. X.509–510):

    > **ἔνθα δὲ Περσεφόνης ἄλσος καὶ δενδρήεντα,
    > μακραί τ᾽ αἴγειροι καὶ ἰτέαι ὠλεσίκαρποι·**
    > εκεί το άλσος της Περσεφόνης και τα σκιερά δέντρα,
    > ψηλές λεύκες και ιτιές που χάνουν τον καρπό τους

    Ίσως οι δύο εικόνες δεν έρχονται σε αντίθεση μεταξύ τους: στον Όμηρο
    οι λεύκες συνδέονται και με το γλυκό νερό (όπως στο δικό μας
    απόσπασμα), και με το βασίλειο των νεκρών — εδώ αυτές οι δύο σημασίες
    φαίνεται να επικαλύπτονται.
    [Κείμενο στο ancientrome.ru](https://ancientrome.ru/antlitr/t.htm?a=1344030010#:~:text=Берег%20там%20низ%C2%ADкий,шаг%20свой%20напра%C2%ADвишь.)
    """,
    }
    mo.md(_TXT.get(lang_sel.value, _TXT["ru"]))
    return


@app.cell(hide_code=True)
def _(lang_sel, mo):
    _TXT = {
        "ru": r"""
    ---
    ## θάλασσα, πόντος, ἅλς — три слова для «моря»

    У Гомера для моря есть не одно слово, а несколько, и в этом отрывке
    встречаются сразу два из них: **ἁλός** (IX.132, «седого моря») и
    **θαλάσσης** (IX.150, «на прибое моря»). Третье, **πόντος** — открытое
    море, морской путь, — в этих строках не встречается, но входит в ту же
    группу.

    **ἅλς** значит и «море», и «соль» одновременно — не совпадение: от него
    современное **«галоген»** (ἅλς + -γενής, «солеобразующий»).
    """,
        "en": r"""
    ---
    ## θάλασσα, πόντος, ἅλς — three words for "sea"

    Homer has not one word for the sea but several, and this passage
    contains two of them: **ἁλός** (IX.132, "of the grey sea") and
    **θαλάσσης** (IX.150, "on the sea's surf"). The third, **πόντος** —
    the open sea, a sea route — does not appear in these lines, but
    belongs to the same group.

    **ἅλς** means both "sea" and "salt" at once — not a coincidence: from
    it comes the modern **"halogen"** (ἅλς + -γενής, "salt-forming").
    """,
        "el": r"""
    ---
    ## θάλασσα, πόντος, ἅλς — τρεις λέξεις για τη «θάλασσα»

    Ο Όμηρος δεν έχει μία μόνο λέξη για τη θάλασσα, αλλά αρκετές, και σε
    αυτό το απόσπασμα συναντάμε δύο από αυτές: **ἁλός** (IX.132, «της
    γκρίζας θάλασσας») και **θαλάσσης** (IX.150, «στον αφρό της
    θάλασσας»). Η τρίτη, **πόντος** — η ανοιχτή θάλασσα, ο θαλάσσιος
    δρόμος — δεν εμφανίζεται σε αυτούς τους στίχους, αλλά ανήκει στην
    ίδια ομάδα.

    Η λέξη **ἅλς** σημαίνει και «θάλασσα» και «αλάτι» ταυτόχρονα — δεν
    είναι σύμπτωση: από αυτήν προέρχεται το σύγχρονο **«αλογόνο»** (ἅλς
    + -γενής, «αυτό που παράγει άλας»).
    """,
    }
    mo.md(_TXT.get(lang_sel.value, _TXT["ru"]))
    return


@app.cell(hide_code=True)
def _(lang_sel, mo):
    _TXT = {
        "ru": r"""
    ---
    ## Ещё отзвуки в современных языках

    | Гомеровское слово | В тексте | Отзвук |
    |---|---|---|
    | **κτίζω** — строить, основывать | ἐϋκτιμένην, IX.130 | новогреч. **κτίριο** — здание |
    | **λεῖος** — гладкий, ровный | λείη, IX.131 | лат. **levis** — гладкий, лёгкий |
    | **βαθύς** — глубокий | βαθὺ, IX.131 | «батиаль», «батискаф» — из βαθύς + σκάφος |
    """,
        "en": r"""
    ---
    ## More echoes in modern languages

    | Homeric word | In the text | Echo |
    |---|---|---|
    | **κτίζω** — to build, to found | ἐϋκτιμένην, IX.130 | Modern Greek **κτίριο** — building |
    | **λεῖος** — smooth, level | λείη, IX.131 | Latin **levis** — smooth, light |
    | **βαθύς** — deep | βαθὺ, IX.131 | "bathyscaphe" — from βαθύς + σκάφος |
    """,
        "el": r"""
    ---
    ## Κι άλλοι αντίλαλοι σε σύγχρονες γλώσσες

    | Ομηρική λέξη | Στο κείμενο | Αντίλαλος |
    |---|---|---|
    | **κτίζω** — χτίζω, ιδρύω | ἐϋκτιμένην, IX.130 | νέα ελλ. **κτίριο** — κτήριο |
    | **λεῖος** — λείος, ομαλός | λείη, IX.131 | λατ. **levis** — λείος, ελαφρύς |
    | **βαθύς** — βαθύς | βαθὺ, IX.131 | **βαθυσκάφος** — από βαθύς + σκάφος |
    """,
    }
    mo.md(_TXT.get(lang_sel.value, _TXT["ru"]))
    return


@app.cell(hide_code=True)
def _(lang_sel, mo):
    _TXT = {
        "ru": r"""
    ---
    ## Инфинитивы

    | Значение | Окончание | Пример |
    |---|---|---|
    | Наст. и буд. время, иногда аорист, активный залог | **-ειν** | βαλέειν |
    | Наст. время активного залога некоторых глаголов + перфект активный | **-ναι** | — |
    | Аорист активный сигматический | **-σαι** | ἀνάψαι, ἐπικέλσαι |
    | Наст. и буд. время, перфект медиального и пассивного залогов + аорист медиальный | **-σθαι** | ἰδέσθαι |
    """,
        "en": r"""
    ---
    ## Infinitives

    | Meaning | Ending | Example |
    |---|---|---|
    | Present and future tense, sometimes aorist, active voice | **-ειν** | βαλέειν |
    | Present tense active voice of some verbs + perfect active | **-ναι** | — |
    | Sigmatic active aorist | **-σαι** | ἀνάψαι, ἐπικέλσαι |
    | Present and future tense, perfect middle and passive voices + middle aorist | **-σθαι** | ἰδέσθαι |
    """,
        "el": r"""
    ---
    ## Απαρέμφατα

    | Σημασία | Κατάληξη | Παράδειγμα |
    |---|---|---|
    | Ενεστώτας και μέλλοντας, μερικές φορές αόριστος, ενεργητική φωνή | **-ειν** | βαλέειν |
    | Ενεστώτας ενεργητικής φωνής μερικών ρημάτων + παρακείμενος ενεργητικός | **-ναι** | — |
    | Σιγματικός ενεργητικός αόριστος | **-σαι** | ἀνάψαι, ἐπικέλσαι |
    | Ενεστώτας και μέλλοντας, παρακείμενος μέσης και παθητικής φωνής + μέσος αόριστος | **-σθαι** | ἰδέσθαι |
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

    - **ἐστιν** — 3 л. ед. ч. наст. времени от глагола «быть», ср. русское «есть»
    - **ἦν** — 3 л. ед. ч. имперфекта от глагола «быть» (был)

    - родит. падеж множ. числа всегда заканчивается на **-ων**: αὐτῶν (их)
    - встретили два характерных гомеровских окончания: родит. падеж ед. ч. на
      **-οιο**: πολιοῖο (седого); и дат. падеж множ. числа на **-εσσι**:
      νεφέεσσιν (облаками); конечное ν поставлено для благозвучия и не входит
      в окончание. Другой, тоже гомеровский, вариант дат. п. множ. ч.:
      **-οισι**, ὀφθαλμοῖσιν (глазами).
    - игра «собери склонение»: слово «корабль» (ναῦς) встречается в этом
      отрывке трижды в двух разных падежах — **νηυσὶ** (дат. п. мн. ч.,
      ст. 142–145 и 146–151) и **νῆας** (вин. п. мн. ч., ст. 146–151);
      попробуйте определить падеж каждой формы по контексту, прежде чем
      смотреть перевод

    #### Частицы

    - **пояснительные:** **γάρ** — потому что, ведь, дело в том что
      (объясняет предшествующую мысль)
    - **соединительные:** **ἄρα** — значит, следовательно; **ἀτάρ** — но,
      ну а (переход к другой теме); **δέ** — а, но, же (слабое противление);
      **μέν... δέ** — противопоставление («с одной стороны... с другой»);
      **οὖν** — и вот, итак, но (переход к теме, слабее чем ἀτάρ)
    - **выделяющие и усилительные:** **γέ** — вот, именно, -то (выделяет
      главное слово); **δή** — именно, же, поистине (подчёркивает
      истинность); **μήν** — воистину, поистине (сильнее δή, часто с
      клятвами)
    - **другие:** **ἄν** — бы, наверное, возможно (потенциальная частица);
      **τοι** — скажу я тебе, смотри-ка (апелляция к собеседнику);
      **τοίνυν** — тогда, в таком случае (вводит ответ)

    #### Местоимения

    *(формы приведены для аттического диалекта — у Гомера часто встречаются
    другие варианты, но и эти формы часто полезно знать.)*

    - **личные** (ἐγώ я, σύ ты, ἡμεῖς мы, ὑμεῖς вы):

      | | ἐγώ | σύ | ἡμεῖς | ὑμεῖς |
      |---|---|---|---|---|
      | Gen | ἐμοῦ / μου | σοῦ / σου | ἡμῶν | ὑμῶν |
      | Dat | ἐμοί / μοι | σοί / σοι | ἡμῖν | ὑμῖν |
      | Acc | ἐμέ / με | σέ / σε | ἡμᾶς | ὑμᾶς |

    - **ὅδε, ἥδε, τόδε** — «этот», совсем близко к говорящему (можно
      показать пальцем); склоняется как артикль + частица **-δε**
    - **οὗτος, αὕτη, τοῦτο** — «этот», ближе к собеседнику («твой»)
    - **ἐκεῖνος, -η, -ο** — «тот» (собеседники его не видят); склоняется
      по 2-1 склонениям
    - **αὐτός, -ή, -ό** — 1) сам; 2) он/она/оно в косв. падежах; 3) тот
      же самый (если перед ним стоит артикль); склоняется по 2-1 склонениям
    - **ὅς, ἥ, ὅ** — относительное местоимение «который»; склоняется как
      артикль, но без начальной **τ** в косвенных падежах
    - **οὐδείς, οὐδεμία, οὐδέν** — «никто»; сложение **οὐδε** (не) +
      **εἷς, μία, ἕν** (один); множ. ч. почти не используется
    - **τίς, τί** — «кто? что? какой?»; форма для муж. и жен. рода одна;
      без ударения (энклитика) — неопределённое «кто-то, какой-то»
    """,
        "en": r"""
    ---
    ## Grammar notes for beginning sailors

    - **ἐστιν** — 3rd person singular present of the verb "to be," cf. English "is"
    - **ἦν** — 3rd person singular imperfect of the verb "to be" ("was")

    - the genitive plural always ends in **-ων**: αὐτῶν ("their")
    - two characteristic Homeric endings appeared: the genitive singular in
      **-οιο**: πολιοῖο ("grey"); and the dative plural in **-εσσι**:
      νεφέεσσιν ("clouds"); the final ν is added for euphony and isn't part
      of the ending. Another, also Homeric, variant of the dative plural:
      **-οισι**, ὀφθαλμοῖσιν ("eyes").
    - a "gather the declension" game: the word for "ship" (ναῦς) appears
      in this passage three times, in two different cases — **νηυσὶ**
      (dative plural, lines 142–145 and 146–151) and **νῆας** (accusative
      plural, lines 146–151); try to work out the case of each form from
      context before checking the translation

    #### Particles

    - **explanatory:** **γάρ** — because, for, the thing is that
      (explains the preceding thought)
    - **connective:** **ἄρα** — so, therefore; **ἀτάρ** — but, well
      (a shift to a different topic); **δέ** — and, but, however (a mild
      contrast); **μέν... δέ** — a contrast ("on the one hand... on the
      other"); **οὖν** — so, then, but (a shift of topic, weaker than
      ἀτάρ)
    - **emphatic and intensive:** **γέ** — indeed, precisely, at least
      (emphasizes the key word); **δή** — indeed, truly, precisely
      (underscores truthfulness); **μήν** — truly, verily (stronger than
      δή, often with oaths)
    - **other:** **ἄν** — would, perhaps, possibly (potential particle);
      **τοι** — let me tell you, look here (an appeal to the listener);
      **τοίνυν** — then, in that case (introduces an answer)

    #### Pronouns

    *(forms are given for the Attic dialect — Homer often uses other
    variants, but these forms are still useful to know.)*

    - **personal** (ἐγώ I, σύ you, ἡμεῖς we, ὑμεῖς you [pl.]):

      | | ἐγώ | σύ | ἡμεῖς | ὑμεῖς |
      |---|---|---|---|---|
      | Gen | ἐμοῦ / μου | σοῦ / σου | ἡμῶν | ὑμῶν |
      | Dat | ἐμοί / μοι | σοί / σοι | ἡμῖν | ὑμῖν |
      | Acc | ἐμέ / με | σέ / σε | ἡμᾶς | ὑμᾶς |

    - **ὅδε, ἥδε, τόδε** — "this," right next to the speaker (you could
      point at it); declines as the article + the particle **-δε**
    - **οὗτος, αὕτη, τοῦτο** — "this," closer to the listener ("yours")
    - **ἐκεῖνος, -η, -ο** — "that" (the interlocutors don't see it);
      declines like a 2nd-1st declension adjective
    - **αὐτός, -ή, -ό** — 1) self; 2) he/she/it in oblique cases; 3) the
      same (if the article precedes it); declines like a 2nd-1st
      declension adjective
    - **ὅς, ἥ, ὅ** — the relative pronoun "who/which"; declines like the
      article, but without the initial **τ** in the oblique cases
    - **οὐδείς, οὐδεμία, οὐδέν** — "no one"; a compound of **οὐδε**
      ("not") + **εἷς, μία, ἕν** ("one"); the plural is almost never used
    - **τίς, τί** — "who? what? which?"; one form for masculine and
      feminine; unaccented (enclitic) it means the indefinite "someone,
      something"
    """,
        "el": r"""
    ---
    ## Γραμματική υπενθύμιση για αρχάριους ναυτικούς

    - **ἐστιν** — γ' ενικό ενεστώτα του ρήματος «είμαι», πρβλ. νέα ελλ. «είναι»
    - **ἦν** — γ' ενικό παρατατικού του ρήματος «είμαι» («ήταν»)

    - η γενική πληθυντικού καταλήγει πάντα σε **-ων**: αὐτῶν («τους/τις/τα»)
    - συναντήσαμε δύο χαρακτηριστικές ομηρικές καταλήξεις: γενική ενικού σε
      **-οιο**: πολιοῖο («γκρίζου»)· και δοτική πληθυντικού σε **-εσσι**:
      νεφέεσσιν («με σύννεφα»)· το τελικό ν προστίθεται για ευφωνία και δεν
      ανήκει στην κατάληξη. Μια άλλη, επίσης ομηρική, παραλλαγή της δοτικής
      πληθυντικού: **-οισι**, ὀφθαλμοῖσιν («με μάτια»).
    - παιχνίδι «σύνθεσε την κλίση»: η λέξη για το «πλοίο» (ναῦς) εμφανίζεται
      σε αυτό το απόσπασμα τρεις φορές, σε δύο διαφορετικές πτώσεις —
      **νηυσὶ** (δοτική πληθυντικού, στ. 142–145 και 146–151) και **νῆας**
      (αιτιατική πληθυντικού, στ. 146–151)· προσπαθήστε να προσδιορίσετε
      την πτώση κάθε τύπου από τα συμφραζόμενα, πριν δείτε τη μετάφραση

    #### Μόρια

    - **επεξηγηματικά:** **γάρ** — επειδή, γιατί, το θέμα είναι ότι
      (επεξηγεί την προηγούμενη σκέψη)
    - **συνδετικά:** **ἄρα** — λοιπόν, συνεπώς· **ἀτάρ** — αλλά, μα
      (μετάβαση σε άλλο θέμα)· **δέ** — και, αλλά, όμως (ήπια αντίθεση)·
      **μέν... δέ** — αντίθεση («από τη μία... από την άλλη»)· **οὖν** —
      λοιπόν, και έτσι, αλλά (μετάβαση σε θέμα, πιο ήπιο από το ἀτάρ)
    - **εμφατικά και ενισχυτικά:** **γέ** — ακριβώς, τουλάχιστον,
      ίσα-ίσα (τονίζει τη βασική λέξη)· **δή** — ακριβώς, πράγματι,
      όντως (υπογραμμίζει την αλήθεια)· **μήν** — πράγματι, αληθώς (πιο
      έντονο από το δή, συχνά με όρκους)
    - **άλλα:** **ἄν** — θα, ίσως, πιθανόν (δυνητικό μόριο)· **τοι** —
      να σου πω, κοίτα (έκκληση προς τον συνομιλητή)· **τοίνυν** — τότε,
      σε αυτήν την περίπτωση (εισάγει απάντηση)

    #### Αντωνυμίες

    *(οι τύποι δίνονται για την αττική διάλεκτο — στον Όμηρο συχνά
    συναντώνται άλλες παραλλαγές, αλλά και αυτοί οι τύποι είναι συχνά
    χρήσιμο να τους γνωρίζετε.)*

    - **προσωπικές** (ἐγώ εγώ, σύ εσύ, ἡμεῖς εμείς, ὑμεῖς εσείς):

      | | ἐγώ | σύ | ἡμεῖς | ὑμεῖς |
      |---|---|---|---|---|
      | Gen | ἐμοῦ / μου | σοῦ / σου | ἡμῶν | ὑμῶν |
      | Dat | ἐμοί / μοι | σοί / σοι | ἡμῖν | ὑμῖν |
      | Acc | ἐμέ / με | σέ / σε | ἡμᾶς | ὑμᾶς |

    - **ὅδε, ἥδε, τόδε** — «αυτός», πολύ κοντά στον ομιλητή (μπορεί να
      τον δείξει με το δάχτυλο)· κλίνεται ως άρθρο + το μόριο **-δε**
    - **οὗτος, αὕτη, τοῦτο** — «αυτός», πιο κοντά στον συνομιλητή («ο
      δικός σου»)
    - **ἐκεῖνος, -η, -ο** — «εκείνος» (οι συνομιλητές δεν τον βλέπουν)·
      κλίνεται όπως τα επίθετα β'-α' κλίσης
    - **αὐτός, -ή, -ό** — 1) ο ίδιος· 2) αυτός/αυτή/αυτό στις πλάγιες
      πτώσεις· 3) ο ίδιος ακριβώς (αν προηγείται το άρθρο)· κλίνεται
      όπως τα επίθετα β'-α' κλίσης
    - **ὅς, ἥ, ὅ** — αναφορική αντωνυμία «ο οποίος»· κλίνεται όπως το
      άρθρο, αλλά χωρίς το αρχικό **τ** στις πλάγιες πτώσεις
    - **οὐδείς, οὐδεμία, οὐδέν** — «κανένας»· σύνθεση **οὐδε** (όχι) +
      **εἷς, μία, ἕν** (ένας)· ο πληθυντικός σχεδόν δεν χρησιμοποιείται
    - **τίς, τί** — «ποιος; τι; ποιο;»· ένας τύπος για αρσενικό και
      θηλυκό· χωρίς τόνο (εγκλιτικό) — αόριστο «κάποιος, κάτι»
    """,
    }
    mo.md(_TXT.get(lang_sel.value, _TXT["ru"]))
    return


@app.cell(hide_code=True)
def _(gu, lang_sel, mo):
    mo.md(gu.ui_label('poem_section_heading', lang_sel.value))
    return


@app.cell(hide_code=True)
def _(mo):
    _EDITION = (
        "<b>Homerus. Odyssea.</b> Ed. M. West. "
        "Bibliotheca Teubneriana, De Gruyter, 2017."
    )
    mo.md(_EDITION)
    return


@app.cell(hide_code=True)
def _(TRANS_DESC, eee, gu, lang_sel, mo, trans_selector):
    _desc_map = {eee.interlinear_translator_key(lang_sel.value): gu.ui_label('interlinear_description', lang_sel.value), **TRANS_DESC}
    mo.md(_desc_map.get(trans_selector.value, ""))
    return


@app.cell(hide_code=True)
def _(cfg, gu, lang_sel, mo):
    from pathlib import Path as _P
    SHOW_ICTUS = mo.ui.switch(value=True)
    SHOW_HOMER = mo.ui.switch(value=True)

    # Shared across all lessons. Fetched via ensure_file, not a bare local
    # read: molab only bundles files that live in the notebook's own directory,
    # so a parent-directory file like this one is missing there unless we
    # download it ourselves (matches the pattern already used for materials PDFs).
    _eee_note_filename = (
        "eee_note.md" if lang_sel.value == "ru" else f"eee_note_{lang_sel.value}.md"
    )
    _eee_note_path = gu.ensure_file(
        _eee_note_filename, nb_dir=_P(__file__).parent.parent, remote_base=cfg.raw_base,
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
def _(QUIZ_WORDS_RAW, build_period_tables, gu, lang_sel, text_widget):
    period_tables, period_selector, gloss_panel = gu.render_gloss_selector(
        QUIZ_WORDS_RAW, text_widget.widget.selected_word, build_period_tables, lang=lang_sel.value,
    )
    gloss_panel
    return period_selector, period_tables


@app.cell(hide_code=True)
def _(gu, period_selector, period_tables):
    gu.render_gloss_table(period_tables, period_selector)
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
    TRANS_BY_LANG,
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
        valid_translators=TRANS_BY_LANG.get(lang_sel.value, TRANS_BY_LANG["ru"]),
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
    TRANS_BY_LANG,
    cfg,
    eee,
    gu,
    lang_sel,
    tp_renew_btn,
    tp_set_cv,
    tp_set_future,
    tp_set_history,
    tp_set_remaining,
    tp_set_restore_entry,
    tp_set_score,
):
    from pathlib import Path as _P

    _interlinear_keys = {eee.interlinear_translator_key(_l) for _l in ("ru", "en", "el")}
    LITERARY_TRANSLATORS = [
        t for t in TRANS_BY_LANG.get(lang_sel.value, TRANS_BY_LANG["ru"])
        if t not in _interlinear_keys
    ]
    _tp_vocab = [w for w in QUIZ_WORDS_RAW if w.get("pos") in eee.TRANSLATION_PRESENCE_CONTENT_POS]
    # Same-directory file, but the WASM export doesn't bundle it -- needs ensure_file like the vocab TSV above.
    _tp_path = gu.ensure_file(
        "translation_presence.tsv", nb_dir=_P(__file__).parent, remote_base=cfg.nb_remote("2026_07_20"),
    )
    gu.sync_translation_presence_tsv(_tp_vocab, LITERARY_TRANSLATORS, STANZAS, _tp_path)
    TP_ITEMS = gu.balance_presence_items(gu.build_translation_presence_items(
        gu.read_translation_presence_tsv(_tp_path), QUIZ_WORDS_RAW, STANZAS,
        valid_translators=LITERARY_TRANSLATORS,
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
def _(TP_ITEMS, gu, lang_sel, tp_cv, tp_history, tp_remaining, tp_restore_entry):
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
def _(eee, gu, lang_sel, mo):
    TRANS_BY_LANG = {
        # Each language's own interlinear crib is a "## interlinear_{lang}"
        # section inside that language's translations_{lang}.md (KB naming
        # convention -- confirmed against greek-knowledge-eee's actual file
        # headers, not the old pre-port local translations_ru.md, which used
        # "подстрочник" instead). eee.interlinear_translator_key derives the
        # per-language key from this same convention -- see the
        # STANZAS-building cell. "Стариковский" is RU-only and NOT in the
        # shared KB (its 2025 translation is excluded there as still under
        # copyright, per greek-knowledge-eee's own CHANGELOG) -- sourced
        # instead from this lesson's own local translations_ru_starikovsky.md
        # (restored from this lesson's pre-KB-port local file, which already
        # had it, via git history -- see the STANZAS-building cell).
        "ru": [eee.interlinear_translator_key("ru"), "Жуковский", "Вересаев", "Стариковский"],
        "en": ["Pope", "Murray", eee.interlinear_translator_key("en")],
        "el": ["Πολυλάς", eee.interlinear_translator_key("el")],
    }
    _DEFAULT_BY_LANG = {"ru": "Жуковский", "en": "Pope", "el": "Πολυλάς"}
    # Only one interlinear variant is ever relevant for the current language,
    # so it's looked up dynamically rather than listed as three static
    # entries -- all three would render the same gu.ui_label(...) text for
    # a given lang_sel.value and silently collide as dict keys otherwise.
    _ALL_OPTIONS = {
        gu.ui_label('interlinear_label', lang_sel.value): eee.interlinear_translator_key(lang_sel.value),
        "Жуковский (1849)":    "Жуковский",
        "Вересаев (1953)":     "Вересаев",
        "Стариковский (2025)": "Стариковский",
        "Pope (1725)":          "Pope",
        "Murray (1919)":        "Murray",
        "Πολυλάς (1875/1877)":  "Πολυλάς",
    }
    _valid = TRANS_BY_LANG.get(lang_sel.value, TRANS_BY_LANG["ru"])
    _opts = {k: v for k, v in _ALL_OPTIONS.items() if v in _valid}
    _default_v = _DEFAULT_BY_LANG.get(lang_sel.value, "Жуковский")
    _default_k = next((k for k, v in _opts.items() if v == _default_v), list(_opts.keys())[0])
    trans_selector = mo.ui.dropdown(
        options=_opts,
        value=_default_k,
        label=gu.ui_label('trans_selector_label', lang_sel.value),
    )
    return TRANS_BY_LANG, trans_selector


@app.cell(hide_code=True)
async def _(cfg, eee):
    from pathlib import Path as _P
    from eee_project import GreekUtils as _GU

    _root = _P(__file__).parent
    _session_remote = cfg.nb_remote("2026_07_20")
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

    # Стариковский (2025): RU-only, excluded from the shared KB (still under
    # copyright there) -- a same-directory, lesson-local file instead, not
    # a remote fetch (see TRANS_BY_LANG cell for why).
    _starikovsky_path = _GU.ensure_file(
        "translations_ru_starikovsky.md", nb_dir=_root, remote_base=_session_remote,
    )
    if _starikovsky_path is not None:
        _tr, _desc = eee.parse_stanza_translations(
            _starikovsky_path.read_text(encoding="utf-8"), ref_prefix="### Odyss. "
        )
        _translations.update(_tr)
        TRANS_DESC.update(_desc)

    # Strip any <!-- ... --> annotation (e.g. an interlinear translator's
    # own echoed Greek source line) from every translator's stanza text --
    # a no-op for translators without one.
    _translations = {
        tr: {ref: eee.strip_comment_lines(txt) for ref, txt in d.items()}
        for tr, d in _translations.items()
    }

    STANZAS = [
        {
            "ref": ref,
            "lines": lines,
            # find_stanza_translation, not a bare d.get(ref, "—"): Pope is
            # transcribed against coarser "equivalent passage" spans than
            # this course's own per-lesson stanza split (Murray/Πολυλάς/
            # interlinear_{ru,en,el}/Стариковский all stay fine-grained
            # here, matching every lesson's own greek.md, since
            # greek-knowledge-eee's KB was re-split 2026-09-28 to fix
            # exactly this mismatch for the interlinear cribs) --
            # allow_coarse_fallback=False for interlinear keys is kept as
            # a safety net regardless: a coarse match there would mean
            # extra lines from a neighboring stanza, not a genuine
            # equivalent passage -- see eee-project's own
            # find_stanza_translation docstring.
            "translations": {
                tr: eee.find_stanza_translation(ref, d, allow_coarse_fallback=not tr.startswith("interlinear_"))
                for tr, d in _translations.items()
            },
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

    _vocab_filename = (
        "vocab_IX_130-151.tsv" if lang_sel.value == "ru" else f"vocab_IX_130-151_{lang_sel.value}.tsv"
    )
    QUIZ_WORDS_RAW = gu.resolve_word_grammar(
        gu.load_inflected_vocab_tsv(_vocab_filename, nb_dir=Path(__file__).parent, remote_base=cfg.nb_remote("2026_07_20")),
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
    build_period_tables = eee.build_grc_period_tables(
        ag_backend, um_backend,
        lexicons=grc_lexicons,
        el_backend=mg,
        require_lexicon="homer",
        lang=lang_sel.value,
    )
    return build_period_tables, build_paradigm_table


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
def _(cfg, gu):
    from pathlib import Path as _P
    NB_DIR = _P(__file__).parent
    NB_REMOTE = cfg.nb_remote("2026_07_20")
    for _f in (
        'Od_IX_130-151.pdf',
        'Od_IX_130-151_vocabula.docx',
    ):
        gu.ensure_file(_f, nb_dir=NB_DIR, remote_base=NB_REMOTE)

    # Set True to underline words known to eee in the poem text (coverage view)
    return (NB_REMOTE,)


@app.cell(hide_code=True)
def _(cfg, lang_sel, mo):
    from eee_project.notebook_utils import eee_footer
    _prev_url, _next_url = cfg.adjacent_urls("2026_07_20/")
    eee_footer(mo, lang=lang_sel.value, prev_url=_prev_url, next_url=_next_url, same_window=True)
    return


@app.cell(hide_code=True)
def _(mo):
    from eee_project import language_bridge
    # own cell, undisplayed: a cell that also displays/uses this would
    # rerun (and reset the bridge) on every dependent re-render
    bridge = language_bridge(mo)
    return (bridge,)


@app.cell(hide_code=True)
def _(bridge, mo):
    from eee_project import language_selector
    # takes `bridge` as a parameter (not just via closure) so marimo
    # reruns this cell -- rebuilding the dropdown with the persisted
    # language -- the moment the browser's async localStorage read lands
    lang_sel = language_selector(mo, bridge)
    return (lang_sel,)


@app.cell(hide_code=True)
def _(bridge, lang_sel, mo):
    from eee_project import save_language_selection
    save_language_selection(bridge, lang_sel)
    mo.Html(f"""
    <div style="position:fixed;top:56px;right:12px;z-index:1000;
                background:white;padding:6px 10px;border-radius:8px;
                box-shadow:0 2px 8px rgba(0,0,0,.12);">
      {lang_sel}{bridge}
    </div>
    """)
    return


if __name__ == "__main__":
    app.run()
