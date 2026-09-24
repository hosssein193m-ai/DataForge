# `iran` — راهنمای کامل

پکیج داده‌های ثابت مربوط به ایران — فقط داده، بدون تابع، بدون منطق.

- **نسخه:** 1.0.0
- **پایتون:** 3.8+
- **مجوز:** MIT
- **وابستگی:** هیچ (فقط کتابخانه استاندارد)

---

## فهرست مطالب

1. [فلسفه طراحی](#1-فلسفه-طراحی)
2. [نصب و استفاده](#2-نصب-و-استفاده)
3. [ساختار پروژه](#3-ساختار-پروژه)
4. [ماژول `letters`](#4-ماژول-letters)
   - 4.1 [حروف الفبا](#41-حروف-الفبا)
   - 4.2 [ارقام](#42-ارقام)
   - 4.3 [اعداد به حروف](#43-اعداد-به-حروف)
   - 4.4 [اعراب](#44-اعراب)
   - 4.5 [نشانه‌گذاری](#45-نشانهگذاری)
   - 4.6 [کاراکترهای نامرئی](#46-کاراکترهای-نامرئی)
   - 4.7 [شکل‌های خاص حروف](#47-شکلهای-خاص-حروف)
   - 4.8 [مجموع‌ها](#48-مجموعها)
5. [ماژول `charset`](#5-ماژول-charset)
6. [ماژول `keyboards`](#6-ماژول-keyboards)
7. [مثال‌های کاربردی](#7-مثالهای-کاربردی)
8. [نکات](#8-نکات)
9. [مجوز](#9-مجوز)

---

## 1. فلسفه طراحی

این پکیج یک **لایه داده** است، نه لایه منطق.

- هر فایل فقط شامل **داده‌های ثابت** است.
- هیچ تابعی برای تحلیل، تبدیل، اعتبارسنجی یا I/O وجود ندارد.
- هیچ وابستگی به `os`، `re`، `io` یا کتابخانه خارجی وجود ندارد.
- همه چیز در زمان import محاسبه می‌شود و immutable است.

**قاعده:** اگر به فایل‌سیستم، شبکه، یا پردازش ورودی نیاز دارد، در این
پکیج جایی ندارد. آن منطق باید در کد خودت باشد.

---

## 2. نصب و استفاده

پکیج کاملاً Pure Python است. کافی است پوشه `iran/` را کنار پروژه‌ات
کپی کنی.

```
your_project/
├── iran/
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
└── your_script.py
```

سپس در کد:

```python
from iran import (
    PERSIAN_LETTERS, PERSIAN_DIGITS, PERSIAN_CHARSET,
    STANDARD_KEYBOARD, PERSIAN_MONTHS, PROVINCES,
)
```

> **نکته:** در حال حاضر فقط سه ماژول `letters`, `charset`, `keyboards`
> در `__init__.py` بارگذاری شده‌اند. بقیه ماژول‌ها به‌صورت جداگانه
> قابل import هستند (`from iran.calendar import PERSIAN_MONTHS`).

---

## 3. ساختار پروژه

| فایل | محتوا | وضعیت |
|------|-------|-------|
| `letters.py`   | حروف، ارقام، اعراب، نشانه‌گذاری | ✅ فعال |
| `charset.py`   | مجموعه‌های ترکیبی کاراکتر | ✅ فعال |
| `keyboards.py` | چیدمان‌های کیبورد فارسی | ✅ فعال |
| `calendar.py`  | ماه‌ها، فصل‌ها، روزهای هفته | ⏸ غیرفعال |
| `provinces.py` | استان‌ها، مراکز، کدها | ⏸ غیرفعال |
| `names.py`     | نام‌های رایج فارسی | ⏸ غیرفعال |
| `holidays.py`  | تعطیلات رسمی | ⏸ غیرفعال |
| `plates.py`    | پلاک خودرو | ⏸ غیرفعال |
| `banking.py`   | کدهای بانکی | ⏸ غیرفعال |
| `telecom.py`   | پیش‌شماره‌ها | ⏸ غیرفعال |

`__init__.py` فعلی:

```python
from .letters import *
from .charset import *
from .keyboards import *
```

---

## 4. ماژول `letters`

فایل `iran/letters.py` — حروف، ارقام، اعراب و نشانه‌گذاری فارسی.

### 4.1 حروف الفبا

| نام | نوع | مقدار |
|-----|-----|-------|
| `PERSIAN_LETTERS` | `str` | `"آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی"` |
| `PERSIAN_LETTERS_LIST` | `list` | همان، به‌صورت لیست |
| `PERSIAN_ALPHABET` | `list` | نام حروف: `["الف", "ب", "پ", ...]` |
| `PERSIAN_VOWELS` | `str` | `"اآوهی"` — حروف صدادار |
| `PERSIAN_CONSONANTS` | `str` | حروف بی‌صدا |
| `PERSIAN_CONNECTING` | `str` | حروفی که به حرف بعدی می‌چسبند |
| `PERSIAN_NON_CONNECTING` | `str` | `"ادذرزژو"` — حروفی که نمی‌چسبند |

```python
>>> from iran import PERSIAN_LETTERS, PERSIAN_ALPHABET
>>> len(PERSIAN_LETTERS)
32
>>> PERSIAN_ALPHABET[0]
'الف'
>>> "چ" in PERSIAN_LETTERS
True
```

### 4.2 ارقام

| نام | نوع | مقدار |
|-----|-----|-------|
| `PERSIAN_DIGITS` | `str` | `"۰۱۲۳۴۵۶۷۸۹"` |
| `PERSIAN_DIGITS_LIST` | `list` | همان، به‌صورت لیست |
| `ARABIC_EASTERN_DIGITS` | `str` | `"٠١٢٣٤٥٦٧٨٩"` (یونیکد عربی شرقی) |
| `PERSIAN_DIGITS_MAP` | `dict` | `{"۰": "0", "۱": "1", ...}` |
| `PERSIAN_DIGITS_REVERSE_MAP` | `dict` | `{"0": "۰", "1": "۱", ...}` |

```python
>>> from iran import PERSIAN_DIGITS, PERSIAN_DIGITS_MAP
>>> PERSIAN_DIGITS[5]
'۵'
>>> PERSIAN_DIGITS_MAP["۵"]
'5'
```

### 4.3 اعداد به حروف

`PERSIAN_NUMBER_WORDS` — دیکشنری عدد → نام فارسی.

| عدد | نام |
|-----|-----|
| 0 | صفر |
| 1 | یک |
| 2 | دو |
| ... | ... |
| 10 | ده |
| 11 | یازده |
| 20 | بیست |
| 30 | سی |
| 100 | صد |
| 1000 | هزار |
| 1_000_000 | میلیون |
| 1_000_000_000 | میلیارد |

```python
>>> from iran.letters import PERSIAN_NUMBER_WORDS
>>> PERSIAN_NUMBER_WORDS[1000]
'هزار'
```

### 4.4 اعراب

| نام | نوع | مقدار |
|-----|-----|-------|
| `PERSIAN_DIACRITICS` | `str` | `"ًٌٍَُِّْ"` — هفت اعراب اصلی |
| `PERSIAN_DIACRITICS_ALL` | `str` | شامل `"ٰٕٓٔ"` هم می‌شود |
| `PERSIAN_DIACRITICS_NAMES` | `dict` | `{"َ": "فتحه", "ِ": "کسره", ...}` |

### 4.5 نشانه‌گذاری

| نام | نوع | مقدار |
|-----|-----|-------|
| `PERSIAN_PUNCTUATION` | `str` | `"،؛؟٪٬٫٭ٰ"` |
| `PERSIAN_PUNCTUATION_NAMES` | `dict` | نام هر نشانه |
| `PUNCTUATION_UNICODE` | `str` | نشانه‌های یونیکد عمومی |

```python
>>> from iran import PERSIAN_PUNCTUATION_NAMES
>>> PERSIAN_PUNCTUATION_NAMES["،"]
'ویرگول'
>>> PERSIAN_PUNCTUATION_NAMES["؟"]
'علامت سؤال'
```

### 4.6 کاراکترهای نامرئی

| نام | کد | کاربرد |
|-----|-----|--------|
| `ZWNJ` | `\u200c` | نیم‌فاصله |
| `ZWJ`  | `\u200d` | اتصال‌دهنده عرض صفر |
| `LRM`  | `\u200e` | علامت چپ‌به‌راست |
| `RLM`  | `\u200f` | علامت راست‌به‌چپ |
| `ALM`  | `\u061c` | علامت عربی |

`PERSIAN_INVISIBLE` — مجموع همه.

```python
>>> from iran import ZWNJ
>>> "می\u200cروم".count(ZWNJ)
1
```

### 4.7 شکل‌های خاص حروف

| نام | مقدار | توضیح |
|-----|-------|--------|
| `PERSIAN_HAMZA_FORMS` | `"أإؤئءٕٔ"` | شکل‌های همزه |
| `PERSIAN_HEH_FORMS` | `"هۀة"` | شکل‌های ه |
| `PERSIAN_YEH_FORMS` | `"یىيئ"` | شکل‌های ی |
| `PERSIAN_KAF_FORMS` | `"کك"` | شکل‌های ک |
| `PERSIAN_ALEF_FORMS` | `"اآأإٱ"` | شکل‌های الف |

### 4.8 مجموع‌ها

| نام | محتوا |
|-----|-------|
| `ALL_PERSIAN_LETTERS` | همه حروف، شامل شکل‌های خاص |
| `ALL_PERSIAN_DIGITS` | ارقام فارسی + عربی شرقی |
| `ALL_PERSIAN_MARKS` | همه اعراب + نشانه‌ها + نامرئی‌ها |

---

## 5. ماژول `charset`

فایل `iran/charset.py` — مجموعه‌های ترکیبی کاراکتر.

| نام | محتوا |
|-----|-------|
| `PERSIAN_CHARSET` | حروف + ارقام + نشانه‌گذاری یونیکد |
| `PERSIAN_CHARSET_LIST` | همان، به‌صورت لیست |
| `PERSIAN_LETTERS_ONLY` | فقط حروف |
| `PERSIAN_LETTERS_WITH_DIACRITICS` | حروف + اعراب |
| `PERSIAN_TEXT_CHARS` | حروف + اعراب + نشانه‌ها + نامرئی‌ها |
| `PERSIAN_ALPHANUMERIC` | حروف + ارقام |
| `PERSIAN_FULL` | همه‌چیز با هم (با تکرار) |
| `PERSIAN_FULL_UNIQUE` | نسخه بدون تکرار |
| `PERSIAN_WHITESPACE` | فاصله‌های مجاز |
| `PERSIAN_FILENAME_SAFE` | کاراکترهای امن برای نام فایل |
| `PERSIAN_URL_SAFE` | کاراکترهای امن برای URL |
| `PERSIAN_PASSWORD_EXTRA` | کاراکترهای اضافی برای رمز |

```python
>>> from iran import PERSIAN_CHARSET, PERSIAN_ALPHANUMERIC
>>> "چ" in PERSIAN_CHARSET
True
>>> "۵" in PERSIAN_ALPHANUMERIC
True
```

---

## 6. ماژول `keyboards`

فایل `iran/keyboards.py` — چیدمان‌های کیبورد فارسی.

### چیدمان‌های موجود

| نام | توضیح |
|-----|-------|
| `STANDARD_KEYBOARD` | چیدمان استاندارد ISIRI 9147 |
| `STANDARD_KEYBOARD_SHIFT` | همان، با کلید Shift |
| `LEGACY_KEYBOARD` | چیدمان قدیمی (میراثی) |
| `PHONETIC_KEYBOARD` | چیدمان آوایی (فینگلیش) |
| `ARABIC_KEYBOARD` | چیدمان عربی |
| `WINDOWS_PERSIAN_KEYBOARD` | چیدمان پیش‌فرض ویندوز فارسی |

### نگاشت‌های معکوس

| نام | توضیح |
|-----|-------|
| `STANDARD_KEYBOARD_REVERSE` | فارسی → انگلیسی |
| `STANDARD_KEYBOARD_SHIFT_REVERSE` | همان، برای Shift |
| `LEGACY_KEYBOARD_REVERSE` | |
| `PHONETIC_KEYBOARD_REVERSE` | |

### مجموع

`ALL_KEYBOARDS` — دیکشنری از همه چیدمان‌ها با کلیدهای نام‌دار.

```python
>>> from iran import STANDARD_KEYBOARD, STANDARD_KEYBOARD_REVERSE
>>> STANDARD_KEYBOARD["q"]
'ض'
>>> STANDARD_KEYBOARD_REVERSE["ض"]
'q'
```

### نمونه‌هایی از چیدمان استاندارد

| کلید انگلیسی | حرف فارسی |
|--------------|-----------|
| q | ض |
| w | ص |
| e | ث |
| r | ق |
| t | ف |
| y | غ |
| u | ع |
| i | ه |
| o | خ |
| p | ح |
| a | ش |
| s | س |
| d | ی |
| f | ب |
| h | ا |
| j | ت |
| k | ن |
| l | م |
| z | ظ |
| c | ز |
| v | ر |
| b | ذ |
| n | د |
| m | پ |

---

## 7. مثال‌های کاربردی

### 7.1 بررسی اینکه یک کاراکتر فارسی است

```python
from iran import PERSIAN_LETTERS

def is_persian_letter(ch: str) -> bool:
    return ch in PERSIAN_LETTERS

is_persian_letter("چ")   # True
is_persian_letter("A")   # False
```

### 7.2 تبدیل ارقام فارسی به لاتین

```python
from iran import PERSIAN_DIGITS_MAP

def fa_to_en_digits(text: str) -> str:
    return "".join(PERSIAN_DIGITS_MAP.get(ch, ch) for ch in text)

fa_to_en_digits("۱۲۳")   # '123'
```

### 7.3 تبدیل متن انگلیسی به فارسی با کیبورد

```python
from iran import STANDARD_KEYBOARD

def en_to_fa(text: str) -> str:
    return "".join(STANDARD_KEYBOARD.get(ch, ch) for ch in text)

en_to_fa("hello")   # 'هثممخ'
```

### 7.4 حذف اعراب از متن

```python
from iran import PERSIAN_DIACRITICS_ALL

def remove_diacritics(text: str) -> str:
    return "".join(ch for ch in text if ch not in PERSIAN_DIACRITICS_ALL)

remove_diacritics("کِتاب")   # 'کتاب'
```

### 7.5 حذف کاراکترهای نامرئی

```python
from iran import PERSIAN_INVISIBLE

def strip_invisible(text: str) -> str:
    return "".join(ch for ch in text if ch not in PERSIAN_INVISIBLE)

strip_invisible("می\u200cروم")   # 'میروم'
```

### 7.6 بررسی اعتبار نام فایل فارسی

```python
from iran import PERSIAN_FILENAME_SAFE

def is_safe_filename(name: str) -> bool:
    return all(ch in PERSIAN_FILENAME_SAFE for ch in name)

is_safe_filename("گزارش-سال.txt")    # True
is_safe_filename("file<>.txt")       # False
```

---

## 8. نکات

### چرا فقط داده؟

چون یک دیتابیس باید دیتابیس باشد. اگر تابع تحلیل داخلش باشد:

- هر import، `os` و `re` را هم می‌کشد داخل
- تست کردن سخت‌تر می‌شود
- وابستگی‌های پنهان ایجاد می‌شود
- استفاده در محیط‌های محدود (مثل sandbox) سخت می‌شود

با نگه‌داشتن داده خالص:

- **سریع** — بدون syscall
- **امن** — بدون دسترسی فایل
- **قابل حمل** — هر OS
- **قابل تست** — فقط lookup
- **قابل ترکیب** — تو روی داده، منطق خودت را بساز

### ترتیب و تکرار

- `PERSIAN_LETTERS` ترتیب سنتی الفبا را نگه می‌دارد.
- `PERSIAN_ALPHABET` ترتیب ابجد را نگه می‌دارد.
- `ALL_PERSIAN_LETTERS` شامل شکل‌های خاص (همزه، کاف، ی) هم می‌شود.
- `PERSIAN_FULL_UNIQUE` بدون تکرار است، ولی ترتیب اولین وقوع را حفظ می‌کند.

### تفاوت `PERSIAN_DIGITS` و `ARABIC_EASTERN_DIGITS`

هر دو در یونیکد جدا هستند:

- `PERSIAN_DIGITS`: `U+06F0` تا `U+06F9` → `۰۱۲۳۴۵۶۷۸۹`
- `ARABIC_EASTERN_DIGITS`: `U+0660` تا `U+0669` → `٠١٢٣٤٥٦٧٨٩`

ایران معمولاً از اولی استفاده می‌کند، ولی هر دو در متن دیده می‌شوند.

### نیم‌فاصله (ZWNJ)

مهم‌ترین کاراکتر نامرئی فارسی. در `letters.py` به‌عنوان `ZWNJ`
تعریف شده و در `PERSIAN_INVISIBLE` هم هست. همیشه وقتی متن فارسی را
پردازش می‌کنی، این کاراکتر را در نظر بگیر.

### گسترش داده‌ها

فقط `letters.py` (یا هر فایل دیگر) را ویرایش کن. هیچ ثبت‌نام،
decorator یا plugin لازم نیست.

---

## 9. مجوز

MIT License.

Copyright © 2024–2026 — iran contributors.

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