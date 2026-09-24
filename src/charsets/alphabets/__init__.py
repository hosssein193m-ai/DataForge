# -*- coding: utf-8 -*-
"""Alphabet subpackage: language-specific letter sets."""

from . import latin
from . import cyrillic
from . import arabic
from . import south_asian
from . import southeast_asian
from . import east_asian
from . import other_scripts

__all__ = [
    "latin", "cyrillic", "arabic",
    "south_asian", "southeast_asian", "east_asian", "other_scripts",
]