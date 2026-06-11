# EvidenceRelay Band

EvidenceRelay Band is a Band of Agents hackathon backup project. It turns a verified incident-response evidence bundle into a multi-agent review room with explicit handoffs, shared context, and human approval gates.

Current status: local Band-compatible simulator. It does not claim live Band API usage yet. The adapter boundary is isolated so a real Band/Codeband integration can replace the simulator when account/API access is available.

## Why This Fits Band of Agents

The workflow uses four cooperating agents:

1. `Triage Agent` summarizes evidence, timeline, and suspected MITRE techniques.
2. `Verifier Agent` checks every confirmed claim for evidence IDs, tool-call IDs, and manifest hashes.
3. `Response Lead Agent` converts verified findings into prioritized containment and investigation actions.
4. `Comms Agent` prepares a non-sensitive executive summary after verifier approval.

Band should be central to the live version: agents share a room, mention each other, hand off state, and keep a durable transcript. The local simulator models that room without credentials.

## Quick Start

```powershell
$env:PYTHONPATH="src"
python -m unittest discover -s tests -v
python -m evidence_relay_band.cli generate --evidencelock-root ..\evidencelock-sift --out build
python -m evidence_relay_band.cli serve --directory build --port 8765
```

Open `http://127.0.0.1:8765/`.

## Generated Artifacts

- `build/transcript.json`: structured multi-agent room transcript.
- `build/index.html`: static judge demo page.
- `build/submission_summary.md`: Devpost/lablab submission copy starter.
- `docs/verification.md`: local test and browser verification record.

## Integrity Boundary

- No passwords, OTPs, API keys, payout data, tax data, KYC data, or private incident data are stored.
- EvidenceRelay reads only public/local EvidenceLock reports.
- A finding does not reach response actions until the Verifier Agent cites evidence, tool calls, and manifest state.
- Real Band integration is a future gate; the current package is honest simulator evidence.

## Human Gates

- lablab.ai enrollment.
- Band/Codeband access.
- Any Band API key or partner API key.
- Public repository creation and final lablab submission.
- Hosted demo deployment if required.
