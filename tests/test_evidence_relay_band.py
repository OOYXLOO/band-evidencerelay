from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from evidence_relay_band.render import render_html
from evidence_relay_band.render import render_submission_summary
from evidence_relay_band.simulator import simulate_room
from evidence_relay_band.simulator import write_transcript


ROOT = Path(__file__).resolve().parents[1]
EVIDENCELOCK = ROOT.parent / "evidencelock-sift"


class EvidenceRelayBandTests(unittest.TestCase):
    def test_simulator_has_required_agent_collaboration_shape(self) -> None:
        transcript = simulate_room(EVIDENCELOCK)

        self.assertEqual(transcript.mode, "band-compatible-simulator")
        self.assertGreaterEqual(len(transcript.agents), 3)
        senders = {message.sender for message in transcript.messages}
        self.assertIn("triage", senders)
        self.assertIn("verifier", senders)
        self.assertIn("response", senders)
        self.assertTrue(any(message.approval_gate for message in transcript.messages))
        self.assertTrue(any("pending-user-gate" in transcript.live_band_status for _ in [0]))

    def test_verifier_gate_precedes_response_action(self) -> None:
        transcript = simulate_room(EVIDENCELOCK)
        verifier_step = next(
            message.step
            for message in transcript.messages
            if message.message_type == "verification_gate"
        )
        response_step = next(
            message.step
            for message in transcript.messages
            if message.message_type == "response_plan"
        )
        self.assertLess(verifier_step, response_step)

    def test_outputs_are_written_and_rendered(self) -> None:
        transcript = simulate_room(EVIDENCELOCK)
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            transcript_path = write_transcript(transcript, out)
            html_path = render_html(transcript, out)
            summary_path = render_submission_summary(transcript, out)

            payload = json.loads(transcript_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["project"], "EvidenceRelay Band")
            self.assertIn("EvidenceRelay Band Demo", html_path.read_text(encoding="utf-8"))
            self.assertIn("Submission Assets", html_path.read_text(encoding="utf-8"))
            self.assertIn("docs/judge_pack.md", html_path.read_text(encoding="utf-8"))
            self.assertIn("docs/evidencerelay-band-pitch.pptx", html_path.read_text(encoding="utf-8"))
            self.assertIn("github.com/OOYXLOO/band-evidencerelay", html_path.read_text(encoding="utf-8"))
            self.assertIn("Band-compatible simulator", summary_path.read_text(encoding="utf-8"))

    def test_submission_assets_are_present(self) -> None:
        for relative in [
            "docs/cover.png",
            "docs/cover.svg",
            "docs/video_script.md",
            "docs/pitch_deck.md",
            "docs/evidencerelay-band-pitch.pptx",
            "docs/judge_pack.md",
            "docs/submission_checklist.md",
        ]:
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_no_secret_words_in_generated_transcript(self) -> None:
        transcript = simulate_room(EVIDENCELOCK)
        text = json.dumps(transcript.to_dict()).lower()
        for forbidden in ["password", "api key", "otp", "tax", "kyc"]:
            self.assertNotIn(forbidden, text)


if __name__ == "__main__":
    unittest.main()
