"""MCP Server: Filesystem — file read/write/list operations."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from src.mcp_servers.base.server import BaseMCPServer, ToolCallResult, ToolDefinition

MAX_READ_SIZE = 1_000_000  # 1 MB


class FilesystemServer(BaseMCPServer):
    """Provides safe filesystem access to agents."""

    def __init__(self, base_dir: str = ".") -> None:
        super().__init__("filesystem")
        self._base = Path(base_dir).resolve()
        self.register_tool(ToolDefinition("read_file", "Read a file's contents"))
        self.register_tool(ToolDefinition("write_file", "Write content to a file"))
        self.register_tool(ToolDefinition("list_directory", "List directory contents"))
        self.register_tool(ToolDefinition("delete_file", "Delete a file"))

    async def call_tool(self, tool_name: str, arguments: dict[str, Any]) -> ToolCallResult:
        handlers = {
            "read_file": self._read_file,
            "write_file": self._write_file,
            "list_directory": self._list_directory,
            "delete_file": self._delete_file,
        }
        handler = handlers.get(tool_name)
        if not handler:
            return ToolCallResult(success=False, error=f"Unknown tool: {tool_name}")
        return handler(arguments)

    def _resolve(self, path: str) -> Path:
        resolved = (self._base / path).resolve()
        if not str(resolved).startswith(str(self._base)):
            raise PermissionError("Path traversal not allowed")
        return resolved

    def _read_file(self, args: dict[str, Any]) -> ToolCallResult:
        try:
            path = self._resolve(args.get("path", ""))
            content = path.read_text(encoding="utf-8")[:MAX_READ_SIZE]
            return ToolCallResult(data={"content": content, "size": path.stat().st_size})
        except Exception as exc:
            return ToolCallResult(success=False, error=str(exc))

    def _write_file(self, args: dict[str, Any]) -> ToolCallResult:
        try:
            path = self._resolve(args.get("path", ""))
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(args.get("content", ""), encoding="utf-8")
            return ToolCallResult(data={"path": str(path), "written": True})
        except Exception as exc:
            return ToolCallResult(success=False, error=str(exc))

    def _list_directory(self, args: dict[str, Any]) -> ToolCallResult:
        try:
            path = self._resolve(args.get("path", "."))
            entries = [{"name": e.name, "is_dir": e.is_dir()} for e in sorted(path.iterdir())]
            return ToolCallResult(data={"entries": entries, "count": len(entries)})
        except Exception as exc:
            return ToolCallResult(success=False, error=str(exc))

    def _delete_file(self, args: dict[str, Any]) -> ToolCallResult:
        try:
            path = self._resolve(args.get("path", ""))
            path.unlink()
            return ToolCallResult(data={"deleted": str(path)})
        except Exception as exc:
            return ToolCallResult(success=False, error=str(exc))
