"""Synthetic data generator — creates test datasets for classification, regression, and time series."""

from __future__ import annotations

import logging
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.datasets import make_classification, make_regression

logger = logging.getLogger(__name__)

DEFAULT_OUTPUT_DIR = Path("datasets/synthetic")
DEFAULT_SAMPLES = 1000


def generate_classification_dataset(
    n_samples: int = DEFAULT_SAMPLES,
    n_features: int = 10,
    output_dir: Path = DEFAULT_OUTPUT_DIR,
) -> Path:
    """Generate a synthetic binary classification dataset."""
    X, y = make_classification(
        n_samples=n_samples, n_features=n_features,
        n_informative=6, n_redundant=2, random_state=42,
    )
    df = pd.DataFrame(X, columns=[f"feature_{i}" for i in range(n_features)])
    df["target"] = y
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / "classification_dataset.csv"
    df.to_csv(path, index=False)
    logger.info("Generated classification dataset: %s (%d rows)", path, n_samples)
    return path


def generate_regression_dataset(
    n_samples: int = DEFAULT_SAMPLES,
    n_features: int = 8,
    output_dir: Path = DEFAULT_OUTPUT_DIR,
) -> Path:
    """Generate a synthetic regression dataset."""
    X, y = make_regression(
        n_samples=n_samples, n_features=n_features,
        n_informative=5, noise=10.0, random_state=42,
    )
    df = pd.DataFrame(X, columns=[f"feature_{i}" for i in range(n_features)])
    df["target"] = y
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / "regression_dataset.csv"
    df.to_csv(path, index=False)
    logger.info("Generated regression dataset: %s (%d rows)", path, n_samples)
    return path


def generate_time_series_dataset(
    n_points: int = 365,
    output_dir: Path = DEFAULT_OUTPUT_DIR,
) -> Path:
    """Generate a synthetic time series dataset with trend and seasonality."""
    rng = np.random.default_rng(42)
    dates = pd.date_range("2023-01-01", periods=n_points, freq="D")
    trend = np.linspace(100, 200, n_points)
    seasonal = 20 * np.sin(2 * np.pi * np.arange(n_points) / 365)
    noise = rng.normal(0, 5, n_points)
    values = trend + seasonal + noise

    df = pd.DataFrame({"date": dates, "value": values})
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / "time_series_dataset.csv"
    df.to_csv(path, index=False)
    logger.info("Generated time series dataset: %s (%d points)", path, n_points)
    return path


def generate_all(output_dir: Path = DEFAULT_OUTPUT_DIR) -> list[Path]:
    """Generate all synthetic datasets."""
    return [
        generate_classification_dataset(output_dir=output_dir),
        generate_regression_dataset(output_dir=output_dir),
        generate_time_series_dataset(output_dir=output_dir),
    ]


if __name__ == "__main__":
    paths = generate_all()
    print(f"Generated {len(paths)} datasets:")
    for p in paths:
        print(f"  {p}")
