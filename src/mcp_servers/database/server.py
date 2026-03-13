"""MCP Server: Database — SQL query execution via SQLAlchemy."""

from __future__ import annotations

from typing import Any

from src.mcp_servers.base.server import BaseMCPServer, ToolCallResult, ToolDefinition


class DatabaseServer(BaseMCPServer):
    """Executes SQL queries against configured databases."""

    def __init__(self, connection_string: str = "sqlite:///oarl.db") -> None:
        super().__init__("database")
        self._conn_str = connection_string
        self.register_tool(ToolDefinition("execute_query", "Execute a SQL query"))
        self.register_tool(ToolDefinition("list_tables", "List all tables"))
        self.register_tool(ToolDefinition("describe_table", "Describe a table schema"))

    async def call_tool(self, tool_name: str, arguments: dict[str, Any]) -> ToolCallResult:
        handlers = {
            "execute_query": self._execute_query,
            "list_tables": self._list_tables,
            "describe_table": self._describe_table,
        }
        handler = handlers.get(tool_name)
        if not handler:
            return ToolCallResult(success=False, error=f"Unknown tool: {tool_name}")
        return handler(arguments)

    def _execute_query(self, args: dict[str, Any]) -> ToolCallResult:
        try:
            from sqlalchemy import create_engine, text

            engine = create_engine(self._conn_str)
            with engine.connect() as conn:
                result = conn.execute(text(args.get("query", "")))
                rows = [dict(row._mapping) for row in result]
            return ToolCallResult(data={"rows": rows, "row_count": len(rows)})
        except Exception as exc:
            return ToolCallResult(success=False, error=str(exc))

    def _list_tables(self, args: dict[str, Any]) -> ToolCallResult:
        try:
            from sqlalchemy import create_engine, inspect

            engine = create_engine(self._conn_str)
            inspector = inspect(engine)
            tables = inspector.get_table_names()
            return ToolCallResult(data={"tables": tables})
        except Exception as exc:
            return ToolCallResult(success=False, error=str(exc))

    def _describe_table(self, args: dict[str, Any]) -> ToolCallResult:
        try:
            from sqlalchemy import create_engine, inspect

            engine = create_engine(self._conn_str)
            inspector = inspect(engine)
            columns = inspector.get_columns(args.get("table", ""))
            col_info = [{"name": c["name"], "type": str(c["type"])} for c in columns]
            return ToolCallResult(data={"columns": col_info})
        except Exception as exc:
            return ToolCallResult(success=False, error=str(exc))
