"""OARL REST API — FastAPI application exposing agent workflows."""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes import datasets, health, workflows

app = FastAPI(
    title="OARL — Open Autonomous Research Lab",
    description="Multi-agent AI platform for autonomous data analysis and ML experimentation.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, tags=["Health"])
app.include_router(workflows.router, prefix="/api", tags=["Workflows"])
app.include_router(datasets.router, prefix="/api", tags=["Datasets"])
