"""Skill: Excel Loader"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Excel Loader."""

    @property
    def name(self) -> str:
        return "excel_loader"

    @property
    def domain(self) -> str:
        return "data_engineering"

    @property
    def description(self) -> str:
        return "Load Excel files into DataFrames"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the excel_loader skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for excel_loader."""
        return {"skill": "excel_loader", "status": "executed", "input_keys": list(data.keys())}
