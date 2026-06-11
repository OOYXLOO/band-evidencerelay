# EvidenceRelay Band Submission Pack

Use this only after lablab/Band enrollment is available.

## Project Title

EvidenceRelay Band

## Short Description

A verifier-gated multi-agent incident-response room where triage, verification, response, and communications agents coordinate around evidence before any action is approved.

## Long Description

EvidenceRelay Band turns an incident-response evidence bundle into a multi-agent room. The Triage Agent summarizes timeline and MITRE technique signals, the Verifier Agent blocks unsupported confirmed claims, the Response Lead Agent creates prioritized actions after verification, and the Comms Agent writes a non-sensitive executive summary.

The current package is a Band-compatible simulator. It proves agent roles, shared context, message handoffs, verifier gating, and human approval gates without storing credentials or claiming live Band API usage before account access exists.

## Tags

multi-agent, incident-response, DFIR, enterprise-workflow, high-stakes-ai, verification

## Links To Fill

- Public GitHub repository: https://github.com/OOYXLOO/band-evidencerelay
- Demo app URL: https://ooyxloo.github.io/band-evidencerelay/
- Video presentation: pending
- Slide deck: pending

## Local Assets Ready For Upload

- Cover image: `docs/cover.png`
- Cover image source: `docs/cover.svg`
- Video script: `docs/video_script.md`
- Pitch deck outline: `docs/pitch_deck.md`
- Submission checklist: `docs/submission_checklist.md`
- Local demo page: `build/index.html`

## Demo Script

1. Show the four agents in the room.
2. Show Triage Agent loading the EvidenceLock case and findings.
3. Show Verifier Agent approving only evidence-backed claims.
4. Show Response Lead Agent creating actions after the verifier gate.
5. Show Comms Agent preparing a non-sensitive summary.
6. Close with the boundary: live Band integration waits for user-gated access.

## Judge Hook

Most multi-agent demos optimize for autonomy. EvidenceRelay Band optimizes for accountable autonomy: the agents can triage, verify, plan, and communicate, but the response step stays blocked until claims are evidence-backed and a human approval gate is visible.
