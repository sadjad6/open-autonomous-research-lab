"""Skills Marketplace — dynamic plugin system for adding new skills at runtime.

Drop skill packages into `skills_marketplace/plugins/` and they will be
auto-discovered and registered with the skill registry.
"""

from __future__ import annotations

import importlib
import logging
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.skills.base.skill import BaseSkill

logger = logging.getLogger(__name__)

PLUGINS_DIR = Path(__file__).parent / "plugins"


def discover_marketplace_skills() -> list[BaseSkill]:
    """Scan the plugins directory and instantiate all Skill classes."""
    PLUGINS_DIR.mkdir(exist_ok=True)
    skills: list[BaseSkill] = []

    for plugin_dir in sorted(PLUGINS_DIR.iterdir()):
        if not plugin_dir.is_dir():
            continue
        init_file = plugin_dir / "__init__.py"
        if not init_file.exists():
            continue
        module_name = f"skills_marketplace.plugins.{plugin_dir.name}"
        try:
            mod = importlib.import_module(module_name)
            skill_cls = getattr(mod, "Skill", None)
            if skill_cls is not None:
                skills.append(skill_cls())
                logger.info("Loaded marketplace skill: %s", plugin_dir.name)
        except Exception:
            logger.exception("Failed to load marketplace plugin: %s", plugin_dir.name)

    return skills
