# charsets — Help & Documentation

A comprehensive, dependency-free Python collection of character sets,
alphabets, digits, punctuation, symbols, ANSI colors, and character-property
groups covering **90+ languages and scripts**.

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
   - 4.1 [Whitespace & Punctuation](#41-whitespace--punctuation)
   - 4.2 [Digits](#42-digits)
   - 4.3 [Alphabets](#43-alphabets)
   - 4.4 [Symbols](#44-symbols)
   - 4.5 [Printable Sets](#45-printable-sets)
   - 4.6 [Functional Sets](#46-functional-sets)
   - 4.7 [Language Groups](#47-language-groups)
   - 4.8 [Character Properties](#48-character-properties)
   - 4.9 [Colors & Styles](#49-colors--styles)
   - 4.10 [Meta & Statistics](#410-meta--statistics)
5. [Examples](#5-examples)
6. [Notes & Limitations](#6-notes--limitations)
7. [References](#7-references)
8. [License](#8-license)

---

## 1. Installation

Pure Python. Just copy the `charsets/` folder into your project.

```bash
your_project/
├── charsets/
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
└── your_script.py
```

Then in your code:

```python
from charsets import ALL_LATIN_LETTERS, RED, colorize
```

---

## 2. Project Structure

| File | Purpose |
|------|---------|
| `whitespace.py` | `WHITESPACE`, `PUNCTUATION` families |
| `digits.py`     | 30+ digit scripts (DEC, HEX, Persian, Devanagari, ...) |
| `alphabets/latin.py`       | 54 Latin-based languages |
| `alphabets/cyrillic.py`    | 16 Cyrillic-based languages |
| `alphabets/arabic.py`      | 10 Arabic-based scripts |
| `alphabets/south_asian.py` | 12 South Asian scripts |
| `alphabets/southeast_asian.py` | Thai, Lao, Khmer, Myanmar, Javanese, Balinese |
| `alphabets/east_asian.py`  | Chinese, Japanese, Korean |
| `alphabets/other_scripts.py` | Greek, Hebrew, Armenian, Georgian, Amharic, ... |
| `symbols.py`    | Currency, math, arrows, music, emoji, ... |
| `printable.py`  | Combined `PRINTABLE_*` sets |
| `functional.py` | `URL_SAFE`, `BASE64`, `EMAIL`, `IDENTIFIER`, ... |
| `groups.py`     | Language families (Germanic, Romance, Slavic, Turkic) |
| `properties.py` | BIDI, RTL, LTR, homoglyphs, zero-width, ... |
| `colors.py`     | ANSI colors, styles, 256-color and true-color helpers |
| `meta.py`       | Statistics, category map, BOM, export configs |

---

## 3. Quick Start

```python
from charsets import (
    ALL_LATIN_LETTERS, ALL_ARABIC_SCRIPTS, ALL_DIGITS,
    PERSIAN_LETTERS, RUSSIAN_LOWERCASE,
    URL_SAFE_CHARS, BASE64_CHARS,
    PRINTABLE_PERSIAN, PRINTABLE_JAPANESE,
    RED, BOLD, RESET, colorize,
    TOTAL_LANGUAGES_COVERED,
)

# Character sets
print("A" in ALL_LATIN_LETTERS)     # True
print("س" in ALL_ARABIC_SCRIPTS)    # True
print("۰" in ALL_DIGITS)            # True
print(TOTAL_LANGUAGES_COVERED)      # 92

# ANSI colors
print(colorize("Hello in red", RED))
print(colorize("Bold red", RED, BOLD))
print(f"{RED}Inline{RESET} usage")
```

---

## 4. API Reference

### 4.1 Whitespace & Punctuation

| Name | Type | Description |
|------|------|-------------|
| `WHITESPACE_STANDARD` | `str` | `\t\n\r\v\f ` |
| `WHITESPACE` | `str` | Extended Unicode whitespace |
| `WHITESPACE_LIST` | `list` | Standard whitespace as list |
| `WHITESPACE_EXTRA` | `str` | Zero-width & formatting chars |
| `WHITESPACE_ALL` | `str` | `WHITESPACE + WHITESPACE_EXTRA` |
| `PUNCTUATION_ASCII` | `str` | ASCII punctuation |
| `PUNCTUATION_UNICODE` | `str` | Unicode punctuation |
| `PUNCTUATION_EXTRA` | `str` | Ornamental / decorative |
| `PUNCTUATION` | `str` | All of the above combined |
| `PUNCTUATION_LIST` | `list` | As list |

```python
>>> from charsets import WHITESPACE_STANDARD, PUNCTUATION_ASCII
>>> "\n" in WHITESPACE_STANDARD
True
>>> "!" in PUNCTUATION_ASCII
True
```

---

### 4.2 Digits

| Name | Description |
|------|-------------|
| `BINARY_DIGITS` | `"01"` |
| `OCTAL_DIGITS` | `"01234567"` |
| `DECIMAL_DIGITS` | `"0123456789"` |
| `HEX_DIGITS` | `"0123456789abcdefABCDEF"` |
| `PERSIAN_DIGITS` | `"۰۱۲۳۴۵۶۷۸۹"` |
| `EASTERN_ARABIC_DIGITS` | Alias of `PERSIAN_DIGITS` |
| `DEVANAGARI_DIGITS` | Hindi/Marathi/Nepali |
| `BENGALI_DIGITS`, `THAI_DIGITS`, `TAMIL_DIGITS`, … | 30+ scripts |
| `PERSIAN_DIGITS_MAP` | `{persian: ascii}` mapping |
| `CIRCLED_NUMBERS`, `PARENTHESIZED_NUMBERS` | Stylized numbers |
| `ROMAN_NUMERALS_UPPER`, `ROMAN_NUMERALS_LOWER` | Roman numerals |
| `ALL_DIGITS` | Every digit string concatenated |
| `ALL_DIGITS_UNIQUE` | Deduplicated version |

---

### 4.3 Alphabets

#### Latin (`charsets.alphabets.latin`)

| Name | Description |
|------|-------------|
| `ASCII_LOWERCASE`, `ASCII_UPPERCASE`, `ASCII_LETTERS` | Base Latin |
| `GERMAN_*`, `FRENCH_*`, `SPANISH_*`, … | 54 languages |
| `ALL_LATIN_LOWERCASE` | Deduped lowercase |
| `ALL_LATIN_UPPERCASE` | Deduped uppercase |
| `ALL_LATIN_LETTERS` | Both |

#### Cyrillic

| Name | Description |
|------|-------------|
| `RUSSIAN_*`, `UKRAINIAN_*`, `BULGARIAN_*`, … | 16 languages |
| `ALL_CYRILLIC_LOWERCASE`, `ALL_CYRILLIC_UPPERCASE`, `ALL_CYRILLIC` | Aggregates |

#### Arabic

| Name | Description |
|------|-------------|
| `ARABIC_LETTERS`, `ARABIC_ALL_FORMS` | Arabic |
| `PERSIAN_LETTERS`, `PERSIAN_FULL` | Persian |
| `URDU_LETTERS`, `PASHTO_LETTERS`, `KURDISH_ARABIC`, … | 10 scripts |
| `ALL_ARABIC_SCRIPTS` | All combined |
| `ARABIC_DIACRITICS`, `PERSIAN_HARAKAT`, `PERSIAN_PUNCTUATION` | Marks |

#### South Asian

| Name | Description |
|------|-------------|
| `DEVANAGARI_LETTERS`, `BENGALI_LETTERS`, `GURMUKHI_LETTERS`, … | 12 scripts |
| `ALL_SOUTH_ASIAN` | Combined |

#### Southeast Asian

`THAI_LETTERS`, `LAO_LETTERS`, `KHMER_LETTERS`, `MYANMAR_LETTERS`,
`JAVANESE_LETTERS`, `JAVANESE_VOWELS`, `BALINESE_LETTERS`, `BALINESE_VOWELS`.

#### East Asian

`CHINESE_COMMON`, `HIRAGANA`, `KATAKANA`, `JAPANESE_LETTERS`,
`HANGUL_INITIAL`, `HANGUL_MEDIAL`, `HANGUL_FINAL`, `HANGUL_SYLLABLES`,
`HANGUL_LETTERS`.

#### Other Scripts

`GREEK_LETTERS`, `HEBREW_FULL`, `ARMENIAN_LETTERS`, `GEORGIAN_LETTERS`,
`AMHARIC_LETTERS`, `TIBETAN_LETTERS`, `SYRIAC_LETTERS`, `THAANA_LETTERS`,
`CHEROKEE_LETTERS`, `IPA_CONSONANTS`, `IPA_VOWELS`, `PHOENICIAN`,
`CUNEIFORM_SAMPLE`, `RUNIC_CHARS`, `OGHAM_CHARS`, `GOTHIC_CHARS`,
`DESERET_CHARS`.

---

### 4.4 Symbols

| Name | Description |
|------|-------------|
| `CURRENCY_SYMBOLS` | `$€£¥₹﷼…` |
| `MATH_SYMBOLS` | `±÷×≈≠≤≥∞∑∏∫…` |
| `ARROWS` | `←↑→↓↔…` |
| `MUSIC_SYMBOLS`, `CHESS_SYMBOLS`, `CARDS_SYMBOLS` | |
| `ZODIAC_SYMBOLS`, `ASTRONOMY_SYMBOLS`, `WEATHER_SYMBOLS` | |
| `FRACTIONS`, `BOX_DRAWING` | |
| `COMMON_EMOJIS`, `EMOJI_FLAGS` | |

---

### 4.5 Printable Sets

Combined script + punctuation + digits (+ local currency).

| Name | Coverage |
|------|----------|
| `PRINTABLE_ASCII` | 7-bit ASCII |
| `PRINTABLE_LATIN` | All Latin letters |
| `PRINTABLE_CYRILLIC` | All Cyrillic |
| `PRINTABLE_ARABIC` | All Arabic-based scripts |
| `PRINTABLE_SOUTH_ASIAN` | Devanagari, Bengali, … |
| `PRINTABLE_EAST_ASIAN` | CJK |
| `PRINTABLE_GREEK`, `PRINTABLE_HEBREW`, `PRINTABLE_ARMENIAN`, `PRINTABLE_GEORGIAN` | |
| `PRINTABLE_THAI`, `PRINTABLE_LAO`, `PRINTABLE_KHMER`, `PRINTABLE_MYANMAR` | |
| `PRINTABLE_TIBETAN`, `PRINTABLE_MONGOLIAN`, `PRINTABLE_CHEROKEE`, `PRINTABLE_ETHIOPIC` | |
| `PRINTABLE_GERMAN`, `PRINTABLE_FRENCH`, `PRINTABLE_SPANISH`, … | Language-specific |
| `PRINTABLE_PERSIAN`, `PRINTABLE_URDU`, `PRINTABLE_HINDI`, `PRINTABLE_BENGALI`, … | |
| `PRINTABLE_JAPANESE`, `PRINTABLE_CHINESE`, `PRINTABLE_KOREAN` | |

---

### 4.6 Functional Sets

| Name | Purpose |
|------|---------|
| `URL_SAFE_CHARS` | RFC 3986 unreserved |
| `BASE64_CHARS`, `BASE32_CHARS`, `CROCKFORD_BASE32` | Encodings |
| `HEX_CHARS` | Hex digits |
| `IDENTIFIER_CHARS`, `SQL_IDENTIFIER_CHARS` | Programming identifiers |
| `EMAIL_LOCAL_CHARS`, `DOMAIN_CHARS` | Email parsing |
| `FILENAME_SAFE_CHARS` | Conservative filenames |
| `PASSWORD_SPECIAL` | Commonly accepted special chars |
| `HTML_ESCAPE_CHARS`, `XML_ESCAPE_CHARS`, `JSON_ESCAPE_CHARS`, `PYTHON_ESCAPE_CHARS` | Escaping |
| `NUMERIC_CHARS`, `INTEGER_CHARS`, `FLOAT_CHARS`, `HEX_NUMERIC_CHARS`, `OCTAL_NUMERIC_CHARS`, `BINARY_NUMERIC_CHARS` | Numeric validation |
| `ALPHA_CHARS`, `ALPHANUMERIC_CHARS`, `ALPHANUMERIC_EXTENDED` | Regex-like classes |

---

### 4.7 Language Groups

| Name | Family |
|------|--------|
| `GERMANIC_LANGUAGES_CHARS` | German, Dutch, Swedish, Norwegian, Danish, Icelandic, Luxembourgish |
| `ROMANCE_LANGUAGES_CHARS` | French, Spanish, Italian, Portuguese, Romanian, Catalan, Galician |
| `SLAVIC_LATIN_CHARS` | Polish, Czech, Slovak, Croatian, Slovene, Bosnian, Serbian (Latin), Montenegrin |
| `SLAVIC_CYRILLIC_CHARS` | Russian, Ukrainian, Bulgarian, Serbian (Cyrillic), Macedonian, Belarusian |
| `TURKIC_LANGUAGES_CHARS` | Turkish, Azerbaijani, Turkmen, Crimean Tatar |

---

### 4.8 Character Properties

| Name | Purpose |
|------|---------|
| `BIDI_CHARS` | Bidirectional scripts |
| `RTL_CHARS` | Right-to-left scripts |
| `LTR_CHARS` | Left-to-right scripts |
| `TTB_CHARS` | Top-to-bottom (CJK) |
| `ZERO_WIDTH_CHARS` | Zero-width characters (security concern) |
| `DIRECTION_CHARS` | Direction overrides |
| `INVISIBLE_CHARS` | All invisible characters |
| `HOMOGLYPH_LATIN_A…Y` | Visually confusable characters |
| `DESCENDER_CHARS`, `ASCENDER_CHARS` | Typography hints |
| `MONOSPACE_DIGITS` | `"0123456789"` |
| `FULLWIDTH_CHARS`, `HALFWIDTH_CHARS` | CJK width variants |

---

### 4.9 Colors & Styles

#### Style modifiers

| Constant | Effect |
|----------|--------|
| `RESET` | Reset all attributes |
| `BOLD` | Bold / increased intensity |
| `DIM` | Faint / decreased intensity |
| `ITALIC` | Italic |
| `UNDERLINE` | Underline |
| `BLINK` | Slow blink |
| `BLINK_FAST` | Fast blink |
| `REVERSE` | Swap fg/bg |
| `HIDDEN` | Conceal |
| `STRIKETHROUGH` | Strikethrough |
| `RESET_BOLD`, `RESET_DIM`, … | Individual resets |

#### Foreground colors

`BLACK`, `RED`, `GREEN`, `YELLOW`, `BLUE`, `MAGENTA`, `CYAN`, `WHITE`, `DEFAULT`,
`BRIGHT_BLACK`, `BRIGHT_RED`, `BRIGHT_GREEN`, `BRIGHT_YELLOW`, `BRIGHT_BLUE`,
`BRIGHT_MAGENTA`, `BRIGHT_CYAN`, `BRIGHT_WHITE`, `GRAY` / `GREY`.

#### Background colors

Same names with a `BG_` prefix (e.g. `BG_RED`, `BG_BRIGHT_BLUE`).

#### 256-color

```python
from charsets import fg256, bg256, COLOR_256_NAMES

print(fg256(196) + "Hello" + RESET)
print(bg256(COLOR_256_NAMES["orange"]) + "Hi" + RESET)
```

#### True color (24-bit)

```python
from charsets import fg_rgb, bg_rgb, RESET

print(fg_rgb(255, 100, 0) + "Orange" + RESET)
print(bg_rgb(0, 0, 128) + "Navy" + RESET)
```

#### Helpers

| Function | Purpose |
|----------|---------|
| `colorize(text, *codes)` | Wrap text with codes + reset |
| `style(text, *codes)` | Alias of `colorize` |
| `strip_ansi(text)` | Remove ANSI escapes |
| `enable_windows_ansi()` | Best-effort Windows ANSI enable |

Examples:

```python
from charsets import RED, BOLD, UNDERLINE, colorize, strip_ansi

print(colorize("Hello", RED))                    # red
print(colorize("Hello", RED, BOLD))              # bold red
print(colorize("Hello", RED, BOLD, UNDERLINE))   # bold underlined red

plain = strip_ansi(colorize("Hi", RED))          # 'Hi'
```

#### Lookup maps

- `FOREGROUND_COLORS`: name → escape
- `BACKGROUND_COLORS`: name → escape
- `STYLE_CODES`: name → escape
- `COLOR_256_NAMES`: name → 256-color index

---

### 4.10 Meta & Statistics

| Name | Purpose |
|------|---------|
| `CHAR_CATEGORY_MAP` | Categories → characters |
| `ASCII_LETTER_CHARS`, `ASCII_DIGIT_CHARS`, … | ASCII category split |
| `ALL_CHARACTERS` | Everything combined |
| `UNIQUE_ALL_CHARACTERS` | Deduplicated |
| `TOTAL_UNIQUE_CHARS` | Count |
| `ASCII_COMPATIBLE`, `LATIN1_COMPATIBLE`, `UTF8_COMPATIBLE`, `UTF16_COMPATIBLE` | Encoding-compatible sets |
| `BOM_UTF8`, `BOM_UTF16_LE`, `BOM_UTF16_BE`, `BOM_UTF32_LE`, `BOM_UTF32_BE` | Byte-order marks |
| `LATIN_LANGUAGES_COUNT`, `CYRILLIC_LANGUAGES_COUNT`, … | Stats |
| `TOTAL_LANGUAGES_COVERED` | Sum |
| `EXPORTS` | Dict of export configs |

---

## 5. Examples

### 5.1 Filter by Script

```python
from charsets import ALL_LATIN_LETTERS, ALL_ARABIC_SCRIPTS

def keep_latin(text):
    return "".join(ch for ch in text if ch in ALL_LATIN_LETTERS)

def keep_arabic(text):
    return "".join(ch for ch in text if ch in ALL_ARABIC_SCRIPTS)

keep_latin("Hello دنیا World")   # 'Hello  World'
keep_arabic("Hello دنیا World")  # 'دنیا'
```

### 5.2 Detect Script of a String

```python
from charsets import (
    ALL_LATIN_LETTERS, ALL_CYRILLIC, ALL_ARABIC_SCRIPTS, ALL_SOUTH_ASIAN,
)

def detect_script(text):
    for ch in text:
        if ch in ALL_LATIN_LETTERS:    return "Latin"
        if ch in ALL_CYRILLIC:         return "Cyrillic"
        if ch in ALL_ARABIC_SCRIPTS:   return "Arabic"
        if ch in ALL_SOUTH_ASIAN:      return "South Asian"
    return "Unknown"

detect_script("Hello")   # 'Latin'
detect_script("Привет")  # 'Cyrillic'
detect_script("سلام")    # 'Arabic'
```

### 5.3 Strip Zero-Width Characters

```python
from charsets import ZERO_WIDTH_CHARS

def sanitize(text):
    return "".join(ch for ch in text if ch not in ZERO_WIDTH_CHARS)

sanitize("Hello\u200bWorld")  # 'HelloWorld'
```

### 5.4 Terminal Colors

```python
from charsets import RED, GREEN, BOLD, RESET, colorize, fg_rgb, bg_rgb

print(colorize("ERROR: file not found", RED, BOLD))
print(colorize("OK", GREEN))
print(fg_rgb(255, 165, 0) + "Orange" + RESET)
print(bg_rgb(0, 100, 0) + "Green background" + RESET)
```

### 5.5 Build a Custom Validation Set

```python
from charsets import ALPHANUMERIC_CHARS, PUNCTUATION_ASCII

ALLOWED = set(ALPHANUMERIC_CHARS + " .-_@")

def is_allowed(text):
    return all(ch in ALLOWED for ch in text)

is_allowed("user@example.com")   # True
is_allowed("user<script>")       # False
```

---

## 6. Notes & Limitations

- **Deduplication.** Aggregated sets (`ALL_LATIN_LETTERS`, `ALL_CYRILLIC`, …)
  are deduplicated while preserving order.
- **Aliases.** `EASTERN_ARABIC_DIGITS` and `PERSIAN_DIGITS` are the same
  code points (Unicode `0660–0669`), so only one appears in `ALL_DIGITS`.
- **Turkish casing.** `TURKISH_*` and `AZERBAIJANI_*` follow the special
  dotted/dotless I convention: `ı ↔ I` and `i ↔ İ`.
- **Windows ANSI.** `colors.py` tries to enable VT processing automatically
  on Windows at import time. If it fails, call `enable_windows_ansi()` manually.
- **Performance.** All sets are computed at import time. Lookups are O(1) for
  `str` `in` checks (Python uses substring search, which is fast in practice).
- **Memory.** The full `ALL_CHARACTERS` string is ~100 KB of Unicode.
  If you need lower memory, import only the submodules you need.

---

## 7. References

- Unicode Standard — https://unicode.org/standard/standard.html
- Unicode Character Database — https://unicode.org/ucd/
- Windows-1252 / CP-1252 — https://en.wikipedia.org/wiki/Windows-1252
- ANSI escape codes — https://en.wikipedia.org/wiki/ANSI_escape_code
- ISO/IEC 6429 (ECMA-48) — https://www.ecma-international.org/publications-and-standards/standards/ecma-48/
- IANA character sets — https://www.iana.org/assignments/character-sets/character-sets.xhtml

---

## 8. License

MIT License.

Copyright © 2024–2026 — charsets contributors.

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