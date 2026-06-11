# EvidenceRelay Band Verification

Updated: 2026-06-12 03:15 CST

## Local Checks

- `PYTHONPATH=src python -m unittest discover -s tests -v`: 5 tests passed.
- `python -m compileall -q src tests`: passed after rerunning sequentially.
- `PYTHONPATH=src python -m evidence_relay_band.cli generate --evidencelock-root ..\evidencelock-sift --out build`: generated transcript, static demo, and submission summary.
- Sensitive scan found only safety-boundary wording and the test forbidden-word list; no real credentials or private data were found.
- Editable deck exported through artifact-tool to `docs/evidencerelay-band-pitch.pptx`.
- Rendered 8 slide previews plus contact sheet; title wrapping and proof-object layout passed visual QA.

## Browser Checks

- Local demo URL checked during QA: `http://127.0.0.1:8766/`.
- Desktop check:
  - Title: `EvidenceRelay Band Demo`
  - H1 present
  - public simulator eyebrow present
  - 3 evaluator proof cards present
  - 7 submission asset links present, including judge pack and editable slide deck
  - simulator boundary present
  - approval gate present
  - no horizontal overflow
  - no console errors
- Mobile 390px check:
  - no horizontal overflow
  - proof, metric, and agent sections collapse to one column
  - 7 submission asset links present
  - no console errors

## Current Boundary

This is not yet a live Band submission. It is a verified public simulator package that can be upgraded when lablab/Band enrollment and API/account access are available.
