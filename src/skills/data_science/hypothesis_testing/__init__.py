"""Skill: Hypothesis Testing"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Hypothesis Testing."""

    @property
    def name(self) -> str:
        return "hypothesis_testing"

    @property
    def domain(self) -> str:
        return "data_science"

    @property
    def description(self) -> str:
        return "Formulate and test research hypotheses"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the hypothesis_testing skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for hypothesis_testing."""
        return {"skill": "hypothesis_testing", "status": "executed", "input_keys": list(data.keys())}
