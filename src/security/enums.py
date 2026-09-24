# -*- coding: utf-8 -*-
"""
================================================================================
 security/enums.py
================================================================================
 Enumerations for file types, permission masks, and risk levels.

 Enums are data: they classify values from `data.py`.
================================================================================
"""

from __future__ import annotations

from enum import Enum, IntEnum


# =============================================================================
# FileType
# =============================================================================

class FileType(Enum):
    """Possible Unix file types."""
    FILE      = "file"
    DIRECTORY = "directory"
    SYMLINK   = "symlink"
    SOCKET    = "socket"
    FIFO      = "fifo"
    DEVICE    = "device"
    UNKNOWN   = "unknown"
    NOT_FOUND = "not_found"


# =============================================================================
# RiskLevel
# =============================================================================

class RiskLevel(IntEnum):
    """
    Security risk level.

    Matches the integer keys in `data.RISK_DESCRIPTIONS`.
    """
    LOW      = 1
    MEDIUM   = 2
    HIGH     = 3
    CRITICAL = 4


# =============================================================================
# Permission (octal masks)
# =============================================================================

class Permission(IntEnum):
    """Standard Unix permission masks with symbolic names."""
    # Owner
    OWNER       = 0o700
    OWNER_READ  = 0o400
    OWNER_WRITE = 0o200
    OWNER_EXEC  = 0o100
    OWNER_RWX   = 0o700
    OWNER_RW    = 0o600
    OWNER_RX    = 0o500

    # Group
    GROUP       = 0o070
    GROUP_READ  = 0o040
    GROUP_WRITE = 0o020
    GROUP_EXEC  = 0o010
    GROUP_RWX   = 0o070
    GROUP_RW    = 0o060
    GROUP_RX    = 0o050

    # Other
    OTHER       = 0o007
    OTHER_READ  = 0o004
    OTHER_WRITE = 0o002
    OTHER_EXEC  = 0o001
    OTHER_RWX   = 0o007
    OTHER_RW    = 0o006
    OTHER_RX    = 0o005

    # Combined
    ALL_RWX  = 0o777
    ALL_RW   = 0o666
    ALL_RX   = 0o555
    USER_RWX = 0o755
    USER_RW  = 0o644

    # Special bits
    SUID   = 0o4000
    SGID   = 0o2000
    STICKY = 0o1000