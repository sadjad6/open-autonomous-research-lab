---
name: trend_analysis
description: Detect trends in temporal or sequential data
---

# Trend Analysis

## Description
Detect trends in temporal or sequential data

## When to Use
When monitoring changes over time

## Workflow
1. Smooth data\n2. Fit trend\n3. Test significance

## Tools Used
scipy, statsmodels

## Examples
```python
from src.skills.data_science.trend_analysis import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use rolling windows for noisy data
