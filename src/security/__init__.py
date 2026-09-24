# -*- coding: utf-8 -*-
"""
================================================================================
 security
================================================================================
 Static data and helpers for Unix file permissions and security risk levels.

 Submodules
 ----------
 data    : All static data (permissions, risk lists, descriptions)
 enums   : FileType, Permission, RiskLevel
 helpers : Small lookup functions over the data

 Design
 ------
 * `data.py` contains only data — no logic, no I/O.
 * `enums.py` contains only Enum definitions.
 * `helpers.py` contains small, pure lookup functions.

 If you need real filesystem analysis (os.stat), keep that logic in your
 own code — this package intentionally stays a data layer.
================================================================================
"""

from .data import (
    ALL_KNOWN_PERMISSIONS,
    COMMON_PERMISSIONS,
    DANGEROUS_PERMISSIONS,
    FILE_TYPE_CHARS,
    HIGH_RISK_PERMISSIONS,
    LOW_RISK_PERMISSIONS,
    MEDIUM_RISK_PERMISSIONS,
    PERMISSION_DESCRIPTIONS,
    PERMISSION_GROUPS,
    PERMISSION_NAMES,
    PERMISSION_TO_RISK,
    RISK_DESCRIPTIONS,
    SAFETY_NOTES,
    SPECIAL_BITS,
    SPECIAL_BIT_SYMBOLS,
)

from .enums import FileType, Permission, RiskLevel

from .helpers import (
    all_common,
    all_dangerous,
    all_high_risk,
    all_known,
    all_low_risk,
    all_medium_risk,
    describe_file_type,
    describe_permission,
    describe_risk,
    filetype_char,
    filetype_from_char,
    get_permission_name,
    get_risk,
    get_risk_level,
    get_safety_note,
    get_special_bit,
    is_dangerous,
    is_high_risk,
    is_low_risk,
    is_medium_risk,
    risk_from_name,
)

__version__ = "1.0.0"