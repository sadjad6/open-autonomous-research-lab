"""Workflow trigger endpoints — start agent analysis pipelines."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel, Field

from src.agents.base.agent import AgentContext
from src.agents.base.registry import AgentRegistry
from src.agents.base.types import _new_id
from src.agents.data_engineer import DataEngineerAgent
from src.agents.data_scientist import DataScientistAgent
from src.agents.evaluation_agent import EvaluationAgent
from src.agents.infrastructure_agent import InfrastructureAgent
from src.agents.knowledge_manager import KnowledgeManagerAgent
from src.agents.ml_engineer import MLEngineerAgent
from src.agents.orchestrator import OrchestratorAgent
from src.agents.planner import PlannerAgent
from src.agents.research_analyst import ResearchAnalystAgent

router = APIRouter()


class AnalysisRequest(BaseModel):
    """Request body for triggering an analysis workflow."""

    request: str = Field(..., description="Natural language analysis request")
    dataset_path: str = Field("", description="Path to the dataset file")
    target_column: str = Field("", description="Target column for ML tasks")


class AnalysisResponse(BaseModel):
    """Response from an analysis workflow."""

    task_id: str
    status: str
    results: dict[str, Any] = {}


def _build_registry() -> tuple[AgentRegistry, OrchestratorAgent]:
    """Construct the full agent registry."""
    registry = AgentRegistry()
    orchestrator = OrchestratorAgent()

    agents = [
        PlannerAgent(),
        DataEngineerAgent(),
        DataScientistAgent(),
        MLEngineerAgent(),
        ResearchAnalystAgent(),
        EvaluationAgent(),
        KnowledgeManagerAgent(),
        InfrastructureAgent(),
    ]
    for agent in agents:
        registry.register(agent)
    registry.register(orchestrator)
    orchestrator.set_registry(registry)
    return registry, orchestrator


@router.post("/analyze", response_model=AnalysisResponse)
async def run_analysis(req: AnalysisRequest) -> AnalysisResponse:
    """Trigger the full agent analysis pipeline."""
    _, orchestrator = _build_registry()
    task_id = _new_id()

    context = AgentContext(
        task_id=task_id,
        user_request=req.request,
        data={"dataset_path": req.dataset_path},
        parameters={"target_column": req.target_column},
    )

    result = await orchestrator.run(context)

    return AnalysisResponse(
        task_id=task_id,
        status=result.status.value,
        results=result.output,
    )


@router.get("/agents")
async def list_agents() -> dict[str, Any]:
    """List all available agents."""
    registry, _ = _build_registry()
    return {
        "agents": [role.value for role in registry.list_agents()],
        "count": registry.count,
    }
