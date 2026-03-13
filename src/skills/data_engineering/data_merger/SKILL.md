---
name: data_merger
description: Merge multiple DataFrames
---

# Data Merger

## Description
Merge multiple DataFrames

## When to Use
When combining data from multiple sources

## Workflow
1. Identify join keys\n2. Choose join type\n3. Merge

## Tools Used
pandas

## Examples
```python
from src.skills.data_engineering.data_merger import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Validate join keys before merging
