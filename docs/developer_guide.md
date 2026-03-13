# OARL Developer Guide

## Setup

```bash
# Install all dependencies (including dev tools)
uv sync --extra dev

# Set up pre-commit hooks
uv run pre-commit install

# Copy environment template
cp .env.example .env
```

## Adding a New Agent

1. Create `src/agents/your_agent.py`
2. Extend `BaseAgent` and implement:
   - `plan()` — create a strategy
   - `execute()` — run the strategy
   - `evaluate()` — score the result (0.0–1.0)
   - `improve()` — refine the strategy based on score
3. Register in `src/api/routes/workflows.py`

## Adding a New Skill

1. Create `src/skills/<domain>/<skill_name>/`
2. Add `__init__.py` with a `Skill` class extending `BaseSkill`
3. Add `SKILL.md` with documentation
4. The skill registry auto-discovers skills at startup

Or use the marketplace:
1. Drop your skill into `skills_marketplace/plugins/<name>/`
2. It will be auto-discovered and loaded

## Adding a New MCP Server

1. Create `src/mcp_servers/<server_name>/server.py`
2. Extend `BaseMCPServer`
3. Register tools with `register_tool(ToolDefinition(...))`
4. Implement `call_tool()` to handle invocations

## Code Quality

```bash
# Lint
uv run ruff check src/

# Format
uv run ruff format src/

# Type check
uv run mypy src/ --ignore-missing-imports

# Test
uv run pytest tests/ -v
```

## Configuration

All settings are loaded from environment variables with the `OARL_` prefix.
See `.env.example` for available options.
