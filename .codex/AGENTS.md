# AGENTS.md

## Purpose

This file defines **persistent project guidance** for OpenAI Codex.  
Codex must read and follow these instructions when generating, modifying, or reviewing code in this repository.

If instructions in this file conflict with ad-hoc user prompts, **this file takes precedence unless explicitly overridden**.

---

## 1. Project Overview

**Project name:** <PROJECT NAME>  
**Primary language(s):** <e.g. Python 3.11>  
**Primary domain:** <e.g. GIS / data engineering / backend services>

**High-level goals:**
- <Brief statement of what this project exists to do>
- <Key constraints or non-goals, if any>

---

## 2. Project Structure (Authoritative)

> **NOTE:** This section is intentionally a placeholder.  
> Maintain this section as the directory structure stabilizes.

Codex should use this section to understand **where new code belongs** and **how components relate**.

```text
<repo-root>/
├─ src/
│  ├─ <module_a>/        # <purpose>
│  ├─ <module_b>/        # <purpose>
│  └─ __init__.py
├─ tests/
│  ├─ unit/
│  └─ integration/
├─ docs/
├─ scripts/
├─ .vscode/
├─ AGENTS.md
├─ README.md
└─ pyproject.toml
```

**Architectural notes (if applicable):**
- <e.g. functional-first, minimal OO>
- <e.g. no business logic in scripts/>
- <e.g. IO isolated from pure logic>

---

## 3. Coding Conventions (Must Follow)

### General
- Write **clear, explicit, readable code**
- Prefer **explicit over clever**
- Avoid unnecessary abstraction
- Favor small, composable functions
- Write for ease of reading and maintainability

### Python Standards (if applicable)
- Follow **PEP 8**
- Use **type hints** for public functions
- Prefer `pathlib` over `os.path`
- Prefer f-strings over `.format()`
- No global state unless explicitly justified

### Naming
- `snake_case` for variables and functions
- `PascalCase` for classes
- Constants in `UPPER_SNAKE_CASE`
- Avoid ambiguous abbreviations unless domain-standard

### Imports
- Standard library first
- Third-party libraries second
- If importing arcpy, use a library in arcpy where a suitable library exists
- Local imports last
- Avoid wildcard imports

---

## 4. Testing Protocols

### Framework
- No rules

### Expectations
- No rules

### Running Tests
- No rules

---

## 5. Logging & Error Handling

- Use the project’s standard logging configuration
- Do not use `print()` for operational logging
- Raise meaningful exceptions
- Fail fast on invalid inputs

---

## 6. Dependency Management

- Do not introduce new dependencies without justification
- Prefer existing libraries already in use
- Document any new dependency in:
  - `pyproject.toml`
  - `README.md` (if user-facing)

---

## 7. Git & Pull Request (PR) Guidelines

### Commit Messages
- **Use the commit message template defined in `.gitmessages`**
- Keep commits focused and atomic
- Do not mix formatting changes with logic changes

### Branch Naming
```
feature/<short-description>
fix/<short-description>
refactor/<short-description>
```

### Pull Requests Must Include
- Clear description of **what changed and why**
- Reference to related issue/ticket (if applicable)
- Notes on testing performed
- Any known limitations or follow-ups

Codex should **follow these conventions when generating PR descriptions or commit messages**.

---

## 8. What Codex Should NOT Do

- Do not reformat unrelated files
- Do not introduce new architectural patterns unprompted
- Do not remove existing functionality unless explicitly instructed
- Do not assume undocumented behavior

---

## 9. When in Doubt

If requirements are unclear:
1. Ask a clarifying question **before** generating code
2. State assumptions explicitly
3. Prefer the simplest viable solution

---

## End of Instructions
