"""Skill: Fairness Checker"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Fairness Checker."""

    @property
    def name(self) -> str:
        return "fairness_checker"

    @property
    def domain(self) -> str:
        return "evaluation"

    @property
    def description(self) -> str:
        return "Check model fairness across groups"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the fairness_checker skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for fairness_checker."""
        return {"skill": "fairness_checker", "status": "executed", "input_keys": list(data.keys())}
