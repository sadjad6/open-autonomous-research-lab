"""Skill: Gradient Boosting"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Gradient Boosting."""

    @property
    def name(self) -> str:
        return "gradient_boosting"

    @property
    def domain(self) -> str:
        return "machine_learning"

    @property
    def description(self) -> str:
        return "Train gradient boosting models"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the gradient_boosting skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for gradient_boosting."""
        return {"skill": "gradient_boosting", "status": "executed", "input_keys": list(data.keys())}
