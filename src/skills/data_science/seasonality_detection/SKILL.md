---
name: seasonality_detection
description: Detect seasonal patterns in time series
---

# Seasonality Detection

## Description
Detect seasonal patterns in time series

## When to Use
When analyzing cyclical behavior

## Workflow
1. Compute ACF\n2. Detect period\n3. Validate

## Tools Used
statsmodels

## Examples
```python
from src.skills.data_science.seasonality_detection import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use autocorrelation to find period
