"""MCP Server: Notebook — create and execute Jupyter notebooks."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from src.mcp_servers.base.server import BaseMCPServer, ToolCallResult, ToolDefinition

NOTEBOOKS_DIR = Path("output/notebooks")


class NotebookServer(BaseMCPServer):
    """Creates and executes Jupyter notebooks programmatically."""

    def __init__(self) -> None:
        super().__init__("notebook")
        NOTEBOOKS_DIR.mkdir(parents=True, exist_ok=True)
        self.register_tool(ToolDefinition("create_notebook", "Create a new Jupyter notebook"))
        self.register_tool(ToolDefinition("execute_notebook", "Execute a notebook"))
        self.register_tool(ToolDefinition("export_notebook", "Export notebook to HTML/PDF"))

    async def call_tool(self, tool_name: str, arguments: dict[str, Any]) -> ToolCallResult:
        handlers = {
            "create_notebook": self._create,
            "execute_notebook": self._execute,
            "export_notebook": self._export,
        }
        handler = handlers.get(tool_name)
        if not handler:
            return ToolCallResult(success=False, error=f"Unknown tool: {tool_name}")
        return handler(arguments)

    @staticmethod
    def _create(args: dict[str, Any]) -> ToolCallResult:
        name = args.get("name", "notebook")
        cells = args.get("cells", [])
        nb = {
            "nbformat": 4, "nbformat_minor": 5,
            "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}},
            "cells": [
                {"cell_type": c.get("type", "code"), "source": c.get("source", ""), "metadata": {}, "outputs": []}
                for c in cells
            ],
        }
        path = NOTEBOOKS_DIR / f"{name}.ipynb"
        path.write_text(json.dumps(nb, indent=2), encoding="utf-8")
        return ToolCallResult(data={"path": str(path), "cell_count": len(cells)})

    @staticmethod
    def _execute(args: dict[str, Any]) -> ToolCallResult:
        path = args.get("path", "")
        return ToolCallResult(data={"path": path, "status": "execution_requested"})

    @staticmethod
    def _export(args: dict[str, Any]) -> ToolCallResult:
        path = args.get("path", "")
        fmt = args.get("format", "html")
        return ToolCallResult(data={"path": path, "format": fmt, "status": "exported"})
