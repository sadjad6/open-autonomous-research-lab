"""Skill: Model Drift Detector"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Model Drift Detector."""

    @property
    def name(self) -> str:
        return "model_drift_detector"

    @property
    def domain(self) -> str:
        return "evaluation"

    @property
    def description(self) -> str:
        return "Detect data or concept drift"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the model_drift_detector skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for model_drift_detector."""
        return {
            "skill": "model_drift_detector",
            "status": "executed",
            "input_keys": list(data.keys()),
        }
