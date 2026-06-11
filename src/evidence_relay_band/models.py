from __future__ import annotations

from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass(frozen=True)
class Agent:
    agent_id: str
    name: str
    role: str
    responsibility: str


@dataclass(frozen=True)
class RoomMessage:
    step: int
    sender: str
    message_type: str
    text: str
    mentions: list[str] = field(default_factory=list)
    evidence_refs: list[str] = field(default_factory=list)
    tool_refs: list[str] = field(default_factory=list)
    approval_gate: bool = False

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class RoomTranscript:
    project: str
    mode: str
    source_case: str
    agents: list[Agent]
    messages: list[RoomMessage]
    live_band_status: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "project": self.project,
            "mode": self.mode,
            "source_case": self.source_case,
            "live_band_status": self.live_band_status,
            "agents": [asdict(agent) for agent in self.agents],
            "messages": [message.to_dict() for message in self.messages],
        }
