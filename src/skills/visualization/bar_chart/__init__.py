"""Skill: Bar Chart"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Bar Chart."""

    @property
    def name(self) -> str:
        return "bar_chart"

    @property
    def domain(self) -> str:
        return "visualization"

    @property
    def description(self) -> str:
        return "Generate bar chart visualizations"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the bar_chart skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for bar_chart."""
        return {"skill": "bar_chart", "status": "executed", "input_keys": list(data.keys())}
