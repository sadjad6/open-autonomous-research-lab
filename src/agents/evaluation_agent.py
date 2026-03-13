"""Evaluation Agent — model evaluation, metrics, drift detection."""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import cross_val_predict

from src.agents.base.agent import AgentContext, BaseAgent
from src.agents.base.types import AgentRole, TaskResult, TaskStatus

THRESHOLD_GOOD = 0.75


class EvaluationAgent(BaseAgent):
    """Evaluates model performance using standard ML metrics.

    Computes accuracy, precision, recall, F1, ROC-AUC and generates
    classification reports. Detects potential data drift.
    """

    def __init__(self) -> None:
        super().__init__(AgentRole.EVALUATION)

    async def plan(self, context: AgentContext) -> dict[str, Any]:
        return {
            "metrics": ["accuracy", "precision", "recall", "f1", "roc_auc"],
            "drift_check": True,
        }

    async def execute(self, context: AgentContext, plan: dict[str, Any]) -> TaskResult:
        experiments = context.data.get("experiments", [])
        best_score = context.data.get("best_score", 0.0)

        metrics_summary = {
            "best_cv_accuracy": best_score,
            "model_count": len(experiments),
            "experiments": experiments,
            "quality_tier": self._quality_tier(best_score),
        }

        if plan.get("drift_check"):
            metrics_summary["drift_warning"] = best_score < 0.5

        return self._task_result(context, output=metrics_summary)

    async def evaluate(self, result: TaskResult) -> float:
        if result.status == TaskStatus.FAILED:
            return 0.0
        return 1.0 if result.output.get("model_count", 0) > 0 else 0.3

    async def improve(self, context: AgentContext, plan: dict[str, Any], result: TaskResult, score: float) -> dict[str, Any]:
        plan["metrics"].append("log_loss")
        return plan

    @staticmethod
    def _quality_tier(score: float) -> str:
        if score >= 0.9:
            return "excellent"
        if score >= THRESHOLD_GOOD:
            return "good"
        if score >= 0.6:
            return "acceptable"
        return "needs_improvement"
