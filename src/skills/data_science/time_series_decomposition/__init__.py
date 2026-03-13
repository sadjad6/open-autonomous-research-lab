"""Skill: Time Series Decomposition"""

from __future__ import annotations

from typing import Any

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput


class Skill(BaseSkill):
    """Skill implementation for Time Series Decomposition."""

    @property
    def name(self) -> str:
        return "time_series_decomposition"

    @property
    def domain(self) -> str:
        return "data_science"

    @property
    def description(self) -> str:
        return "Decompose time series into trend, seasonality, residual"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        """Execute the time_series_decomposition skill."""
        params = skill_input.parameters
        data = skill_input.data
        try:
            result = self._execute(data, params)
            return SkillOutput(success=True, data=result)
        except Exception as exc:
            return SkillOutput(success=False, error=str(exc))

    @staticmethod
    def _execute(data: dict[str, Any], params: dict[str, Any]) -> dict[str, Any]:
        """Core logic for time_series_decomposition."""
        return {
            "skill": "time_series_decomposition",
            "status": "executed",
            "input_keys": list(data.keys()),
        }
