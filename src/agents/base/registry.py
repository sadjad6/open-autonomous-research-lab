"""Agent registry — discovery, lifecycle, and lookup of agents."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.agents.base.agent import BaseAgent
    from src.agents.base.types import AgentRole

logger = logging.getLogger(__name__)


class AgentRegistry:
    """Singleton-style registry that manages all active agents."""

    def __init__(self) -> None:
        self._agents: dict[AgentRole, BaseAgent] = {}

    def register(self, agent: BaseAgent) -> None:
        """Register an agent instance under its role."""
        if agent.role in self._agents:
            logger.warning("Overwriting existing agent for role %s", agent.role.value)
        self._agents[agent.role] = agent
        logger.info("Registered agent: %s (id=%s)", agent.role.value, agent.agent_id)

    def get(self, role: AgentRole) -> BaseAgent:
        """Retrieve a registered agent by role."""
        if role not in self._agents:
            raise KeyError(f"No agent registered for role: {role.value}")
        return self._agents[role]

    def list_agents(self) -> list[AgentRole]:
        """Return all registered agent roles."""
        return list(self._agents.keys())

    def unregister(self, role: AgentRole) -> None:
        """Remove an agent from the registry."""
        self._agents.pop(role, None)

    def clear(self) -> None:
        """Remove all agents."""
        self._agents.clear()

    @property
    def count(self) -> int:
        return len(self._agents)
