# -*- coding: utf-8 -*-
"""
================================================================================
 converters.py
================================================================================
 Conversion functions between text, binary, decimal, hex, octal, and UTF-8.

 All functions are pure, type-hinted, and documented with examples.

 Exported
 --------
 char_to_binary, binary_to_char
 text_to_binary, binary_to_text
 dec_to_binary, binary_to_dec
 hex_to_binary, binary_to_hex
 oct_to_binary, binary_to_oct
 text_to_bytes, bytes_to_text
 text_to_utf8_binary, utf8_binary_to_text
 char_info, char_info_from_binary, char_info_from_dec
 to_upper_binary, to_lower_binary
================================================================================
"""

from __future__ import annotations
from typing import Dict, Union

from .tables import (
    ASCII_TO_BINARY, BINARY_TO_ASCII, ASCII_INFO,
)
from .utils import (
    normalize_binary, is_ascii, is_control, is_printable, is_extended,
)


# =============================================================================
# Core: char <-> binary
# =============================================================================

def char_to_binary(char: str, pad: int = 8) -> str:
    """
    Convert a single character to its binary representation.

    Parameters
    ----------
    char : str
        A single character.
    pad : int, optional
        Minimum number of bits (default 8).

    Returns
    -------
    str
        Zero-padded binary string.

    Raises
    ------
    ValueError
        If `char` is not exactly one character.

    Examples
    --------
    >>> char_to_binary('A')
    '01000001'
    >>> char_to_binary('A', pad=16)
    '0000000001000001'
    """
    if len(char) != 1:
        raise ValueError("char_to_binary expects exactly one character.")
    if char in ASCII_TO_BINARY and pad == 8:
        return ASCII_TO_BINARY[char]
    return format(ord(char) & 0xFF, f"0{pad}b")


def binary_to_char(binary: str) -> str:
    """
    Convert an 8-bit binary string to a character.

    Examples
    --------
    >>> binary_to_char('01000001')
    'A'
    """
    binary = normalize_binary(binary)
    if len(binary) != 8:
        raise ValueError("binary_to_char expects exactly 8 bits.")
    return BINARY_TO_ASCII.get(binary, chr(int(binary, 2)))


# =============================================================================
# Core: text <-> binary
# =============================================================================

def text_to_binary(text: str, sep: str = " ", pad: int = 8) -> str:
    """
    Convert a text string to its binary representation.

    Examples
    --------
    >>> text_to_binary('Hi')
    '01001000 01101001'
    >>> text_to_binary('Hi', sep='')
    '0100100001101001'
    """
    return sep.join(char_to_binary(ch, pad=pad) for ch in text)


def binary_to_text(binary: str) -> str:
    """
    Decode a binary string back to text.

    Examples
    --------
    >>> binary_to_text('01001000 01101001')
    'Hi'
    """
    clean = normalize_binary(binary)
    if len(clean) % 8 != 0:
        raise ValueError(f"Binary length ({len(clean)}) must be a multiple of 8.")
    return "".join(
        BINARY_TO_ASCII.get(clean[i:i + 8], chr(int(clean[i:i + 8], 2)))
        for i in range(0, len(clean), 8)
    )


# =============================================================================
# Numeric base conversions
# =============================================================================

def dec_to_binary(value: int, pad: int = 8) -> str:
    """
    Convert a decimal integer (0-255) to an 8-bit binary string.

    Examples
    --------
    >>> dec_to_binary(65)
    '01000001'
    """
    if not 0 <= value <= 255:
        raise ValueError("Decimal value must be between 0 and 255.")
    return format(value, f"0{pad}b")


def binary_to_dec(binary: str) -> int:
    """
    Convert a binary string to a decimal integer.

    Examples
    --------
    >>> binary_to_dec('01000001')
    65
    """
    binary = normalize_binary(binary)
    if not binary:
        raise ValueError("Empty binary string.")
    return int(binary, 2)


