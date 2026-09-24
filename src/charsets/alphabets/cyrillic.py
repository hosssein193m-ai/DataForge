# -*- coding: utf-8 -*-
"""Cyrillic-based alphabets for 16+ languages."""

# =============================================================================
# SLAVIC
# =============================================================================

RUSSIAN_LOWERCASE = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
RUSSIAN_UPPERCASE = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

UKRAINIAN_LOWERCASE = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
UKRAINIAN_UPPERCASE = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"

BULGARIAN_LOWERCASE = "абвгдежзийклмнопрстуфхцчшщъьюя"
BULGARIAN_UPPERCASE = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЬЮЯ"

SERBIAN_CYRILLIC_LOWERCASE = "абвгдђежзијклљмнњопрстћуфхцчџш"
SERBIAN_CYRILLIC_UPPERCASE = "АБВГДЂЕЖЗИЈКЛЉМНЊОПРСТЋУФХЦЧЏШ"

MACEDONIAN_CYRILLIC_LOWERCASE = "абвгдѓежзѕијклљмнњопрстќуфхцчџш"
MACEDONIAN_CYRILLIC_UPPERCASE = "АБВГДЃЕЖЗЅИЈКЛЉМНЊОПРСТЌУФХЦЧЏШ"

BELARUSIAN_LOWERCASE = "абвгдежзйклмнопрстуфхцчшыьэюяёіў"
BELARUSIAN_UPPERCASE = "АБВГДЕЖЗЙКЛМНОПРСТУФХЦЧШЫЬЭЮЯЁІЎ"


# =============================================================================
# TURKIC & MONGOLIC
# =============================================================================

MONGOLIAN_CYRILLIC_LOWERCASE = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяөү"
MONGOLIAN_CYRILLIC_UPPERCASE = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯӨҮ"

KAZAKH_CYRILLIC_LOWERCASE = "абвгдеёжзийклмнопрстуфхцчшщъыіьэюяғқңөұүһ"
KAZAKH_CYRILLIC_UPPERCASE = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫІЬЭЮЯҒҚҢӨҰҮҺ"

KYRGYZ_CYRILLIC_LOWERCASE = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяңөү"
KYRGYZ_CYRILLIC_UPPERCASE = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯҢӨҮ"

TATAR_CYRILLIC_LOWERCASE = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяәөүҗңһ"
TATAR_CYRILLIC_UPPERCASE = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯӘӨҮҖҢҺ"

BASHKIR_CYRILLIC_LOWERCASE = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяәөүҡңҫһ"
BASHKIR_CYRILLIC_UPPERCASE = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯӘӨҮҠҢҪҺ"

CHUVASH_CYRILLIC_LOWERCASE = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяӑӗ"
CHUVASH_CYRILLIC_UPPERCASE = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯӐӖ"


# =============================================================================
# IRANIAN (CYRILLIC)
# =============================================================================

TAJIK_CYRILLIC_LOWERCASE = "абвгдеёжзийклмнопрстуфхцчшъыьэюяғӣқӯҳҷ"
TAJIK_CYRILLIC_UPPERCASE = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЪЫЬЭЮЯҒӢҚӮҲҶ"

OSSETIAN_CYRILLIC_LOWERCASE = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяæӕ"
OSSETIAN_CYRILLIC_UPPERCASE = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯÆӔ"


# =============================================================================
# URALIC
# =============================================================================

MARI_CYRILLIC_LOWERCASE = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяӧӱ"
MARI_CYRILLIC_UPPERCASE = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯӦӰ"

UDMURT_CYRILLIC_LOWERCASE = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяӥӧ"
UDMURT_CYRILLIC_UPPERCASE = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯӤӦ"


# =============================================================================
# AGGREGATED
# =============================================================================

_LOWER_SOURCES = [
    RUSSIAN_LOWERCASE, UKRAINIAN_LOWERCASE, BULGARIAN_LOWERCASE,
    SERBIAN_CYRILLIC_LOWERCASE, MACEDONIAN_CYRILLIC_LOWERCASE,
    BELARUSIAN_LOWERCASE, MONGOLIAN_CYRILLIC_LOWERCASE,
    KAZAKH_CYRILLIC_LOWERCASE, KYRGYZ_CYRILLIC_LOWERCASE,
    TAJIK_CYRILLIC_LOWERCASE, TATAR_CYRILLIC_LOWERCASE,
    BASHKIR_CYRILLIC_LOWERCASE, CHUVASH_CYRILLIC_LOWERCASE,
    OSSETIAN_CYRILLIC_LOWERCASE, MARI_CYRILLIC_LOWERCASE,
    UDMURT_CYRILLIC_LOWERCASE,
]

_UPPER_SOURCES = [
    RUSSIAN_UPPERCASE, UKRAINIAN_UPPERCASE, BULGARIAN_UPPERCASE,
    SERBIAN_CYRILLIC_UPPERCASE, MACEDONIAN_CYRILLIC_UPPERCASE,
    BELARUSIAN_UPPERCASE, MONGOLIAN_CYRILLIC_UPPERCASE,
    KAZAKH_CYRILLIC_UPPERCASE, KYRGYZ_CYRILLIC_UPPERCASE,
    TAJIK_CYRILLIC_UPPERCASE, TATAR_CYRILLIC_UPPERCASE,
    BASHKIR_CYRILLIC_UPPERCASE, CHUVASH_CYRILLIC_UPPERCASE,
    OSSETIAN_CYRILLIC_UPPERCASE, MARI_CYRILLIC_UPPERCASE,
    UDMURT_CYRILLIC_UPPERCASE,
]

ALL_CYRILLIC_LOWERCASE = "".join(dict.fromkeys("".join(_LOWER_SOURCES)))
ALL_CYRILLIC_UPPERCASE = "".join(dict.fromkeys("".join(_UPPER_SOURCES)))
ALL_CYRILLIC           = ALL_CYRILLIC_LOWERCASE + ALL_CYRILLIC_UPPERCASE


__all__ = [name for name in dir() if name.isupper() and not name.startswith("_")]