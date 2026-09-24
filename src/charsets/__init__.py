# -*- coding: utf-8 -*-
"""
================================================================================
 charsets
================================================================================
 A comprehensive collection of character sets, alphabets, digits, punctuation,
 symbols, and character-property groups covering 90+ languages and scripts.

 Submodules
 ----------
 whitespace        : WHITESPACE, PUNCTUATION
 digits            : All digit systems (DEC, HEX, Persian, Devanagari, ...)
 alphabets.latin   : 54 Latin-based languages
 alphabets.cyrillic: 16 Cyrillic-based languages
 alphabets.arabic  : 10 Arabic-based scripts
 alphabets.south_asian    : 12 South Asian scripts
 alphabets.southeast_asian: Thai, Lao, Khmer, Myanmar, Javanese, Balinese
 alphabets.east_asian     : Chinese, Japanese, Korean
 alphabets.other_scripts  : Greek, Hebrew, Armenian, Georgian, Amharic, ...
 symbols           : Currency, math, arrows, music, emoji, ...
 printable         : Combined PRINTABLE_* sets
 functional        : URL, BASE64, EMAIL, IDENTIFIER, PASSWORD, ...
 groups            : Language families (Germanic, Romance, Slavic, Turkic)
 properties        : BIDI, RTL, LTR, HOMOGLYPH, ZERO_WIDTH, ...
 meta              : Statistics, BOM, category map, export configs

 Version : 1.0.0
 License : MIT
================================================================================
"""

from .whitespace import *
from .digits import *
from .symbols import *
from .printable import *
from .functional import *
from .groups import *
from .properties import *
from .meta import *
from .colors import *

from .alphabets.latin import *
from .alphabets.cyrillic import *
from .alphabets.arabic import *
from .alphabets.south_asian import *
from .alphabets.southeast_asian import *
from .alphabets.east_asian import *
from .alphabets.other_scripts import *

__version__ = "1.0.0"