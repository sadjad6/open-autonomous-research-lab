"""Evaluation framework — metrics, experiment tracking, and MLflow integration."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any, cast

import numpy as np

logger = logging.getLogger(__name__)


@dataclass
class EvaluationResult:
    """Holds metrics from a single model evaluation."""

    model_name: str = ""
    metrics: dict[str, float] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


class MetricComputer:
    """Compute standard ML evaluation metrics."""

    @staticmethod
    def classification_metrics(y_true: list[Any], y_pred: list[Any]) -> dict[str, float]:
        from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

        y_t, y_p = np.array(y_true), np.array(y_pred)
        return {
            "accuracy": float(accuracy_score(y_t, y_p)),
            "precision": float(precision_score(y_t, y_p, average="weighted", zero_division=0)),
            "recall": float(recall_score(y_t, y_p, average="weighted", zero_division=0)),
            "f1": float(f1_score(y_t, y_p, average="weighted", zero_division=0)),
        }

    @staticmethod
    def regression_metrics(y_true: list[float], y_pred: list[float]) -> dict[str, float]:
        from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

        y_t, y_p = np.array(y_true), np.array(y_pred)
        return {
            "mae": float(mean_absolute_error(y_t, y_p)),
            "rmse": float(np.sqrt(mean_squared_error(y_t, y_p))),
            "r2": float(r2_score(y_t, y_p)),
        }


class MLflowTracker:
    """Wraps MLflow experiment tracking."""

    def __init__(
        self, tracking_uri: str = "sqlite:///mlruns.db", experiment_name: str = "oarl"
    ) -> None:
        self._uri = tracking_uri
        self._experiment = experiment_name
        self._initialized = False

    def _init_mlflow(self) -> None:
        if self._initialized:
            return
        try:
            import mlflow

            mlflow.set_tracking_uri(self._uri)
            mlflow.set_experiment(self._experiment)
            self._initialized = True
        except Exception:
            logger.warning("MLflow not available — tracking disabled")

    def log_experiment(
        self, name: str, params: dict[str, Any], metrics: dict[str, float]
    ) -> str | None:
        """Log an experiment run to MLflow. Returns run ID or None."""
        self._init_mlflow()
        if not self._initialized:
            return None
        try:
            import mlflow

            with mlflow.start_run(run_name=name) as run:
                mlflow.log_params(params)
                mlflow.log_metrics(metrics)
                return cast("str", run.info.run_id)
        except Exception:
            logger.exception("Failed to log MLflow experiment")
            return None
