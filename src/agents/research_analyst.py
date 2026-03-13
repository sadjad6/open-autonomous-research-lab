"""Research Analyst Agent — report writing, insight synthesis, recommendations."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from src.agents.base.agent import AgentContext, BaseAgent
from src.agents.base.types import (
    AgentRole,
    ReportSection,
    ResearchReport,
    TaskResult,
    TaskStatus,
)

MIN_SECTIONS = 4


class ResearchAnalystAgent(BaseAgent):
    """Generates comprehensive research reports from analysis results.

    Synthesizes insights from data analysis, modeling experiments,
    and evaluation metrics into a structured markdown report.
    """

    def __init__(self) -> None:
        super().__init__(AgentRole.RESEARCH_ANALYST)

    async def plan(self, context: AgentContext) -> dict[str, Any]:
        return {
            "sections": [
                "executive_summary",
                "data_overview",
                "exploratory_analysis",
                "modeling_results",
                "evaluation_metrics",
                "recommendations",
            ],
        }

    async def execute(self, context: AgentContext, plan: dict[str, Any]) -> TaskResult:
        try:
            report = self._generate_report(context, plan)
            return self._task_result(
                context,
                output={
                    "report_id": report.report_id,
                    "title": report.title,
                    "section_count": len(report.sections),
                    "sections": [{"heading": s.heading, "content": s.content} for s in report.sections],
                    "report_markdown": self._to_markdown(report),
                },
            )
        except Exception as exc:
            return self._task_result(context, TaskStatus.FAILED, error=str(exc))

    async def evaluate(self, result: TaskResult) -> float:
        if result.status == TaskStatus.FAILED:
            return 0.0
        count = result.output.get("section_count", 0)
        return min(1.0, count / MIN_SECTIONS)

    async def improve(self, context: AgentContext, plan: dict[str, Any], result: TaskResult, score: float) -> dict[str, Any]:
        plan["sections"].append("limitations")
        plan["sections"].append("future_work")
        return plan

    def _generate_report(self, context: AgentContext, plan: dict[str, Any]) -> ResearchReport:
        data = context.data
        sections: list[ReportSection] = []

        sections.append(ReportSection(
            heading="Executive Summary",
            content=f"This report presents the analysis of the research request: {context.user_request}",
        ))
        sections.append(ReportSection(
            heading="Data Overview",
            content=self._data_overview_text(data),
        ))
        sections.append(ReportSection(
            heading="Exploratory Analysis",
            content=self._eda_text(data),
        ))
        sections.append(ReportSection(
            heading="Modeling Results",
            content=self._modeling_text(data),
        ))
        sections.append(ReportSection(
            heading="Evaluation Metrics",
            content=self._eval_text(data),
        ))
        sections.append(ReportSection(
            heading="Recommendations",
            content="Based on the analysis, we recommend further investigation of the strongest predictive features.",
        ))

        return ResearchReport(
            title=f"Research Report — {context.user_request[:60]}",
            sections=sections,
        )

    @staticmethod
    def _data_overview_text(data: dict[str, Any]) -> str:
        shape = data.get("cleaned_shape", [0, 0])
        cols = data.get("columns", [])
        return f"Dataset contains {shape[0]} rows and {shape[1]} columns: {', '.join(cols[:10])}."

    @staticmethod
    def _eda_text(data: dict[str, Any]) -> str:
        insights = data.get("insights", [])
        if not insights:
            return "No significant patterns detected during exploratory analysis."
        return "Key findings:\n" + "\n".join(f"- {i}" for i in insights)

    @staticmethod
    def _modeling_text(data: dict[str, Any]) -> str:
        experiments = data.get("experiments", [])
        if not experiments:
            return "No models were trained in this analysis."
        lines = [f"- {e['model']}: CV accuracy = {e['cv_mean']:.4f} (±{e['cv_std']:.4f})" for e in experiments]
        best = data.get("best_model", "N/A")
        return f"Models trained:\n" + "\n".join(lines) + f"\n\nBest model: **{best}**"

    @staticmethod
    def _eval_text(data: dict[str, Any]) -> str:
        best_score = data.get("best_score", 0.0)
        return f"Best cross-validated accuracy: {best_score:.4f}"

    @staticmethod
    def _to_markdown(report: ResearchReport) -> str:
        lines = [f"# {report.title}", ""]
        for section in report.sections:
            lines.append(f"## {section.heading}")
            lines.append(section.content)
            lines.append("")
        return "\n".join(lines)
