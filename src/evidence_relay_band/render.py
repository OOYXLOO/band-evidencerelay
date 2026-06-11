from __future__ import annotations

import html
import json
from pathlib import Path

from evidence_relay_band.models import RoomTranscript

REPO_BLOB_BASE = "https://github.com/OOYXLOO/band-evidencerelay/blob/main"


def render_html(transcript: RoomTranscript, out_dir: Path) -> Path:
    data = transcript.to_dict()
    agent_tiles = "\n".join(
        f"<article class=\"tile\"><h3>{html.escape(agent['name'])}</h3><p>{html.escape(agent['responsibility'])}</p><span>{html.escape(agent['role'])}</span></article>"
        for agent in data["agents"]
    )
    message_rows = "\n".join(
        f"<li><b>{message['step']:02d} {html.escape(message['sender'])}</b><span>{html.escape(message['message_type'])}</span><p>{html.escape(message['text'])}</p></li>"
        for message in data["messages"]
    )
    payload = html.escape(json.dumps(data, indent=2))
    page = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>EvidenceRelay Band Demo</title>
  <style>
    :root {{ color-scheme: light; --ink: #17202a; --muted: #536273; --line: #d7dde5; --paper: #ffffff; --wash: #f4f7fa; --blue: #2563eb; --green: #047857; --amber: #b45309; }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; font-family: Arial, Helvetica, sans-serif; color: var(--ink); background: var(--wash); }}
    main {{ width: min(1120px, calc(100% - 32px)); margin: 0 auto; padding: 42px 0 64px; }}
    h1 {{ max-width: 880px; margin: 0; font-size: clamp(34px, 5vw, 58px); line-height: 1.06; letter-spacing: 0; }}
    .eyebrow {{ margin: 0 0 12px; color: var(--blue); font-size: 14px; font-weight: 700; text-transform: uppercase; letter-spacing: 0; }}
    .dek {{ max-width: 820px; margin: 18px 0 0; color: var(--muted); font-size: 18px; line-height: 1.6; }}
    .metrics {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px; margin-top: 28px; }}
    .metric, .tile, .panel {{ min-width: 0; background: var(--paper); border: 1px solid var(--line); padding: 18px; }}
    .metric strong {{ display: block; color: var(--green); font-size: 32px; margin-bottom: 8px; }}
    .grid {{ min-width: 0; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 18px; margin-top: 28px; }}
    .agents {{ min-width: 0; display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px; margin-top: 28px; }}
    .tile h3 {{ margin: 0 0 8px; font-size: 18px; }}
    .tile p, .metric span, li p, .panel p {{ color: var(--muted); line-height: 1.55; }}
    .tile span {{ color: var(--blue); font-weight: 700; font-size: 13px; }}
    ol {{ margin: 0; padding-left: 20px; }}
    li {{ margin-bottom: 14px; }}
    li b {{ display: block; }}
    li span {{ color: var(--amber); font-size: 13px; font-weight: 700; }}
    pre {{ max-width: 100%; overflow-x: auto; margin: 0; padding: 16px; background: #17202a; color: #eff6ff; font-size: 13px; line-height: 1.45; }}
    .assets a {{ color: var(--blue); font-weight: 700; text-decoration: none; }}
    .assets li {{ margin-bottom: 10px; }}
    @media (max-width: 920px) {{ .agents {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }} }}
    @media (max-width: 780px) {{ .metrics, .grid, .agents {{ grid-template-columns: 1fr; }} }}
  </style>
</head>
<body>
  <main>
    <p class="eyebrow">Band of Agents backup submission</p>
    <h1>EvidenceRelay Band shows four agents coordinating a verified incident-response handoff.</h1>
    <p class="dek">This is a Band-compatible simulator: it proves the room model, shared context, handoffs, verifier gate, and human approval boundary while real Band account/API access remains gated.</p>
    <section class="metrics">
      <div class="metric"><strong>{len(data['agents'])}</strong><span>cooperating agents</span></div>
      <div class="metric"><strong>{len(data['messages'])}</strong><span>room messages and handoffs</span></div>
      <div class="metric"><strong>2</strong><span>verified incident findings</span></div>
      <div class="metric"><strong>1</strong><span>human approval gate before response action</span></div>
    </section>
    <section class="agents" aria-label="Agent roles">{agent_tiles}</section>
    <section class="grid">
      <div class="panel">
        <h2>Room Timeline</h2>
        <ol>{message_rows}</ol>
      </div>
      <div class="panel">
        <h2>Boundary</h2>
        <p>{html.escape(data['live_band_status'])}</p>
        <p>Submission assets are ready locally: cover image, video script, pitch deck outline, and final checklist.</p>
      </div>
      <div class="panel assets">
        <h2>Submission Assets</h2>
        <ol>
          <li><a href="{REPO_BLOB_BASE}/docs/cover.png">Cover image</a></li>
          <li><a href="{REPO_BLOB_BASE}/docs/cover.svg">Cover image source</a></li>
          <li><a href="{REPO_BLOB_BASE}/docs/video_script.md">Video script</a></li>
          <li><a href="{REPO_BLOB_BASE}/docs/pitch_deck.md">Pitch deck outline</a></li>
          <li><a href="{REPO_BLOB_BASE}/docs/submission_checklist.md">Submission checklist</a></li>
        </ol>
      </div>
      <div class="panel">
        <h2>Transcript JSON</h2>
        <pre>{payload}</pre>
      </div>
    </section>
  </main>
</body>
</html>
"""
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "index.html"
    path.write_text(page, encoding="utf-8")
    return path


def render_submission_summary(transcript: RoomTranscript, out_dir: Path) -> Path:
    lines = [
        "# EvidenceRelay Band Submission Summary",
        "",
        "EvidenceRelay Band is a multi-agent incident-response room for high-stakes workflows.",
        "",
        "## What It Demonstrates",
        "",
        "- Four agents collaborate around one verified incident-response evidence bundle.",
        "- The Verifier Agent blocks response planning until evidence IDs, tool-call IDs, and manifest state are present.",
        "- The Response Lead Agent creates actions only after verification and marks a human approval gate.",
        "- Submission assets are ready locally: cover source, video script, pitch deck outline, and checklist.",
        "- The current demo is a Band-compatible simulator, not a claim of live Band API execution.",
        "",
        "## Human-Gated Upgrade",
        "",
        "When Band account/API access is available, replace the local simulator transport with the real room/message adapter while preserving the transcript schema and verifier gate.",
    ]
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "submission_summary.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path
