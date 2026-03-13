---
name: parquet_loader
description: Load Parquet files into DataFrames
---

# Parquet Loader

## Description
Load Parquet files into DataFrames

## When to Use
When working with columnar data

## Workflow
1. Read parquet file\n2. Return DataFrame

## Tools Used
pandas, pyarrow

## Examples
```python
from src.skills.data_engineering.parquet_loader import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use pyarrow engine for best performance
