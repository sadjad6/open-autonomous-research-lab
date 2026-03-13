"""Skill: Statistical Testing"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Statistical Testing."""

    @property
    def name(self) -> str:
        return "statistical_testing"

    @property
    def domain(self) -> str:
        return "data_science"

    @property
    def description(self) -> str:
        return "Perform hypothesis tests (t-test, chi-square, etc.)"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the statistical_testing skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for statistical_testing."""
        return {
            "skill": "statistical_testing",
            "status": "executed",
            "input_keys": list(data.keys()),
        }
