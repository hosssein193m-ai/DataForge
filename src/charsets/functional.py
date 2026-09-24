# -*- coding: utf-8 -*-
"""Functional character sets: URL-safe, BASE64, EMAIL, IDENTIFIER, ..."""

from .alphabets.latin import ASCII_LOWERCASE, ASCII_UPPERCASE, ASCII_LETTERS
from .digits import DECIMAL_DIGITS, HEX_DIGITS

# ---------------------------------------------------------------------------
# Common encoding alphabets
# ---------------------------------------------------------------------------
URL_SAFE_CHARS = ASCII_LOWERCASE + ASCII_UPPERCASE + DECIMAL_DIGITS + "-._~"
BASE64_CHARS = ASCII_UPPERCASE + ASCII_LOWERCASE + DECIMAL_DIGITS + "+/="
BASE32_CHARS = ASCII_UPPERCASE + "234567="
CROCKFORD_BASE32 = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"

HEX_CHARS = HEX_DIGITS

# ---------------------------------------------------------------------------
# Programming / markup
# ---------------------------------------------------------------------------
IDENTIFIER_CHARS = ASCII_LETTERS + DECIMAL_DIGITS + "_"
SQL_IDENTIFIER_CHARS = ASCII_LETTERS + DECIMAL_DIGITS + "_"

# HTML/XML
HTML_ESCAPE_CHARS = "<>&\"'"
XML_ESCAPE_CHARS = "<>&\"'"

# JSON
JSON_ESCAPE_CHARS = "\"\\/\b\f\n\r\t"

# Python
PYTHON_ESCAPE_CHARS = "\n\r\t\\'\"\a\b\f\v"

# ---------------------------------------------------------------------------
# Internet
# ---------------------------------------------------------------------------
EMAIL_LOCAL_CHARS = ASCII_LETTERS + DECIMAL_DIGITS + "!#$%&'*+-/=?^_`{|}~."
DOMAIN_CHARS = ASCII_LOWERCASE + DECIMAL_DIGITS + "-."

# ---------------------------------------------------------------------------
# Files / passwords / UI
# ---------------------------------------------------------------------------
FILENAME_SAFE_CHARS = ASCII_LETTERS + DECIMAL_DIGITS + "._-"
PASSWORD_SPECIAL = "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"

# Regex-style numeric validation character sets
NUMERIC_CHARS = DECIMAL_DIGITS + ".-+eE"
INTEGER_CHARS = DECIMAL_DIGITS + "-"
FLOAT_CHARS = DECIMAL_DIGITS + ".-+eE"
HEX_NUMERIC_CHARS = HEX_DIGITS + "xX"
OCTAL_NUMERIC_CHARS = "01234567" + "oO"
BINARY_NUMERIC_CHARS = "01" + "bB"

ALPHA_CHARS = ASCII_LETTERS
ALPHANUMERIC_CHARS = ASCII_LETTERS + DECIMAL_DIGITS
ALPHANUMERIC_EXTENDED = ALPHANUMERIC_CHARS + "_-"


__all__ = [name for name in dir() if name.isupper() and not name.startswith("_")]