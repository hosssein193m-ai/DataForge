# -*- coding: utf-8 -*-
"""
================================================================================
 utils.py
================================================================================
 Utility functions: validation, normalization, classification, bitwise ops,
 and ASCII/binary art.

 Exported
 --------
 is_valid_binary, normalize_binary, count_bits, binary_length, split_binary
 is_control, is_printable, is_extended, is_ascii
 XOR, AND, OR, NOT
 binary_art, ascii_art_from_text
================================================================================
"""

from __future__ import annotations
import re
from typing import Dict, List, Tuple


# =============================================================================
# Validation / normalization
# =============================================================================

_BIN_CLEAN_RE = re.compile(r"[^01]")


def is_valid_binary(binary: str) -> bool:
    """
    Return True if the string contains at least one '0' or '1' and no
    invalid characters (after ignoring whitespace).

    Examples
    --------
    >>> is_valid_binary('0100 0001')
    True
    >>> is_valid_binary('0100 0002')
    False
    """
    return bool(_BIN_CLEAN_RE.sub("", binary))


def normalize_binary(binary: str) -> str:
    """
    Remove every non-binary character (spaces, tabs, newlines, ...).

    Examples
    --------
    >>> normalize_binary('0100 0001\\n0100 0010')
    '0100000101000010'
    """
    return _BIN_CLEAN_RE.sub("", binary)


def count_bits(binary: str) -> Dict[str, int]:
    """
    Count '0' and '1' bits in a binary string.

    Examples
    --------
    >>> count_bits('01000001')
    {'zeros': 7, 'ones': 1, 'total': 8}
    """
    clean = normalize_binary(binary)
    ones = clean.count("1")
    zeros = clean.count("0")
    return {"zeros": zeros, "ones": ones, "total": len(clean)}


def binary_length(binary: str) -> int:
    """Return the number of significant bits."""
    return len(normalize_binary(binary))


def split_binary(binary: str, chunk: int = 8, sep: str = " ") -> str:
    """
    Split a binary string into chunks of `chunk` bits.

    Examples
    --------
    >>> split_binary('0100000101000010')
    '01000001 01000010'
    """
    clean = normalize_binary(binary)
    return sep.join(clean[i:i + chunk] for i in range(0, len(clean), chunk))


# =============================================================================
# Character classification
# =============================================================================

def is_control(char: str) -> bool:
    """True if `char` is an ASCII control character (0-31 or 127)."""
    return len(char) == 1 and (ord(char) < 32 or ord(char) == 127)


def is_printable(char: str) -> bool:
    """True if `char` is a printable ASCII character (32-126)."""
    return len(char) == 1 and 32 <= ord(char) <= 126


def is_extended(char: str) -> bool:
    """True if `char` is in the extended range (128-255)."""
    return len(char) == 1 and 128 <= ord(char) <= 255


def is_ascii(char: str) -> bool:
    """True if `char` is within the 7-bit ASCII range (0-127)."""
    return len(char) == 1 and 0 <= ord(char) <= 127


# =============================================================================
# Bitwise operations
# =============================================================================

def _align(a: str, b: str) -> Tuple[str, str]:
    """Left-pad two binary strings to equal length."""
    a, b = normalize_binary(a), normalize_binary(b)
    n = max(len(a), len(b))
    return a.zfill(n), b.zfill(n)


def XOR(a: str, b: str) -> str:
    """
    Bitwise XOR of two binary strings.

    Examples
    --------
    >>> XOR('1010', '0110')
    '1100'
    """
    a, b = _align(a, b)
    return "".join("1" if x != y else "0" for x, y in zip(a, b))


def AND(a: str, b: str) -> str:
    """
    Bitwise AND of two binary strings.

    Examples
    --------
    >>> AND('1010', '0110')
    '0010'
    """
    a, b = _align(a, b)
    return "".join("1" if x == y == "1" else "0" for x, y in zip(a, b))


def OR(a: str, b: str) -> str:
    """
    Bitwise OR of two binary strings.

    Examples
    --------
    >>> OR('1010', '0110')
    '1110'
    """
    a, b = _align(a, b)
    return "".join("1" if x == "1" or y == "1" else "0" for x, y in zip(a, b))


def NOT(a: str) -> str:
    """
    Bitwise NOT (one's complement) of a binary string.

    Examples
    --------
    >>> NOT('1010')
    '0101'
    """
    return "".join("1" if x == "0" else "0" for x in normalize_binary(a))


# =============================================================================
# ASCII / Binary art
# =============================================================================

def binary_art(text: str, on: str = "█", off: str = "·") -> str:
    """
    Render text as binary art using two glyphs.

    Examples
    --------
    >>> print(binary_art('A'))
    ·█·····█
    """
    from .converters import char_to_binary
    lines: List[str] = []
    for ch in text:
        lines.append("".join(on if b == "1" else off for b in char_to_binary(ch)))
    return "\n".join(lines)


def ascii_art_from_text(text: str, on: str = "#", off: str = " ") -> str:
    """
    Alias of `binary_art` with ASCII-friendly default glyphs.

    Examples
    --------
    >>> print(ascii_art_from_text('A'))
     #     #
    """
    return binary_art(text, on=on, off=off)