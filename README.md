# 📚 Data & Utility Packages

A collection of **dependency-free Python packages** for ASCII/binary
conversion, character data, security data, and Iran-specific static data.

> **Data only. No logic. No dependencies.**

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)]()
[![Platform](https://img.shields.io/badge/platform-cross--platform-lightgrey)]()

---

## 📖 Table of Contents

1. [Overview](#-overview)
2. [Packages](#-packages)
3. [Features](#-features)
4. [Project Structure](#-project-structure)
5. [Installation](#-installation)
6. [Quick Start](#-quick-start)
7. [Package Details](#-package-details)
   - 7.1 [ascii_binary](#71-ascii_binary)
   - 7.2 [charsets](#72-charsets)
   - 7.3 [security](#73-security)
   - 7.4 [iran](#74-iran)
8. [Design Philosophy](#-design-philosophy)
9. [Documentation](#-documentation)
10. [File Inventory](#-file-inventory)
11. [Use Cases](#-use-cases)
12. [Performance](#-performance)
13. [Compatibility](#-compatibility)
14. [Contributing](#-contributing)
15. [FAQ](#-faq)
16. [License](#-license)

---

## 🌟 Overview

This project provides four self-contained Python packages that serve as
**pure data layers and simple utilities** for common text and system needs:

- **`ascii_binary`** — ASCII ↔ binary conversion, bitwise operations, and
  binary art (the *original* package that started it all).
- **`charsets`** — every character set you'll ever need: Latin, Cyrillic,
  Arabic, South Asian, East Asian, symbols, emoji, ANSI colors.
- **`security`** — Unix file permissions, risk levels, and file types.
- **`iran`** — Persian alphabet, digits, keyboards, calendar, provinces,
  names, and more.

All four packages share a single guiding principle: **static data and
pure functions only** — no file I/O, no network access, no external
dependencies.

---

## 📦 Packages

| Package | Topic | Language | Files | Help |
|---------|-------|----------|-------|------|
| **`ascii_binary`** | ASCII ↔ binary, bitwise ops, binary art | English | 6 | [`ascii_binary/HELP.md`](ascii_binary/HELP.md) |
| **`charsets`** | Character sets, alphabets, digits, symbols, ANSI colors | English | 19 | [`charsets/HELP.md`](charsets/HELP.md) |
| **`security`** | File permissions, risk levels, file types | English | 4 | [`security/HELP.md`](security/HELP.md) |
| **`iran`** | Persian letters, digits, keyboards, calendar, provinces | فارسی | 11 | [`iran/HELP.md`](iran/HELP.md) |

📖 **Full project guide:** [`HELP.md`](HELP.md)

---

## ✨ Features

- 🔢 **ASCII ↔ binary** — encode/decode text, decimals, hex, octal
- 🎨 **Binary art** — render text as blocks of 0/1
- 🔗 **Bitwise operations** — `XOR`, `AND`, `OR`, `NOT` on binary strings
- 🗃 **Data-only design** — no I/O, no side effects (for `charsets`, `security`, `iran`)
- 🚫 **Zero dependencies** — Python standard library only
- 🌍 **Wide coverage** — 92 languages, 30+ digit systems, 100+ character groups
- 🎨 **ANSI colors** — terminal styles, 256-color, true-color helpers
- 🔒 **Security data** — permission masks, risk levels, file types
- 🇮🇷 **Iran data** — Persian alphabet, digits, keyboards, calendar, provinces
- 📚 **Complete docs** — a `HELP.md` per package
- ⚡ **Fast** — tables computed at import time
- 🧪 **Testable** — pure lookups and pure functions

---

## 🗂 Project Structure

```
project/
│
├── ascii_binary/                 ← ASCII ↔ binary conversion
│   ├── __init__.py
│   ├── tables.py                 ← char ↔ binary, dec, hex, oct
│   ├── converters.py             ← conversion functions
│   ├── utils.py                  ← validation, bitwise, art
│   └── HELP.md
│
├── charsets/                     ← Character sets package
│   ├── __init__.py
│   ├── whitespace.py
│   ├── digits.py
│   ├── symbols.py
│   ├── printable.py
│   ├── functional.py
│   ├── groups.py
│   ├── properties.py
│   ├── colors.py
│   ├── meta.py
│   ├── HELP.md
│   └── alphabets/
│       ├── __init__.py
│       ├── latin.py
│       ├── cyrillic.py
│       ├── arabic.py
│       ├── south_asian.py
│       ├── southeast_asian.py
│       ├── east_asian.py
│       └── other_scripts.py
│
├── security/                     ← File security data (standalone)
│   ├── __init__.py
│   ├── data.py
│   ├── enums.py
│   ├── helpers.py
│   └── HELP.md
│
├── iran/                         ← Iran data package (standalone)
│   ├── __init__.py
│   ├── letters.py
│   ├── charset.py
│   ├── keyboards.py
│   └── HELP.md
│
├── README.md                     ← This file
└── HELP.md                       ← Full project guide
```

---

## 🚀 Installation

There is no official installation. Just copy the folders you need next
to your project:

```bash
cp -r ascii_binary/ charsets/ security/ iran/ /path/to/your_project/
```

Or, if you only need one package:

```bash
cp -r ascii_binary/ /path/to/your_project/
```

### Requirements

| Requirement | Value |
|-------------|-------|
| Python | 3.8+ |
| Dependencies | None |
| Platform | Any (Linux, macOS, Windows, BSD) |

### Optional: Editable Install

If you want to use them system-wide, create a `pyproject.toml` at the
root and run:

```bash
pip install -e .
```

---

## ⚡ Quick Start

### `ascii_binary`

```python
from ascii_binary import (
    text_to_binary, binary_to_text,
    char_info, XOR, AND, OR, NOT,
    text_to_utf8_binary, binary_art,
    count_bits, describe_permission if False else None,
)

# Encode / decode
print(text_to_binary("Hi"))          # '01001000 01101001'
print(binary_to_text("01001000 01101001"))  # 'Hi'

# Character info
print(char_info("A")["bin"])         # '01000001'

# Bitwise
print(XOR("1010", "0110"))           # '1100'

# UTF-8 (Persian, emoji, ...)
print(text_to_utf8_binary("س"))      # '11011000 10110011'

# Binary art
print(binary_art("A"))               # '·█·····█'
```

### `charsets`

```python
from charsets import (
    ALL_LATIN_LETTERS, ALL_ARABIC_SCRIPTS,
    URL_SAFE_CHARS, BASE64_CHARS,
    RED, BOLD, RESET, colorize,
    TOTAL_LANGUAGES_COVERED,
)

print(TOTAL_LANGUAGES_COVERED)              # 92
print("س" in ALL_ARABIC_SCRIPTS)            # True
print(colorize("Hello", RED, BOLD))         # bold red text
```

### `security`

```python
from security import (
    get_risk, describe_permission, get_safety_note,
    DANGEROUS_PERMISSIONS, HIGH_RISK_PERMISSIONS,
    RiskLevel, FileType, Permission,
)

print(get_risk("rwxrwxrwx"))                # 4
print(describe_permission("rw-------"))
# 'Private file. Only the owner can read or write.'
print(get_safety_note("rwxrwxrwx"))
# 'Never use 777 in production. Prefer 755 or 750.'
```

### `iran`

```python
from iran import (
    PERSIAN_LETTERS, PERSIAN_DIGITS,
    PERSIAN_DIGITS_MAP, STANDARD_KEYBOARD,
    PERSIAN_CHARSET, ZWNJ,
)

print(len(PERSIAN_LETTERS))                 # 32
print(PERSIAN_DIGITS_MAP["۵"])              # '5'
print(STANDARD_KEYBOARD["q"])               # 'ض'
print("چ" in PERSIAN_CHARSET)               # True
```

---

## 📘 Package Details

### 7.1 `ascii_binary`

**Purpose:** Convert between text and binary, inspect ASCII characters,
perform bitwise operations, and render binary art.

**Contents:**

| Module | Contents |
|--------|----------|
| `tables` | `ASCII_TO_BINARY`, `BINARY_TO_ASCII`, `DEC_TO_BINARY`, `BINARY_TO_DEC`, `HEX_TO_BINARY`, `BINARY_TO_HEX`, `OCT_TO_BINARY`, `BINARY_TO_OCT`, `ASCII_INFO` |
| `converters` | `char_to_binary`, `binary_to_char`, `text_to_binary`, `binary_to_text`, `dec_to_binary`, `binary_to_dec`, `hex_to_binary`, `binary_to_hex`, `oct_to_binary`, `binary_to_oct`, `text_to_bytes`, `bytes_to_text`, `text_to_utf8_binary`, `utf8_binary_to_text`, `char_info`, `char_info_from_binary`, `char_info_from_dec`, `to_upper_binary`, `to_lower_binary` |
| `utils` | `is_valid_binary`, `normalize_binary`, `count_bits`, `binary_length`, `split_binary`, `is_control`, `is_printable`, `is_extended`, `is_ascii`, `XOR`, `AND`, `OR`, `NOT`, `binary_art`, `ascii_art_from_text` |
| `demo` | Runnable demo script (`python -m ascii_binary.demo`) |

**Coverage:**

| Category | Count |
|----------|-------|
| ASCII characters | 256 (full Windows-1252) |
| Conversion functions | 20+ |
| Bitwise operations | 4 |
| Utility functions | 10+ |
| Art renderers | 2 |

**Example use cases:**

- Encode any text as binary (0/1)
- Decode binary back to text
- Convert between decimal, hex, octal, and binary
- Inspect a character's code point, HTML entity, category
- Perform bitwise XOR for simple ciphers
- Render text as binary art
- Count bits for parity / Hamming weight
- Encode non-Latin scripts using UTF-8

📖 Full docs: [`ascii_binary/HELP.md`](ascii_binary/HELP.md)

---

### 7.2 `charsets`

**Purpose:** Every character set you might need — from ASCII to emoji.

**Coverage:**

| Category | Count | Examples |
|----------|-------|----------|
| Languages | 92 | English, German, Russian, Persian, Hindi, Chinese, Japanese, Korean, ... |
| Digit systems | 30+ | ASCII, Persian, Devanagari, Bengali, Thai, Tibetan, ... |
| Symbol groups | 15+ | Currency, math, arrows, music, chess, zodiac, emoji |
| Character properties | 10+ | BIDI, RTL, LTR, homoglyphs, zero-width |
| Color codes | 8 / 16 / 256 / true-color | ANSI styles, RGB helpers |

**Modules:**

| Module | Contents |
|--------|----------|
| `whitespace` | `WHITESPACE`, `PUNCTUATION` families |
| `digits` | 30+ digit scripts |
| `symbols` | Currency, math, arrows, music, emoji |
| `printable` | Combined `PRINTABLE_*` sets per script |
| `functional` | `URL_SAFE`, `BASE64`, `EMAIL`, `IDENTIFIER`, ... |
| `groups` | Language families (Germanic, Romance, Slavic, Turkic) |
| `properties` | BIDI, RTL, LTR, homoglyphs, zero-width |
| `colors` | ANSI colors, styles, 256-color, true-color |
| `meta` | Statistics, `BOM_*`, category map |
| `alphabets/latin` | 54 Latin-based languages |
| `alphabets/cyrillic` | 16 Cyrillic-based languages |
| `alphabets/arabic` | 10 Arabic-based scripts |
| `alphabets/south_asian` | 12 South Asian scripts |
| `alphabets/southeast_asian` | Thai, Lao, Khmer, Myanmar, Javanese, Balinese |
| `alphabets/east_asian` | Chinese, Japanese, Korean |
| `alphabets/other_scripts` | Greek, Hebrew, Armenian, Georgian, Amharic, ... |

📖 Full docs: [`charsets/HELP.md`](charsets/HELP.md)

---

### 7.3 `security`

**Purpose:** Static data about Unix file permissions, risk levels, and
file types.

**Contents:**

| Category | Contents |
|----------|----------|
| Risk lists | `DANGEROUS_PERMISSIONS`, `HIGH_RISK_PERMISSIONS`, `MEDIUM_RISK_PERMISSIONS`, `LOW_RISK_PERMISSIONS` |
| Octal values | `SPECIAL_BITS` (SUID, SGID, STICKY) |
| Names | `PERMISSION_NAMES`, `COMMON_PERMISSIONS` |
| Type chars | `FILE_TYPE_CHARS` |
| Descriptions | `RISK_DESCRIPTIONS`, `PERMISSION_DESCRIPTIONS`, `SAFETY_NOTES` |
| Enums | `FileType`, `RiskLevel`, `Permission` |
| Helpers | `get_risk`, `describe_permission`, `is_dangerous`, `get_safety_note`, ... |

📖 Full docs: [`security/HELP.md`](security/HELP.md)

---

### 7.4 `iran`

**Purpose:** Static data about Iran — letters, digits, keyboards,
calendar, provinces, and more.

**Modules:**

| Module | Contents | Status |
|--------|----------|--------|
| `letters` | Persian alphabet, digits, diacritics, punctuation | ✅ Active |
| `charset` | Combined Persian character sets | ✅ Active |
| `keyboards` | Persian keyboard layouts (ISIRI 9147, legacy, phonetic) | ✅ Active |
| `calendar` | Persian months, seasons, weekdays, Hijri months | ⏸ Optional |
| `provinces` | 31 provinces, capitals, ISO codes, cities, phone codes | ⏸ Optional |
| `names` | Common male / female / family names | ⏸ Optional |
| `holidays` | Official holidays (fixed, religious, national) | ⏸ Optional |
| `plates` | Iranian vehicle plate letters and province codes | ⏸ Optional |
| `banking` | Bank codes, IBAN prefix, card prefixes | ⏸ Optional |
| `telecom` | Mobile prefixes, landline codes, operators | ⏸ Optional |

📖 Full docs: [`iran/HELP.md`](iran/HELP.md)

---

## 🎯 Design Philosophy

All four packages follow the same principle:

> **Data and pure functions only.**

Every file contains only:

- `str` constants (`PERSIAN_LETTERS = "..."`)
- `list` constants (`PROVINCES = [...]`)
- `dict` constants (`PERSIAN_DIGITS_MAP = {...}`)
- `Enum` classes (`FileType`, `RiskLevel`)
- **Pure functions** (only in `ascii_binary`)

Nothing else. No I/O, no parsing, no side effects.

### Why?

| Benefit | Explanation |
|---------|-------------|
| ⚡ **Fast** | No syscalls at import time |
| 🔒 **Safe** | No accidental file or network access |
| 🌐 **Portable** | Works on any OS, even sandboxes |
| 🧪 **Testable** | Pure lookups and pure functions |
| 🧩 **Composable** | Build your own logic on top |
| 📦 **Tiny** | No dependency tree to audit |
| 📖 **Readable** | The data *is* the documentation |

### Why is `ascii_binary` allowed to have functions?

Because ASCII ↔ binary conversion is a **pure transformation**, not
analysis. `text_to_binary("Hi")` has no side effects, no I/O, and always
returns the same output for the same input. This is the only kind of
function allowed in the project.

### What Doesn't Belong Here

- ❌ `os.stat()` calls
- ❌ File reading / writing
- ❌ Network requests
- ❌ State, caches, singletons
- ❌ Class hierarchies beyond `Enum`

---

## 📖 Documentation

| File | Language | Contents |
|------|----------|----------|
| [`README.md`](README.md) | English | This file — overview, install, examples |
| [`HELP.md`](HELP.md) | English | Full project guide, package summary |
| [`ascii_binary/HELP.md`](ascii_binary/HELP.md) | English | Complete ascii_binary docs |
| [`charsets/HELP.md`](charsets/HELP.md) | English | Complete charsets docs |
| [`security/HELP.md`](security/HELP.md) | English | Complete security docs |
| [`iran/HELP.md`](iran/HELP.md) | فارسی | Complete iran docs |

Each package's `HELP.md` includes:

- Design philosophy
- Installation
- Module layout
- API reference (every constant, function, and helper)
- Usage examples
- Notes and limitations
- References
- License

---

## 📋 File Inventory

<details>
<summary><b>ascii_binary</b> — 6 files</summary>

| File | Contents |
|------|----------|
| `__init__.py` | Re-exports everything |
| `tables.py` | All lookup dictionaries |
| `converters.py` | 20+ conversion functions |
| `utils.py` | Validation, classification, bitwise, art |
| `demo.py` | Runnable demo |
| `HELP.md` | Full documentation |

</details>

<details>
<summary><b>charsets</b> — 19 files</summary>

| File | Contents |
|------|----------|
| `__init__.py` | Re-exports everything |
| `whitespace.py` | `WHITESPACE`, `PUNCTUATION` |
| `digits.py` | 30+ digit systems |
| `symbols.py` | Currency, math, arrows, music, emoji |
| `printable.py` | Combined printable sets |
| `functional.py` | URL, BASE64, EMAIL, IDENTIFIER |
| `groups.py` | Language families |
| `properties.py` | BIDI, RTL, homoglyphs |
| `colors.py` | ANSI colors and styles |
| `meta.py` | Statistics, BOM, categories |
| `alphabets/__init__.py` | Alphabet subpackage |
| `alphabets/latin.py` | 54 Latin-based languages |
| `alphabets/cyrillic.py` | 16 Cyrillic-based languages |
| `alphabets/arabic.py` | 10 Arabic-based scripts |
| `alphabets/south_asian.py` | 12 South Asian scripts |
| `alphabets/southeast_asian.py` | Thai, Lao, Khmer, ... |
| `alphabets/east_asian.py` | Chinese, Japanese, Korean |
| `alphabets/other_scripts.py` | Greek, Hebrew, Armenian, ... |
| `HELP.md` | Full documentation |

</details>

<details>
<summary><b>security</b> — 5 files</summary>

| File | Contents |
|------|----------|
| `__init__.py` | Re-exports everything |
| `data.py` | All static data |
| `enums.py` | `FileType`, `RiskLevel`, `Permission` |
| `helpers.py` | Small lookup functions |
| `HELP.md` | Full documentation |

</details>

<details>
<summary><b>iran</b> — 12 files</summary>

| File | Contents | Status |
|------|----------|--------|
| `__init__.py` | Re-exports everything | ✅ |
| `letters.py` | Persian alphabet, digits, diacritics | ✅ |
| `charset.py` | Combined character sets | ✅ |
| `keyboards.py` | Keyboard layouts | ✅ |
| `calendar.py` | Months, seasons, weekdays | ⏸ |
| `provinces.py` | Provinces, capitals, codes | ⏸ |
| `names.py` | Common names | ⏸ |
| `holidays.py` | Official holidays | ⏸ |
| `plates.py` | Vehicle plates | ⏸ |
| `banking.py` | Bank codes | ⏸ |
| `telecom.py` | Phone prefixes | ⏸ |
| `HELP.md` | Full documentation | ✅ |

</details>

---

## 🎯 Use Cases

### ASCII/Binary Conversion

```python
from ascii_binary import text_to_binary, binary_to_text, XOR

# Simple encode/decode
enc = text_to_binary("Secret")
dec = binary_to_text(enc)

# XOR cipher
key = "10101010"
data = "11001100"
cipher = XOR(data, key)
plain  = XOR(cipher, key)
```

### Text Processing

```python
from charsets import ALL_LATIN_LETTERS
from iran import PERSIAN_DIACRITICS_ALL, PERSIAN_INVISIBLE

def clean_text(text):
    for ch in PERSIAN_INVISIBLE + PERSIAN_DIACRITICS_ALL:
        text = text.replace(ch, "")
    return text
```

### Security Audit

```python
import os, stat
from security import get_risk

def audit(path):
    st = os.stat(path)
    mode = stat.S_IMODE(st.st_mode)
    symbolic = oct(mode)[2:]
    return {"path": path, "octal": oct(mode), "risk": get_risk(symbolic)}
```

### Terminal Styling

```python
from charsets import RED, GREEN, BOLD, RESET, colorize

print(colorize("ERROR", RED, BOLD))
print(colorize("OK", GREEN))
```

### Keyboard Conversion

```python
from iran import STANDARD_KEYBOARD

def en_to_fa(text: str) -> str:
    return "".join(STANDARD_KEYBOARD.get(c, c) for c in text)

print(en_to_fa("hello"))   # 'هثممخ'
```

### Binary Art

```python
from ascii_binary import binary_art

print(binary_art("Hi"))
# ·█··█···
# ·██·█·██
```

---

## ⚡ Performance

All packages compute their tables at import time and are immutable
afterwards. There are no runtime allocations beyond what you request.

### Import Time

| Package | Approximate Import Time |
|---------|-------------------------|
| `ascii_binary` | ~5 ms |
| `charsets` | ~15 ms |
| `security` | ~2 ms |
| `iran` | ~5 ms |

(Measured on Python 3.11, Intel i7, Linux. Numbers vary by platform.)

### Memory

| Package | Approximate Memory |
|---------|--------------------|
| `ascii_binary` | ~100 KB |
| `charsets` | ~2 MB |
| `security` | ~200 KB |
| `iran` | ~500 KB |

---

## 🌐 Compatibility

| Python Version | Status |
|----------------|--------|
| 3.8 | ✅ Supported |
| 3.9 | ✅ Supported |
| 3.10 | ✅ Supported |
| 3.11 | ✅ Supported |
| 3.12 | ✅ Supported |
| 3.13 | ✅ Supported |

| Operating System | Status |
|------------------|--------|
| Linux | ✅ |
| macOS | ✅ |
| Windows | ✅ (ANSI colors auto-enabled) |
| BSD | ✅ |

---

## 🤝 Contributing

### Adding Data

1. Find the right file (e.g. `iran/letters.py`)
2. Add your entry to the relevant list or dict
3. If it's a new top-level constant, add it to `__all__`
4. Done — no registration, no `__init__.py` edits needed

### Adding a Function

For `ascii_binary`, you may add **pure functions**:

- No I/O
- No state
- Deterministic output
- Type hints
- Docstring with examples

### Style Guidelines

- **Type hints** on every function
- **Docstrings** on every module, class, and function
- **`__all__`** in every file
- **Sorted imports** (stdlib first, then local)
- **UTF-8 header** at the top: `# -*- coding: utf-8 -*-`
- **Line length:** ≤ 100 characters
- **No trailing whitespace**

---

## ❓ FAQ

### Why data-only (mostly)?

Because databases should be reusable, testable, and free of hidden
dependencies. Logic belongs in the consumer's code.

### Why does `ascii_binary` have functions?

Because ASCII ↔ binary conversion is a pure transformation. These
functions are the *only* logic allowed — pure, side-effect-free, and
deterministic.

### Why no external dependencies?

To make every package copy-pasteable, sandbox-friendly, and auditable.

### Can I use only part of a package?

Yes. Import submodules directly:

```python
from ascii_binary.converters import text_to_binary
from iran.letters import PERSIAN_LETTERS
from charsets.colors import RED, colorize
from security.data import DANGEROUS_PERMISSIONS
```

### Why isn't `analyze_path()` in `security`?

Because it touches the filesystem. It's a consumer's job, not a data
layer's.

### What about missing constants?

Open an issue or add them yourself — the packages are designed to grow
incrementally.

### Is there a version guarantee?

The packages follow semantic versioning. Breaking changes bump the major
version; new data bumps the minor; bug fixes bump the patch.

### Can I use these in commercial software?

Yes. MIT license.

### Why are some packages documented in Persian?

Because `iran` is aimed at Persian-speaking developers. `ascii_binary`,
`charsets`, and `security` are general-purpose and documented in English.

---

## 📜 License

MIT License.

Copyright © 2024–2026 — contributors.

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

---

**Built with ❤️ for clean, static data.**