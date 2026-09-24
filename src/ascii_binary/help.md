# `HELP.md` — Complete Documentation

Here is the complete `HELP.md` file for the `ascii_binary` package. Save it in the root of the package folder.

---

```markdown
# ascii_binary — Help & Documentation

A comprehensive, dependency-free Python library for **ASCII ↔ Binary** conversions,
based on the ASCII table and the **Windows-1252** extended character set
(source: [ascii-code.com](https://www.ascii-code.com)).

- **Version:** 1.1.0
- **Python:** 3.8+
- **License:** MIT
- **Dependencies:** none (standard library only)

---

## Table of Contents

1. [Installation](#1-installation)
2. [Project Structure](#2-project-structure)
3. [Quick Start](#3-quick-start)
4. [API Reference](#4-api-reference)
   - 4.1 [Lookup Tables](#41-lookup-tables)
   - 4.2 [Core Conversions](#42-core-conversions)
   - 4.3 [Numeric Base Conversions](#43-numeric-base-conversions)
   - 4.4 [UTF-8 / Bytes Helpers](#44-utf-8--bytes-helpers)
   - 4.5 [Validation & Normalization](#45-validation--normalization)
   - 4.6 [Character Classification](#46-character-classification)
   - 4.7 [Case Helpers](#47-case-helpers)
   - 4.8 [Information Helpers](#48-information-helpers)
   - 4.9 [Bitwise Operations](#49-bitwise-operations)
   - 4.10 [Binary / ASCII Art](#410-binary--ascii-art)
5. [Examples](#5-examples)
6. [Command-Line Demo](#6-command-line-demo)
7. [Error Handling](#7-error-handling)
8. [Notes & Limitations](#8-notes--limitations)
9. [References](#9-references)
10. [License](#10-license)

---

## 1. Installation

The package is pure Python. Just copy the `ascii_binary/` folder into your
project and import it.

```bash
your_project/
├── ascii_binary/
│   ├── __init__.py
│   ├── tables.py
│   ├── converters.py
│   ├── utils.py
│   └── demo.py
├── HELP.md
└── your_script.py
```

Then in your code:

```python
from ascii_binary import text_to_binary, binary_to_text
```

If you want to run the demo directly:

```bash
python -m ascii_binary.demo
```

---

## 2. Project Structure

| File | Purpose |
|------|---------|
| `__init__.py`  | Package entry point. Re-exports everything for convenience. |
| `tables.py`    | All lookup dictionaries (`ASCII_TO_BINARY`, `BINARY_TO_ASCII`, …). |
| `converters.py`| Conversion functions (text ↔ binary, base conversions, UTF-8). |
| `utils.py`     | Validation, classification, bitwise operations, ASCII art. |
| `demo.py`      | Runnable demo showing all major features. |

---

## 3. Quick Start

```python
from ascii_binary import (
    text_to_binary, binary_to_text,
    char_info, XOR,
)

# Encode text to binary
binary = text_to_binary("Hi")
print(binary)                    # 01001000 01101001

# Decode binary back to text
print(binary_to_text(binary))    # Hi

# Inspect a character
info = char_info("A")
print(info["dec"], info["hex"], info["bin"])
# 65 41 01000001

# Bitwise XOR
print(XOR("1010", "0110"))       # 1100
```

---

## 4. API Reference

### 4.1 Lookup Tables

| Name | Type | Key → Value |
|------|------|-------------|
| `ASCII_TO_BINARY` | `dict[str, str]` | `'A'` → `'01000001'` |
| `BINARY_TO_ASCII` | `dict[str, str]` | `'01000001'` → `'A'` |
| `DEC_TO_BINARY`   | `dict[int, str]` | `65` → `'01000001'` |
| `BINARY_TO_DEC`   | `dict[str, int]` | `'01000001'` → `65` |
| `HEX_TO_BINARY`   | `dict[str, str]` | `'41'` → `'01000001'` |
| `BINARY_TO_HEX`   | `dict[str, str]` | `'01000001'` → `'41'` |
| `OCT_TO_BINARY`   | `dict[str, str]` | `'101'` → `'01000001'` |
| `BINARY_TO_OCT`   | `dict[str, str]` | `'01000001'` → `'101'` |
| `ASCII_INFO`      | `dict[str, dict]`| `'A'` → `{dec, oct, hex, bin, html, …}` |

**Example**

```python
from ascii_binary import ASCII_TO_BINARY, DEC_TO_BINARY

