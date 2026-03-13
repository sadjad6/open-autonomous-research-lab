"""Skill: Methodology Writer"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Methodology Writer."""

    @property
    def name(self) -> str:
        return "methodology_writer"

    @property
    def domain(self) -> str:
        return "research"

    @property
    def description(self) -> str:
        return "Write methodology sections for reports"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the methodology_writer skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for methodology_writer."""
        return {"skill": "methodology_writer", "status": "executed", "input_keys": list(data.keys())}
