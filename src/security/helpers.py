# -*- coding: utf-8 -*-
"""
================================================================================
 security/helpers.py
================================================================================
 Tiny convenience functions over the static data in `data.py`.

 These are not analysis functions — they are thin wrappers that make
 lookups easier. Every function is pure, fast, and has no I/O.
================================================================================
"""

from __future__ import annotations

from typing import Dict, List, Optional

from .data import (
    ALL_KNOWN_PERMISSIONS,
    COMMON_PERMISSIONS,
    DANGEROUS_PERMISSIONS,
    FILE_TYPE_CHARS,
    HIGH_RISK_PERMISSIONS,
    LOW_RISK_PERMISSIONS,
    MEDIUM_RISK_PERMISSIONS,
    PERMISSION_DESCRIPTIONS,
    PERMISSION_NAMES,
    PERMISSION_TO_RISK,
    RISK_DESCRIPTIONS,
    SAFETY_NOTES,
    SPECIAL_BITS,
)
from .enums import FileType, RiskLevel

__all__ = [
    "describe_permission",
    "describe_risk",
    "describe_file_type",
    "get_risk",
    "get_risk_level",
    "is_dangerous",
    "is_high_risk",
    "is_medium_risk",
    "is_low_risk",
    "get_safety_note",
    "get_permission_name",
    "get_special_bit",
    "all_dangerous",
    "all_high_risk",
    "all_medium_risk",
    "all_low_risk",
    "all_common",
    "all_known",
    "filetype_from_char",
    "filetype_char",
    "risk_from_name",
]


# =============================================================================
# Descriptions
# =============================================================================

def describe_permission(symbolic: str) -> str:
    """
    Long description for a symbolic permission string.

    Falls back to a generic message if the string is unknown.

    Examples
    --------
    >>> describe_permission("rwxrwxrwx")
    'Full access for everyone. ...'
    >>> describe_permission("rw-------")
    'Private file. Only the owner can read or write.'
    """
    if symbolic in PERMISSION_DESCRIPTIONS:
        return PERMISSION_DESCRIPTIONS[symbolic]
    if symbolic in COMMON_PERMISSIONS:
        return COMMON_PERMISSIONS[symbolic]
    return "No description available."


def describe_risk(risk: "RiskLevel | int") -> str:
    """
    One-line description for a risk level.

    Examples
    --------
    >>> describe_risk(RiskLevel.CRITICAL)
    'CRITICAL — world-writable and executable, or full 777'
    >>> describe_risk(2)
    'MEDIUM — standard read/execute for group/other'
    """
    level = int(risk)
    return RISK_DESCRIPTIONS.get(level, "Unknown risk level.")


def describe_file_type(ft: "FileType | str") -> str:
    """
    Return the long name of a file type.

    Examples
    --------
    >>> describe_file_type(FileType.FILE)
    'file'
    >>> describe_file_type("directory")
    'directory'
    """
    if isinstance(ft, FileType):
        return ft.value
    return str(ft)


# =============================================================================
# Risk lookups
# =============================================================================

def get_risk(symbolic: str) -> int:
    """
    Integer risk level (1–4) for a symbolic permission string.

    Defaults to 1 (LOW) for unknown strings.

    Examples
    --------
    >>> get_risk("rwxrwxrwx")
    4
    >>> get_risk("rw-------")
    1
    """
    return PERMISSION_TO_RISK.get(symbolic, 1)


def get_risk_level(symbolic: str) -> RiskLevel:
    """RiskLevel enum for a symbolic permission string."""
    return RiskLevel(get_risk(symbolic))


def is_dangerous(symbolic: str) -> bool:
    """True if the string is in `DANGEROUS_PERMISSIONS`."""
    return symbolic in DANGEROUS_PERMISSIONS


def is_high_risk(symbolic: str) -> bool:
    """True if the string is in `HIGH_RISK_PERMISSIONS`."""
    return symbolic in HIGH_RISK_PERMISSIONS


def is_medium_risk(symbolic: str) -> bool:
    """True if the string is in `MEDIUM_RISK_PERMISSIONS`."""
    return symbolic in MEDIUM_RISK_PERMISSIONS


