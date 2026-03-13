"""Skill: Insight Extractor"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Insight Extractor."""

    @property
    def name(self) -> str:
        return "insight_extractor"

    @property
    def domain(self) -> str:
        return "research"

    @property
    def description(self) -> str:
        return "Extract key insights from analysis results"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the insight_extractor skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for insight_extractor."""
        return {"skill": "insight_extractor", "status": "executed", "input_keys": list(data.keys())}
