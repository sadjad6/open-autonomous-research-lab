"""Structured logging and observability for OARL."""

from __future__ import annotations

import logging
import sys
from datetime import datetime, timezone
from typing import Any

import structlog


def setup_logging(level: str = "INFO") -> None:
    """Configure structured logging for the platform."""
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.dev.ConsoleRenderer(),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(
            getattr(logging, level.upper(), logging.INFO),
        ),
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(),
    )

    # Also configure stdlib logging for third-party libs
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        level=getattr(logging, level.upper(), logging.INFO),
        stream=sys.stdout,
    )


class ActivityTracker:
    """Tracks agent activity, skill usage, and MCP tool calls."""

    def __init__(self) -> None:
        self._events: list[dict[str, Any]] = []
        self._logger = structlog.get_logger("oarl.activity")

    def log_agent_activity(self, agent_role: str, action: str, details: dict[str, Any] | None = None) -> None:
        event = self._build_event("agent_activity", agent_role=agent_role, action=action, details=details)
        self._events.append(event)
        self._logger.info("agent_activity", agent=agent_role, action=action)

    def log_skill_usage(self, skill_name: str, domain: str, duration_ms: float) -> None:
        event = self._build_event("skill_usage", skill=skill_name, domain=domain, duration_ms=duration_ms)
        self._events.append(event)
        self._logger.info("skill_usage", skill=skill_name, duration_ms=round(duration_ms, 1))

    def log_mcp_call(self, server: str, tool: str, duration_ms: float) -> None:
        event = self._build_event("mcp_call", server=server, tool=tool, duration_ms=duration_ms)
        self._events.append(event)
        self._logger.info("mcp_call", server=server, tool=tool, duration_ms=round(duration_ms, 1))

    def get_events(self, event_type: str | None = None) -> list[dict[str, Any]]:
        if event_type:
            return [e for e in self._events if e["type"] == event_type]
        return list(self._events)

    @staticmethod
    def _build_event(event_type: str, **kwargs: Any) -> dict[str, Any]:
        return {
            "type": event_type,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            **{k: v for k, v in kwargs.items() if v is not None},
        }
