"""Skill: Model Selector"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Model Selector."""

    @property
    def name(self) -> str:
        return "model_selector"

    @property
    def domain(self) -> str:
        return "machine_learning"

    @property
    def description(self) -> str:
        return "Compare and select the best model"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the model_selector skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for model_selector."""
        return {"skill": "model_selector", "status": "executed", "input_keys": list(data.keys())}
