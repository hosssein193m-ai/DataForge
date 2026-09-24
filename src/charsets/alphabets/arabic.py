# -*- coding: utf-8 -*-
"""Arabic-based scripts for 10+ languages."""

ARABIC_LETTERS = "ءآأؤإئابةتثجحخدذرزسشصضطظعغفقكلمنهويى"
ARABIC_LETTERS_LIST = list(ARABIC_LETTERS)

ARABIC_ALL_FORMS = (
    ARABIC_LETTERS
    + "ۀةكىًٌٍَُِّْٰٕٓٔٱٹپچڈڑژکگںھہۃیے"
)

PERSIAN_LETTERS = "آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی"
PERSIAN_LETTERS_LIST = list(PERSIAN_LETTERS)
PERSIAN_FULL = PERSIAN_LETTERS + "ءأؤإئۀةك"

URDU_LETTERS = "آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهیٹڈڑںھے"
URDU_LETTERS_LIST = list(URDU_LETTERS)

PASHTO_LETTERS = "آابپتټثجځچڅحخدډذرړزژږسشښصضطظعغفقکګلمنڼوهیې"
PASHTO_LETTERS_LIST = list(PASHTO_LETTERS)

KURDISH_ARABIC = "ئابپتجچحخدرزژسشعغفڤقکگلڵمنهوەێ"
KURDISH_ARABIC_LIST = list(KURDISH_ARABIC)

SINDHI_LETTERS = "آابٻتثپجڄچحخدڌڏرزسشصضطظعغفڦقڪکگڱلمنڻوهءي"
SINDHI_LETTERS_LIST = list(SINDHI_LETTERS)

UYGHUR_ARABIC = "ئابپتجچخدرزژسشغفقكگڭلمنھوۇۆۈۋېى"
UYGHUR_ARABIC_LIST = list(UYGHUR_ARABIC)

JAWI_LETTERS = "ابجچدرفغهيحکلمنڤوقسرتوءيڠ"
JAWI_LETTERS_LIST = list(JAWI_LETTERS)

BALOCHI_ARABIC = "آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهیءے"
BALOCHI_ARABIC_LIST = list(BALOCHI_ARABIC)

KASHMIRI_ARABIC = "آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهیٹڈڑں"
KASHMIRI_ARABIC_LIST = list(KASHMIRI_ARABIC)


# Diacritics / harakat
ARABIC_DIACRITICS  = "ًٌٍَُِّْٰٕٓٔ"
PERSIAN_HARAKAT    = "ًٌٍَُِّْ"
PERSIAN_PUNCTUATION = "،؛؟٪٬٫٭ٰ"


ALL_ARABIC_SCRIPTS = "".join(dict.fromkeys(
    ARABIC_LETTERS + PERSIAN_LETTERS + URDU_LETTERS
    + PASHTO_LETTERS + KURDISH_ARABIC + SINDHI_LETTERS
    + UYGHUR_ARABIC + JAWI_LETTERS + BALOCHI_ARABIC
    + KASHMIRI_ARABIC
))


__all__ = [name for name in dir() if name.isupper() and not name.startswith("_")]