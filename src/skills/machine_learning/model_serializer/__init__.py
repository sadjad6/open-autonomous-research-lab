"""Skill: Model Serializer"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Model Serializer."""

    @property
    def name(self) -> str:
        return "model_serializer"

    @property
    def domain(self) -> str:
        return "machine_learning"

    @property
    def description(self) -> str:
        return "Save and load trained models"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the model_serializer skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for model_serializer."""
        return {"skill": "model_serializer", "status": "executed", "input_keys": list(data.keys())}
