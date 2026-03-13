"""Knowledge Manager Agent — memory management, indexing, retrieval."""

from __future__ import annotations

from typing import Any

from src.agents.base.agent import AgentContext, BaseAgent
from src.agents.base.types import AgentRole, ExperimentRecord, TaskResult, TaskStatus
from src.memory.knowledge_base import KnowledgeBase
from src.memory.vector_store import VectorStore


class KnowledgeManagerAgent(BaseAgent):
    """Manages the persistent knowledge store.

    Indexes insights, experiment results, and reasoning traces
    into the vector store and knowledge base for future retrieval.
    """

    def __init__(self, memory_dir: str = "./memory") -> None:
        super().__init__(AgentRole.KNOWLEDGE_MANAGER)
        self._kb = KnowledgeBase(f"{memory_dir}/knowledge")
        self._vs = VectorStore(f"{memory_dir}/chroma_data")

    async def plan(self, context: AgentContext) -> dict[str, Any]:
        return {
            "actions": ["store_insights", "index_experiments", "store_report"],
        }

    async def execute(self, context: AgentContext, plan: dict[str, Any]) -> TaskResult:
        stored_ids: list[str] = []
        data = context.data

        # Store insights
        for insight in data.get("insights", []):
            iid = self._kb.add_insight(insight)
            self._vs.add(iid, insight, {"type": "insight"})
            stored_ids.append(iid)

        # Store experiments
        for exp in data.get("experiments", []):
            record = ExperimentRecord(
                name=exp.get("model", "unknown"),
                model_type=exp.get("model", ""),
                metrics={"cv_mean": exp.get("cv_mean", 0.0)},
            )
            self._kb.save_experiment(record)
            stored_ids.append(record.experiment_id)

        # Store report text
        report_md = data.get("report_markdown", "")
        if report_md:
            rid = self._kb.add_insight(report_md[:500], {"type": "report_summary"})
            self._vs.add(rid, report_md[:500], {"type": "report"})
            stored_ids.append(rid)

        return self._task_result(
            context,
            output={
                "stored_items": len(stored_ids),
                "item_ids": stored_ids,
                "vector_store_count": self._vs.count,
            },
        )

    async def evaluate(self, result: TaskResult) -> float:
        if result.status == TaskStatus.FAILED:
            return 0.0
        return 1.0 if result.output.get("stored_items", 0) > 0 else 0.3

    async def improve(self, context: AgentContext, plan: dict[str, Any], result: TaskResult, score: float) -> dict[str, Any]:
        return plan  # knowledge storage is best-effort
