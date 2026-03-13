"""Base MCP server framework for OARL tool exposure."""

from __future__ import annotations

import abc
import logging
from dataclasses import dataclass, field
from typing import Any

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class ToolDefinition:
    """Describes a single tool exposed by an MCP server."""

    name: str
    description: str
    parameters: dict[str, Any] = field(default_factory=dict)


@dataclass
class ToolCallResult:
    """Result from executing an MCP tool."""

    success: bool = True
    data: dict[str, Any] = field(default_factory=dict)
    error: str | None = None


class BaseMCPServer(abc.ABC):
    """Abstract base class for MCP-compliant tool servers.

    Each server exposes a set of tools that agents can discover
    and invoke via the MCP protocol.
    """

    def __init__(self, server_name: str) -> None:
        self.server_name = server_name
        self._tools: dict[str, ToolDefinition] = {}
        self._logger = logging.getLogger(f"oarl.mcp.{server_name}")

    def register_tool(self, tool: ToolDefinition) -> None:
        """Register a tool with this server."""
        self._tools[tool.name] = tool

    def list_tools(self) -> list[ToolDefinition]:
        """Return all tools this server exposes."""
        return list(self._tools.values())

    def get_tool(self, name: str) -> ToolDefinition:
        """Look up a tool by name."""
        if name not in self._tools:
            raise KeyError(f"Tool not found: {name}")
        return self._tools[name]

    @abc.abstractmethod
    async def call_tool(self, tool_name: str, arguments: dict[str, Any]) -> ToolCallResult:
        """Invoke a tool by name with the given arguments."""

    def to_dict(self) -> dict[str, Any]:
        """Serialize server metadata for discovery."""
        return {
            "server_name": self.server_name,
            "tools": [{"name": t.name, "description": t.description} for t in self._tools.values()],
        }
