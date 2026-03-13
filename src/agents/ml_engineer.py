"""ML Engineer Agent — model training, tuning, and selection."""

from __future__ import annotations

from typing import Any

import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder

from src.agents.base.agent import AgentContext, BaseAgent
from src.agents.base.types import AgentRole, ExperimentRecord, TaskResult, TaskStatus

TARGET_COL_KEY = "target_column"
CROSS_VAL_FOLDS = 5
MIN_ACCEPTABLE_SCORE = 0.6


class MLEngineerAgent(BaseAgent):
    """Trains multiple models, performs cross-validation, and selects the best.

    Supports classification out of the box with extensibility for
    regression and other tasks.
    """

    def __init__(self) -> None:
        super().__init__(AgentRole.ML_ENGINEER)

    async def plan(self, context: AgentContext) -> dict[str, Any]:
        return {
            "models": ["logistic_regression", "random_forest", "gradient_boosting"],
            "target_column": context.parameters.get(TARGET_COL_KEY, ""),
            "cv_folds": CROSS_VAL_FOLDS,
        }

    async def execute(self, context: AgentContext, plan: dict[str, Any]) -> TaskResult:
        df_json = context.data.get("dataframe_json")
        target_col = plan.get("target_column") or context.parameters.get(TARGET_COL_KEY, "")
        if not df_json or not target_col:
            return self._task_result(context, TaskStatus.FAILED, error="Missing dataframe or target_column")

        try:
            df = pd.read_json(df_json)
            results = self._train_models(df, target_col, plan)
            return self._task_result(context, output=results)
        except Exception as exc:
            return self._task_result(context, TaskStatus.FAILED, error=str(exc))

    async def evaluate(self, result: TaskResult) -> float:
        if result.status == TaskStatus.FAILED:
            return 0.0
        best_score = result.output.get("best_score", 0.0)
        return best_score

    async def improve(self, context: AgentContext, plan: dict[str, Any], result: TaskResult, score: float) -> dict[str, Any]:
        plan["cv_folds"] = 10  # more thorough cross-validation
        return plan

    def _train_models(self, df: pd.DataFrame, target: str, plan: dict[str, Any]) -> dict[str, Any]:
        X, y = self._prepare_data(df, target)
        cv_folds = plan.get("cv_folds", CROSS_VAL_FOLDS)
        model_map = self._get_model_map()
        experiments: list[dict[str, Any]] = []
        best_name, best_score = "", 0.0

        for name in plan.get("models", []):
            model = model_map.get(name)
            if model is None:
                continue
            scores = cross_val_score(model, X, y, cv=cv_folds, scoring="accuracy")
            mean_score = float(scores.mean())
            experiments.append({"model": name, "cv_mean": mean_score, "cv_std": float(scores.std())})
            if mean_score > best_score:
                best_name, best_score = name, mean_score

        return {
            "experiments": experiments,
            "best_model": best_name,
            "best_score": best_score,
            "target_column": target,
        }

    @staticmethod
    def _prepare_data(df: pd.DataFrame, target: str) -> tuple[pd.DataFrame, pd.Series]:
        y = df[target].copy()
        X = df.drop(columns=[target])

        # Encode categorical features
        le = LabelEncoder()
        for col in X.select_dtypes(include=["object", "category"]).columns:
            X[col] = le.fit_transform(X[col].astype(str))
        if y.dtype == "object":
            y = pd.Series(le.fit_transform(y.astype(str)), name=target)

        X = X.fillna(0)
        return X, y

    @staticmethod
    def _get_model_map() -> dict[str, Any]:
        return {
            "logistic_regression": LogisticRegression(max_iter=1000, random_state=42),
            "random_forest": RandomForestClassifier(n_estimators=100, random_state=42),
            "gradient_boosting": GradientBoostingClassifier(n_estimators=100, random_state=42),
        }
