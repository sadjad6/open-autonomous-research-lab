---
name: sql_loader
description: Load data from SQL databases
---

# SQL Loader

## Description
Load data from SQL databases

## When to Use
When querying relational databases

## Workflow
1. Connect to DB\n2. Execute query\n3. Return DataFrame

## Tools Used
sqlalchemy, pandas

## Examples
```python
from src.skills.data_engineering.sql_loader import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use parameterized queries
