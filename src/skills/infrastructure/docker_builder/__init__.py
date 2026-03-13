"""Skill: Docker Builder"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Docker Builder."""

    @property
    def name(self) -> str:
        return "docker_builder"

    @property
    def domain(self) -> str:
        return "infrastructure"

    @property
    def description(self) -> str:
        return "Build Docker images for deployment"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the docker_builder skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for docker_builder."""
        return {"skill": "docker_builder", "status": "executed", "input_keys": list(data.keys())}
