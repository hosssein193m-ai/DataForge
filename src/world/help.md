# `world` — Help & Documentation

Static data about countries: calling codes, ISO codes, continents,
languages, top-level domains, and regions.

> **Data only.** No functions. No logic. Every module exports plain Python
> dictionaries and lists.

- **Version:** 1.0.0
- **Python:** 3.8+
- **License:** MIT
- **Dependencies:** none (standard library only)

---

## Table of Contents

1. [Installation](#1-installation)
2. [Module Layout](#2-module-layout)
3. [Calling Codes](#3-calling-codes)
4. [ISO Codes](#4-iso-codes)
5. [Continents](#5-continents)
6. [Languages](#6-languages)
7. [TLDs](#7-tlds)
8. [Regions](#8-regions)
9. [Examples](#9-examples)
10. [Notes](#10-notes)
11. [License](#11-license)

---

## 1. Installation

Pure Python, no dependencies. Copy the `world/` folder into your project.

```python
from world import (
    COUNTRY_TO_CALLING_CODE, CALLING_CODE_TO_COUNTRY,
    ISO_ALPHA2, ISO_ALPHA3, ISO_NUMERIC,
    COUNTRY_CONTINENT, CONTINENT_COUNTRIES,
    COUNTRY_LANGUAGE, LANGUAGE_COUNTRIES,
    COUNTRY_TLD, TLD_TO_COUNTRY,
    REGION_COUNTRIES, COUNTRY_REGION,
)
```

---

## 2. Module Layout

| File | Contents |
|------|----------|
| `calling_codes.py` | Calling codes, NANP area codes, dial-out prefixes |
| `iso_codes.py`     | ISO alpha-2, alpha-3, numeric codes |
| `continents.py`    | Country → continent, continent → countries |
| `languages.py`     | Country → official languages, reverse index |
| `tlds.py`          | Country → ccTLD, reverse index |
| `regions.py`       | Region groupings (geographic, political, economic) |

---

## 3. Calling Codes

### `CALLING_CODE_TO_COUNTRY`

`Dict[int, str]` — calling code → country name.

```python
>>> CALLING_CODE_TO_COUNTRY[98]
'Iran'
>>> CALLING_CODE_TO_COUNTRY[1]  # not present — see NANP
```

Calling code `1` is not in this dict because it covers multiple
countries. See `NANP_AREA_CODES`.

### `COUNTRY_TO_CALLING_CODE`

`Dict[str, int]` — country name → calling code.

```python
>>> COUNTRY_TO_CALLING_CODE["Iran"]
98
>>> COUNTRY_TO_CALLING_CODE["United States"]
1
```

### `NANP_AREA_CODES`

`Dict[int, str]` — NANP area codes (all start with `1`).

```python
>>> NANP_AREA_CODES[1202]
'United States (Washington, D.C.)'
>>> NANP_AREA_CODES[1416]
'Canada (Ontario)'
>>> NANP_AREA_CODES[1868]
'Trinidad and Tobago'
```

### `INTERNATIONAL_DIAL_OUT`

`Dict[str, str]` — country → dial-out prefix.

```python
>>> INTERNATIONAL_DIAL_OUT["United States"]
'011'
>>> INTERNATIONAL_DIAL_OUT["Iran"]
'00'
```

---

## 4. ISO Codes

### `ISO_ALPHA2`

`Dict[str, str]` — country → ISO 3166-1 alpha-2.

```python
>>> ISO_ALPHA2["Iran"]
'IR'
>>> ISO_ALPHA2["United States"]
'US'
```

### `ISO2_TO_COUNTRY`

Reverse: alpha-2 → country.

```python
>>> ISO2_TO_COUNTRY["IR"]
'Iran'
```

### `ISO_ALPHA3`

`Dict[str, str]` — country → ISO 3166-1 alpha-3.

```python
>>> ISO_ALPHA3["Iran"]
'IRN'
```

### `ISO_NUMERIC`

`Dict[str, str]` — country → ISO 3166-1 numeric (3-digit string).

```python
>>> ISO_NUMERIC["Iran"]
'364'
```

---

## 5. Continents

### `COUNTRY_CONTINENT`

`Dict[str, str]` — country → continent.

```python
>>> COUNTRY_CONTINENT["Iran"]
'Asia'
>>> COUNTRY_CONTINENT["France"]
'Europe'
```

### `CONTINENT_COUNTRIES`

`Dict[str, List[str]]` — continent → countries.

```python
>>> CONTINENT_COUNTRIES["Europe"][:3]
['Albania', 'Andorra', 'Austria']
```

### `CONTINENTS`

`List[str]` — the six continents used here.

```python
['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']
```

### `CONTINENT_AREA_KM2` / `CONTINENT_POPULATION`

Metadata per continent.

---

## 6. Languages

### `COUNTRY_LANGUAGE`

`Dict[str, List[str]]` — country → official languages.

```python
>>> COUNTRY_LANGUAGE["Iran"]
['Persian']
>>> COUNTRY_LANGUAGE["Switzerland"]
['German', 'French', 'Italian', 'Romansh']
```

### `LANGUAGE_COUNTRIES`

Reverse index: language → countries.

```python
>>> LANGUAGE_COUNTRIES["Persian"]
['Iran', 'Afghanistan', ...]
```

### `LANGUAGE_ISO`

`Dict[str, str]` — language → ISO 639-1 code.

```python
>>> LANGUAGE_ISO["Persian"]
'fa'
>>> LANGUAGE_ISO["English"]
'en'
```

---

## 7. TLDs

### `COUNTRY_TLD`

`Dict[str, str]` — country → ccTLD.

```python
>>> COUNTRY_TLD["Iran"]
'.ir'
>>> COUNTRY_TLD["United States"]
'.us'
```

### `TLD_TO_COUNTRY`

Reverse: TLD → country.

```python
>>> TLD_TO_COUNTRY[".ir"]
'Iran'
```

---

## 8. Regions

### `REGION_COUNTRIES`

`Dict[str, List[str]]` — region → countries.

Covers geographic, cultural, political, military, and economic
groupings.

```python
>>> REGION_COUNTRIES["G7"]
['Canada', 'France', 'Germany', 'Italy', 'Japan', 'United Kingdom', 'United States']
>>> REGION_COUNTRIES["EU"][:5]
['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus']
```

### `COUNTRY_REGION`

Reverse index: country → list of regions.

```python
>>> COUNTRY_REGION["Iran"]
['Middle East', 'G20', 'BRICS', 'OPEC', 'Non-Aligned Movement', ...]
```

### `REGION_TYPE`

`Dict[str, str]` — region → type (`geographic`, `political`,
`economic`, `military`, `cultural`).

```python
>>> REGION_TYPE["G7"]
'economic'
>>> REGION_TYPE["NATO"]
'military'
```

---

## 9. Examples

### 9.1 Look Up Country Info

```python
from world import (
    COUNTRY_TO_CALLING_CODE, ISO_ALPHA2, ISO_ALPHA3,
    COUNTRY_CONTINENT, COUNTRY_LANGUAGE, COUNTRY_TLD,
)

country = "Iran"
print(COUNTRY_TO_CALLING_CODE[country])  # 98
print(ISO_ALPHA2[country])                # 'IR'
print(ISO_ALPHA3[country])                # 'IRN'
print(COUNTRY_CONTINENT[country])         # 'Asia'
print(COUNTRY_LANGUAGE[country])          # ['Persian']
print(COUNTRY_TLD[country])               # '.ir'
```

### 9.2 Reverse Lookup by ISO

```python
from world import ISO2_TO_COUNTRY, COUNTRY_TO_CALLING_CODE

iso = "DE"
country = ISO2_TO_COUNTRY[iso]
print(country)                        # 'Germany'
print(COUNTRY_TO_CALLING_CODE[country])  # 49
```

### 9.3 Parse a Phone Number

```python
from world import CALLING_CODE_TO_COUNTRY, NANP_AREA_CODES

def identify(number: str):
    digits = "".join(c for c in number if c.isdigit())
    if digits.startswith("1") and len(digits) >= 4:
        area = int(digits[:4])
        return NANP_AREA_CODES.get(area, "Unknown NANP area")
    for length in (3, 2, 1):
        prefix = int(digits[:length])
        if prefix in CALLING_CODE_TO_COUNTRY:
            return CALLING_CODE_TO_COUNTRY[prefix]
    return "Unknown"

identify("+98 21 1234 5678")   # 'Iran'
identify("+1 202 555 0142")    # 'United States (Washington, D.C.)'
```

### 9.4 List All EU Countries

```python
from world import REGION_COUNTRIES

for c in sorted(REGION_COUNTRIES["EU"]):
    print(c)
```

### 9.5 Find All Countries Speaking French

```python
from world import LANGUAGE_COUNTRIES

print(LANGUAGE_COUNTRIES["French"])
# ['Belgium', 'Canada', 'France', 'Haiti', 'Ivory Coast', ...]
```

---

## 10. Notes

### Calling code 1

The United States, Canada, and many Caribbean territories share
calling code **+1** under the North American Numbering Plan (NANP).
For this reason:

- `CALLING_CODE_TO_COUNTRY` does **not** contain key `1`.
- `NANP_AREA_CODES` contains all area codes starting with `1`.
- `COUNTRY_TO_CALLING_CODE` maps both `"United States"` and `"Canada"`
  to `1`.

### Official names

Some countries are listed under their official short name:
`Timor-Leste` (not East Timor), `Réunion` (with accent),
`São Tomé and Príncipe` (Sao Tome and Principe without diacritics
in the source data for compatibility).

### Diacritics

For maximum compatibility, most country names are ASCII-only.
Exceptions are `Réunion` and `Curaçao`, which include their
official diacritics.

### Overlaps

A country can appear in multiple regions:

```python
>>> COUNTRY_REGION["Turkey"]
['Middle East', 'NATO', 'G20', 'Non-Aligned Movement', 'Levant']
```

This is intentional — geographic, political, and economic
groupings are not mutually exclusive.

### Extending

Just edit the relevant data file. All reverse indexes are built
automatically at import time.

---

## 11. License

MIT License.

Copyright © 2024–2026 — world contributors.

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