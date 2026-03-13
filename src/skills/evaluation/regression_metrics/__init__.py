"""Skill: Regression Metrics"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Regression Metrics."""

    @property
    def name(self) -> str:
        return "regression_metrics"

    @property
    def domain(self) -> str:
        return "evaluation"

    @property
    def description(self) -> str:
        return "Compute regression evaluation metrics"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the regression_metrics skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for regression_metrics."""
        return {"skill": "regression_metrics", "status": "executed", "input_keys": list(data.keys())}
