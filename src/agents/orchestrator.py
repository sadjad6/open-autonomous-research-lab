"""Orchestrator Agent — central coordinator that decomposes user requests."""

from __future__ import annotations

import logging
from typing import Any

from src.agents.base.agent import AgentContext, BaseAgent
from src.agents.base.types import AgentRole, TaskResult, TaskStatus

logger = logging.getLogger(__name__)

ORCHESTRATION_PIPELINE = [
    AgentRole.PLANNER,
    AgentRole.DATA_ENGINEER,
    AgentRole.DATA_SCIENTIST,
    AgentRole.ML_ENGINEER,
    AgentRole.EVALUATION,
    AgentRole.RESEARCH_ANALYST,
    AgentRole.KNOWLEDGE_MANAGER,
]


class OrchestratorAgent(BaseAgent):
    """Decomposes a user request and delegates to specialist agents.

    The orchestrator determines which agents to invoke and in what
    order, then collects and merges their results into a unified
    response.
    """

    def __init__(self) -> None:
        super().__init__(AgentRole.ORCHESTRATOR)
        self._registry = None  # set externally after construction

    def set_registry(self, registry: Any) -> None:
        """Inject the agent registry for delegation."""
        self._registry = registry

    async def plan(self, context: AgentContext) -> dict[str, Any]:
        """Determine the pipeline of agents to invoke."""
        pipeline = [role.value for role in ORCHESTRATION_PIPELINE]
        return {"pipeline": pipeline, "objective": context.user_request}

    async def execute(self, context: AgentContext, plan: dict[str, Any]) -> TaskResult:
        """Execute each agent in the pipeline sequentially."""
        results: list[dict[str, Any]] = []
        accumulated_data: dict[str, Any] = dict(context.data)

        for role_name in plan["pipeline"]:
            role = AgentRole(role_name)
            if self._registry is None:
                continue
            try:
                agent = self._registry.get(role)
            except KeyError:
                logger.warning("Agent %s not registered — skipping", role_name)
                continue

            sub_context = AgentContext(
                task_id=context.task_id,
                user_request=context.user_request,
                data=accumulated_data,
                parameters=context.parameters,
            )
            result = await agent.run(sub_context)
            results.append(
                {"agent": role_name, "status": result.status.value, "output": result.output}
            )
            accumulated_data.update(result.output)

        return self._task_result(
            context, output={"pipeline_results": results, "merged_data": accumulated_data}
        )

    async def evaluate(self, result: TaskResult) -> float:
        pipeline_results = result.output.get("pipeline_results", [])
        if not pipeline_results:
            return 0.0
        completed = sum(1 for r in pipeline_results if r["status"] == TaskStatus.COMPLETED.value)
        return completed / len(pipeline_results)

    async def improve(
        self, context: AgentContext, plan: dict[str, Any], result: TaskResult, score: float
    ) -> dict[str, Any]:
        """Retry only the failed agents."""
        pipeline_results = result.output.get("pipeline_results", [])
        failed = [r["agent"] for r in pipeline_results if r["status"] != TaskStatus.COMPLETED.value]
        plan["pipeline"] = failed
        return plan
