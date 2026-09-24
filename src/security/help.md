# `security` — Help & Documentation

Static data and small helpers for Unix file permissions and security risk levels.

> **Standalone package.** This package does **not** depend on `charsets`
> or any other package. It uses only the Python standard library.

- **Version:** 1.0.0
- **Python:** 3.8+
- **License:** MIT
- **Dependencies:** none (standard library only)

---

## Table of Contents

1. [Design Philosophy](#1-design-philosophy)
2. [Installation & Import](#2-installation--import)
3. [Module Layout](#3-module-layout)
4. [Enums](#4-enums)
   - 4.1 [`FileType`](#41-filetype)
   - 4.2 [`RiskLevel`](#42-risklevel)
   - 4.3 [`Permission`](#43-permission)
5. [Static Data](#5-static-data)
   - 5.1 [`DANGEROUS_PERMISSIONS`](#51-dangerous_permissions)
   - 5.2 [`HIGH_RISK_PERMISSIONS`](#52-high_risk_permissions)
   - 5.3 [`MEDIUM_RISK_PERMISSIONS`](#53-medium_risk_permissions)
   - 5.4 [`LOW_RISK_PERMISSIONS`](#54-low_risk_permissions)
   - 5.5 [`SPECIAL_BITS`](#55-special_bits)
   - 5.6 [`PERMISSION_NAMES`](#56-permission_names)
   - 5.7 [`COMMON_PERMISSIONS`](#57-common_permissions)
   - 5.8 [`FILE_TYPE_CHARS`](#58-file_type_chars)
   - 5.9 [`PERMISSION_GROUPS`](#59-permission_groups)
   - 5.10 [`RISK_DESCRIPTIONS`](#510-risk_descriptions)
   - 5.11 [`PERMISSION_DESCRIPTIONS`](#511-permission_descriptions)
   - 5.12 [`SAFETY_NOTES`](#512-safety_notes)
   - 5.13 [`PERMISSION_TO_RISK`](#513-permission_to_risk)
   - 5.14 [`ALL_KNOWN_PERMISSIONS`](#514-all_known_permissions)
6. [Helper Functions](#6-helper-functions)
7. [Examples](#7-examples)
8. [Notes](#8-notes)
9. [License](#9-license)

---

## 1. Design Philosophy

This package is a **data layer**, not a logic layer.

- `data.py` contains **only static data** — no I/O, no logic.
- `enums.py` contains **only Enum definitions**.
- `helpers.py` contains **small, pure lookup functions** over the data.

There is deliberately **no `os.stat` call, no filesystem access, no
analysis function**. If you need to inspect a real file, that logic belongs
in your own code. This package stays a clean, importable database.

**Rule of thumb:** if it touches the filesystem or needs arguments that
aren't already data, it doesn't belong here.

---

## 2. Installation & Import

Pure Python, no dependencies, no relation to any other package.

```python
from security import (
    # enums
    FileType, RiskLevel, Permission,
    # data
    DANGEROUS_PERMISSIONS, HIGH_RISK_PERMISSIONS, MEDIUM_RISK_PERMISSIONS,
    LOW_RISK_PERMISSIONS, SPECIAL_BITS, PERMISSION_NAMES,
    COMMON_PERMISSIONS, FILE_TYPE_CHARS, PERMISSION_GROUPS,
    RISK_DESCRIPTIONS, PERMISSION_DESCRIPTIONS, SAFETY_NOTES,
    PERMISSION_TO_RISK, ALL_KNOWN_PERMISSIONS,
    # helpers
    describe_permission, describe_risk, get_risk, is_dangerous,
    get_safety_note, filetype_from_char, filetype_char,
)
```

---

## 3. Module Layout

```
security/
├── __init__.py   ← re-exports everything
├── data.py       ← static data only
├── enums.py      ← FileType, RiskLevel, Permission
├── helpers.py    ← small pure functions over data.py
└── HELP.md       ← this file
```

| File | Contains | Touches FS? |
|------|----------|-------------|
| `data.py`     | All static data (dicts, lists, strings) | ❌ |
| `enums.py`    | `FileType`, `RiskLevel`, `Permission`   | ❌ |
| `helpers.py`  | Tiny lookup functions over `data.py`    | ❌ |
| `__init__.py` | Re-exports everything                   | ❌ |

---

## 4. Enums

### 4.1 `FileType`

Possible Unix file types.

| Member | Value |
|--------|-------|
| `FileType.FILE` | `"file"` |
| `FileType.DIRECTORY` | `"directory"` |
| `FileType.SYMLINK` | `"symlink"` |
| `FileType.SOCKET` | `"socket"` |
| `FileType.FIFO` | `"fifo"` |
| `FileType.DEVICE` | `"device"` |
| `FileType.UNKNOWN` | `"unknown"` |
| `FileType.NOT_FOUND` | `"not_found"` |

```python
>>> from security import FileType
>>> FileType.FILE.value
'file'
>>> FileType.DIRECTORY.value
'directory'
```

---

### 4.2 `RiskLevel`

Security risk level. Values match the integer keys in `RISK_DESCRIPTIONS`.

| Member | Value | Meaning |
|--------|-------|---------|
| `RiskLevel.LOW` | `1` | Safe |
| `RiskLevel.MEDIUM` | `2` | Standard group/other access |
| `RiskLevel.HIGH` | `3` | World-writable or setuid/setgid |
| `RiskLevel.CRITICAL` | `4` | World-writable **and** executable, or full 777 |

```python
>>> from security import RiskLevel
>>> RiskLevel.CRITICAL.value
4
>>> int(RiskLevel.MEDIUM)
2
```

---

### 4.3 `Permission`

Standard Unix permission masks with symbolic names. Values are **octal
integers** (Python `IntEnum`).

#### Owner

| Name | Octal |
|------|-------|
| `Permission.OWNER` | `0o700` |
| `Permission.OWNER_READ` | `0o400` |
| `Permission.OWNER_WRITE` | `0o200` |
| `Permission.OWNER_EXEC` | `0o100` |
| `Permission.OWNER_RWX` | `0o700` |
| `Permission.OWNER_RW` | `0o600` |
| `Permission.OWNER_RX` | `0o500` |

#### Group

| Name | Octal |
|------|-------|
| `Permission.GROUP` | `0o070` |
| `Permission.GROUP_READ` | `0o040` |
| `Permission.GROUP_WRITE` | `0o020` |
| `Permission.GROUP_EXEC` | `0o010` |
| `Permission.GROUP_RWX` | `0o070` |
| `Permission.GROUP_RW` | `0o060` |
| `Permission.GROUP_RX` | `0o050` |

#### Other

| Name | Octal |
|------|-------|
| `Permission.OTHER` | `0o007` |
| `Permission.OTHER_READ` | `0o004` |
| `Permission.OTHER_WRITE` | `0o002` |
| `Permission.OTHER_EXEC` | `0o001` |
| `Permission.OTHER_RWX` | `0o007` |
| `Permission.OTHER_RW` | `0o006` |
| `Permission.OTHER_RX` | `0o005` |

#### Combined

| Name | Octal |
|------|-------|
| `Permission.ALL_RWX` | `0o777` |
| `Permission.ALL_RW` | `0o666` |
| `Permission.ALL_RX` | `0o555` |
| `Permission.USER_RWX` | `0o755` |
| `Permission.USER_RW` | `0o644` |

#### Special bits

| Name | Octal |
|------|-------|
| `Permission.SUID` | `0o4000` |
| `Permission.SGID` | `0o2000` |
| `Permission.STICKY` | `0o1000` |

```python
>>> from security import Permission
>>> oct(Permission.OWNER_RW)
'0o600'
>>> Permission.OWNER_READ | Permission.OWNER_WRITE
384  # 0o600
```

---

## 5. Static Data

All static data lives in `data.py`. Import directly from `security`
or from `security.data`.

### 5.1 `DANGEROUS_PERMISSIONS`

`List[str]` — symbolic permission strings considered unsafe.

```python
[
    "rwxrwxrwx", "rw-rw-rw-", "rwxrwxrw-", "rwxrwxrwt",
    "rwxrwxr-x", "rwxrwx--x", "rwxrwx--w", "rwxrwx-wx",
    "rwxrwx-w-", "rw-rw-rwx",
    # directory (10-char) forms
    "drwxrwxrwx", "drwxrwxrw-", "drwxrwxr-x", "drwxrwx--x",
    "drwxrwx--w", "drwxrwx-wx", "drwxrwx-w-",
]
```

Length: **17**.

---

### 5.2 `HIGH_RISK_PERMISSIONS`

`List[str]` — the most severe subset.

```python
[
    "rwxrwxrwx", "drwxrwxrwx", "rw-rw-rw-",
    "rwxrwxrw-", "rwxrwx-wx", "rwxrwx--w",
]
```

Length: **6**.

---

### 5.3 `MEDIUM_RISK_PERMISSIONS`

`List[str]` — standard, commonly used, but worth reviewing.

```python
[
    "rwxr-xr-x", "rw-r--r--", "rwxr-x---",
    "rw-r-----", "rwx------",
]
```

Length: **5**.

---

### 5.4 `LOW_RISK_PERMISSIONS`

`List[str]` — explicitly safe patterns.

```python
[
    "rw-------", "r--------", "rwx------",
    "rw-r-----", "rwxr-x---",
]
```

Length: **5**.

---

### 5.5 `SPECIAL_BITS`

`Dict[str, int]` — setuid / setgid / sticky octal values.

| Key | Value |
|-----|-------|
| `"SUID"` | `0o4000` = 2048 |
| `"SGID"` | `0o2000` = 1024 |
| `"STICKY"` | `0o1000` = 512 |

Also available: `SPECIAL_BIT_SYMBOLS` (`Dict[str, str]`) with the symbolic
letters `s/S` and `t/T`.

```python
>>> from security import SPECIAL_BITS
>>> SPECIAL_BITS["STICKY"]
512
```

---

### 5.6 `PERMISSION_NAMES`

`Dict[int, str]` — human-readable name for common octal values.

| Octal | Name |
|-------|------|
| `0o000` | no permissions |
| `0o400` | owner read |
| `0o600` | owner read/write |
| `0o644` | owner rw, group/other read |
| `0o700` | owner only |
| `0o750` | owner full, group read/exec |
| `0o755` | standard executable |
| `0o777` | full access for everyone |
| `0o1777` | world-writable with sticky |
| `0o4755` | setuid root executable |
| `0o2755` | setgid executable |

---

### 5.7 `COMMON_PERMISSIONS`

`Dict[str, str]` — frequently seen symbolic strings → short description.

| Symbolic | Meaning |
|----------|---------|
| `----------` | no permissions |
| `r--------` | read-only, owner |
| `rw-------` | private file |
| `rw-r--r--` | world-readable file |
| `rw-rw-r--` | group-writable file |
| `rw-rw-rw-` | world-writable file |
| `rwx------` | private executable |
| `rwxr-x---` | group-executable |
| `rwxr-xr-x` | standard executable |
| `rwxrwxrwx` | world-writable executable |
| `rwxrwxrwt` | world-writable with sticky (e.g. /tmp) |

---

### 5.8 `FILE_TYPE_CHARS`

`Dict[str, str]` — first char of `ls -l` output → file-type name.

| Char | Meaning |
|------|---------|
| `-` | file |
| `d` | directory |
| `l` | symlink |
| `s` | socket |
| `p` | fifo |
| `c` | character device |
| `b` | block device |

---

### 5.9 `PERMISSION_GROUPS`

`Dict[str, str]` — coarse permission categories with descriptions.

| Key | Meaning |
|-----|---------|
| `owner_only` | access restricted to the file owner |
| `group_only` | access restricted to owner and group |
| `public_read` | readable by everyone |
| `public_write` | writable by everyone (dangerous) |
| `public_exec` | executable by everyone |
| `public_full` | full access for everyone (critical) |
| `special_bits` | uses setuid, setgid, or sticky bit |

---

### 5.10 `RISK_DESCRIPTIONS`

`Dict[int, str]` — one-line description per risk level.

| Key | Value |
|-----|-------|
| `1` | LOW — safe, owner-restricted or read-only |
| `2` | MEDIUM — standard read/execute for group/other |
| `3` | HIGH — world-writable or setuid/setgid |
| `4` | CRITICAL — world-writable and executable, or full 777 |

---

### 5.11 `PERMISSION_DESCRIPTIONS`

`Dict[str, str]` — long description per symbolic permission string.

Includes entries for: `rwxrwxrwx`, `rw-rw-rw-`, `rwxr-xr-x`, `rw-r--r--`,
`rwxr-x---`, `rw-r-----`, `rwx------`, `rw-------`, `rwxrwxrwt`, `r--------`,
`----------`.

```python
>>> from security import PERMISSION_DESCRIPTIONS
>>> PERMISSION_DESCRIPTIONS["rwxrwxrwx"][:40]
'Full access for everyone. Any user can '
```

---

### 5.12 `SAFETY_NOTES`

`Dict[str, str]` — short actionable note per symbolic string.

| Symbolic | Note |
|----------|------|
| `rwxrwxrwx` | Never use 777 in production. Prefer 755 or 750. |
| `rw-rw-rw-` | World-writable files can be tampered with by anyone. |
| `rwxr-xr-x` | Acceptable for public binaries, but review for secrets. |
| `rw-r--r--` | Acceptable for public docs; not for private data. |
| `rwxr-x---` | Good default for internal executables. |
| `rw-r-----` | Good default for configuration files. |
| `rwx------` | Good default for private scripts. |
| `rw-------` | Good default for private files (keys, tokens). |
| `rwxrwxrwt` | Standard for /tmp. Do not rely on it for secrets. |
| `r--------` | Good for read-only sensitive data. |
| `----------` | Only useful as a lockdown state. |

---

### 5.13 `PERMISSION_TO_RISK`

`Dict[str, int]` — symbolic string → risk level (1–4).

Built by combining all four risk lists.

```python
>>> from security import PERMISSION_TO_RISK
>>> PERMISSION_TO_RISK["rwxrwxrwx"]
4
>>> PERMISSION_TO_RISK["rw-------"]
1
```

---

### 5.14 `ALL_KNOWN_PERMISSIONS`

`List[str]` — every symbolic permission string we know about, deduplicated.

Combines: `DANGEROUS_PERMISSIONS` + `HIGH_RISK_PERMISSIONS` +
`MEDIUM_RISK_PERMISSIONS` + `LOW_RISK_PERMISSIONS` + keys of
`COMMON_PERMISSIONS`.

---

## 6. Helper Functions

All helpers are pure, fast, and have **no I/O**.

### Descriptions

| Function | Purpose |
|----------|---------|
| `describe_permission(symbolic)` | Long description for a symbolic string |
| `describe_risk(risk)` | One-line description for a risk level |
| `describe_file_type(ft)` | Long name of a file type |

```python
>>> describe_permission("rw-r--r--")
'Standard readable file. Owner can modify; everyone else can read.'
>>> describe_risk(4)
'CRITICAL — world-writable and executable, or full 777'
>>> describe_file_type(FileType.DIRECTORY)
'directory'
```

### Risk lookups

| Function | Purpose |
|----------|---------|
| `get_risk(symbolic)` | Integer risk level (1–4), defaults to 1 |
| `get_risk_level(symbolic)` | Returns a `RiskLevel` enum |
| `is_dangerous(symbolic)` | `True` if in `DANGEROUS_PERMISSIONS` |
| `is_high_risk(symbolic)` | `True` if in `HIGH_RISK_PERMISSIONS` |
| `is_medium_risk(symbolic)` | `True` if in `MEDIUM_RISK_PERMISSIONS` |
| `is_low_risk(symbolic)` | `True` if in `LOW_RISK_PERMISSIONS` |

```python
>>> get_risk("rwxrwxrwx")
4
>>> is_dangerous("rwxrwxrwx")
True
>>> is_low_risk("rw-------")
True
```

### Notes, names, special bits

| Function | Purpose |
|----------|---------|
| `get_safety_note(symbolic)` | Short safety note or `None` |
| `get_permission_name(octal)` | Human-readable name for an octal value |
| `get_special_bit(name)` | Octal value for `"SUID"`, `"SGID"`, `"STICKY"` |

```python
>>> get_safety_note("rwxrwxrwx")
'Never use 777 in production. Prefer 755 or 750.'
>>> get_permission_name(0o644)
'owner rw, group/other read'
>>> get_special_bit("STICKY")
512
```

### Data accessors (read-only copies)

| Function | Returns |
|----------|---------|
| `all_dangerous()` | copy of `DANGEROUS_PERMISSIONS` |
| `all_high_risk()` | copy of `HIGH_RISK_PERMISSIONS` |
| `all_medium_risk()` | copy of `MEDIUM_RISK_PERMISSIONS` |
| `all_low_risk()` | copy of `LOW_RISK_PERMISSIONS` |
| `all_common()` | copy of `COMMON_PERMISSIONS` |
| `all_known()` | copy of `ALL_KNOWN_PERMISSIONS` |

### File type helpers

| Function | Purpose |
|----------|---------|
| `filetype_from_char(c)` | `"-"` → `FileType.FILE`, etc. |
| `filetype_char(ft)` | Reverse of `filetype_from_char` |

```python
>>> filetype_from_char("d")
<FileType.DIRECTORY: 'directory'>
>>> filetype_char(FileType.SYMLINK)
'l'
```

### Risk name lookup

| Function | Purpose |
|----------|---------|
| `risk_from_name(name)` | `"critical"` → `RiskLevel.CRITICAL`, `None` if unknown |

---

## 7. Examples

### 7.1 Look up a Permission's Risk

```python
from security import get_risk, describe_risk, get_safety_note

perm = "rwxrwxrwx"
level = get_risk(perm)
print(level)                     # 4
print(describe_risk(level))      # CRITICAL — ...
print(get_safety_note(perm))     # Never use 777 in production. ...
```

### 7.2 Iterate Over Every Dangerous Permission

```python
from security import all_dangerous, describe_permission

for perm in all_dangerous():
    print(f"{perm:<12} {describe_permission(perm)[:50]}")
```

### 7.3 Build a Custom Warning Set

```python
from security import DANGEROUS_PERMISSIONS, HIGH_RISK_PERMISSIONS

WARN_ON = set(DANGEROUS_PERMISSIONS) | set(HIGH_RISK_PERMISSIONS)

def should_warn(perm: str) -> bool:
    return perm in WARN_ON

should_warn("rwxrwxrwx")   # True
should_warn("rw-------")   # False
```

### 7.4 Map ls -l Output

```python
from security import FILE_TYPE_CHARS, filetype_from_char

def parse_ls_line(line: str):
    type_char = line[0]
    ft = filetype_from_char(type_char)
    symbolic = line[1:10]
    return ft, symbolic

# ls -l style: "drwxr-xr-x  3 user group ..."
ft, symbolic = parse_ls_line("drwxr-xr-x  3 user group ...")
print(ft.value)         # 'directory'
print(symbolic)         # 'rwxr-xr-x'
```

### 7.5 Build a Table of All Known Permissions

```python
from security import (
    all_known, get_risk, describe_permission, SAFETY_NOTES,
)

for perm in sorted(all_known()):
    risk = get_risk(perm)
    note = SAFETY_NOTES.get(perm, "")
    print(f"{perm:<12} risk={risk}  {note}")
```

### 7.6 Use with Octal Values

```python
from security import PERMISSION_NAMES, Permission

# PERMISSION_NAMES is keyed by octal int
print(PERMISSION_NAMES[0o644])   # 'owner rw, group/other read'

# Permission is an IntEnum
print(oct(Permission.USER_RWX))  # '0o755'
```

---

## 8. Notes

### Standalone package

`security` is **not** a subpackage of `charsets`. It has its own folder at
the project root and its own `__init__.py`. You can copy it anywhere and it
will still work, because it only imports from itself and the standard library.

If you want to keep the two together, just place `security/` next to
`charsets/`:

```
project/
├── charsets/
└── security/
```

### Why no filesystem logic?

Because a database should be a database. If `analyze_path()` lives here, then
every import pulls in `os`, `stat`, and the semantics of a live filesystem.
By keeping `security/` purely data, it stays:

- **fast** — no syscalls at import time
- **safe** — no accidental file access
- **portable** — works on any OS, even those without POSIX permissions
- **testable** — pure lookups are trivial to unit-test
- **composable** — you can layer your own analysis on top

### What about `os.stat`?

Call it in your code:

```python
import os, stat
from security import (
    PERMISSION_TO_RISK, FILE_TYPE_CHARS, RISK_DESCRIPTIONS,
)

def inspect(path: str):
    st = os.lstat(path)
    mode = stat.S_IMODE(st.st_mode)
    # ... your logic ...
```

The data module gives you the values; you decide what to do with them.

### Order and deduplication

- `DANGEROUS_PERMISSIONS` keeps the order you wrote in the source.
- `ALL_KNOWN_PERMISSIONS` is deduplicated while preserving first-seen order.
- `PERMISSION_TO_RISK` uses `setdefault`, so the **first** list that mentions
  a permission wins. Order of construction: HIGH → DANGEROUS → MEDIUM → LOW.

### Directory forms

Both 9-char (`rwxrwxrwx`) and 10-char (`drwxrwxrwx`) forms are included in
`DANGEROUS_PERMISSIONS`. When comparing against `os.stat` output, strip the
leading type character first.

### Extending the data

Just edit `data.py`. The helpers read from it automatically. No registration,
no decorators, no plugin system.

---

## 9. License

MIT License.

Copyright © 2024–2026 — security contributors.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.