"""Planner Agent — creates step-by-step execution plans."""

from __future__ import annotations

from typing import Any

from src.agents.base.agent import AgentContext, BaseAgent
from src.agents.base.types import (
    AgentRole,
    ExecutionPlan,
    PlanStep,
    TaskResult,
)


class PlannerAgent(BaseAgent):
    """Analyzes user requests and produces structured execution plans.

    The planner determines which skills and agents are needed, orders
    the steps by dependency, and estimates resource requirements.
    """

    def __init__(self) -> None:
        super().__init__(AgentRole.PLANNER)

    async def plan(self, context: AgentContext) -> dict[str, Any]:
        steps = self._generate_steps(context.user_request)
        execution_plan = ExecutionPlan(objective=context.user_request, steps=steps)
        return {"execution_plan": execution_plan}

    async def execute(self, context: AgentContext, plan: dict[str, Any]) -> TaskResult:
        execution_plan: ExecutionPlan = plan["execution_plan"]
        step_dicts = [
            {
                "step_id": s.step_id,
                "description": s.description,
                "agent": s.agent_role.value,
                "skills": s.skills,
                "dependencies": s.dependencies,
            }
            for s in execution_plan.steps
        ]
        return self._task_result(
            context,
            output={
                "plan_id": execution_plan.plan_id,
                "objective": execution_plan.objective,
                "steps": step_dicts,
                "step_count": len(step_dicts),
            },
        )

    async def evaluate(self, result: TaskResult) -> float:
        step_count = result.output.get("step_count", 0)
        return 1.0 if step_count > 0 else 0.0

    async def improve(
        self, context: AgentContext, plan: dict[str, Any], result: TaskResult, score: float
    ) -> dict[str, Any]:
        # Re-generate with more granularity
        steps = self._generate_steps(context.user_request, granular=True)
        plan["execution_plan"] = ExecutionPlan(objective=context.user_request, steps=steps)
        return plan

    @staticmethod
    def _generate_steps(request: str, granular: bool = False) -> list[PlanStep]:
        """Build a default pipeline of steps for the request."""
        base_steps = [
            PlanStep(
                description="Ingest and validate dataset",
                agent_role=AgentRole.DATA_ENGINEER,
                skills=["csv_loader", "schema_validator"],
            ),
            PlanStep(
                description="Clean and transform data",
                agent_role=AgentRole.DATA_ENGINEER,
                skills=["data_cleaning", "missing_value_handler"],
            ),
            PlanStep(
                description="Perform exploratory data analysis",
                agent_role=AgentRole.DATA_SCIENTIST,
                skills=["eda_generator", "correlation_analysis"],
            ),
            PlanStep(
                description="Run statistical tests",
                agent_role=AgentRole.DATA_SCIENTIST,
                skills=["statistical_testing"],
            ),
            PlanStep(
                description="Engineer features for modeling",
                agent_role=AgentRole.ML_ENGINEER,
                skills=["feature_engineer"],
            ),
            PlanStep(
                description="Train candidate models",
                agent_role=AgentRole.ML_ENGINEER,
                skills=["random_forest", "xgboost_trainer"],
            ),
            PlanStep(
                description="Tune hyperparameters",
                agent_role=AgentRole.ML_ENGINEER,
                skills=["hyperparameter_tuner"],
            ),
            PlanStep(
                description="Evaluate models",
                agent_role=AgentRole.EVALUATION,
                skills=["accuracy_evaluator", "roc_auc"],
            ),
            PlanStep(
                description="Generate research report",
                agent_role=AgentRole.RESEARCH_ANALYST,
                skills=["report_writer"],
            ),
        ]
        if granular:
            base_steps.insert(
                2,
                PlanStep(
                    description="Detect and handle outliers",
                    agent_role=AgentRole.DATA_ENGINEER,
                    skills=["outlier_detector"],
                ),
            )
            base_steps.insert(
                4,
                PlanStep(
                    description="Analyze feature distributions",
                    agent_role=AgentRole.DATA_SCIENTIST,
                    skills=["distribution_analysis"],
                ),
            )
        return base_steps
