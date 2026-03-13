"""Skill: Dimensionality Reduction"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Dimensionality Reduction."""

    @property
    def name(self) -> str:
        return "dimensionality_reduction"

    @property
    def domain(self) -> str:
        return "data_science"

    @property
    def description(self) -> str:
        return "Reduce feature space using PCA or t-SNE"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the dimensionality_reduction skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for dimensionality_reduction."""
        return {
            "skill": "dimensionality_reduction",
            "status": "executed",
            "input_keys": list(data.keys()),
        }
