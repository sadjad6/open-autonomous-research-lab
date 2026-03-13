"""Skill: Research Planner"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Research Planner."""

    @property
    def name(self) -> str:
        return "research_planner"

    @property
    def domain(self) -> str:
        return "research"

    @property
    def description(self) -> str:
        return "Plan research investigations"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the research_planner skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for research_planner."""
        return {"skill": "research_planner", "status": "executed", "input_keys": list(data.keys())}
