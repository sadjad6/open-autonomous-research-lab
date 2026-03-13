"""Abstract base skill and related types."""

from __future__ import annotations

import abc
from dataclasses import dataclass, field
from typing import Any

from src.agents.base.types import _new_id


@dataclass
class SkillInput:
    """Standard input envelope for a skill."""

    data: dict[str, Any] = field(default_factory=dict)
    parameters: dict[str, Any] = field(default_factory=dict)
    context: dict[str, Any] = field(default_factory=dict)


@dataclass
class SkillOutput:
    """Standard output envelope from a skill."""

    success: bool = True
    data: dict[str, Any] = field(default_factory=dict)
    artifacts: list[str] = field(default_factory=list)
    metrics: dict[str, float] = field(default_factory=dict)
    error: str | None = None


class BaseSkill(abc.ABC):
    """Base class for all OARL skills.

    Each skill encapsulates a single, reusable capability
    (e.g. "train a random forest", "generate a histogram").
    """

    def __init__(self) -> None:
        self.skill_id: str = _new_id()

    @property
    @abc.abstractmethod
    def name(self) -> str:
        """Human-readable skill name."""

    @property
    @abc.abstractmethod
    def domain(self) -> str:
        """Domain this skill belongs to (e.g. 'data_engineering')."""

    @property
    @abc.abstractmethod
    def description(self) -> str:
        """One-line description of what the skill does."""

    @abc.abstractmethod
    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the skill with the given input."""

    def to_dict(self) -> dict[str, str]:
        """Serialize skill metadata for discovery."""
        return {
            "skill_id": self.skill_id,
            "name": self.name,
            "domain": self.domain,
            "description": self.description,
        }
