"""Skill: Report Writer"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Report Writer."""

    @property
    def name(self) -> str:
        return "report_writer"

    @property
    def domain(self) -> str:
        return "research"

    @property
    def description(self) -> str:
        return "Generate structured research reports"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the report_writer skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for report_writer."""
        return {"skill": "report_writer", "status": "executed", "input_keys": list(data.keys())}
