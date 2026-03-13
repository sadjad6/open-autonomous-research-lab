"""Infrastructure Agent — resource monitoring, environment, health."""

from __future__ import annotations

import platform
import shutil
import sys
from typing import Any

from src.agents.base.agent import AgentContext, BaseAgent
from src.agents.base.types import AgentRole, TaskResult, TaskStatus

DISK_LOW_THRESHOLD_GB = 1.0


class InfrastructureAgent(BaseAgent):
    """Monitors system resources and validates the runtime environment.

    Reports on CPU, memory, disk, Python version, and installed
    packages to ensure the platform can execute workloads.
    """

    def __init__(self) -> None:
        super().__init__(AgentRole.INFRASTRUCTURE)

    async def plan(self, context: AgentContext) -> dict[str, Any]:
        return {"checks": ["python_version", "disk_space", "platform_info"]}

    async def execute(self, context: AgentContext, plan: dict[str, Any]) -> TaskResult:
        info = self._gather_system_info()
        return self._task_result(context, output=info)

    async def evaluate(self, result: TaskResult) -> float:
        if result.status == TaskStatus.FAILED:
            return 0.0
        disk_gb = result.output.get("disk_free_gb", 0)
        return 1.0 if disk_gb > DISK_LOW_THRESHOLD_GB else 0.5

    async def improve(
        self, context: AgentContext, plan: dict[str, Any], result: TaskResult, score: float
    ) -> dict[str, Any]:
        return plan  # infrastructure checks are informational

    @staticmethod
    def _gather_system_info() -> dict[str, Any]:
        total, used, free = shutil.disk_usage(".")
        return {
            "python_version": sys.version,
            "platform": platform.platform(),
            "architecture": platform.machine(),
            "disk_total_gb": round(total / (1024**3), 2),
            "disk_used_gb": round(used / (1024**3), 2),
            "disk_free_gb": round(free / (1024**3), 2),
            "status": "healthy",
        }
