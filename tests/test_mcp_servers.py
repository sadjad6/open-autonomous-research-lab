"""Tests for MCP servers."""

from __future__ import annotations

import pytest

from src.mcp_servers.base.server import BaseMCPServer, ToolCallResult, ToolDefinition
from src.mcp_servers.filesystem.server import FilesystemServer
from src.mcp_servers.python_executor.server import PythonExecutorServer


class MockMCPServer(BaseMCPServer):
    def __init__(self) -> None:
        super().__init__("mock")
        self.register_tool(ToolDefinition("test_tool", "A test tool"))

    async def call_tool(self, tool_name: str, arguments: dict) -> ToolCallResult:
        if tool_name == "test_tool":
            return ToolCallResult(data={"result": "ok"})
        return ToolCallResult(success=False, error="Unknown tool")


def test_server_list_tools() -> None:
    server = MockMCPServer()
    tools = server.list_tools()
    assert len(tools) == 1
    assert tools[0].name == "test_tool"


@pytest.mark.asyncio
async def test_server_call_tool() -> None:
    server = MockMCPServer()
    result = await server.call_tool("test_tool", {})
    assert result.success is True
    assert result.data["result"] == "ok"


@pytest.mark.asyncio
async def test_server_unknown_tool() -> None:
    server = MockMCPServer()
    result = await server.call_tool("bad_tool", {})
    assert result.success is False


@pytest.mark.asyncio
async def test_python_executor_code() -> None:
    server = PythonExecutorServer()
    result = await server.call_tool("execute_code", {"code": "x = 1 + 1"})
    assert result.success is True


@pytest.mark.asyncio
async def test_filesystem_list_dir() -> None:
    server = FilesystemServer(".")
    result = await server.call_tool("list_directory", {"path": "."})
    assert result.success is True
    assert "entries" in result.data
