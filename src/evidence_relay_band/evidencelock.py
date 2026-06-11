from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_evidence_bundle(root: Path) -> dict[str, Any]:
    reports = root / "reports"
    manifest_path = reports / "integrity_manifest.json"
    investigation_path = reports / "investigation_report.json"
    analyst_handoff_path = reports / "analyst_handoff.md"
    timeline_path = reports / "timeline_report.md"

    missing = [
        str(path)
        for path in [manifest_path, investigation_path, analyst_handoff_path, timeline_path]
        if not path.is_file()
    ]
    if missing:
        raise FileNotFoundError("Missing EvidenceLock artifacts: " + ", ".join(missing))

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    investigation = json.loads(investigation_path.read_text(encoding="utf-8"))
    return {
        "case_id": investigation["case_id"],
        "title": investigation["title"],
        "findings": investigation["findings"],
        "manifest": manifest,
        "analyst_handoff": analyst_handoff_path.read_text(encoding="utf-8"),
        "timeline": timeline_path.read_text(encoding="utf-8"),
    }
