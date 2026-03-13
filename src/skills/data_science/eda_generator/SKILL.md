---
name: eda_generator
description: Generate comprehensive exploratory data analysis
---

# EDA Generator

## Description
Generate comprehensive exploratory data analysis

## When to Use
As the first analytical step

## Workflow
1. Compute stats\n2. Create visuals\n3. Identify patterns

## Tools Used
pandas, matplotlib

## Examples
```python
from src.skills.data_science.eda_generator import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Focus on distributions, correlations, and outliers