def is_low_risk(symbolic: str) -> bool:
    """True if the string is in `LOW_RISK_PERMISSIONS`."""
    return symbolic in LOW_RISK_PERMISSIONS


# =============================================================================
# Notes and names
# =============================================================================

def get_safety_note(symbolic: str) -> Optional[str]:
    """
    Return a short safety note, or None if there is none.

    Examples
    --------
    >>> get_safety_note("rwxrwxrwx")
    'Never use 777 in production. Prefer 755 or 750.'
    >>> get_safety_note("rw-------") is None
    False
    """
    return SAFETY_NOTES.get(symbolic)


def get_permission_name(octal: int) -> Optional[str]:
    """
    Human-readable name for an octal permission value.

    Examples
    --------
    >>> get_permission_name(0o644)
    'owner rw, group/other read'
    >>> get_permission_name(0o999)
    """
    return PERMISSION_NAMES.get(octal)


def get_special_bit(name: str) -> Optional[int]:
    """
    Octal value for a special bit name ('SUID', 'SGID', 'STICKY').

    Examples
    --------
    >>> get_special_bit("SUID")
    2048
    >>> get_special_bit("UNKNOWN") is None
    True
    """
    return SPECIAL_BITS.get(name.upper())


# =============================================================================
# Data accessors (read-only copies)
# =============================================================================

def all_dangerous() -> List[str]:
    """Return a copy of DANGEROUS_PERMISSIONS."""
    return list(DANGEROUS_PERMISSIONS)


def all_high_risk() -> List[str]:
    """Return a copy of HIGH_RISK_PERMISSIONS."""
    return list(HIGH_RISK_PERMISSIONS)


def all_medium_risk() -> List[str]:
    """Return a copy of MEDIUM_RISK_PERMISSIONS."""
    return list(MEDIUM_RISK_PERMISSIONS)


def all_low_risk() -> List[str]:
    """Return a copy of LOW_RISK_PERMISSIONS."""
    return list(LOW_RISK_PERMISSIONS)


def all_common() -> Dict[str, str]:
    """Return a copy of COMMON_PERMISSIONS."""
    return dict(COMMON_PERMISSIONS)


def all_known() -> List[str]:
    """Return a copy of ALL_KNOWN_PERMISSIONS."""
    return list(ALL_KNOWN_PERMISSIONS)


# =============================================================================
# File type helpers
# =============================================================================

def filetype_from_char(c: str) -> FileType:
    """
    Map a single symbolic character to a FileType.

    Examples
    --------
    >>> filetype_from_char("-")
    <FileType.FILE: 'file'>
    >>> filetype_from_char("d")
    <FileType.DIRECTORY: 'directory'>
    """
    name = FILE_TYPE_CHARS.get(c, "unknown")
    return {
        "file":             FileType.FILE,
        "directory":        FileType.DIRECTORY,
        "symlink":          FileType.SYMLINK,
        "socket":           FileType.SOCKET,
        "fifo":             FileType.FIFO,
        "character device": FileType.DEVICE,
        "block device":     FileType.DEVICE,
        "unknown":          FileType.UNKNOWN,
    }[name]


def filetype_char(ft: FileType) -> str:
    """
    Reverse of `filetype_from_char`.

    Examples
    --------
    >>> filetype_char(FileType.FILE)
    '-'
    >>> filetype_char(FileType.DIRECTORY)
    'd'
    """
    return {
        FileType.FILE:      "-",
        FileType.DIRECTORY: "d",
        FileType.SYMLINK:   "l",
        FileType.SOCKET:    "s",
        FileType.FIFO:      "p",
        FileType.DEVICE:    "?",
        FileType.UNKNOWN:   "?",
        FileType.NOT_FOUND: "?",
    }[ft]


# =============================================================================
# Risk name lookup
# =============================================================================

def risk_from_name(name: str) -> Optional[RiskLevel]:
    """
    Convert a risk name to a RiskLevel.

    Examples
    --------
    >>> risk_from_name("critical")
    <RiskLevel.CRITICAL: 4>
    >>> risk_from_name("unknown") is None
    True
    """
    try:
        return RiskLevel[name.upper()]
    except KeyError:
        return None