print(ASCII_TO_BINARY["A"])   # 01000001
print(DEC_TO_BINARY[65])      # 01000001
```

---

### 4.2 Core Conversions

#### `char_to_binary(char, pad=8) -> str`

Convert a single character to binary.

```python
>>> char_to_binary("A")
'01000001'
>>> char_to_binary("A", pad=16)
'0000000001000001'
```

Raises `ValueError` if `char` is not exactly one character.

---

#### `binary_to_char(binary) -> str`

Convert an 8-bit binary string to a character.

```python
>>> binary_to_char("01000001")
'A'
```

Raises `ValueError` if the cleaned string is not exactly 8 bits.

---

#### `text_to_binary(text, sep=" ", pad=8) -> str`

Convert a string to its binary representation.

```python
>>> text_to_binary("Hi")
'01001000 01101001'
>>> text_to_binary("Hi", sep="")
'0100100001101001'
>>> text_to_binary("Hi", sep="-")
'01001000-01101001'
```

---

#### `binary_to_text(binary) -> str`

Decode a binary string back to text. Spaces, tabs and newlines are ignored.

```python
>>> binary_to_text("01001000 01101001")
'Hi'
>>> binary_to_text("0100100001101001")
'Hi'
```

Raises `ValueError` if the cleaned length is not a multiple of 8.

---

### 4.3 Numeric Base Conversions

| Function | Example |
|----------|---------|
| `dec_to_binary(65)` | → `'01000001'` |
| `binary_to_dec('01000001')` | → `65` |
| `hex_to_binary('41')` | → `'01000001'` |
| `binary_to_hex('01000001')` | → `'41'` |
| `oct_to_binary('101')` | → `'01000001'` |
| `binary_to_oct('01000001')` | → `'101'` |

```python
>>> dec_to_binary(65)
'01000001'
>>> hex_to_binary("0x41")
'01000001'
>>> binary_to_hex("01000001")
'41'
```

`dec_to_binary` raises `ValueError` if the value is outside 0–255.

---

### 4.4 UTF-8 / Bytes Helpers

| Function | Purpose |
|----------|---------|
| `text_to_bytes(text, encoding='utf-8')` | Encode `str` → `bytes` |
| `bytes_to_text(data, encoding='utf-8')` | Decode `bytes` → `str` |
| `text_to_utf8_binary(text, sep=' ')` | Text → UTF-8 binary (variable length) |
| `utf8_binary_to_text(binary)` | UTF-8 binary → text |

```python
>>> text_to_utf8_binary("A")
'01000001'
>>> text_to_utf8_binary("س")
'11011000 10110011'
>>> utf8_binary_to_text("11011000 10110011")
'س'
```

Use these when working with non-Latin scripts (Persian, Arabic, emoji, …),
where the 8-bit ASCII table is not enough.

---

### 4.5 Validation & Normalization

#### `is_valid_binary(binary) -> bool`

Returns `True` if the string contains at least one `0`/`1` and no invalid
characters (after ignoring whitespace).

```python
>>> is_valid_binary("0100 0001")
True
>>> is_valid_binary("0100 0002")
False
```

---

#### `normalize_binary(binary) -> str`

Remove every non-binary character.

```python
>>> normalize_binary("0100 0001\n0100 0010")
'0100000101000010'
```

---

#### `count_bits(binary) -> dict`

Count `0` and `1` bits.

```python
>>> count_bits("01000001")
{'zeros': 7, 'ones': 1, 'total': 8}
```

---

#### `binary_length(binary) -> int`

Number of significant bits.

```python
>>> binary_length("0100 0001")
8
```

---

#### `split_binary(binary, chunk=8, sep=" ") -> str`

Split a binary string into chunks.

```python
>>> split_binary("0100000101000010")
'01000001 01000010'
>>> split_binary("0100000101000010", chunk=4)
'0100 0001 0100 0010'
```

---

### 4.6 Character Classification

| Function | Range | Example |
|----------|-------|---------|
| `is_control(ch)`   | 0–31, 127 | `is_control('\n')` → `True` |
| `is_printable(ch)` | 32–126    | `is_printable('A')` → `True` |
| `is_extended(ch)`  | 128–255   | `is_extended('é')` → `True` |
| `is_ascii(ch)`     | 0–127     | `is_ascii('A')` → `True` |

All functions expect exactly one character and return `bool`.

---

### 4.7 Case Helpers

#### `to_upper_binary(binary) -> str`

```python
>>> to_upper_binary(text_to_binary("abc"))
'01000001 01000010 01000011'
```

#### `to_lower_binary(binary) -> str`

```python
>>> to_lower_binary(text_to_binary("ABC"))
'01100001 01100010 01100011'
```

---

### 4.8 Information Helpers

#### `char_info(char) -> dict`

Return a full information dictionary.

```python
>>> char_info("A")
{
    'char': 'A',
    'dec': 65,
    'oct': '101',
    'hex': '41',
    'bin': '01000001',
    'html': '&#65;',
    'is_ascii': True,
    'is_control': False,
    'is_printable': True,
    'is_extended': False,
}
```

#### `char_info_from_binary(binary) -> dict`

Same as `char_info`, but takes an 8-bit binary string.

#### `char_info_from_dec(value) -> dict`

Same as `char_info`, but takes a decimal code (`0–255`).

---

### 4.9 Bitwise Operations

All operate on binary strings. Shorter strings are left-padded with zeros.

| Function | Example | Result |
|----------|---------|--------|
| `XOR('1010', '0110')` | | `'1100'` |
| `AND('1010', '0110')` | | `'0010'` |
| `OR('1010', '0110')`  | | `'1110'` |
| `NOT('1010')`         | | `'0101'` |

```python
>>> XOR("1010", "0110")
'1100'
>>> NOT("1010")
'0101'
```

---

### 4.10 Binary / ASCII Art

#### `binary_art(text, on="█", off="·") -> str`

Render text as binary art with two glyphs.

```python
>>> print(binary_art("A"))
·█·····█
```

#### `ascii_art_from_text(text, on="#", off=" ") -> str`

Same, with ASCII-friendly glyphs.

```python
>>> print(ascii_art_from_text("A"))
 #     #