def hex_to_binary(hex_str: str, pad: int = 8) -> str:
    """
    Convert a hexadecimal string to binary.

    Examples
    --------
    >>> hex_to_binary('41')
    '01000001'
    """
    hex_str = hex_str.strip().upper().replace("0X", "")
    return format(int(hex_str, 16), f"0{pad}b")


def binary_to_hex(binary: str) -> str:
    """
    Convert a binary string to an uppercase hexadecimal string.

    Examples
    --------
    >>> binary_to_hex('01000001')
    '41'
    """
    return format(binary_to_dec(binary), "02X")


def oct_to_binary(oct_str: str, pad: int = 8) -> str:
    """
    Convert an octal string to binary.

    Examples
    --------
    >>> oct_to_binary('101')
    '01000001'
    """
    return format(int(oct_str.strip(), 8), f"0{pad}b")


def binary_to_oct(binary: str) -> str:
    """
    Convert a binary string to an octal string.

    Examples
    --------
    >>> binary_to_oct('01000001')
    '101'
    """
    return format(binary_to_dec(binary), "03o")


# =============================================================================
# Bytes / UTF-8 helpers
# =============================================================================

def text_to_bytes(text: str, encoding: str = "utf-8") -> bytes:
    """Encode text to bytes."""
    return text.encode(encoding)


def bytes_to_text(data: bytes, encoding: str = "utf-8") -> str:
    """Decode bytes to text."""
    return data.decode(encoding)


def text_to_utf8_binary(text: str, sep: str = " ") -> str:
    """
    Convert text to its UTF-8 binary representation.

    Examples
    --------
    >>> text_to_utf8_binary('A')
    '01000001'
    >>> text_to_utf8_binary('س')
    '11011000 10110011'
    """
    return sep.join(format(b, "08b") for b in text.encode("utf-8"))


def utf8_binary_to_text(binary: str) -> str:
    """
    Decode a UTF-8 binary string back to text.

    Examples
    --------
    >>> utf8_binary_to_text('01000001')
    'A'
    """
    clean = normalize_binary(binary)
    if len(clean) % 8 != 0:
        raise ValueError("Binary length must be a multiple of 8.")
    data = bytes(int(clean[i:i + 8], 2) for i in range(0, len(clean), 8))
    return data.decode("utf-8")


# =============================================================================
# Info helpers
# =============================================================================

def char_info(char: str) -> Dict[str, Union[int, str, bool]]:
    """
    Return a full information dictionary for a character.

    Examples
    --------
    >>> char_info('A')['dec']
    65
    """
    if len(char) != 1:
        raise ValueError("char_info expects exactly one character.")
    code = ord(char)
    return {
        "char":         char,
        "dec":          code,
        "oct":          format(code, "03o"),
        "hex":          format(code, "02X"),
        "bin":          char_to_binary(char),
        "html":         f"&#{code};",
        "is_ascii":     is_ascii(char),
        "is_control":   is_control(char),
        "is_printable": is_printable(char),
        "is_extended":  is_extended(char),
    }


def char_info_from_binary(binary: str) -> Dict[str, Union[int, str, bool]]:
    """Return char_info() for the character decoded from `binary`."""
    return char_info(binary_to_char(binary))


def char_info_from_dec(value: int) -> Dict[str, Union[int, str, bool]]:
    """Return char_info() for the character with decimal code `value`."""
    return char_info(chr(value))


# =============================================================================
# Case helpers
# =============================================================================

def to_upper_binary(binary: str) -> str:
    """
    Convert a lowercase-ASCII binary string to uppercase.

    Examples
    --------
    >>> to_upper_binary(text_to_binary('abc'))
    '01000001 01000010 01000011'
    """
    return text_to_binary(binary_to_text(binary).upper())


def to_lower_binary(binary: str) -> str:
    """
    Convert an uppercase-ASCII binary string to lowercase.

    Examples
    --------
    >>> to_lower_binary(text_to_binary('ABC'))
    '01100001 01100010 01100011'
    """
    return text_to_binary(binary_to_text(binary).lower())