"""Skill: Data Merger"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Data Merger."""

    @property
    def name(self) -> str:
        return "data_merger"

    @property
    def domain(self) -> str:
        return "data_engineering"

    @property
    def description(self) -> str:
        return "Merge multiple DataFrames"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the data_merger skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for data_merger."""
        return {"skill": "data_merger", "status": "executed", "input_keys": list(data.keys())}
