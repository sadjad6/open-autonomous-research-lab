---
name: dataset_profiler
description: Generate comprehensive dataset profiles
---

# Dataset Profiler

## Description
Generate comprehensive dataset profiles

## When to Use
As first step in any analysis

## Workflow
1. Compute stats\n2. Check quality\n3. Generate profile

## Tools Used
pandas

## Examples
```python
from src.skills.data_engineering.dataset_profiler import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Run profiling before any transformations
