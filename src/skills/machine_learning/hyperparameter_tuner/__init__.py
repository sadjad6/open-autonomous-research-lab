"""Skill: Hyperparameter Tuner"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Hyperparameter Tuner."""

    @property
    def name(self) -> str:
        return "hyperparameter_tuner"

    @property
    def domain(self) -> str:
        return "machine_learning"

    @property
    def description(self) -> str:
        return "Optimize model hyperparameters"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the hyperparameter_tuner skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for hyperparameter_tuner."""
        return {"skill": "hyperparameter_tuner", "status": "executed", "input_keys": list(data.keys())}
