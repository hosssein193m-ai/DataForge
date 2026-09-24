# -*- coding: utf-8 -*-
"""
================================================================================
 iran/charset.py
================================================================================
 مجموعه‌های ترکیبی کاراکتر فارسی.
================================================================================
"""

from .letters import (
    PERSIAN_LETTERS, PERSIAN_DIGITS, PERSIAN_DIACRITICS_ALL,
    PERSIAN_PUNCTUATION, PERSIAN_INVISIBLE, PUNCTUATION_UNICODE,
)

PERSIAN_CHARSET      = PERSIAN_LETTERS + PERSIAN_DIGITS + PUNCTUATION_UNICODE
PERSIAN_CHARSET_LIST = list(PERSIAN_CHARSET)

PERSIAN_LETTERS_ONLY           = PERSIAN_LETTERS
PERSIAN_LETTERS_WITH_DIACRITICS = PERSIAN_LETTERS + PERSIAN_DIACRITICS_ALL

PERSIAN_TEXT_CHARS = (
    PERSIAN_LETTERS + PERSIAN_DIACRITICS_ALL
    + PERSIAN_PUNCTUATION + PERSIAN_INVISIBLE
)

PERSIAN_ALPHANUMERIC = PERSIAN_LETTERS + PERSIAN_DIGITS

PERSIAN_FULL = (
    PERSIAN_LETTERS + PERSIAN_DIGITS + PERSIAN_DIACRITICS_ALL
    + PERSIAN_PUNCTUATION + PERSIAN_INVISIBLE + PUNCTUATION_UNICODE
)
PERSIAN_FULL_UNIQUE = "".join(dict.fromkeys(PERSIAN_FULL))

PERSIAN_WHITESPACE       = " \t\n\r" + PERSIAN_INVISIBLE
PERSIAN_FILENAME_SAFE    = PERSIAN_ALPHANUMERIC + " -_.()"
PERSIAN_URL_SAFE         = PERSIAN_ALPHANUMERIC + "-._~"
PERSIAN_PASSWORD_EXTRA   = "!@#$%^&*()-_=+[]{}|;:,.<>?/"


__all__ = [name for name in dir() if name.isupper() and not name.startswith("_")]