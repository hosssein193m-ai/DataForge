# -*- coding: utf-8 -*-
"""
================================================================================
 ascii_binary — Python package
================================================================================
 A comprehensive ASCII / Binary conversion library based on the ASCII table
 and Windows-1252 extended character set (source: ascii-code.com).

 Quick start
 -----------
 >>> from ascii_binary import text_to_binary, binary_to_text
 >>> text_to_binary('Hi')
 '01001000 01101001'
 >>> binary_to_text('01001000 01101001')
 'Hi'

"""

from __future__ import annotations

# --- Lookup tables -----------------------------------------------------------
from .tables import (
    ASCII_TO_BINARY, BINARY_TO_ASCII,
    DEC_TO_BINARY, BINARY_TO_DEC,
    HEX_TO_BINARY, BINARY_TO_HEX,
    OCT_TO_BINARY, BINARY_TO_OCT,
    ASCII_INFO,
)

# --- Converters --------------------------------------------------------------
from .converters import (
    char_to_binary, binary_to_char,
    text_to_binary, binary_to_text,
    dec_to_binary, binary_to_dec,
    hex_to_binary, binary_to_hex,
    oct_to_binary, binary_to_oct,
    text_to_bytes, bytes_to_text,
    text_to_utf8_binary, utf8_binary_to_text,
    char_info, char_info_from_binary, char_info_from_dec,
    to_upper_binary, to_lower_binary,
)

# --- Utilities ---------------------------------------------------------------
from .utils import (
    is_valid_binary, normalize_binary, count_bits,
    binary_length, split_binary,
    is_control, is_printable, is_extended, is_ascii,
    XOR, AND, OR, NOT,
    binary_art, ascii_art_from_text,
)

__version__ = "1.1.0"

__all__ = [
    # Tables
    "ASCII_TO_BINARY", "BINARY_TO_ASCII",
    "DEC_TO_BINARY", "BINARY_TO_DEC",
    "HEX_TO_BINARY", "BINARY_TO_HEX",
    "OCT_TO_BINARY", "BINARY_TO_OCT",
    "ASCII_INFO",
    # Converters
    "char_to_binary", "binary_to_char",
    "text_to_binary", "binary_to_text",
    "dec_to_binary", "binary_to_dec",
    "hex_to_binary", "binary_to_hex",
    "oct_to_binary", "binary_to_oct",
    "text_to_bytes", "bytes_to_text",
    "text_to_utf8_binary", "utf8_binary_to_text",
    "char_info", "char_info_from_binary", "char_info_from_dec",
    "to_upper_binary", "to_lower_binary",
    # Utilities
    "is_valid_binary", "normalize_binary", "count_bits",
    "binary_length", "split_binary",
    "is_control", "is_printable", "is_extended", "is_ascii",
    "XOR", "AND", "OR", "NOT",
    "binary_art", "ascii_art_from_text",
]