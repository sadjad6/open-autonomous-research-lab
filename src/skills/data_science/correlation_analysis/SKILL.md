---
name: correlation_analysis
description: Compute and visualize correlation matrices
---

# Correlation Analysis

## Description
Compute and visualize correlation matrices

## When to Use
When exploring feature relationships

## Workflow
1. Compute correlations\n2. Filter significant\n3. Visualize

## Tools Used
pandas, seaborn

## Examples
```python
from src.skills.data_science.correlation_analysis import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use Spearman for non-linear relationships
