# -*- coding: utf-8 -*-
"""
================================================================================
 colors.py
================================================================================
 ANSI escape sequences for terminal colors and text styling.

 Includes:
 * Reset / style modifiers (bold, dim, italic, underline, ...)
 * Standard 8/16 foreground & background colors
 * Bright (high-intensity) colors
 * 256-color and true-color (24-bit) helpers
 * Convenience functions for wrapping text with color codes
 * Automatic Windows ANSI enable (best effort)

 All constants are raw escape strings. Use the helper functions to
 wrap text with a reset at the end.

 Examples
 --------
 >>> from charsets.colors import RED, RESET, colorize
 >>> print(f"{RED}Hello{RESET}")
 >>> print(colorize("Hello", RED))
 >>> print(colorize("Bold red", RED, BOLD))
================================================================================
"""

from __future__ import annotations

import os
import sys
from typing import Optional

__all__ = [
    # Reset / styles
    "RESET", "BOLD", "DIM", "ITALIC", "UNDERLINE", "BLINK",
    "BLINK_FAST", "REVERSE", "HIDDEN", "STRIKETHROUGH",
    "RESET_BOLD", "RESET_DIM", "RESET_ITALIC", "RESET_UNDERLINE",
    "RESET_BLINK", "RESET_REVERSE", "RESET_HIDDEN", "RESET_STRIKETHROUGH",

    # Foreground (normal)
    "BLACK", "RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "WHITE",
    "DEFAULT",

    # Foreground (bright)
    "BRIGHT_BLACK", "BRIGHT_RED", "BRIGHT_GREEN", "BRIGHT_YELLOW",
    "BRIGHT_BLUE", "BRIGHT_MAGENTA", "BRIGHT_CYAN", "BRIGHT_WHITE",
    "GRAY", "GREY",

    # Background (normal)
    "BG_BLACK", "BG_RED", "BG_GREEN", "BG_YELLOW", "BG_BLUE",
    "BG_MAGENTA", "BG_CYAN", "BG_WHITE", "BG_DEFAULT",

    # Background (bright)
    "BG_BRIGHT_BLACK", "BG_BRIGHT_RED", "BG_BRIGHT_GREEN", "BG_BRIGHT_YELLOW",
    "BG_BRIGHT_BLUE", "BG_BRIGHT_MAGENTA", "BG_BRIGHT_CYAN", "BG_BRIGHT_WHITE",

    # 256-color
    "fg256", "bg256",
    "COLOR_256_NAMES",

    # True color
    "fg_rgb", "bg_rgb",

    # Helpers
    "colorize", "style", "strip_ansi", "enable_windows_ansi",

    # Maps
    "FOREGROUND_COLORS", "BACKGROUND_COLORS", "STYLE_CODES",
]


# =============================================================================
# 1. RESET & STYLE MODIFIERS
# =============================================================================

RESET              = "\033[0m"

# Text styles
BOLD               = "\033[1m"
DIM                = "\033[2m"
ITALIC             = "\033[3m"
UNDERLINE          = "\033[4m"
BLINK              = "\033[5m"
BLINK_FAST         = "\033[6m"
REVERSE            = "\033[7m"
HIDDEN             = "\033[8m"
STRIKETHROUGH      = "\033[9m"

# Individual resets (turn off a single attribute)
RESET_BOLD         = "\033[22m"   # also resets DIM
RESET_DIM          = "\033[22m"
RESET_ITALIC       = "\033[23m"
RESET_UNDERLINE    = "\033[24m"
RESET_BLINK        = "\033[25m"
RESET_REVERSE      = "\033[27m"
RESET_HIDDEN       = "\033[28m"
RESET_STRIKETHROUGH = "\033[29m"


# =============================================================================
# 2. FOREGROUND COLORS (standard 30-37)
# =============================================================================

BLACK              = "\033[30m"
RED                = "\033[31m"
GREEN              = "\033[32m"
YELLOW             = "\033[33m"
BLUE               = "\033[34m"
MAGENTA            = "\033[35m"
CYAN               = "\033[36m"
WHITE              = "\033[37m"
DEFAULT            = "\033[39m"


# =============================================================================
# 3. FOREGROUND COLORS (bright / high-intensity 90-97)
# =============================================================================

