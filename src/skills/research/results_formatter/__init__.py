"""Skill: Results Formatter"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Results Formatter."""

    @property
    def name(self) -> str:
        return "results_formatter"

    @property
    def domain(self) -> str:
        return "research"

    @property
    def description(self) -> str:
        return "Format analysis results for presentation"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the results_formatter skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for results_formatter."""
        return {"skill": "results_formatter", "status": "executed", "input_keys": list(data.keys())}
