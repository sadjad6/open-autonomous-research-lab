# 🔬 Open Autonomous Research Lab (OARL)

[![CI](https://github.com/sadjad6/open-autonomous-research-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/sadjad6/open-autonomous-research-lab/actions)
[![Python 3.12](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Open-source prototype for structured data-analysis and ML workflows.** Its FastAPI route invokes an orchestrator with a fixed seven-role pipeline for dataset preparation, basic analysis, baseline model comparison, evaluation summaries, and a templated report. The repository also contains skill, tool-server, memory, and MLflow components at different stages of integration.

---

## ✨ Key Features

| Component | Current status |
|-----------|----------------|
| **Agent workflow** | FastAPI invokes an orchestrator that runs seven roles in a fixed sequence; additional agent classes are registered but not called by that default route. |
| **Skills** | The tree contains 95 built-in skill packages and 5 marketplace plugin packages. The inspected skill examples return placeholder results; the default API route does not execute the skill registry. |
| **Tool servers** | Seven server modules expose local `list_tools` / `call_tool` methods. The default workflow does not call them, and MCP protocol transport is not established by the current code. |
| **Memory** | A ChromaDB-backed vector-store module is present. API initialization depends on the optional `vector` extra. |
| **MLflow** | A tracking wrapper and a Docker Compose service are present; the default analysis route does not log runs. |
| **REST API** | FastAPI exposes analysis, agent-list, and health routes. |
| **Streamlit UI** | Dataset preview and demonstration results are available; the UI does not invoke the analysis API. |
| **Docker Compose** | Defines API, UI, and MLflow services; deployment and cross-service behavior are not demonstrated here. |

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/sadjad6/open-autonomous-research-lab.git
cd open-autonomous-research-lab

# Install dependencies
uv sync --extra vector

# Generate demo datasets
uv run python scripts/generate_datasets.py

# Copy and configure environment
cp .env.example .env
```

### Run the API

```bash
uv run uvicorn src.api.main:app --reload --port 8000
# Visit: http://localhost:8000/docs
```

### Run the UI

```bash
uv run streamlit run src/ui/app.py
# Visit: http://localhost:8501
# The current UI previews uploads and shows demonstration results; it does not call /api/analyze.
```

### Run with Docker

```bash
docker compose up -d
# API: http://localhost:8000
# UI:  http://localhost:8501
# MLflow: http://localhost:5000
```

---

## 🏗️ Architecture

```text
FastAPI /api/analyze → Orchestrator
                          ↓
Planner → Data Engineer → Data Scientist → ML Engineer
                          ↓
Evaluation → Research Analyst → Knowledge Manager
```

The orchestrator uses a fixed role sequence. Individual agents implement a plan → execute → evaluate → improve loop, but the default workflow does not execute the skill registry or tool-server modules. The report is assembled from templates, and model comparison uses baseline scikit-learn classifiers.

## 📡 API Usage

```bash
# Trigger an analysis pipeline
curl -X POST http://localhost:8000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"request": "Analyze customer churn patterns", "dataset_path": "datasets/customer_churn.csv", "target_column": "churn"}'

# List available agents
curl http://localhost:8000/api/agents

# Check health
curl http://localhost:8000/health
```

---

## 🧪 Testing

```bash
# Run all tests
uv run pytest tests/ -v

# Run with coverage
uv run pytest tests/ -v --cov=src

# Lint
uv run ruff check src/

# Type check
uv run mypy src/ --ignore-missing-imports
```

---

## 📁 Repository Structure

```
src/
├── agents/          # Agent roles and fixed orchestration pipeline
├── skills/          # Skill packages and registry scaffold
├── mcp_servers/     # Local tool-server modules
├── memory/          # Vector store, knowledge base, archive
├── evaluation/      # Metrics helpers and MLflow wrapper
├── api/             # FastAPI REST endpoints
├── ui/              # Streamlit demonstration interface
├── observability/   # Structured logging
└── config/          # Pydantic settings
```

---

## 📄 License

[MIT](LICENSE)


