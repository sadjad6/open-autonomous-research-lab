"""Skill: Accuracy Evaluator"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Accuracy Evaluator."""

    @property
    def name(self) -> str:
        return "accuracy_evaluator"

    @property
    def domain(self) -> str:
        return "evaluation"

    @property
    def description(self) -> str:
        return "Compute classification accuracy metrics"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the accuracy_evaluator skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for accuracy_evaluator."""
        return {"skill": "accuracy_evaluator", "status": "executed", "input_keys": list(data.keys())}
