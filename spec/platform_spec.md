# OARL Platform Specification

## 1. Project Vision

**Open Autonomous Research Lab (OARL)** is an open-source platform where multiple specialized AI agents collaborate to perform autonomous data analysis, machine learning experimentation, research discovery, and report generation.

A user provides a dataset and a natural-language research question. OARL autonomously plans an analysis pipeline, executes it through coordinated agents, evaluates results, and produces a comprehensive research report — all without manual intervention.

---

## 2. Architecture Overview

```
┌─────────────────────────────────────────┐
│           User Interface Layer          │
│         (Streamlit / REST API)          │
├─────────────────────────────────────────┤
│         API Gateway (FastAPI)           │
├─────────────────────────────────────────┤
│      Agent Orchestration Layer          │
│  ┌───────┐ ┌───────┐ ┌──────────────┐  │
│  │Orch.  │ │Planner│ │Data Engineer │  │
│  │Agent  │ │Agent  │ │Agent         │  │
│  └───────┘ └───────┘ └──────────────┘  │
│  ┌───────┐ ┌───────┐ ┌──────────────┐  │
│  │Data   │ │ML     │ │Research      │  │
│  │Sci.   │ │Eng.   │ │Analyst Agent │  │
│  └───────┘ └───────┘ └──────────────┘  │
│  ┌───────┐ ┌───────┐ ┌──────────────┐  │
│  │Eval   │ │Know.  │ │Infrastructure│  │
│  │Agent  │ │Mgr    │ │Agent         │  │
│  └───────┘ └───────┘ └──────────────┘  │
├─────────────────────────────────────────┤
│       Skill Execution Layer             │
│   100+ modular skills organized by      │
│   domain (data eng, ML, viz, etc.)      │
├─────────────────────────────────────────┤
│          MCP Tool Layer                 │
│  Python │ FS │ DB │ Viz │ Search │ ...  │
├─────────────────────────────────────────┤
│       Infrastructure Layer              │
│  Memory │ MLflow │ Logging │ Config     │
└─────────────────────────────────────────┘
```

---

## 3. Agent Responsibilities

| Agent | Responsibility |
|-------|---------------|
| **Orchestrator** | Decomposes user requests, delegates to specialists, manages pipeline |
| **Planner** | Creates step-by-step execution plans with dependencies |
| **Data Engineer** | Data ingestion, cleaning, transformation, feature engineering |
| **Data Scientist** | EDA, statistical analysis, hypothesis testing, insights |
| **ML Engineer** | Model training, tuning, cross-validation, selection |
| **Research Analyst** | Report writing, insight synthesis, recommendations |
| **Evaluation** | Model evaluation, metrics, drift detection, fairness |
| **Knowledge Manager** | Memory management, knowledge indexing, retrieval |
| **Infrastructure** | Resource monitoring, environment setup, health checks |

---

## 4. Data Flow

```
User Request → Orchestrator → Planner (creates plan)
                                ↓
                    Data Engineer (ingest & clean)
                                ↓
                    Data Scientist (EDA & stats)
                                ↓
                    ML Engineer (train & tune)
                                ↓
                    Evaluation Agent (evaluate)
                                ↓
                    Research Analyst (report)
                                ↓
                    Knowledge Manager (store)
                                ↓
                         User ← Final Report
```

---

## 5. Functional Requirements

- **FR-01**: Accept datasets via file upload or API
- **FR-02**: Parse natural-language research requests
- **FR-03**: Generate execution plans automatically
- **FR-04**: Execute data cleaning and transformation pipelines
- **FR-05**: Perform exploratory data analysis with visualizations
- **FR-06**: Train multiple ML models and compare performance
- **FR-07**: Run hyperparameter optimization
- **FR-08**: Evaluate models with standard metrics
- **FR-09**: Detect data drift and model fairness issues
- **FR-10**: Generate comprehensive research reports
- **FR-11**: Store results in persistent memory
- **FR-12**: Track experiments via MLflow
- **FR-13**: Expose functionality via REST API
- **FR-14**: Provide an interactive Streamlit UI

---

## 6. Non-Functional Requirements

- **NFR-01**: Modular architecture — each component independently deployable
- **NFR-02**: Response time < 5s for API health checks
- **NFR-03**: Support datasets up to 1GB in memory
- **NFR-04**: Structured logging for all agent activities
- **NFR-05**: Type-safe codebase with full type hints
- **NFR-06**: Test coverage > 70%
- **NFR-07**: Python 3.12 compatible

---

## 7. Scalability Considerations

- Agent communication via async message bus (expandable to Redis/Kafka)
- Skill registry supports hot-loading of new skills at runtime
- MCP servers can run as separate processes or containers
- Memory system backed by vector DB (ChromaDB, swappable to Pinecone/Weaviate)
- Stateless API layer supports horizontal scaling

---

## 8. Security Considerations

- No hardcoded secrets — all credentials via environment variables
- Sandboxed Python execution for user-submitted code
- Input validation on all API endpoints (Pydantic models)
- Rate limiting on public API endpoints
- Dataset access scoped per session
