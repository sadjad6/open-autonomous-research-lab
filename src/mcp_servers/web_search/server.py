"""MCP Server: Web Search — search the web and extract content."""

from __future__ import annotations

from typing import Any

from src.mcp_servers.base.server import BaseMCPServer, ToolCallResult, ToolDefinition


class WebSearchServer(BaseMCPServer):
    """Provides web search capabilities to agents."""

    def __init__(self) -> None:
        super().__init__("web_search")
        self.register_tool(ToolDefinition("search", "Search the web for a query"))
        self.register_tool(ToolDefinition("fetch_page", "Fetch content from a URL"))
        self.register_tool(ToolDefinition("extract_content", "Extract structured content from a page"))

    async def call_tool(self, tool_name: str, arguments: dict[str, Any]) -> ToolCallResult:
        handlers = {
            "search": self._search,
            "fetch_page": self._fetch_page,
            "extract_content": self._extract_content,
        }
        handler = handlers.get(tool_name)
        if not handler:
            return ToolCallResult(success=False, error=f"Unknown tool: {tool_name}")
        return await handler(arguments)

    @staticmethod
    async def _search(args: dict[str, Any]) -> ToolCallResult:
        query = args.get("query", "")
        # In production this would call a search API
        return ToolCallResult(data={"query": query, "results": [], "note": "Configure search API key"})

    @staticmethod
    async def _fetch_page(args: dict[str, Any]) -> ToolCallResult:
        url = args.get("url", "")
        try:
            import httpx

            async with httpx.AsyncClient() as client:
                resp = await client.get(url, timeout=10.0)
                return ToolCallResult(data={"url": url, "status": resp.status_code, "length": len(resp.text)})
        except Exception as exc:
            return ToolCallResult(success=False, error=str(exc))

    @staticmethod
    async def _extract_content(args: dict[str, Any]) -> ToolCallResult:
        return ToolCallResult(data={"content": args.get("html", "")[:1000]})
