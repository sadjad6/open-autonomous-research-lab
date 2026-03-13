"""Tests for the OARL agent base framework."""

from __future__ import annotations

import pytest

from src.agents.base.agent import AgentContext, BaseAgent
from src.agents.base.communication import MessageBus
from src.agents.base.registry import AgentRegistry
from src.agents.base.types import (
    AgentMessage,
    AgentRole,
    ExecutionPlan,
    MessageType,
    PlanStep,
    TaskResult,
    TaskStatus,
)

# ── Concrete test agent ──────────────────────────────────────


class MockAgent(BaseAgent):
    """Simple agent for testing the base framework."""

    def __init__(self, role: AgentRole = AgentRole.PLANNER) -> None:
        super().__init__(role)

    async def plan(self, context: AgentContext) -> dict:
        return {"strategy": "test"}

    async def execute(self, context: AgentContext, plan: dict) -> TaskResult:
        return self._task_result(context, output={"result": "ok"})

    async def evaluate(self, result: TaskResult) -> float:
        return 0.9

    async def improve(
        self, context: AgentContext, plan: dict, result: TaskResult, score: float
    ) -> dict:
        return plan


# ── Agent Tests ──────────────────────────────────────────────


@pytest.mark.asyncio
async def test_agent_run_completes() -> None:
    agent = MockAgent()
    ctx = AgentContext(user_request="test request")
    result = await agent.run(ctx)
    assert result.status == TaskStatus.COMPLETED
    assert result.output["result"] == "ok"


@pytest.mark.asyncio
async def test_agent_run_records_metrics() -> None:
    agent = MockAgent()
    ctx = AgentContext(user_request="test")
    result = await agent.run(ctx)
    assert "quality_score" in result.metrics
    assert result.metrics["quality_score"] >= 0.7


# ── Registry Tests ───────────────────────────────────────────


def test_registry_register_and_get() -> None:
    registry = AgentRegistry()
    agent = MockAgent(AgentRole.DATA_ENGINEER)
    registry.register(agent)
    found = registry.get(AgentRole.DATA_ENGINEER)
    assert found.role == AgentRole.DATA_ENGINEER


def test_registry_missing_agent_raises() -> None:
    registry = AgentRegistry()
    with pytest.raises(KeyError):
        registry.get(AgentRole.ML_ENGINEER)


def test_registry_list_agents() -> None:
    registry = AgentRegistry()
    registry.register(MockAgent(AgentRole.PLANNER))
    registry.register(MockAgent(AgentRole.DATA_SCIENTIST))
    assert len(registry.list_agents()) == 2


# ── Message Bus Tests ────────────────────────────────────────


@pytest.mark.asyncio
async def test_message_bus_publish() -> None:
    bus = MessageBus()
    received: list[AgentMessage] = []

    async def handler(msg: AgentMessage) -> None:
        received.append(msg)

    bus.subscribe(AgentRole.PLANNER, handler)
    msg = AgentMessage(
        sender=AgentRole.ORCHESTRATOR,
        receiver=AgentRole.PLANNER,
        message_type=MessageType.TASK_REQUEST,
        payload={"task": "analyze"},
    )
    await bus.publish(msg)
    assert len(received) == 1
    assert received[0].payload["task"] == "analyze"


@pytest.mark.asyncio
async def test_message_bus_no_handler() -> None:
    bus = MessageBus()
    msg = AgentMessage(
        sender=AgentRole.ORCHESTRATOR,
        receiver=AgentRole.DATA_ENGINEER,
        message_type=MessageType.TASK_REQUEST,
        payload={},
    )
    await bus.publish(msg)  # Should not raise


# ── Type Tests ───────────────────────────────────────────────


def test_plan_step_defaults() -> None:
    step = PlanStep(description="test step")
    assert step.status == TaskStatus.PENDING
    assert step.agent_role == AgentRole.ORCHESTRATOR


def test_execution_plan_has_steps() -> None:
    plan = ExecutionPlan(
        objective="test",
        steps=[PlanStep(description="s1"), PlanStep(description="s2")],
    )
    assert len(plan.steps) == 2
