"""Skill: SQL Loader"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for SQL Loader."""

    @property
    def name(self) -> str:
        return "sql_loader"

    @property
    def domain(self) -> str:
        return "data_engineering"

    @property
    def description(self) -> str:
        return "Load data from SQL databases"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the sql_loader skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for sql_loader."""
        return {"skill": "sql_loader", "status": "executed", "input_keys": list(data.keys())}
