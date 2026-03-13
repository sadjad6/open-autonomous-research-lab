"""Skill: Paper Searcher"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Paper Searcher."""

    @property
    def name(self) -> str:
        return "paper_searcher"

    @property
    def domain(self) -> str:
        return "research"

    @property
    def description(self) -> str:
        return "Search for relevant academic papers"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the paper_searcher skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for paper_searcher."""
        return {"skill": "paper_searcher", "status": "executed", "input_keys": list(data.keys())}
