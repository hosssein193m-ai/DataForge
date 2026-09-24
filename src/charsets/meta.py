# -*- coding: utf-8 -*-
"""Statistics, category map, BOM constants, export configurations."""

from .whitespace import PUNCTUATION, PUNCTUATION_ASCII, WHITESPACE_ALL, WHITESPACE_STANDARD
from .digits import ALL_DIGITS
from .symbols import CURRENCY_SYMBOLS, MATH_SYMBOLS, ARROWS, COMMON_EMOJIS, EMOJI_FLAGS
from .alphabets.latin import ALL_LATIN_LETTERS, ASCII_LETTERS, ASCII_LOWERCASE, ASCII_UPPERCASE
from .alphabets.cyrillic import ALL_CYRILLIC
from .alphabets.arabic import ALL_ARABIC_SCRIPTS
from .alphabets.south_asian import ALL_SOUTH_ASIAN
from .alphabets.southeast_asian import (
    THAI_LETTERS, LAO_LETTERS, KHMER_LETTERS, MYANMAR_LETTERS,
    JAVANESE_LETTERS, JAVANESE_VOWELS, BALINESE_LETTERS, BALINESE_VOWELS,
)
from .alphabets.east_asian import (
    CHINESE_COMMON, HIRAGANA, KATAKANA, HANGUL_LETTERS,
)
from .alphabets.other_scripts import (
    GREEK_LETTERS, HEBREW_FULL, ARMENIAN_LETTERS, GEORGIAN_LETTERS,
    AMHARIC_LETTERS, TIBETAN_LETTERS, SYRIAC_LETTERS, THAANA_LETTERS,
    CHEROKEE_LETTERS, IPA_CONSONANTS, IPA_VOWELS, PHOENICIAN, CUNEIFORM_SAMPLE,
)

# ---------------------------------------------------------------------------
# Category map
# ---------------------------------------------------------------------------
CHAR_CATEGORY_MAP = {
    "LETTERS": (
        ALL_LATIN_LETTERS + ALL_CYRILLIC + ALL_ARABIC_SCRIPTS
        + ALL_SOUTH_ASIAN + GREEK_LETTERS + HEBREW_FULL
        + ARMENIAN_LETTERS + GEORGIAN_LETTERS
    ),
    "DIGITS": ALL_DIGITS,
    "PUNCTUATION": PUNCTUATION,
    "SYMBOLS": CURRENCY_SYMBOLS + MATH_SYMBOLS + ARROWS,
    "WHITESPACE": WHITESPACE_ALL,
    "EMOJI": COMMON_EMOJIS + EMOJI_FLAGS,
}

# ---------------------------------------------------------------------------
# ASCII category split
# ---------------------------------------------------------------------------
ASCII_LETTER_CHARS = ASCII_LETTERS
ASCII_DIGIT_CHARS = "0123456789"
ASCII_PUNCT_CHARS = PUNCTUATION_ASCII
ASCII_WHITESPACE_CHARS = WHITESPACE_STANDARD
ASCII_CONTROL_CHARS = "".join(chr(i) for i in range(32)) + chr(127)
ASCII_PRINTABLE_CHARS = "".join(chr(i) for i in range(32, 127))

# ---------------------------------------------------------------------------
# Aggregate "all characters" collection
# ---------------------------------------------------------------------------
ALL_CHARACTERS = (
    ALL_LATIN_LETTERS + ALL_CYRILLIC + ALL_ARABIC_SCRIPTS
    + ALL_SOUTH_ASIAN + THAI_LETTERS + LAO_LETTERS
    + KHMER_LETTERS + MYANMAR_LETTERS + JAVANESE_LETTERS + JAVANESE_VOWELS
    + BALINESE_LETTERS + BALINESE_VOWELS
    + HIRAGANA + KATAKANA + CHINESE_COMMON + HANGUL_LETTERS
    + GREEK_LETTERS + HEBREW_FULL + ARMENIAN_LETTERS
    + GEORGIAN_LETTERS + AMHARIC_LETTERS + TIBETAN_LETTERS
    + SYRIAC_LETTERS + THAANA_LETTERS + CHEROKEE_LETTERS
    + IPA_CONSONANTS + IPA_VOWELS + PHOENICIAN + CUNEIFORM_SAMPLE
    + ALL_DIGITS + PUNCTUATION + CURRENCY_SYMBOLS + MATH_SYMBOLS
    + ARROWS + COMMON_EMOJIS + EMOJI_FLAGS
)

UNIQUE_ALL_CHARACTERS = "".join(dict.fromkeys(ALL_CHARACTERS))
TOTAL_UNIQUE_CHARS = len(UNIQUE_ALL_CHARACTERS)

# ---------------------------------------------------------------------------
# Encoding compatibility
# ---------------------------------------------------------------------------
ASCII_COMPATIBLE = "".join(chr(i) for i in range(128))
LATIN1_COMPATIBLE = "".join(chr(i) for i in range(256))
UTF8_COMPATIBLE = ALL_CHARACTERS
UTF16_COMPATIBLE = ALL_CHARACTERS

# ---------------------------------------------------------------------------
# BOM constants
# ---------------------------------------------------------------------------
BOM_UTF8     = "\ufeff"
BOM_UTF16_LE = "\ufffe"
BOM_UTF16_BE = "\ufeff"
BOM_UTF32_LE = "\ufffe"
BOM_UTF32_BE = "\ufeff"

# ---------------------------------------------------------------------------
# Statistics
# ---------------------------------------------------------------------------
LATIN_LANGUAGES_COUNT       = 54
CYRILLIC_LANGUAGES_COUNT    = 16
ARABIC_LANGUAGES_COUNT      = 10
SOUTH_ASIAN_LANGUAGES_COUNT = 12
TOTAL_LANGUAGES_COVERED = (
    LATIN_LANGUAGES_COUNT + CYRILLIC_LANGUAGES_COUNT
    + ARABIC_LANGUAGES_COUNT + SOUTH_ASIAN_LANGUAGES_COUNT + 10
)

# ---------------------------------------------------------------------------
# Export configurations
# ---------------------------------------------------------------------------
EXPORTS = {
    "ascii":   ASCII_COMPATIBLE,
    "latin1":  LATIN1_COMPATIBLE,
    "utf8":    UTF8_COMPATIBLE,
    "utf16":   UTF16_COMPATIBLE,
}


__all__ = [name for name in dir() if name.isupper() and not name.startswith("_")]