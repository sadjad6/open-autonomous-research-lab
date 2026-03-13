"""Skill: Precision-Recall Evaluator"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Precision-Recall Evaluator."""

    @property
    def name(self) -> str:
        return "precision_recall"

    @property
    def domain(self) -> str:
        return "evaluation"

    @property
    def description(self) -> str:
        return "Compute precision and recall metrics"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the precision_recall skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for precision_recall."""
        return {"skill": "precision_recall", "status": "executed", "input_keys": list(data.keys())}
