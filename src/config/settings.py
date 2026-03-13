"""Platform-wide configuration using Pydantic settings."""

from __future__ import annotations

from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings

_PROJECT_ROOT = Path(__file__).resolve().parents[2]


class OARLSettings(BaseSettings):
    """Central configuration loaded from environment variables."""

    model_config = {"env_prefix": "OARL_", "env_file": ".env", "extra": "ignore"}

    # --- General ---
    project_name: str = "OARL"
    debug: bool = False
    log_level: str = "INFO"

    # --- Paths ---
    data_dir: Path = Field(default=_PROJECT_ROOT / "datasets")
    output_dir: Path = Field(default=_PROJECT_ROOT / "output")
    memory_dir: Path = Field(default=_PROJECT_ROOT / "memory")

    # --- LLM Backend (pluggable) ---
    llm_provider: str = "openai"
    llm_model: str = "gpt-4o-mini"
    llm_api_key: str = ""
    llm_temperature: float = 0.2
    llm_max_tokens: int = 4096

    # --- MLflow ---
    mlflow_tracking_uri: str = "sqlite:///mlruns.db"
    mlflow_experiment_name: str = "oarl-experiments"

    # --- API ---
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    # --- Streamlit UI ---
    ui_port: int = 8501

    # --- Vector Memory ---
    chroma_persist_dir: str = str(_PROJECT_ROOT / "memory" / "chroma_data")


def get_settings() -> OARLSettings:
    """Factory that returns the cached settings singleton."""
    return OARLSettings()
