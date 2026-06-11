# EvidenceRelay Band Video Script

Target length: 90 seconds.

## Opening

EvidenceRelay Band is a verifier-gated incident-response room for high-stakes teams. Four agents collaborate around the same evidence bundle, but no response action is published until the Verifier Agent approves the claim trail.

## Scene 1: The Room

Show the demo page. Point out the four roles:

- Triage Agent
- Verifier Agent
- Response Lead Agent
- Comms Agent

Each agent has a specific responsibility, shared context, and a transcript entry.

## Scene 2: Evidence Handoff

Show the first two transcript messages. The Triage Agent loads the EvidenceLock case, summarizes the suspicious behaviors, and mentions the Verifier Agent.

## Scene 3: Verification Gate

Show the Verifier Agent message. The key product point is that confirmed findings must include evidence IDs, tool-call IDs, and manifest state before the Response Lead Agent can proceed.

## Scene 4: Human Approval

Show the Response Lead Agent action plan. The plan includes a human approval gate before containment or isolation, so the workflow is appropriate for regulated or high-stakes response.

## Scene 5: Honest Boundary

Close by showing the boundary section:

This is currently a Band-compatible simulator. It does not claim live Band API usage yet. Once lablab/Band access is available, the simulator transport can be replaced with the real room adapter while keeping the verifier gate and transcript model.

