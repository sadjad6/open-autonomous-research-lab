"""Data Scientist Agent — EDA, statistical analysis, and hypothesis testing."""

from __future__ import annotations

from typing import Any

import pandas as pd

from src.agents.base.agent import AgentContext, BaseAgent
from src.agents.base.types import AgentRole, TaskResult, TaskStatus

MIN_INSIGHT_COUNT = 3


class DataScientistAgent(BaseAgent):
    """Performs exploratory data analysis and statistical testing.

    Produces insights, correlations, distributions, and statistical
    test results.
    """

    def __init__(self) -> None:
        super().__init__(AgentRole.DATA_SCIENTIST)

    async def plan(self, context: AgentContext) -> dict[str, Any]:
        return {
            "analyses": [
                "descriptive_statistics",
                "correlation_matrix",
                "distribution_analysis",
                "target_analysis",
            ],
        }

    async def execute(self, context: AgentContext, plan: dict[str, Any]) -> TaskResult:
        df_json = context.data.get("dataframe_json")
        if not df_json:
            return self._task_result(
                context, TaskStatus.FAILED, error="No dataframe data available"
            )

        try:
            df = pd.read_json(df_json)
            insights = self._analyze(df)
            return self._task_result(context, output=insights)
        except Exception as exc:
            return self._task_result(context, TaskStatus.FAILED, error=str(exc))

    async def evaluate(self, result: TaskResult) -> float:
        if result.status == TaskStatus.FAILED:
            return 0.0
        insight_count = len(result.output.get("insights", []))
        return min(1.0, insight_count / MIN_INSIGHT_COUNT)

    async def improve(
        self, context: AgentContext, plan: dict[str, Any], result: TaskResult, score: float
    ) -> dict[str, Any]:
        plan["analyses"].extend(["outlier_analysis", "skewness_check"])
        return plan

    @staticmethod
    def _analyze(df: pd.DataFrame) -> dict[str, Any]:
        numeric = df.select_dtypes(include="number")
        stats = numeric.describe().to_dict()
        correlations = numeric.corr().to_dict() if len(numeric.columns) > 1 else {}

        insights: list[str] = []
        for col in numeric.columns:
            skew = numeric[col].skew()
            if abs(skew) > 1:
                insights.append(f"Column '{col}' is highly skewed (skewness={skew:.2f})")

        if correlations:
            for c1 in numeric.columns:
                for c2 in numeric.columns:
                    if c1 >= c2:
                        continue
                    corr_val = numeric[c1].corr(numeric[c2])
                    if abs(corr_val) > 0.7:
                        insights.append(
                            f"Strong correlation between '{c1}' and '{c2}' (r={corr_val:.2f})"
                        )

        categorical_cols = list(df.select_dtypes(include=["object", "category"]).columns)
        category_summary = {col: int(df[col].nunique()) for col in categorical_cols}

        return {
            "descriptive_stats": stats,
            "correlations": correlations,
            "insights": insights,
            "categorical_summary": category_summary,
            "num_rows": len(df),
            "num_numeric_columns": len(numeric.columns),
            "num_categorical_columns": len(categorical_cols),
        }
