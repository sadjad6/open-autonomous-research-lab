"""Skill: Data Storyteller"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Data Storyteller."""

    @property
    def name(self) -> str:
        return "data_storyteller"

    @property
    def domain(self) -> str:
        return "research"

    @property
    def description(self) -> str:
        return "Create compelling data narratives"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the data_storyteller skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for data_storyteller."""
        return {"skill": "data_storyteller", "status": "executed", "input_keys": list(data.keys())}
