from __future__ import annotations

import json
from pathlib import Path

from evidence_relay_band.evidencelock import load_evidence_bundle
from evidence_relay_band.models import Agent
from evidence_relay_band.models import RoomMessage
from evidence_relay_band.models import RoomTranscript


AGENTS = [
    Agent(
        agent_id="triage",
        name="Triage Agent",
        role="Evidence summarizer",
        responsibility="Extracts timeline, suspicious behaviors, MITRE hints, and open questions.",
    ),
    Agent(
        agent_id="verifier",
        name="Verifier Agent",
        role="Claim gatekeeper",
        responsibility="Blocks confirmed findings unless evidence IDs, tool-call IDs, and manifest state are present.",
    ),
    Agent(
        agent_id="response",
        name="Response Lead Agent",
        role="Action planner",
        responsibility="Converts verified findings into prioritized analyst actions and human approval gates.",
    ),
    Agent(
        agent_id="comms",
        name="Comms Agent",
        role="Executive summary writer",
        responsibility="Writes a non-sensitive summary only after verifier approval.",
    ),
]


def _finding_summary(finding: dict) -> str:
    mitre = ", ".join(finding.get("mitre_techniques", [])) or "none"
    evidence = finding.get("evidence_refs", [{}])[0].get("evidence_id", "missing")
    tool = finding.get("tool_refs", [{}])[0].get("command_id", "missing")
    return f"{finding['finding_id']} {finding['title']} maps to {mitre}, cites {evidence}, and uses tool call {tool}."


def simulate_room(evidencelock_root: Path) -> RoomTranscript:
    bundle = load_evidence_bundle(evidencelock_root)
    findings = bundle["findings"]
    evidence_count = len(bundle["manifest"].get("evidence", []))
    output_count = len(bundle["manifest"].get("outputs", []))
    finding_lines = [_finding_summary(finding) for finding in findings]
    missing_refs = [
        finding["finding_id"]
        for finding in findings
        if not finding.get("evidence_refs") or not finding.get("tool_refs")
    ]
    verifier_status = (
        "approved: all confirmed findings have evidence and tool references"
        if not missing_refs
        else "blocked: missing references for " + ", ".join(missing_refs)
    )

    messages = [
        RoomMessage(
            step=1,
            sender="triage",
            message_type="context_handoff",
            text=f"Loaded case {bundle['case_id']} with {len(findings)} confirmed findings, {evidence_count} evidence artifact, and {output_count} hashed outputs.",
            mentions=["verifier", "response"],
        ),
        RoomMessage(
            step=2,
            sender="triage",
            message_type="finding_digest",
            text="; ".join(finding_lines),
            mentions=["verifier"],
            evidence_refs=[
                ref["evidence_id"]
                for finding in findings
                for ref in finding.get("evidence_refs", [])
            ],
            tool_refs=[
                ref["command_id"]
                for finding in findings
                for ref in finding.get("tool_refs", [])
            ],
        ),
        RoomMessage(
            step=3,
            sender="verifier",
            message_type="verification_gate",
            text=verifier_status + "; manifest verification is expected to return ok=true before any incident response action is published.",
            mentions=["response", "comms"],
            evidence_refs=[
                entry["evidence_id"]
                for entry in bundle["manifest"].get("evidence", [])
            ],
        ),
        RoomMessage(
            step=4,
            sender="response",
            message_type="response_plan",
            text="Prioritize PowerShell process-tree collection, service binary preservation, lateral search for matching indicators, and a human approval gate before isolation.",
            mentions=["comms"],
            approval_gate=True,
        ),
        RoomMessage(
            step=5,
            sender="comms",
            message_type="executive_summary",
            text="Two verifier-backed behaviors need analyst review: encoded PowerShell from a document process and temp-path service persistence. No private data is included in this summary.",
            mentions=["triage", "verifier", "response"],
        ),
    ]
    return RoomTranscript(
        project="EvidenceRelay Band",
        mode="band-compatible-simulator",
        source_case=bundle["case_id"],
        agents=AGENTS,
        messages=messages,
        live_band_status="pending-user-gate: lablab/Band account access required before claiming real Band execution",
    )


def write_transcript(transcript: RoomTranscript, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "transcript.json"
    path.write_text(json.dumps(transcript.to_dict(), indent=2), encoding="utf-8")
    return path
