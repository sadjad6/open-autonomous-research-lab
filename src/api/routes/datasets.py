"""Dataset management endpoints."""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any

from fastapi import APIRouter, UploadFile, File

router = APIRouter()

UPLOAD_DIR = Path("datasets/uploads")


@router.post("/datasets/upload")
async def upload_dataset(file: UploadFile = File(...)) -> dict[str, Any]:
    """Upload a dataset file."""
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    dest = UPLOAD_DIR / (file.filename or "upload.csv")
    with dest.open("wb") as f:
        contents = await file.read()
        f.write(contents)
    return {"filename": file.filename, "path": str(dest), "size": len(contents)}


@router.get("/datasets")
async def list_datasets() -> dict[str, Any]:
    """List available datasets."""
    datasets_dir = Path("datasets")
    files: list[dict[str, Any]] = []
    if datasets_dir.exists():
        for f in datasets_dir.rglob("*.csv"):
            files.append({"name": f.name, "path": str(f), "size": f.stat().st_size})
    return {"datasets": files, "count": len(files)}
