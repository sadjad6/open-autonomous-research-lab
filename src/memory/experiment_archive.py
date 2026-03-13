"""Experiment archive — stores and retrieves ML experiment records."""

from __future__ import annotations

import json
import logging
from dataclasses import asdict
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from src.agents.base.types import ExperimentRecord

logger = logging.getLogger(__name__)

ARCHIVE_FILE = "experiment_archive.jsonl"


class ExperimentArchive:
    """Append-only archive for ML experiment tracking."""

    def __init__(self, base_dir: str = "./memory/experiments") -> None:
        self._base = Path(base_dir)
        self._base.mkdir(parents=True, exist_ok=True)

    def save(self, record: ExperimentRecord) -> str:
        """Persist an experiment record. Returns the experiment ID."""
        path = self._base / ARCHIVE_FILE
        with path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(asdict(record), default=str) + "\n")
        logger.info("Saved experiment %s (%s)", record.experiment_id, record.model_type)
        return record.experiment_id

    def list_all(self) -> list[dict[str, Any]]:
        """Return all archived experiments."""
        path = self._base / ARCHIVE_FILE
        if not path.exists():
            return []
        lines = path.read_text(encoding="utf-8").strip().splitlines()
        return [json.loads(line) for line in lines if line.strip()]

    def get(self, experiment_id: str) -> dict[str, Any] | None:
        """Retrieve a single experiment by ID."""
        for record in self.list_all():
            if record.get("experiment_id") == experiment_id:
                return record
        return None

    def search(
        self, model_type: str | None = None, dataset_id: str | None = None
    ) -> list[dict[str, Any]]:
        """Filter experiments by model type or dataset."""
        results = self.list_all()
        if model_type:
            results = [r for r in results if r.get("model_type") == model_type]
        if dataset_id:
            results = [r for r in results if r.get("dataset_id") == dataset_id]
        return results
