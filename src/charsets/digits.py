# -*- coding: utf-8 -*-
"""
Numeric systems: binary, octal, decimal, hex, and 30+ international digit
scripts.
"""

# =============================================================================
# BASE SYSTEMS
# =============================================================================

BINARY_DIGITS  = "01"
OCTAL_DIGITS   = "01234567"
DECIMAL_DIGITS = "0123456789"
HEX_DIGITS     = DECIMAL_DIGITS + "abcdefABCDEF"


# =============================================================================
# INTERNATIONAL DIGIT SCRIPTS
# =============================================================================

PERSIAN_DIGITS         = "۰۱۲۳۴۵۶۷۸۹"
EASTERN_ARABIC_DIGITS  = PERSIAN_DIGITS   # same code points
PERSIAN_DIGITS_MAP     = {p: d for p, d in zip(PERSIAN_DIGITS, DECIMAL_DIGITS)}

DEVANAGARI_DIGITS = "०१२३४५६७८९"
BENGALI_DIGITS    = "০১২৩৪৫৬৭৮৯"
THAI_DIGITS       = "๐๑๒๓๔๕๖๗๘๙"
TAMIL_DIGITS      = "௦௧௨௩௪௫௬௭௮௯"
TELUGU_DIGITS     = "౦౧౨౩౪౫౬౭౮౯"
KANNADA_DIGITS    = "೦೧೨೩೪೫೬೭೮೯"
MALAYALAM_DIGITS  = "൦൧൨൩൪൫൬൭൮൯"
GURMUKHI_DIGITS   = "੦੧੨੩੪੫੬੭੮੯"
GUJARATI_DIGITS   = "૦૧૨૩૪૫૬૭૮૯"
ORIYA_DIGITS      = "୦୧୨୩୪୫୬୭୮୯"
TIBETAN_DIGITS    = "༠༡༢༣༤༥༦༧༨༩"
MYANMAR_DIGITS    = "၀၁၂၃၄၅၆၇၈၉"
KHMER_DIGITS      = "០១២៣៤៥៦៧៨៩"
LAO_DIGITS        = "໐໑໒໓໔໕໖໗໘໙"
MONGOLIAN_DIGITS  = "᠐᠑᠒᠓᠔᠕᠖᠗᠘᠙"
JAVANESE_DIGITS   = "꧐꧑꧒꧓꧔꧕꧖꧗꧘꧙"
BALINESE_DIGITS   = "᭐᭑᭒᭓᭔᭕᭖᭗᭘᭙"
SUNDANESE_DIGITS  = "᮰᮱᮲᮳᮴᮵᮶᮷᮸᮹"
LEPCHA_DIGITS     = "ᰰᰱᰲᰳᰴᰵᰶ᰷"
OL_CHIKI_DIGITS   = "᱐᱑᱒᱓᱔᱕᱖᱗᱘᱙"
SAURASHTRA_DIGITS = "꣐꣑꣒꣓꣔꣕꣖꣗꣘꣙"
WARANG_CITI_DIGITS = "꣰꣱ꣲꣳꣴꣵꣶꣷ꣸꣹"
MAHAJANI_DIGITS   = "𑁦𑁧𑁨𑁩𑁪𑁫𑁬𑁭𑁮𑁯"
MODI_DIGITS       = "𑙐𑙑𑙒𑙓𑙔𑙕𑙖𑙗𑙘𑙙"
NANDINAGARI_DIGITS = "𑦠𑦡𑦢𑦣𑦤𑦥𑦦𑦧𑦨𑦩"
TAKRI_DIGITS      = "𑛀𑛁𑛂𑛃𑛄𑛅𑛆𑛇𑛈𑛉"
DOGRA_DIGITS      = "𑠰𑠱𑠲𑠳𑠴𑠵𑠶𑠷𑠸𑠹"


# =============================================================================
# STYLIZED NUMBERS
# =============================================================================

CIRCLED_NUMBERS       = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳"
PARENTHESIZED_NUMBERS = "⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽⑾⑿⒀⒁⒂⒃⒄⒅⒆⒇"
ROMAN_NUMERALS_UPPER  = "ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ"
ROMAN_NUMERALS_LOWER  = "ⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹⅺⅻ"
CHINESE_NUMBERS       = "〇一二三四五六七八九十百千万亿兆"


# =============================================================================
# AGGREGATED
# =============================================================================

# NOTE: PERSIAN_DIGITS and EASTERN_ARABIC_DIGITS are the same string,
# so we only include one of them to avoid duplication.
ALL_DIGITS = (
    DECIMAL_DIGITS
    + PERSIAN_DIGITS
    + DEVANAGARI_DIGITS
    + BENGALI_DIGITS
    + THAI_DIGITS
    + TAMIL_DIGITS
    + TELUGU_DIGITS
    + KANNADA_DIGITS
    + MALAYALAM_DIGITS
    + GURMUKHI_DIGITS
    + GUJARATI_DIGITS
    + ORIYA_DIGITS
    + TIBETAN_DIGITS
    + MYANMAR_DIGITS
    + KHMER_DIGITS
    + LAO_DIGITS
    + MONGOLIAN_DIGITS
    + JAVANESE_DIGITS
    + BALINESE_DIGITS
    + SUNDANESE_DIGITS
    + LEPCHA_DIGITS
    + OL_CHIKI_DIGITS
    + SAURASHTRA_DIGITS
    + WARANG_CITI_DIGITS
    + MAHAJANI_DIGITS
    + MODI_DIGITS
    + NANDINAGARI_DIGITS
    + TAKRI_DIGITS
    + DOGRA_DIGITS
    + CIRCLED_NUMBERS
    + PARENTHESIZED_NUMBERS
    + ROMAN_NUMERALS_UPPER
    + ROMAN_NUMERALS_LOWER
    + CHINESE_NUMBERS
)

ALL_DIGITS_UNIQUE = "".join(dict.fromkeys(ALL_DIGITS))


__all__ = [
    "BINARY_DIGITS", "OCTAL_DIGITS", "DECIMAL_DIGITS", "HEX_DIGITS",
    "PERSIAN_DIGITS", "EASTERN_ARABIC_DIGITS", "PERSIAN_DIGITS_MAP",
    "DEVANAGARI_DIGITS", "BENGALI_DIGITS", "THAI_DIGITS", "TAMIL_DIGITS",
    "TELUGU_DIGITS", "KANNADA_DIGITS", "MALAYALAM_DIGITS", "GURMUKHI_DIGITS",
    "GUJARATI_DIGITS", "ORIYA_DIGITS", "TIBETAN_DIGITS", "MYANMAR_DIGITS",
    "KHMER_DIGITS", "LAO_DIGITS", "MONGOLIAN_DIGITS", "JAVANESE_DIGITS",
    "BALINESE_DIGITS", "SUNDANESE_DIGITS", "LEPCHA_DIGITS", "OL_CHIKI_DIGITS",
    "SAURASHTRA_DIGITS", "WARANG_CITI_DIGITS", "MAHAJANI_DIGITS", "MODI_DIGITS",
    "NANDINAGARI_DIGITS", "TAKRI_DIGITS", "DOGRA_DIGITS",
    "CIRCLED_NUMBERS", "PARENTHESIZED_NUMBERS",
    "ROMAN_NUMERALS_UPPER", "ROMAN_NUMERALS_LOWER", "CHINESE_NUMBERS",
    "ALL_DIGITS", "ALL_DIGITS_UNIQUE",
]