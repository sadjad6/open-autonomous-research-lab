"""Skill: Resource Monitor"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Resource Monitor."""

    @property
    def name(self) -> str:
        return "resource_monitor"

    @property
    def domain(self) -> str:
        return "infrastructure"

    @property
    def description(self) -> str:
        return "Monitor CPU, memory, and disk usage"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the resource_monitor skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for resource_monitor."""
        return {"skill": "resource_monitor", "status": "executed", "input_keys": list(data.keys())}
