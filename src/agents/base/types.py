"""Shared type definitions for the OARL agent ecosystem."""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import StrEnum
from typing import Any


class AgentRole(StrEnum):
    """Roles available in the OARL agent ecosystem."""

    ORCHESTRATOR = "orchestrator"
    PLANNER = "planner"
    DATA_ENGINEER = "data_engineer"
    DATA_SCIENTIST = "data_scientist"
    ML_ENGINEER = "ml_engineer"
    RESEARCH_ANALYST = "research_analyst"
    EVALUATION = "evaluation"
    KNOWLEDGE_MANAGER = "knowledge_manager"
    INFRASTRUCTURE = "infrastructure"


class TaskStatus(StrEnum):
    """Lifecycle states for agent tasks."""

    PENDING = "pending"
    PLANNING = "planning"
    IN_PROGRESS = "in_progress"
    WAITING = "waiting"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class MessageType(StrEnum):
    """Types of inter-agent messages."""

    TASK_REQUEST = "task_request"
    TASK_RESULT = "task_result"
    STATUS_UPDATE = "status_update"
    DATA_TRANSFER = "data_transfer"
    ERROR = "error"
    QUERY = "query"
    RESPONSE = "response"


def _utcnow() -> datetime:
    return datetime.now(UTC)


def _new_id() -> str:
    return uuid.uuid4().hex[:12]


@dataclass(frozen=True)
class AgentMessage:
    """Message exchanged between agents."""

    sender: AgentRole
    receiver: AgentRole
    message_type: MessageType
    payload: dict[str, Any]
    message_id: str = field(default_factory=_new_id)
    timestamp: datetime = field(default_factory=_utcnow)
    correlation_id: str | None = None


@dataclass
class TaskResult:
    """Result produced by an agent after executing a task."""

    task_id: str
    agent_role: AgentRole
    status: TaskStatus
    output: dict[str, Any] = field(default_factory=dict)
    metrics: dict[str, float] = field(default_factory=dict)
    artifacts: list[str] = field(default_factory=list)
    error: str | None = None
    started_at: datetime = field(default_factory=_utcnow)
    completed_at: datetime | None = None


@dataclass
class ExecutionPlan:
    """A step-by-step execution plan created by the Planner agent."""

    plan_id: str = field(default_factory=_new_id)
    objective: str = ""
    steps: list[PlanStep] = field(default_factory=list)
    created_at: datetime = field(default_factory=_utcnow)


@dataclass
class PlanStep:
    """A single step within an execution plan."""

    step_id: str = field(default_factory=_new_id)
    description: str = ""
    agent_role: AgentRole = AgentRole.ORCHESTRATOR
    skills: list[str] = field(default_factory=list)
    dependencies: list[str] = field(default_factory=list)
    status: TaskStatus = TaskStatus.PENDING
    result: TaskResult | None = None


@dataclass
class DatasetMetadata:
    """Metadata describing a dataset in the system."""

    dataset_id: str = field(default_factory=_new_id)
    name: str = ""
    path: str = ""
    format: str = "csv"
    num_rows: int = 0
    num_columns: int = 0
    columns: list[str] = field(default_factory=list)
    dtypes: dict[str, str] = field(default_factory=dict)
    size_bytes: int = 0
    created_at: datetime = field(default_factory=_utcnow)


@dataclass
class ExperimentRecord:
    """Record of a single ML experiment."""

    experiment_id: str = field(default_factory=_new_id)
    name: str = ""
    model_type: str = ""
    parameters: dict[str, Any] = field(default_factory=dict)
    metrics: dict[str, float] = field(default_factory=dict)
    dataset_id: str = ""
    artifacts: list[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=_utcnow)


@dataclass
class ResearchReport:
    """A generated research report."""

    report_id: str = field(default_factory=_new_id)
    title: str = ""
    sections: list[ReportSection] = field(default_factory=list)
    created_at: datetime = field(default_factory=_utcnow)


@dataclass
class ReportSection:
    """A section within a research report."""

    heading: str = ""
    content: str = ""
    charts: list[str] = field(default_factory=list)
    tables: list[dict[str, Any]] = field(default_factory=list)
