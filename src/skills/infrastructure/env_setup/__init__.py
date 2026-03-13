"""Skill: Environment Setup"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Environment Setup."""

    @property
    def name(self) -> str:
        return "env_setup"

    @property
    def domain(self) -> str:
        return "infrastructure"

    @property
    def description(self) -> str:
        return "Set up Python environments"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the env_setup skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for env_setup."""
        return {"skill": "env_setup", "status": "executed", "input_keys": list(data.keys())}
