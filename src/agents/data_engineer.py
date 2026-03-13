"""Data Engineer Agent — data ingestion, cleaning, and transformation."""

from __future__ import annotations

from typing import Any

import pandas as pd

from src.agents.base.agent import AgentContext, BaseAgent
from src.agents.base.types import AgentRole, DatasetMetadata, TaskResult, TaskStatus


class DataEngineerAgent(BaseAgent):
    """Handles data ingestion, validation, cleaning, and transformation.

    Produces a clean, analysis-ready DataFrame along with dataset metadata.
    """

    def __init__(self) -> None:
        super().__init__(AgentRole.DATA_ENGINEER)

    async def plan(self, context: AgentContext) -> dict[str, Any]:
        return {
            "steps": [
                "load_dataset",
                "validate_schema",
                "handle_missing_values",
                "detect_outliers",
                "convert_types",
            ],
            "dataset_path": context.data.get("dataset_path", ""),
        }

    async def execute(self, context: AgentContext, plan: dict[str, Any]) -> TaskResult:
        path = plan.get("dataset_path", "")
        if not path:
            return self._task_result(context, TaskStatus.FAILED, error="No dataset_path provided")

        try:
            df = self._load_dataset(path)
            original_shape = df.shape
            df = self._clean_data(df)
            metadata = self._build_metadata(path, df)

            return self._task_result(
                context,
                output={
                    "dataset_path": path,
                    "original_shape": list(original_shape),
                    "cleaned_shape": list(df.shape),
                    "columns": list(df.columns),
                    "dtypes": {col: str(dtype) for col, dtype in df.dtypes.items()},
                    "missing_values": int(df.isna().sum().sum()),
                    "metadata": metadata.__dict__,
                    "dataframe_json": df.head(100).to_json(),
                },
            )
        except Exception as exc:
            return self._task_result(context, TaskStatus.FAILED, error=str(exc))

    async def evaluate(self, result: TaskResult) -> float:
        if result.status == TaskStatus.FAILED:
            return 0.0
        missing = result.output.get("missing_values", 0)
        return 1.0 if missing == 0 else 0.8

    async def improve(self, context: AgentContext, plan: dict[str, Any], result: TaskResult, score: float) -> dict[str, Any]:
        plan["steps"].append("aggressive_imputation")
        return plan

    @staticmethod
    def _load_dataset(path: str) -> pd.DataFrame:
        if path.endswith(".csv"):
            return pd.read_csv(path)
        if path.endswith(".parquet"):
            return pd.read_parquet(path)
        if path.endswith((".xls", ".xlsx")):
            return pd.read_excel(path)
        if path.endswith(".json"):
            return pd.read_json(path)
        raise ValueError(f"Unsupported format: {path}")

    @staticmethod
    def _clean_data(df: pd.DataFrame) -> pd.DataFrame:
        """Basic cleaning: drop duplicates, fill numeric NaN with median."""
        df = df.drop_duplicates()
        numeric_cols = df.select_dtypes(include="number").columns
        for col in numeric_cols:
            if df[col].isna().any():
                df[col] = df[col].fillna(df[col].median())
        return df

    @staticmethod
    def _build_metadata(path: str, df: pd.DataFrame) -> DatasetMetadata:
        return DatasetMetadata(
            name=path.split("/")[-1].split("\\")[-1],
            path=path,
            num_rows=len(df),
            num_columns=len(df.columns),
            columns=list(df.columns),
            dtypes={col: str(dtype) for col, dtype in df.dtypes.items()},
        )
