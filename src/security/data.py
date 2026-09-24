# -*- coding: utf-8 -*-
"""
================================================================================
 security/data.py
================================================================================
 Pure static data about Unix file permissions and security risk levels.

 This module contains ONLY data — no logic, no side effects.

 Sections
 --------
 1. DANGEROUS_PERMISSIONS       — symbolic strings considered unsafe
 2. HIGH_RISK_PERMISSIONS       — most severe subset
 3. MEDIUM_RISK_PERMISSIONS     — moderate risk
 4. LOW_RISK_PERMISSIONS        — explicitly safe
 5. SPECIAL_BITS                — setuid / setgid / sticky names & values
 6. PERMISSION_NAMES            — human-readable names per octal value
 7. COMMON_PERMISSIONS          — frequently seen permission strings
 8. FILE_TYPE_CHARS             — symbolic leading characters
 9. PERMISSION_GROUPS           — permission → group label
10. RISK_DESCRIPTIONS           — textual descriptions per risk level
11. PERMISSION_DESCRIPTIONS     — long description per symbolic string
================================================================================
"""

from typing import Dict, List, Tuple

# =============================================================================
# 1. DANGEROUS PERMISSIONS
# =============================================================================
# Symbolic permission strings (9 chars, without file-type prefix) that are
# considered dangerous in typical Unix security reviews.

DANGEROUS_PERMISSIONS: List[str] = [
    "rwxrwxrwx",   # 777 — everyone has everything
    "rw-rw-rw-",   # 666 — world-writable file
    "rwxrwxrw-",   # 776
    "rwxrwxrwt",   # 1777 — sticky, but still world-writable
    "rwxrwxr-x",   # 775
    "rwxrwx--x",   # 771
    "rwxrwx--w",   # 772
    "rwxrwx-wx",   # 773
    "rwxrwx-w-",   # 762
    "rw-rw-rwx",   # 667
    "drwxrwxrwx",  # dir form (10 chars, kept for convenience)
    "drwxrwxrw-",
    "drwxrwxr-x",
    "drwxrwx--x",
    "drwxrwx--w",
    "drwxrwx-wx",
    "drwxrwx-w-",
]


# =============================================================================
# 2. HIGH RISK PERMISSIONS
# =============================================================================
# The most severe cases — usually reported as critical findings.

HIGH_RISK_PERMISSIONS: List[str] = [
    "rwxrwxrwx",
    "drwxrwxrwx",
    "rw-rw-rw-",
    "rwxrwxrw-",
    "rwxrwx-wx",
    "rwxrwx--w",
]


# =============================================================================
# 3. MEDIUM RISK PERMISSIONS
# =============================================================================
# Standard, commonly used, but still worth noting for sensitive files.

MEDIUM_RISK_PERMISSIONS: List[str] = [
    "rwxr-xr-x",   # 755
    "rw-r--r--",   # 644
    "rwxr-x---",   # 750
    "rw-r-----",   # 640
    "rwx------",   # 700 (owner-only but wide)
]


# =============================================================================
# 4. LOW RISK PERMISSIONS
# =============================================================================
# Explicitly safe patterns.

LOW_RISK_PERMISSIONS: List[str] = [
    "rw-------",   # 600
    "r--------",   # 400
    "rwx------",   # 700
    "rw-r-----",   # 640
    "rwxr-x---",   # 750
]


# =============================================================================
# 5. SPECIAL BITS
# =============================================================================
# Octal values and symbolic markers for setuid / setgid / sticky.

SPECIAL_BITS: Dict[str, int] = {
    "SUID":   0o4000,
    "SGID":   0o2000,
    "STICKY": 0o1000,
}

SPECIAL_BIT_SYMBOLS: Dict[str, str] = {
    "SUID":   "s/S",   # s = setuid + exec, S = setuid without exec
    "SGID":   "s/S",
    "STICKY": "t/T",   # t = sticky + exec, T = sticky without exec
}


# =============================================================================
# 6. PERMISSION NAMES
# =============================================================================
# Human-readable name for common octal values.

PERMISSION_NAMES: Dict[int, str] = {
    0o000: "no permissions",
    0o400: "owner read",
    0o600: "owner read/write",
    0o644: "owner rw, group/other read",
    0o700: "owner only",
    0o750: "owner full, group read/exec",
    0o755: "standard executable",
    0o777: "full access for everyone",
    0o1777: "world-writable with sticky",
    0o4755: "setuid root executable",
    0o2755: "setgid executable",
}


# =============================================================================
# 7. COMMON PERMISSIONS
# =============================================================================
# Frequently seen symbolic strings and their typical meanings.

COMMON_PERMISSIONS: Dict[str, str] = {
    "----------": "no permissions",
    "r--------":  "read-only, owner",
    "rw-------":  "private file",
    "rw-r--r--":  "world-readable file",
    "rw-rw-r--":  "group-writable file",
    "rw-rw-rw-":  "world-writable file",
    "rwx------":  "private executable",
    "rwxr-x---":  "group-executable",
    "rwxr-xr-x":  "standard executable",
    "rwxrwxrwx":  "world-writable executable",
    "rwxrwxrwt":  "world-writable with sticky (e.g. /tmp)",
}


