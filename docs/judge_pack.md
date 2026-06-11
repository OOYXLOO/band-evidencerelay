# EvidenceRelay Band Judge Pack

## One-Sentence Hook

EvidenceRelay Band is a verifier-gated multi-agent incident-response room: triage, verification, response, and communications agents collaborate, but response actions stay blocked until evidence-backed claims pass a verifier gate.

## Evaluator Matrix

| Criterion | Evidence |
| --- | --- |
| Multi-agent collaboration | Four named agents share one room transcript with mentions, handoffs, and role-specific responsibilities. |
| Band fit | The live target is a Band room where agents exchange context, preserve a durable transcript, and make approval gates visible. |
| Working demo | Public static simulator: https://ooyxloo.github.io/band-evidencerelay/ |
| Technical proof | `build/transcript.json` records agent messages, evidence references, tool references, and the human approval gate. |
| Safety boundary | The current package is a Band-compatible simulator and does not claim live Band API usage before account/API access exists. |
| Upload assets | `docs/cover.png`, `docs/video_script.md`, `docs/evidencerelay-band-pitch.pptx`, and this judge pack. |

## Why It Is Different

Most multi-agent demos optimize for autonomy. EvidenceRelay Band optimizes for accountable autonomy: the agents can move quickly, but a confirmed incident-response claim cannot drive action unless the Verifier Agent can cite evidence IDs, tool-call IDs, and manifest state.

## Live Band Upgrade Path

The simulator transport is intentionally isolated. After lablab/Band access is available, replace the local room transport with the real Band room/message adapter while preserving the transcript schema, verifier gate, and human approval boundary.

## Honest Boundary

No passwords, OTPs, API keys, payout data, tax data, KYC data, or private incident data are stored in this repository. Real Band execution should be claimed only after it is visible in the demo or official platform proof.
