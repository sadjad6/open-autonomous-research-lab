---
name: csv_loader
description: Load CSV files into DataFrames
---

# CSV Loader

## Description
Load CSV files into DataFrames

## When to Use
When ingesting CSV datasets

## Workflow
1. Read file path\n2. Parse CSV\n3. Return DataFrame

## Tools Used
pandas

## Examples
```python
from src.skills.data_engineering.csv_loader import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Specify encoding and delimiter