# =============================================================================
# 8. FILE TYPE CHARACTERS
# =============================================================================
# First character of `ls -l` output → file type.

FILE_TYPE_CHARS: Dict[str, str] = {
    "-": "file",
    "d": "directory",
    "l": "symlink",
    "s": "socket",
    "p": "fifo",
    "c": "character device",
    "b": "block device",
}


# =============================================================================
# 9. PERMISSION GROUPS
# =============================================================================
# Maps a symbolic permission string to a coarse category.

PERMISSION_GROUPS: Dict[str, str] = {
    "owner_only":      "access restricted to the file owner",
    "group_only":      "access restricted to owner and group",
    "public_read":     "readable by everyone",
    "public_write":    "writable by everyone (dangerous)",
    "public_exec":     "executable by everyone",
    "public_full":     "full access for everyone (critical)",
    "special_bits":    "uses setuid, setgid, or sticky bit",
}


# =============================================================================
# 10. RISK DESCRIPTIONS
# =============================================================================
# One-line description per risk level.

RISK_DESCRIPTIONS: Dict[int, str] = {
    1: "LOW — safe, owner-restricted or read-only",
    2: "MEDIUM — standard read/execute for group/other",
    3: "HIGH — world-writable or setuid/setgid",
    4: "CRITICAL — world-writable and executable, or full 777",
}


# =============================================================================
# 11. PERMISSION DESCRIPTIONS
# =============================================================================
# Long description for common symbolic strings.

PERMISSION_DESCRIPTIONS: Dict[str, str] = {
    "rwxrwxrwx": (
        "Full access for everyone. Any user can read, modify, or execute "
        "the file. This is almost always a security issue."
    ),
    "rw-rw-rw-": (
        "World-writable, non-executable. Any user can modify the file."
    ),
    "rwxr-xr-x": (
        "Standard executable. Owner can modify; everyone else can read "
        "and execute."
    ),
    "rw-r--r--": (
        "Standard readable file. Owner can modify; everyone else can read."
    ),
    "rwxr-x---": (
        "Group-executable, not world-readable. Typical for internal "
        "tools and scripts."
    ),
    "rw-r-----": (
        "Group-readable, not world-readable. Typical for config files."
    ),
    "rwx------": (
        "Private executable. Only the owner can access."
    ),
    "rw-------": (
        "Private file. Only the owner can read or write."
    ),
    "rwxrwxrwt": (
        "World-writable directory with sticky bit (e.g. /tmp). Any user "
        "can create files, but only the owner can delete their own."
    ),
    "r--------": (
        "Read-only for the owner. Typically used for sensitive files."
    ),
    "----------": (
        "No permissions at all."
    ),
}


# =============================================================================
# 12. AGGREGATED VIEWS
# =============================================================================

# Flat list of every symbolic permission string we know about.
ALL_KNOWN_PERMISSIONS: List[str] = list(dict.fromkeys(
    DANGEROUS_PERMISSIONS
    + HIGH_RISK_PERMISSIONS
    + MEDIUM_RISK_PERMISSIONS
    + LOW_RISK_PERMISSIONS
    + list(COMMON_PERMISSIONS.keys())
))

# Mapping: symbolic string → risk level (1–4)
PERMISSION_TO_RISK: Dict[str, int] = {}
for _p in HIGH_RISK_PERMISSIONS:
    PERMISSION_TO_RISK[_p] = 4
for _p in DANGEROUS_PERMISSIONS:
    PERMISSION_TO_RISK.setdefault(_p, 3)
for _p in MEDIUM_RISK_PERMISSIONS:
    PERMISSION_TO_RISK.setdefault(_p, 2)
for _p in LOW_RISK_PERMISSIONS:
    PERMISSION_TO_RISK.setdefault(_p, 1)
del _p


# =============================================================================
# 13. SAFETY NOTES
# =============================================================================
# Short security notes, indexed by symbolic permission string.

SAFETY_NOTES: Dict[str, str] = {
    "rwxrwxrwx": "Never use 777 in production. Prefer 755 or 750.",
    "rw-rw-rw-": "World-writable files can be tampered with by anyone.",
    "rwxr-xr-x": "Acceptable for public binaries, but review for secrets.",
    "rw-r--r--": "Acceptable for public docs; not for private data.",
    "rwxr-x---": "Good default for internal executables.",
    "rw-r-----": "Good default for configuration files.",
    "rwx------": "Good default for private scripts.",
    "rw-------": "Good default for private files (keys, tokens).",
    "rwxrwxrwt": "Standard for /tmp. Do not rely on it for secrets.",
    "r--------": "Good for read-only sensitive data.",
    "----------": "Only useful as a lockdown state.",
}