```

---

## 5. Examples

### 5.1 Encode / Decode a Message

```python
from ascii_binary import text_to_binary, binary_to_text

msg = "Hello"
enc = text_to_binary(msg)
print(enc)              # 01001000 01100101 01101100 01101100 01101111

dec = binary_to_text(enc)
print(dec)              # Hello
```

### 5.2 Work With a Single Character

```python
from ascii_binary import char_info

info = char_info("é")
print(info["dec"])      # 233
print(info["hex"])      # E9
print(info["bin"])      # 11101001
print(info["is_extended"])  # True
```

### 5.3 Convert Between Bases

```python
from ascii_binary import binary_to_dec, binary_to_hex, binary_to_oct

b = "01000001"
print(binary_to_dec(b))  # 65
print(binary_to_hex(b))  # 41
print(binary_to_oct(b))  # 101
```

### 5.4 Encode Non-Latin Text (UTF-8)

```python
from ascii_binary import text_to_utf8_binary, utf8_binary_to_text

b = text_to_utf8_binary("سلام")
print(b)
# 11011000 10110011 11011001 10000100 11011000 10100111 11011001 10000101

print(utf8_binary_to_text(b))
# سلام
```

### 5.5 Bitwise Operations

```python
from ascii_binary import XOR

key  = "10101010"
data = "11001100"
enc  = XOR(data, key)
dec  = XOR(enc, key)

print(enc)   # 01100110
print(dec)   # 11001100
```

### 5.6 Inspect Every Character of a String

```python
from ascii_binary import char_info

for ch in "AB1":
    info = char_info(ch)
    print(f"{ch!r} -> DEC={info['dec']:3d}  HEX={info['hex']}  BIN={info['bin']}")
# 'A' -> DEC= 65  HEX=41  BIN=01000001
# 'B' -> DEC= 66  HEX=42  BIN=01000010
# '1' -> DEC= 49  HEX=31  BIN=00110001
```

---

## 6. Command-Line Demo

```bash
python -m ascii_binary.demo
```

Prints a full demonstration covering:

- Encoding / decoding text
- Character information
- Numeric base conversions
- Bitwise operations
- Bit counting
- UTF-8 encoding
- Binary art

---

## 7. Error Handling

| Function | Raises | When |
|----------|--------|------|
| `char_to_binary` | `ValueError` | input length ≠ 1 |
| `binary_to_char` | `ValueError` | cleaned length ≠ 8 |
| `binary_to_text` | `ValueError` | cleaned length % 8 ≠ 0 |
| `dec_to_binary`  | `ValueError` | value outside 0–255 |
| `binary_to_dec`  | `ValueError` | empty input |
| `char_info`      | `ValueError` | input length ≠ 1 |

Example:

```python
from ascii_binary import binary_to_text

try:
    binary_to_text("01001")   # 5 bits
except ValueError as e:
    print(e)   # Binary length (5) must be a multiple of 8.
```

---

## 8. Notes & Limitations

- **Windows-1252, not ISO-8859-1.**
  Characters in the range 128–159 follow Windows-1252 (printable), which is
  the practical superset used everywhere. ISO-8859-1 defines the same range
  as control characters.

- **Unused codes.**
  Windows-1252 leaves 129, 141, 143, 144, 157 undefined. These are omitted
  from `ASCII_TO_BINARY`.

- **Non-Latin scripts.**
  Characters outside 0–255 are not in the 8-bit table. Use
  `text_to_utf8_binary` / `utf8_binary_to_text` for Persian, Arabic, emoji,
  CJK, etc.

- **Pure ASCII vs. Windows-1252.**
  For strictly 7-bit ASCII, only codes 0–127 are valid. Pass `pad=7` to
  `char_to_binary` if you need 7-bit output.

- **Performance.**
  Tables are precomputed at import time. All functions are pure and can be
  safely called from multiple threads.

---

## 9. References

- ASCII table — https://www.ascii-code.com
- Extended ASCII — https://en.wikipedia.org/wiki/Extended_ASCII
- Windows-1252 — https://en.wikipedia.org/wiki/Windows-1252
- Microsoft CP1252 mapping —
  https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS/CP1252.TXT
- IANA character sets —
  https://www.iana.org/assignments/character-sets/character-sets.xhtml

---

## 10. License

MIT License.

Copyright © 2024–2026 — ascii_binary contributors.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```