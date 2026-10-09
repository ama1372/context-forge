# Contributing to context-forge

Thanks for wanting to help. This project is intentionally small — a single rule document plus one Python tool — so the contribution surface is small too.

## What we welcome

- **README translations.** New languages are always welcome. Copy `README.md`, translate, keep the language bar at the top consistent.
- **Bug reports** on `run.py` or on the rule document.
- **Typo and clarity fixes** in `PROJECT_CONTEXT.en.md`.
- **New flags** for `run.py` if they're clearly useful (open an issue first).

## What we don't accept

- **Translated rule documents** (`PROJECT_CONTEXT.<lang>.md`). See Section 33 of the rule document — the rule document stays English-only.
- **Rewrites of the rule document.** It is stable. Patches only.
- **Large refactors of `run.py`** without an issue first.

## How to submit

1. **Open an issue** describing what you want to change and why.
2. **Fork, branch, patch.** Keep the change focused.
3. **Test locally:**
   ```
   python run.py --version
   python run.py --capabilities
   python run.py --check-md
   ```
4. **Open a PR** with a clear description and a reference to the issue.

## Adding a README translation

1. Copy `README.md` to `README.<lang>.md` (`<lang>` = ISO 639-1 code).
2. Translate the prose. **Do not translate** file names, commands, tag names, or code.
3. Add the new language to the language bar in **all** existing README files (the script `_work/fix_bars.py` can help — see the top of the file for the LANGS list).
4. Open a PR. One language per PR is fine.

## Code style

- Python: PEP 8, 4-space indent, max ~100 columns.
- English only for file names, tags, commands, code identifiers.
- Commit messages: one line, imperative, emoji-friendly (`✨`, `🐛`, `🌍`, `🔧`, `🧹`, `📘`, `📝`).

## License

By contributing, you agree your work is licensed under the MIT License (see `LICENSE`).