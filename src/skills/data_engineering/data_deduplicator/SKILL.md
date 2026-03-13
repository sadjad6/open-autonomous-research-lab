---
name: data_deduplicator
description: Find and remove duplicate records
---

# Data Deduplicator

## Description
Find and remove duplicate records

## When to Use
When data may contain duplicates

## Workflow
1. Identify key columns\n2. Find duplicates\n3. Remove or merge

## Tools Used
pandas

## Examples
```python
from src.skills.data_engineering.data_deduplicator import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Consider fuzzy matching for near-duplicates
