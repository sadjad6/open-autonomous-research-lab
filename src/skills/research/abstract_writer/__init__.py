"""Skill: Abstract Writer"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Abstract Writer."""

    @property
    def name(self) -> str:
        return "abstract_writer"

    @property
    def domain(self) -> str:
        return "research"

    @property
    def description(self) -> str:
        return "Generate research abstracts"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the abstract_writer skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for abstract_writer."""
        return {"skill": "abstract_writer", "status": "executed", "input_keys": list(data.keys())}
