"""Tests for the skill framework."""

from __future__ import annotations

import pytest

from src.skills.base.skill import BaseSkill, SkillInput, SkillOutput
from src.skills.base.registry import SkillRegistry


class MockSkill(BaseSkill):
    @property
    def name(self) -> str:
        return "mock_skill"

    @property
    def domain(self) -> str:
        return "testing"

    @property
    def description(self) -> str:
        return "A mock skill for testing"

    async def run(self, skill_input: SkillInput) -> SkillOutput:
        return SkillOutput(success=True, data={"mock": True})


@pytest.mark.asyncio
async def test_skill_run() -> None:
    skill = MockSkill()
    result = await skill.run(SkillInput())
    assert result.success is True
    assert result.data["mock"] is True


def test_skill_to_dict() -> None:
    skill = MockSkill()
    info = skill.to_dict()
    assert info["name"] == "mock_skill"
    assert info["domain"] == "testing"


def test_registry_register_and_get() -> None:
    registry = SkillRegistry()
    registry.register(MockSkill())
    skill = registry.get("mock_skill")
    assert skill.name == "mock_skill"


def test_registry_missing_skill_raises() -> None:
    registry = SkillRegistry()
    with pytest.raises(KeyError):
        registry.get("nonexistent")


def test_registry_list_skills() -> None:
    registry = SkillRegistry()
    registry.register(MockSkill())
    skills = registry.list_skills()
    assert len(skills) == 1


def test_registry_list_domains() -> None:
    registry = SkillRegistry()
    registry.register(MockSkill())
    domains = registry.list_domains()
    assert "testing" in domains
