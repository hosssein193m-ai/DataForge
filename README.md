# 📚 Data & Utility Packages

A collection of **dependency-free Python packages** for character data,
security data, and Iran-specific static data.

> **Data only. No logic. No dependencies.**
> **فقط داده. بدون منطق. بدون وابستگی.**

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
   - 7.1 [charsets](#71-charsets)
   - 7.2 [security](#72-security)
   - 7.3 [iran](#73-iran)
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

This project provides three self-contained Python packages that serve as
**pure data layers** for common text and system needs:

- **`charsets`** — every character set you'll ever need: Latin, Cyrillic,
  Arabic, South Asian, East Asian, symbols, emoji, ANSI colors.
- **`security`** — Unix file permissions, risk levels, and file types.
- **`iran`** — Persian alphabet, digits, keyboards, calendar, provinces,
  names, and more.

All three packages share a single guiding principle: **static data only,
no logic**. They contain `dict` / `list` / `str` / `Enum` definitions
and small lookup helpers — nothing else. No file I/O, no network access,
no external dependencies.

**Why?** Because a database should be a database. When you need analysis
or transformation, you build it *on top* of these datasets in your own
code, on your own terms, with your own dependencies.

---

## 📦 Packages

| Package | Topic | Language | Files | Help |
|---------|-------|----------|-------|------|
| **`charsets`** | Character sets, alphabets, digits, symbols, ANSI colors | English | 19 | [`charsets/HELP.md`](charsets/HELP.md) |
| **`security`** | File permissions, risk levels, file types | English | 4 | [`security/HELP.md`](security/HELP.md) |
| **`iran`** | Persian letters, digits, keyboards, calendar, provinces | فارسی | 11 | [`iran/HELP.md`](iran/HELP.md) |

📖 **Full project guide:** [`HELP.md`](HELP.md)

---

## ✨ Features

- 🗃 **Data-only design** — no logic, no I/O, no side effects
- 🚫 **Zero dependencies** — Python standard library only
- 🌍 **Wide coverage** — 92 languages, 30+ digit systems, 100+ character groups
- 🎨 **ANSI colors** — terminal styles, 256-color, true-color helpers
- 🔒 **Security data** — permission masks, risk levels, file types
- 🇮🇷 **Iran data** — Persian alphabet, digits, keyboards, calendar, provinces
- 📚 **Complete docs** — a `HELP.md` per package
- 🔌 **Copy-paste friendly** — every package works standalone
- ⚡ **Fast** — all tables computed at import time
- 🧪 **Testable** — pure lookups, trivial to unit test
- 🌐 **Portable** — runs on any OS, including non-POSIX systems
- 🧩 **Composable** — build your own logic on top

---

## 🗂 Project Structure

```
project/
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
│   ├── calendar.py
│   ├── provinces.py
│   ├── names.py
│   ├── holidays.py
│   ├── plates.py
│   ├── banking.py
│   ├── telecom.py
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
cp -r charsets/ security/ iran/ /path/to/your_project/
```

Or, if you only need one package:

```bash
cp -r iran/ /path/to/your_project/
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

### `charsets`

```python
from charsets import (
    ALL_LATIN_LETTERS, ALL_ARABIC_SCRIPTS,
    URL_SAFE_CHARS, BASE64_CHARS,
    RED, BOLD, RESET, colorize,
    TOTAL_LANGUAGES_COVERED,
)

print(TOTAL_LANGUAGES_COVERED)              # 92
print(len(ALL_LATIN_LETTERS))               # ~120 unique letters
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
print(oct(Permission.USER_RWX))             # '0o755'
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
print(f"می{ZWNJ}روم")                       # with ZWNJ
```

---

## 📘 Package Details

### 7.1 `charsets`

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
| `digits` | 30+ digit scripts (DEC, HEX, Persian, Devanagari, ...) |
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

**Example use cases:**

- Sanitize user input by stripping zero-width characters
- Detect the script of a string
- Filter text to only Latin letters
- Build a URL-safe slug from any alphabet
- Render colored terminal output
- Validate email / filename / identifier characters
- Generate random characters from any script

📖 Full docs: [`charsets/HELP.md`](charsets/HELP.md)

---

### 7.2 `security`

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

**Example use cases:**

- Audit a directory and warn about world-writable files
- Detect setuid / setgid binaries
- Build a security report
- Sanitize permission strings from `ls -l` output
- Validate permission strings before applying them

📖 Full docs: [`security/HELP.md`](security/HELP.md)

---

### 7.3 `iran`

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

**Example use cases:**

- Normalize Persian text (remove diacritics, invisible chars)
- Convert Persian digits to Latin digits
- Convert English keyboard input to Persian (or vice versa)
- Validate Persian filenames / URLs
- Look up a province's capital or phone code
- Check if a name is a common Persian name

📖 Full docs: [`iran/HELP.md`](iran/HELP.md)

---

## 🎯 Design Philosophy

All three packages follow the same principle:

> **Data, not logic.**

Every file contains only:

- `str` constants (`PERSIAN_LETTERS = "..."`)
- `list` constants (`PROVINCES = [...]`)
- `dict` constants (`PERSIAN_DIGITS_MAP = {...}`)
- `Enum` classes (`FileType`, `RiskLevel`)

Nothing else. No functions that do I/O, no analysis, no parsing, no
validation logic beyond trivial lookups.

### Why?

| Benefit | Explanation |
|---------|-------------|
| ⚡ **Fast** | No syscalls at import time |
| 🔒 **Safe** | No accidental file or network access |
| 🌐 **Portable** | Works on any OS, even sandboxes |
| 🧪 **Testable** | Pure lookups, trivial to unit test |
| 🧩 **Composable** | Build your own logic on top |
| 📦 **Tiny** | No dependency tree to audit |
| 📖 **Readable** | The data *is* the documentation |

### Helper Functions

Each package includes a handful of **pure lookup helpers** that make the
data easier to use:

```python
# security/helpers.py
def get_risk(symbolic: str) -> int:
    return PERMISSION_TO_RISK.get(symbolic, 1)
```

These are the *only* functions allowed. They:
- Take data as input
- Return data as output
- Have no side effects
- Never touch the filesystem

### What Doesn't Belong Here

- ❌ `os.stat()` calls
- ❌ File reading / writing
- ❌ Network requests
- ❌ Regex-based parsing
- ❌ Class hierarchies beyond `Enum`
- ❌ State, caches, singletons

If you need these, build them **on top** of the packages.

---

## 📖 Documentation

| File | Language | Contents |
|------|----------|----------|
| [`README.md`](README.md) | English | This file — overview, install, examples |
| [`HELP.md`](HELP.md) | فارسی | Full project guide, package summary |
| [`charsets/HELP.md`](charsets/HELP.md) | English | Complete charsets documentation |
| [`security/HELP.md`](security/HELP.md) | English | Complete security documentation |
| [`iran/HELP.md`](iran/HELP.md) | فارسی | Complete iran documentation |

Each package's `HELP.md` includes:

- Design philosophy
- Installation
- Module layout
- API reference (every constant and helper)
- Usage examples
- Notes and limitations
- References
- License

---

## 📋 File Inventory

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
<summary><b>security</b> — 4 files</summary>

| File | Contents |
|------|----------|
| `__init__.py` | Re-exports everything |
| `data.py` | All static data |
| `enums.py` | `FileType`, `RiskLevel`, `Permission` |
| `helpers.py` | Small lookup functions |
| `HELP.md` | Full documentation |

</details>

<details>
<summary><b>iran</b> — 11 files</summary>

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

### Text Processing

```python
from charsets import ALL_LATIN_LETTERS, ZERO_WIDTH_CHARS if False else None
from iran import PERSIAN_DIACRITICS_ALL, PERSIAN_INVISIBLE

def clean_text(text):
    # Remove zero-width and diacritics
    for ch in PERSIAN_INVISIBLE + PERSIAN_DIACRITICS_ALL:
        text = text.replace(ch, "")
    return text
```

### Input Validation

```python
from charsets import URL_SAFE_CHARS
from iran import PERSIAN_URL_SAFE

def is_safe_slug(slug: str) -> bool:
    return all(ch in PERSIAN_URL_SAFE for ch in slug)
```

### Security Audit

```python
import os, stat
from security import get_risk, describe_permission, Permission

def audit(path):
    st = os.stat(path)
    mode = stat.S_IMODE(st.st_mode)
    symbolic = oct(mode)[2:]
    return {
        "path": path,
        "octal": oct(mode),
        "risk": get_risk(symbolic),
    }
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

---

## ⚡ Performance

All packages compute their tables at import time and are immutable
afterwards. There are no runtime allocations beyond what you request.

### Import Time

| Package | Approximate Import Time |
|---------|-------------------------|
| `charsets` | ~15 ms |
| `security` | ~2 ms |
| `iran` | ~5 ms |

(Measured on Python 3.11, Intel i7, Linux. Numbers vary by platform.)

### Memory

| Package | Approximate Memory |
|---------|--------------------|
| `charsets` | ~2 MB |
| `security` | ~200 KB |
| `iran` | ~500 KB |

If you need lower memory, import only the submodules you need:

```python
from charsets.alphabets.latin import ALL_LATIN_LETTERS  # instead of `from charsets import *`
```

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

| Encoding | Notes |
|----------|-------|
| UTF-8 | Fully supported |
| UTF-16 | Fully supported |
| Latin-1 | Partial (charsets has `LATIN1_COMPATIBLE`) |

---

## 🤝 Contributing

### Adding Data

1. Find the right file (e.g. `iran/letters.py`)
2. Add your entry to the relevant list or dict
3. If it's a new top-level constant, add it to `__all__`
4. Done — no registration, no `__init__.py` edits needed

### Adding a New Module

1. Create `iran/newmodule.py`
2. Define your data constants
3. Add `from .newmodule import *` to `iran/__init__.py`
4. Add `newmodule` to the `try/except` block (if optional)
5. Update `HELP.md`

### Adding a Helper Function

Only if it is **pure** and **trivial**:

```python
def get_something(key: str) -> Optional[str]:
    return SOME_DICT.get(key)
```

No I/O, no parsing, no side effects.

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

### Why data-only?

Because databases should be reusable, testable, and free of hidden
dependencies. Logic belongs in the consumer's code.

### Why no external dependencies?

To make every package copy-pasteable, sandbox-friendly, and auditable.

### Can I use only part of a package?

Yes. Import submodules directly:

```python
from iran.letters import PERSIAN_LETTERS     # only this module
from charsets.colors import RED, colorize    # only colors
from security.data import DANGEROUS_PERMISSIONS
```

### Why isn't `analyze_path()` in `security`?

Because it touches the filesystem. It's a consumer's job, not a data
layer's. See [`security/HELP.md §8`](security/HELP.md#8-notes).

### How do I add a new language to `charsets`?

1. Add a new file under `charsets/alphabets/`
2. Define `LOWERCASE` / `UPPERCASE` constants
3. Import in `alphabets/__init__.py`
4. Add to `ALL_LATIN_LETTERS` if applicable
5. Update `HELP.md`

### What about missing constants?

Open an issue or add them yourself — the packages are designed to grow
incrementally.

### Is there a version guarantee?

The packages follow semantic versioning. Breaking changes bump the major
version; new data bumps the minor; bug fixes bump the patch.

### Can I use these in commercial software?

Yes. MIT license.

### Why is the `iran` documentation in Persian but the others in English?

Because `iran` is aimed at Persian-speaking developers, while `charsets`
and `security` are general-purpose. If you want an English version of
`iran/HELP.md`, open an issue.

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
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

---

**Built with ❤️ for clean, static data.**