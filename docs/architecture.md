# OARL Architecture

## System Layers

### 1. User Interface Layer
- **Streamlit UI** — Interactive web interface for dataset upload, analysis requests, and report viewing.
- **REST API** — FastAPI endpoints for programmatic access.

### 2. Agent Orchestration Layer
Nine specialized agents coordinate using an async message bus:

| Agent | Role |
|-------|------|
| Orchestrator | Decomposes requests, delegates to pipeline, merges results |
| Planner | Creates step-by-step execution plans with skill assignments |
| Data Engineer | Ingests, validates, cleans, and transforms data |
| Data Scientist | Performs EDA, statistical analysis, generates insights |
| ML Engineer | Trains models, tunes hyperparameters, runs cross-validation |
| Research Analyst | Synthesizes findings into structured research reports |
| Evaluation | Computes metrics, detects drift, checks fairness |
| Knowledge Manager | Stores insights and experiments in persistent memory |
| Infrastructure | Monitors resources, validates environment health |

### 3. Skill Execution Layer
100+ modular skills organized by domain. Each skill has:
- A Python implementation (`__init__.py`)
- Documentation (`SKILL.md`)
- Standard `SkillInput` / `SkillOutput` interface

### 4. MCP Tool Layer
Seven MCP-compliant servers expose tools via a standard protocol:
- Python Executor, Filesystem, Database, Visualization
- Web Search, Dataset Registry, Notebook

### 5. Infrastructure Layer
- **Memory**: ChromaDB vector store + JSONL knowledge base
- **Tracking**: MLflow experiment logging
- **Observability**: Structured logging with structlog

## Reasoning Loop
Every agent implements the autonomous improvement loop:
```
plan → execute → evaluate → improve (repeat if score < threshold)
```

## Communication
Agents communicate via `MessageBus` using typed `AgentMessage` objects with correlation IDs for request tracking.