BRIGHT_BLACK       = "\033[90m"
BRIGHT_RED         = "\033[91m"
BRIGHT_GREEN       = "\033[92m"
BRIGHT_YELLOW      = "\033[93m"
BRIGHT_BLUE        = "\033[94m"
BRIGHT_MAGENTA     = "\033[95m"
BRIGHT_CYAN        = "\033[96m"
BRIGHT_WHITE       = "\033[97m"

# Common aliases
GRAY               = BRIGHT_BLACK
GREY               = BRIGHT_BLACK


# =============================================================================
# 4. BACKGROUND COLORS (standard 40-47)
# =============================================================================

BG_BLACK           = "\033[40m"
BG_RED             = "\033[41m"
BG_GREEN           = "\033[42m"
BG_YELLOW          = "\033[43m"
BG_BLUE            = "\033[44m"
BG_MAGENTA         = "\033[45m"
BG_CYAN            = "\033[46m"
BG_WHITE           = "\033[47m"
BG_DEFAULT         = "\033[49m"


# =============================================================================
# 5. BACKGROUND COLORS (bright 100-107)
# =============================================================================

BG_BRIGHT_BLACK    = "\033[100m"
BG_BRIGHT_RED      = "\033[101m"
BG_BRIGHT_GREEN    = "\033[102m"
BG_BRIGHT_YELLOW   = "\033[103m"
BG_BRIGHT_BLUE     = "\033[104m"
BG_BRIGHT_MAGENTA  = "\033[105m"
BG_BRIGHT_CYAN     = "\033[106m"
BG_BRIGHT_WHITE    = "\033[107m"


# =============================================================================
# 6. 256-COLOR SUPPORT
# =============================================================================

def fg256(n: int) -> str:
    """
    Return the ANSI escape for a 256-color foreground.

    Parameters
    ----------
    n : int
        Color index in the range 0–255.

    Raises
    ------
    ValueError
        If `n` is outside 0–255.

    Examples
    --------
    >>> fg256(196)   # bright red
    '\\x1b[38;5;196m'
    """
    if not 0 <= n <= 255:
        raise ValueError("256-color index must be between 0 and 255.")
    return f"\033[38;5;{n}m"


def bg256(n: int) -> str:
    """
    Return the ANSI escape for a 256-color background.

    Examples
    --------
    >>> bg256(196)
    '\\x1b[48;5;196m'
    """
    if not 0 <= n <= 255:
        raise ValueError("256-color index must be between 0 and 255.")
    return f"\033[48;5;{n}m"


# Named indices in the standard 256-color palette
COLOR_256_NAMES = {
    "black":         0,
    "red":           1,
    "green":         2,
    "yellow":        3,
    "blue":          4,
    "magenta":       5,
    "cyan":          6,
    "white":         7,
    "bright_black":  8,
    "bright_red":    9,
    "bright_green":  10,
    "bright_yellow": 11,
    "bright_blue":   12,
    "bright_magenta":13,
    "bright_cyan":   14,
    "bright_white":  15,
    "orange":        208,
    "pink":          213,
    "purple":        93,
    "teal":          30,
    "lime":          118,
    "gold":          220,
    "silver":        250,
    "gray":          244,
    "grey":          244,
}


# =============================================================================
# 7. TRUE COLOR (24-BIT RGB)
# =============================================================================

def fg_rgb(r: int, g: int, b: int) -> str:
    """
    Return the ANSI escape for a true-color (24-bit) foreground.

    Each channel must be in the range 0–255.

    Examples
    --------
    >>> fg_rgb(255, 0, 0)
    '\\x1b[38;2;255;0;0m'
    """
    if not all(0 <= v <= 255 for v in (r, g, b)):
        raise ValueError("RGB channels must be between 0 and 255.")
    return f"\033[38;2;{r};{g};{b}m"


def bg_rgb(r: int, g: int, b: int) -> str:
    """
    Return the ANSI escape for a true-color (24-bit) background.

    Examples
    --------
    >>> bg_rgb(0, 0, 255)
    '\\x1b[48;2;0;0;255m'
    """
    if not all(0 <= v <= 255 for v in (r, g, b)):
        raise ValueError("RGB channels must be between 0 and 255.")
    return f"\033[48;2;{r};{g};{b}m"


