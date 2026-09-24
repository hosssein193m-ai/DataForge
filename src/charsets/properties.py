# -*- coding: utf-8 -*-
"""Character property groups: BIDI, RTL, LTR, homoglyphs, zero-width, ..."""

from .alphabets.arabic import (
    ALL_ARABIC_SCRIPTS
)
from .alphabets.other_scripts import HEBREW_FULL, SYRIAC_LETTERS, THAANA_LETTERS
from .alphabets.south_asian import ALL_SOUTH_ASIAN
from .alphabets.cyrillic import ALL_CYRILLIC
from .alphabets.latin import ALL_LATIN_LETTERS, ASCII_LETTERS
from .alphabets.east_asian import CHINESE_COMMON, HIRAGANA, KATAKANA, HANGUL_LETTERS
from .alphabets.other_scripts import GREEK_LETTERS

# ---------------------------------------------------------------------------
# Writing direction
# ---------------------------------------------------------------------------
BIDI_CHARS = ALL_ARABIC_SCRIPTS + HEBREW_FULL + SYRIAC_LETTERS
RTL_CHARS = ALL_ARABIC_SCRIPTS + HEBREW_FULL + SYRIAC_LETTERS + THAANA_LETTERS
LTR_CHARS = ALL_LATIN_LETTERS + ALL_CYRILLIC + GREEK_LETTERS
TTB_CHARS = CHINESE_COMMON + HIRAGANA + KATAKANA + HANGUL_LETTERS

# Zero-width and formatting characters
ZERO_WIDTH_CHARS = (
    "\u200b\u200c\u200d\u200e\u200f\u2060\ufeff\u00ad\u034f"
    "\u061c\u2061\u2062\u2063\u2064"
)
DIRECTION_CHARS = (
    "\u200e\u200f\u061c"
    "\u202a\u202b\u202c\u202d\u202e"
    "\u2066\u2067\u2068\u2069"
)
INVISIBLE_CHARS = ZERO_WIDTH_CHARS + DIRECTION_CHARS

# ---------------------------------------------------------------------------
# Homoglyphs (visually confusable Latin letters)
# ---------------------------------------------------------------------------
HOMOGLYPH_LATIN_A = "AΑАᎪ"
HOMOGLYPH_LATIN_B = "BΒВᏴ"
HOMOGLYPH_LATIN_E = "EΕЕ"
HOMOGLYPH_LATIN_H = "HΗНᎻ"
HOMOGLYPH_LATIN_I = "IΙІӀ"
HOMOGLYPH_LATIN_K = "KΚКᏦ"
HOMOGLYPH_LATIN_M = "MΜМᎷ"
HOMOGLYPH_LATIN_N = "NΝΝᏁ"
HOMOGLYPH_LATIN_O = "OΟОՕ"
HOMOGLYPH_LATIN_P = "PΡРᏢ"
HOMOGLYPH_LATIN_T = "TΤТᎢ"
HOMOGLYPH_LATIN_X = "XΧХᚷ"
HOMOGLYPH_LATIN_Y = "YΥҮ"

# ---------------------------------------------------------------------------
# Layout hints
# ---------------------------------------------------------------------------
DESCENDER_CHARS = "gjpqyQ"
ASCENDER_CHARS = "bdfhikltABCDEFGHIJKLMNOPQRSTUVWXYZ"
MONOSPACE_DIGITS = "0123456789"

FULLWIDTH_CHARS = (
    "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
    "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"
    "０１２３４５６７８９"
)
HALFWIDTH_CHARS = (
    "ｦｧｨｩｪｫｬｭｮｯｰｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝﾞﾟ"
)


__all__ = [name for name in dir() if name.isupper() and not name.startswith("_")]