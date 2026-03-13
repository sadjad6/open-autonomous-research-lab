"""Abstract base agent with the plan→execute→evaluate→improve reasoning loop."""

from __future__ import annotations

import abc
import logging
from dataclasses import dataclass, field
from typing import Any

from src.agents.base.types import (
    AgentMessage,
    AgentRole,
    MessageType,
    TaskResult,
    TaskStatus,
    _new_id,
    _utcnow,
)

logger = logging.getLogger(__name__)

MAX_IMPROVEMENT_ITERATIONS = 3
QUALITY_THRESHOLD = 0.7


@dataclass
class AgentContext:
    """Runtime context passed to an agent during execution."""

    task_id: str = field(default_factory=_new_id)
    user_request: str = ""
    data: dict[str, Any] = field(default_factory=dict)
    history: list[TaskResult] = field(default_factory=list)
    parameters: dict[str, Any] = field(default_factory=dict)


class BaseAgent(abc.ABC):
    """Abstract base class for all OARL agents.

    Implements the autonomous reasoning loop:
        plan → execute → evaluate → improve

    Subclasses must implement the four abstract methods.
    """

    def __init__(self, role: AgentRole) -> None:
        self.role = role
        self.agent_id: str = _new_id()
        self._logger = logging.getLogger(f"oarl.agent.{role.value}")

    # ------------------------------------------------------------------
    # Abstract methods — subclasses define domain-specific behaviour
    # ------------------------------------------------------------------

    @abc.abstractmethod
    async def plan(self, context: AgentContext) -> dict[str, Any]:
        """Create a plan for the given context. Returns plan data."""

    @abc.abstractmethod
    async def execute(self, context: AgentContext, plan: dict[str, Any]) -> TaskResult:
        """Execute the plan and return a result."""

    @abc.abstractmethod
    async def evaluate(self, result: TaskResult) -> float:
        """Evaluate the quality of a result. Returns a score in [0, 1]."""

    @abc.abstractmethod
    async def improve(
        self,
        context: AgentContext,
        plan: dict[str, Any],
        result: TaskResult,
        score: float,
    ) -> dict[str, Any]:
        """Refine the plan based on evaluation feedback. Returns improved plan."""

    # ------------------------------------------------------------------
    # Core reasoning loop
    # ------------------------------------------------------------------

    async def run(self, context: AgentContext) -> TaskResult:
        """Execute the full plan→execute→evaluate→improve loop."""
        self._logger.info("Agent %s starting task %s", self.role.value, context.task_id)

        plan = await self.plan(context)
        result = await self.execute(context, plan)
        score = await self.evaluate(result)

        iteration = 0
        while score < QUALITY_THRESHOLD and iteration < MAX_IMPROVEMENT_ITERATIONS:
            self._logger.info(
                "Iteration %d: score=%.2f < %.2f, improving…",
                iteration, score, QUALITY_THRESHOLD,
            )
            plan = await self.improve(context, plan, result, score)
            result = await self.execute(context, plan)
            score = await self.evaluate(result)
            iteration += 1

        result.completed_at = _utcnow()
        result.metrics["quality_score"] = score
        result.metrics["improvement_iterations"] = float(iteration)
        self._logger.info(
            "Agent %s finished task %s — score=%.2f",
            self.role.value, context.task_id, score,
        )
        return result

    # ------------------------------------------------------------------
    # Messaging helpers
    # ------------------------------------------------------------------

    def create_message(
        self,
        receiver: AgentRole,
        message_type: MessageType,
        payload: dict[str, Any],
        correlation_id: str | None = None,
    ) -> AgentMessage:
        """Build an outbound message from this agent."""
        return AgentMessage(
            sender=self.role,
            receiver=receiver,
            message_type=message_type,
            payload=payload,
            correlation_id=correlation_id,
        )

    def _task_result(
        self,
        context: AgentContext,
        status: TaskStatus = TaskStatus.COMPLETED,
        output: dict[str, Any] | None = None,
        error: str | None = None,
    ) -> TaskResult:
        """Convenience builder for TaskResult."""
        return TaskResult(
            task_id=context.task_id,
            agent_role=self.role,
            status=status,
            output=output or {},
            error=error,
        )