# =============================================================================
# 8. HELPER FUNCTIONS
# =============================================================================

def colorize(text: str, *codes: str, reset: bool = True) -> str:
    """
    Wrap `text` with one or more ANSI codes and a trailing reset.

    Parameters
    ----------
    text : str
        The text to wrap.
    *codes : str
        One or more ANSI escape sequences (e.g. RED, BOLD).
    reset : bool, optional
        Whether to append RESET at the end (default True).

    Returns
    -------
    str
        The styled text.

    Examples
    --------
    >>> colorize("Hello", RED)
    '\\x1b[31mHello\\x1b[0m'
    >>> colorize("Bold red", RED, BOLD)
    '\\x1b[31m\\x1b[1mBold red\\x1b[0m'
    """
    prefix = "".join(codes)
    return f"{prefix}{text}{RESET if reset else ''}"


def style(text: str, *codes: str) -> str:
    """Alias of `colorize` (kept for readability)."""
    return colorize(text, *codes)


_ANSI_RE = __import__("re").compile(r"\033\[[0-9;]*m")


def strip_ansi(text: str) -> str:
    """
    Remove every ANSI escape sequence from `text`.

    Examples
    --------
    >>> strip_ansi('\\x1b[31mHello\\x1b[0m')
    'Hello'
    """
    return _ANSI_RE.sub("", text)


def enable_windows_ansi() -> bool:
    """
    Best-effort enabling of ANSI escape processing on Windows.

    Returns
    -------
    bool
        True if ANSI is (probably) enabled, False otherwise.
    """
    if os.name != "nt":
        return True
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        # -11 = STD_OUTPUT_HANDLE
        handle = kernel32.GetStdHandle(-11)
        mode = ctypes.c_uint32()
        if not kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            return False
        # 0x0004 = ENABLE_VIRTUAL_TERMINAL_PROCESSING
        new_mode = mode.value | 0x0004
        return bool(kernel32.SetConsoleMode(handle, new_mode))
    except Exception:
        return False


# Auto-enable on Windows when this module is imported
if os.name == "nt":
    enable_windows_ansi()


# =============================================================================
# 9. LOOKUP MAPS (for iteration / tooling)
# =============================================================================

FOREGROUND_COLORS = {
    "black":         BLACK,
    "red":           RED,
    "green":         GREEN,
    "yellow":        YELLOW,
    "blue":          BLUE,
    "magenta":       MAGENTA,
    "cyan":          CYAN,
    "white":         WHITE,
    "default":       DEFAULT,
    "bright_black":  BRIGHT_BLACK,
    "bright_red":    BRIGHT_RED,
    "bright_green":  BRIGHT_GREEN,
    "bright_yellow": BRIGHT_YELLOW,
    "bright_blue":   BRIGHT_BLUE,
    "bright_magenta":BRIGHT_MAGENTA,
    "bright_cyan":   BRIGHT_CYAN,
    "bright_white":  BRIGHT_WHITE,
}

BACKGROUND_COLORS = {
    "black":         BG_BLACK,
    "red":           BG_RED,
    "green":         BG_GREEN,
    "yellow":        BG_YELLOW,
    "blue":          BG_BLUE,
    "magenta":       BG_MAGENTA,
    "cyan":          BG_CYAN,
    "white":         BG_WHITE,
    "default":       BG_DEFAULT,
    "bright_black":  BG_BRIGHT_BLACK,
    "bright_red":    BG_BRIGHT_RED,
    "bright_green":  BG_BRIGHT_GREEN,
    "bright_yellow": BG_BRIGHT_YELLOW,
    "bright_blue":   BG_BRIGHT_BLUE,
    "bright_magenta":BG_BRIGHT_MAGENTA,
    "bright_cyan":   BG_BRIGHT_CYAN,
    "bright_white":  BG_BRIGHT_WHITE,
}

STYLE_CODES = {
    "reset":         RESET,
    "bold":          BOLD,
    "dim":           DIM,
    "italic":        ITALIC,
    "underline":     UNDERLINE,
    "blink":         BLINK,
    "blink_fast":    BLINK_FAST,
    "reverse":       REVERSE,
    "hidden":        HIDDEN,
    "strikethrough": STRIKETHROUGH,
}