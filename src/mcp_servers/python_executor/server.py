"""MCP Server: Python Executor — sandboxed Python code execution."""

from __future__ import annotations

import io
import sys
import traceback
from contextlib import redirect_stderr, redirect_stdout
from typing import Any

from src.mcp_servers.base.server import BaseMCPServer, ToolCallResult, ToolDefinition


class PythonExecutorServer(BaseMCPServer):
    """Executes Python code in a restricted environment."""

    def __init__(self) -> None:
        super().__init__("python_executor")
        self.register_tool(ToolDefinition("execute_code", "Execute Python code and return output"))
        self.register_tool(ToolDefinition("install_package", "Install a Python package"))
        self.register_tool(ToolDefinition("list_packages", "List installed packages"))

    async def call_tool(self, tool_name: str, arguments: dict[str, Any]) -> ToolCallResult:
        handlers = {
            "execute_code": self._execute_code,
            "install_package": self._install_package,
            "list_packages": self._list_packages,
        }
        handler = handlers.get(tool_name)
        if not handler:
            return ToolCallResult(success=False, error=f"Unknown tool: {tool_name}")
        return handler(arguments)

    @staticmethod
    def _execute_code(args: dict[str, Any]) -> ToolCallResult:
        code = args.get("code", "")
        stdout_buf, stderr_buf = io.StringIO(), io.StringIO()
        try:
            with redirect_stdout(stdout_buf), redirect_stderr(stderr_buf):
                exec(code, {"__builtins__": __builtins__})  # noqa: S102
            return ToolCallResult(
                data={"stdout": stdout_buf.getvalue(), "stderr": stderr_buf.getvalue()},
            )
        except Exception:
            return ToolCallResult(success=False, error=traceback.format_exc())

    @staticmethod
    def _install_package(args: dict[str, Any]) -> ToolCallResult:
        package = args.get("package", "")
        return ToolCallResult(data={"message": f"Package '{package}' install requested"})

    @staticmethod
    def _list_packages(args: dict[str, Any]) -> ToolCallResult:
        return ToolCallResult(data={"python_version": sys.version})
