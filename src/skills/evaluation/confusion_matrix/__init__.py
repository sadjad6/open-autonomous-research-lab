"""Skill: Confusion Matrix"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Confusion Matrix."""

    @property
    def name(self) -> str:
        return "confusion_matrix"

    @property
    def domain(self) -> str:
        return "evaluation"

    @property
    def description(self) -> str:
        return "Generate confusion matrices"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the confusion_matrix skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for confusion_matrix."""
        return {"skill": "confusion_matrix", "status": "executed", "input_keys": list(data.keys())}
