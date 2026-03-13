---
name: time_series_decomposition
description: Decompose time series into trend, seasonality, residual
---

# Time Series Decomposition

## Description
Decompose time series into trend, seasonality, residual

## When to Use
When analyzing temporal patterns

## Workflow
1. Detect frequency\n2. Decompose\n3. Analyze components

## Tools Used
statsmodels

## Examples
```python
from src.skills.data_science.time_series_decomposition import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Choose additive vs multiplicative based on variance
