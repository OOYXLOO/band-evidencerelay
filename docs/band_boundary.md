# Band Integration Boundary

EvidenceRelay Band currently uses a local room simulator because live Band/lablab access is human-gated.

## Simulator Contract

The simulator models the parts that matter for judging:

- named agents
- room messages
- mentions
- shared evidence context
- verifier gate
- human approval gate
- durable transcript JSON

## Live Upgrade Path

When account/API access exists, replace only the transport layer:

1. Create or join a real Band room.
2. Send each `RoomMessage` as a Band room message or agent event.
3. Preserve `sender`, `mentions`, `message_type`, `evidence_refs`, `tool_refs`, and `approval_gate`.
4. Export the Band transcript URL or screenshots.
5. Keep the local JSON transcript as reproducibility evidence.

## No-Claim Boundary

Until that live path is complete, public copy must say "Band-compatible simulator" rather than "live Band integration."
