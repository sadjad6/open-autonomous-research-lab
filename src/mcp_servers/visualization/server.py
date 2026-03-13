"""MCP Server: Visualization — chart generation via Matplotlib/Plotly."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from src.mcp_servers.base.server import BaseMCPServer, ToolCallResult, ToolDefinition

OUTPUT_DIR = Path("output/charts")


class VisualizationServer(BaseMCPServer):
    """Generates charts and dashboards for agents."""

    def __init__(self) -> None:
        super().__init__("visualization")
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        self.register_tool(ToolDefinition("create_chart", "Create a chart from data"))
        self.register_tool(ToolDefinition("create_dashboard", "Create a multi-panel dashboard"))
        self.register_tool(ToolDefinition("export_chart", "Export a chart to file"))

    async def call_tool(self, tool_name: str, arguments: dict[str, Any]) -> ToolCallResult:
        handlers = {
            "create_chart": self._create_chart,
            "create_dashboard": self._create_dashboard,
            "export_chart": self._export_chart,
        }
        handler = handlers.get(tool_name)
        if not handler:
            return ToolCallResult(success=False, error=f"Unknown tool: {tool_name}")
        return handler(arguments)

    @staticmethod
    def _create_chart(args: dict[str, Any]) -> ToolCallResult:
        try:
            import matplotlib.pyplot as plt

            chart_type = args.get("type", "bar")
            title = args.get("title", "Chart")
            data = args.get("data", {})

            fig, ax = plt.subplots(figsize=(10, 6))
            if chart_type == "bar":
                ax.bar(range(len(data.get("values", []))), data.get("values", []))
            elif chart_type == "line":
                ax.plot(data.get("values", []))
            ax.set_title(title)

            filename = f"{title.lower().replace(' ', '_')}.png"
            path = OUTPUT_DIR / filename
            fig.savefig(path, dpi=150, bbox_inches="tight")
            plt.close(fig)
            return ToolCallResult(data={"path": str(path), "type": chart_type})
        except Exception as exc:
            return ToolCallResult(success=False, error=str(exc))

    @staticmethod
    def _create_dashboard(args: dict[str, Any]) -> ToolCallResult:
        panels = args.get("panels", [])
        return ToolCallResult(data={"panels": len(panels), "status": "created"})

    @staticmethod
    def _export_chart(args: dict[str, Any]) -> ToolCallResult:
        path = args.get("path", "")
        fmt = args.get("format", "png")
        return ToolCallResult(data={"exported": path, "format": fmt})
