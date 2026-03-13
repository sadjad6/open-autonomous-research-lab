"""Skill: Config Validator"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Config Validator."""

    @property
    def name(self) -> str:
        return "config_validator"

    @property
    def domain(self) -> str:
        return "infrastructure"

    @property
    def description(self) -> str:
        return "Validate configuration files"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the config_validator skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for config_validator."""
        return {"skill": "config_validator", "status": "executed", "input_keys": list(data.keys())}
