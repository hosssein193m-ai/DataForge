# -*- coding: utf-8 -*-
"""
Whitespace and punctuation character sets.
"""

# =============================================================================
# WHITESPACE
# =============================================================================

# Standard whitespace characters
WHITESPACE_STANDARD = "\t\n\r\v\f "

# Extended Unicode whitespace
WHITESPACE = (
    "\t\n\r\v\f"
    "\x1c\x1d\x1e\x1f"
    "\x85"
    "\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a"
    "\u2028\u2029"
    "\u205f\u3000"
    "\u00a0\u1680\u202f"
)

WHITESPACE_LIST = list(WHITESPACE_STANDARD)

# Zero-width and formatting characters (not truly whitespace but invisible)
WHITESPACE_EXTRA = "\u200b\u200c\u200d\u200e\u200f\u2060\ufeff"

WHITESPACE_ALL = WHITESPACE + WHITESPACE_EXTRA


# =============================================================================
# PUNCTUATION
# =============================================================================

PUNCTUATION_ASCII = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

PUNCTUATION_UNICODE = (
    "«»""''"
    "‒–—―… ′″‹›¡¿‽※·¨¸ˆˇˉ˘˙˚˛˜˝"
    "‖‗‚‛„‟†‡•‣․‥‧‰‱‴‵‶‷‸‼‾‿⁀⁁⁂⁃⁄⁅⁆⁇⁈⁉"
    "⁊⁋⁌⁍⁎⁏⁐⁑⁒⁓⁔⁕⁖⁗⁘⁙⁚⁛⁜⁝⁞"
)

PUNCTUATION_EXTRA = (
    "❛❜❝❞❟❠❡❢❣❤❥❦❧"
    "➔➘➙➚➛➜➝➞➟➠➡➢➣➤➥➦➧➨➩➪➫➬➭➮➯➰➱➲➳➴➵➶➷➸➹➺➻➼➽➾➿"
)

PUNCTUATION = PUNCTUATION_ASCII + PUNCTUATION_UNICODE + PUNCTUATION_EXTRA
PUNCTUATION_LIST = list(PUNCTUATION)


__all__ = [
    "WHITESPACE", "WHITESPACE_STANDARD", "WHITESPACE_LIST",
    "WHITESPACE_EXTRA", "WHITESPACE_ALL",
    "PUNCTUATION", "PUNCTUATION_ASCII", "PUNCTUATION_UNICODE",
    "PUNCTUATION_EXTRA", "PUNCTUATION_LIST",
]