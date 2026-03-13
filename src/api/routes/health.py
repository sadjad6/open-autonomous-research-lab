"""Health check endpoints."""

from __future__ import annotations

from datetime import UTC, datetime

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check() -> dict[str, str]:
    """Return platform health status."""
    return {
        "status": "healthy",
        "platform": "OARL",
        "version": "0.1.0",
        "timestamp": datetime.now(UTC).isoformat(),
    }


@router.get("/ready")
async def readiness_check() -> dict[str, str]:
    """Return readiness status for orchestration."""
    return {"status": "ready"}
