"""MCP Server: Dataset Registry — manage datasets in the platform."""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from typing import Any

from src.agents.base.types import DatasetMetadata
from src.mcp_servers.base.server import BaseMCPServer, ToolCallResult, ToolDefinition

REGISTRY_FILE = Path("memory/dataset_registry.json")


class DatasetRegistryServer(BaseMCPServer):
    """Manages the catalog of datasets available in the platform."""

    def __init__(self) -> None:
        super().__init__("dataset_registry")
        self.register_tool(ToolDefinition("register_dataset", "Register a new dataset"))
        self.register_tool(ToolDefinition("list_datasets", "List all registered datasets"))
        self.register_tool(ToolDefinition("get_dataset_info", "Get details of a dataset"))

    async def call_tool(self, tool_name: str, arguments: dict[str, Any]) -> ToolCallResult:
        handlers = {
            "register_dataset": self._register,
            "list_datasets": self._list,
            "get_dataset_info": self._get_info,
        }
        handler = handlers.get(tool_name)
        if not handler:
            return ToolCallResult(success=False, error=f"Unknown tool: {tool_name}")
        return handler(arguments)

    def _load_registry(self) -> list[dict[str, Any]]:
        if not REGISTRY_FILE.exists():
            return []
        return json.loads(REGISTRY_FILE.read_text(encoding="utf-8"))

    def _save_registry(self, entries: list[dict[str, Any]]) -> None:
        REGISTRY_FILE.parent.mkdir(parents=True, exist_ok=True)
        REGISTRY_FILE.write_text(json.dumps(entries, default=str, indent=2), encoding="utf-8")

    def _register(self, args: dict[str, Any]) -> ToolCallResult:
        entries = self._load_registry()
        meta = DatasetMetadata(
            name=args.get("name", "unnamed"),
            path=args.get("path", ""),
            format=args.get("format", "csv"),
        )
        entries.append(asdict(meta))
        self._save_registry(entries)
        return ToolCallResult(data={"dataset_id": meta.dataset_id, "registered": True})

    def _list(self, args: dict[str, Any]) -> ToolCallResult:
        entries = self._load_registry()
        return ToolCallResult(data={"datasets": entries, "count": len(entries)})

    def _get_info(self, args: dict[str, Any]) -> ToolCallResult:
        dataset_id = args.get("dataset_id", "")
        for entry in self._load_registry():
            if entry.get("dataset_id") == dataset_id:
                return ToolCallResult(data=entry)
        return ToolCallResult(success=False, error=f"Dataset not found: {dataset_id}")
