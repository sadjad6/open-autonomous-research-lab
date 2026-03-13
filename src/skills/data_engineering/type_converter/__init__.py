"""Skill: Type Converter"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Type Converter."""

    @property
    def name(self) -> str:
        return "type_converter"

    @property
    def domain(self) -> str:
        return "data_engineering"

    @property
    def description(self) -> str:
        return "Convert column data types"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the type_converter skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for type_converter."""
        return {"skill": "type_converter", "status": "executed", "input_keys": list(data.keys())}
