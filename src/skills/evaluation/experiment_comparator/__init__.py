"""Skill: Experiment Comparator"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Experiment Comparator."""

    @property
    def name(self) -> str:
        return "experiment_comparator"

    @property
    def domain(self) -> str:
        return "evaluation"

    @property
    def description(self) -> str:
        return "Compare multiple experiments side-by-side"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the experiment_comparator skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for experiment_comparator."""
        return {"skill": "experiment_comparator", "status": "executed", "input_keys": list(data.keys())}
