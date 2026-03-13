"""Benchmark suite for evaluating OARL agent performance."""

from __future__ import annotations

import asyncio
import logging
import time
from dataclasses import dataclass, field
from typing import Any

from src.agents.base.agent import AgentContext, BaseAgent
from src.agents.base.types import _new_id

logger = logging.getLogger(__name__)


@dataclass
class BenchmarkTask:
    """Definition of a single benchmark task."""

    task_id: str = field(default_factory=_new_id)
    name: str = ""
    description: str = ""
    input_data: dict[str, Any] = field(default_factory=dict)
    expected_output_keys: list[str] = field(default_factory=list)


@dataclass
class BenchmarkResult:
    """Result of running a benchmark task."""

    task_id: str = ""
    agent_role: str = ""
    runtime_seconds: float = 0.0
    success: bool = False
    output_keys: list[str] = field(default_factory=list)
    score: float = 0.0


class BenchmarkRunner:
    """Runs benchmark tasks against agents and measures performance."""

    def __init__(self) -> None:
        self._tasks: list[BenchmarkTask] = []
        self._results: list[BenchmarkResult] = []

    def add_task(self, task: BenchmarkTask) -> None:
        self._tasks.append(task)

    async def run(self, agent: BaseAgent, tasks: list[BenchmarkTask] | None = None) -> list[BenchmarkResult]:
        """Run all benchmark tasks against an agent."""
        target_tasks = tasks or self._tasks
        results: list[BenchmarkResult] = []

        for task in target_tasks:
            context = AgentContext(
                task_id=task.task_id,
                user_request=task.description,
                data=task.input_data,
            )
            start = time.perf_counter()
            try:
                result = await agent.run(context)
                elapsed = time.perf_counter() - start
                output_keys = list(result.output.keys())
                matched = [k for k in task.expected_output_keys if k in output_keys]
                score = len(matched) / max(len(task.expected_output_keys), 1)

                bench_result = BenchmarkResult(
                    task_id=task.task_id,
                    agent_role=agent.role.value,
                    runtime_seconds=round(elapsed, 3),
                    success=result.status.value == "completed",
                    output_keys=output_keys,
                    score=score,
                )
            except Exception as exc:
                elapsed = time.perf_counter() - start
                bench_result = BenchmarkResult(
                    task_id=task.task_id,
                    agent_role=agent.role.value,
                    runtime_seconds=round(elapsed, 3),
                    success=False,
                    score=0.0,
                )
                logger.exception("Benchmark task %s failed", task.name)

            results.append(bench_result)

        self._results.extend(results)
        return results

    @property
    def all_results(self) -> list[BenchmarkResult]:
        return list(self._results)
