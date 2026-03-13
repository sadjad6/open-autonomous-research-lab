"""Generate demo datasets for the OARL platform."""

import numpy as np
import pandas as pd
from pathlib import Path

OUTPUT = Path("datasets")
OUTPUT.mkdir(exist_ok=True)
rng = np.random.default_rng(42)

# ── Customer Churn Dataset ───────────────────────────────────
n = 500
churn = pd.DataFrame({
    "customer_id": range(1, n + 1),
    "tenure_months": rng.integers(1, 72, n),
    "monthly_charges": rng.uniform(20, 120, n).round(2),
    "total_charges": rng.uniform(100, 8000, n).round(2),
    "contract_type": rng.choice(["month-to-month", "one_year", "two_year"], n),
    "payment_method": rng.choice(["credit_card", "bank_transfer", "electronic_check"], n),
    "internet_service": rng.choice(["fiber_optic", "dsl", "none"], n),
    "num_support_tickets": rng.integers(0, 10, n),
    "churn": rng.choice([0, 1], n, p=[0.73, 0.27]),
})
churn.to_csv(OUTPUT / "customer_churn.csv", index=False)

# ── Housing Prices Dataset ───────────────────────────────────
n = 400
housing = pd.DataFrame({
    "square_feet": rng.integers(600, 5000, n),
    "bedrooms": rng.integers(1, 6, n),
    "bathrooms": rng.integers(1, 4, n),
    "age_years": rng.integers(0, 50, n),
    "garage_size": rng.integers(0, 3, n),
    "neighborhood": rng.choice(["downtown", "suburbs", "rural", "midtown"], n),
    "has_pool": rng.choice([0, 1], n),
    "price": (rng.uniform(100_000, 900_000, n)).round(0).astype(int),
})
housing.to_csv(OUTPUT / "housing_prices.csv", index=False)

# ── Sales Forecasting Dataset ────────────────────────────────
dates = pd.date_range("2022-01-01", periods=365, freq="D")
trend = np.linspace(1000, 2000, 365)
seasonal = 300 * np.sin(2 * np.pi * np.arange(365) / 365)
sales = pd.DataFrame({
    "date": dates,
    "daily_sales": (trend + seasonal + rng.normal(0, 100, 365)).round(2),
    "customers": rng.integers(50, 300, 365),
    "promotions": rng.choice([0, 1], 365, p=[0.8, 0.2]),
    "day_of_week": [d.strftime("%A") for d in dates],
})
sales.to_csv(OUTPUT / "sales_forecasting.csv", index=False)

print("Generated 3 demo datasets:")
for f in OUTPUT.glob("*.csv"):
    df = pd.read_csv(f)
    print(f"  {f.name}: {df.shape[0]} rows × {df.shape[1]} columns")
