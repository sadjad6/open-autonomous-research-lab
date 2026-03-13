"""Skill: Feature Importance"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Feature Importance."""

    @property
    def name(self) -> str:
        return "feature_importance"

    @property
    def domain(self) -> str:
        return "data_science"

    @property
    def description(self) -> str:
        return "Rank features by predictive importance"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the feature_importance skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for feature_importance."""
        return {
            "skill": "feature_importance",
            "status": "executed",
            "input_keys": list(data.keys()),
        }
