"""Knowledge base for storing and retrieving structured insights."""

from __future__ import annotations

import json
import logging
from dataclasses import asdict
from pathlib import Path
from typing import Any

from src.agents.base.types import ExperimentRecord, ResearchReport, _new_id

logger = logging.getLogger(__name__)

INSIGHTS_FILE = "insights.jsonl"
EXPERIMENTS_FILE = "experiments.jsonl"
REPORTS_DIR = "reports"


class KnowledgeBase:
    """File-backed knowledge base for structured research artifacts.

    Stores dataset insights, experiment records, and research reports
    as JSONL files for easy append and streaming read.
    """

    def __init__(self, base_dir: str = "./memory/knowledge") -> None:
        self._base = Path(base_dir)
        self._base.mkdir(parents=True, exist_ok=True)
        (self._base / REPORTS_DIR).mkdir(exist_ok=True)

    # ---- Insights ----

    def add_insight(self, text: str, metadata: dict[str, Any] | None = None) -> str:
        """Append a textual insight. Returns the insight ID."""
        insight_id = _new_id()
        record = {"id": insight_id, "text": text, "metadata": metadata or {}}
        self._append_jsonl(INSIGHTS_FILE, record)
        return insight_id

    def list_insights(self) -> list[dict[str, Any]]:
        return self._read_jsonl(INSIGHTS_FILE)

    # ---- Experiments ----

    def save_experiment(self, record: ExperimentRecord) -> None:
        self._append_jsonl(EXPERIMENTS_FILE, asdict(record))

    def list_experiments(self) -> list[dict[str, Any]]:
        return self._read_jsonl(EXPERIMENTS_FILE)

    # ---- Reports ----

    def save_report(self, report: ResearchReport) -> str:
        path = self._base / REPORTS_DIR / f"{report.report_id}.json"
        path.write_text(json.dumps(asdict(report), default=str, indent=2))
        return str(path)

    def get_report(self, report_id: str) -> dict[str, Any] | None:
        path = self._base / REPORTS_DIR / f"{report_id}.json"
        if not path.exists():
            return None
        from typing import cast

        return cast("dict[str, Any]", json.loads(path.read_text()))

    # ---- Internal helpers ----

    def _append_jsonl(self, filename: str, record: dict[str, Any]) -> None:
        path = self._base / filename
        with path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, default=str) + "\n")

    def _read_jsonl(self, filename: str) -> list[dict[str, Any]]:
        path = self._base / filename
        if not path.exists():
            return []
        lines = path.read_text(encoding="utf-8").strip().splitlines()
        return [json.loads(line) for line in lines if line.strip()]
