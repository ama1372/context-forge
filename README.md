# PROJECT_CONTEXT

A single-document protocol for building software with an AI (DeepSeek, Claude, GPT, Gemini). Every AI message is a code patch + a context patch. Everything travels through `_work/input.txt` and `_work/output.txt`, applied by one tool: `run.py`.

<p align="center">
  <b>English</b> ·
  <a href="README.fa.md">فارسی</a>
</p>

## What it solves

- **Chat limits.** The context is updated in every message, so a new chat can resume with just this document + a status dump.
- **Token burn.** Flags in `run.py` let the AI ask only for what it needs — `--status` is ~300 bytes, `--file X` is a few KB.
- **Anchor drift.** Fuzzy matching + hash verification keep patches valid even after edits.
- **Account blocking.** MSG-SEED + batching + time spacing keep the account safe.

## Files

| File | Role |
|------|------|
| `PROJECT_CONTEXT.md` | The constitution — rules, workflow, templates |
| `run.py` | The only tool — dump / apply / commit / tag |
| `_work/` | The AI communication folder |

## Quick start

    python run.py --init

Then place `PROJECT_CONTEXT.md` in the project root, open a chat with the AI, and paste the document.

The AI writes a patch. You drop it into `_work/input.txt` and run:

    python run.py

The AI's next message is built from `_work/output.txt`.

## Language

The main document is English. Translations live in sibling files:

- `PROJECT_CONTEXT.md` — English
- `PROJECT_CONTEXT.fa.md` — Persian (in progress)
- (more to come — see Section 33 in the main document)

## License

See `LICENSE`.

---

*This README is a pointer. Everything lives in `PROJECT_CONTEXT.md`.*