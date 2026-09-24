# -*- coding: utf-8 -*-
"""
================================================================================
 world
================================================================================
 Static data about countries: calling codes, ISO codes, continents, languages,
 top-level domains, and regions.

 Data only. No functions. No logic.

 Submodules
 ----------
 calling_codes : Country calling codes (+1, +98, ...)
 iso_codes     : ISO 3166-1 alpha-2 codes
 continents    : Country → continent mapping
 languages     : Country → official languages
 tlds          : Country → top-level domain
 regions       : Country → region (for grouping)

 Version : 1.0.0
 License : MIT
================================================================================
"""

from .calling_codes import *
from .iso_codes import *
from .continents import *
from .languages import *
from .tlds import *
from .regions import *

__version__ = "1.0.0"