"""Skill registry with dynamic discovery and lookup."""

from __future__ import annotations

import importlib
import logging
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.skills.base.skill import BaseSkill

logger = logging.getLogger(__name__)


class SkillRegistry:
    """Registry that manages, discovers, and looks up skills."""

    def __init__(self) -> None:
        self._skills: dict[str, BaseSkill] = {}

    def register(self, skill: BaseSkill) -> None:
        """Add a skill to the registry."""
        self._skills[skill.name] = skill
        logger.info("Registered skill: %s [%s]", skill.name, skill.domain)

    def get(self, name: str) -> BaseSkill:
        """Retrieve a skill by name."""
        if name not in self._skills:
            raise KeyError(f"Skill not found: {name}")
        return self._skills[name]

    def list_skills(self, domain: str | None = None) -> list[dict[str, str]]:
        """List all skills, optionally filtered by domain."""
        skills = self._skills.values()
        if domain:
            skills = [s for s in skills if s.domain == domain]
        return [s.to_dict() for s in skills]

    def list_domains(self) -> list[str]:
        """Return unique domains of registered skills."""
        return sorted({s.domain for s in self._skills.values()})

    def discover_skills(self, package_path: str) -> int:
        """Auto-discover and register skill modules under a package.

        Each module is expected to expose a ``Skill`` class that
        extends ``BaseSkill``.  Returns the count of skills loaded.
        """
        base = Path(package_path)
        loaded = 0
        for module_dir in sorted(base.iterdir()):
            init_file = module_dir / "__init__.py"
            if not module_dir.is_dir() or not init_file.exists():
                continue
            module_name = f"src.skills.{module_dir.parent.name}.{module_dir.name}"
            try:
                mod = importlib.import_module(module_name)
                skill_cls = getattr(mod, "Skill", None)
                if skill_cls is not None:
                    self.register(skill_cls())
                    loaded += 1
            except Exception:
                logger.exception("Failed to load skill from %s", module_name)
        return loaded

    def unregister(self, name: str) -> None:
        self._skills.pop(name, None)

    @property
    def count(self) -> int:
        return len(self._skills)
