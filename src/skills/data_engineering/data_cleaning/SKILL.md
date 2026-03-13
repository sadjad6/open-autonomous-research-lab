---
name: data_cleaning
description: Clean and standardize raw data
---

# Data Cleaning

## Description
Clean and standardize raw data

## When to Use
After initial data loading

## Workflow
1. Remove duplicates\n2. Fix types\n3. Standardize formats

## Tools Used
pandas

## Examples
```python
from src.skills.data_engineering.data_cleaning import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Always document cleaning steps
