---
name: missing_value_handler
description: Detect and handle missing values
---

# Missing Value Handler

## Description
Detect and handle missing values

## When to Use
When data has NaN/null values

## Workflow
1. Detect nulls\n2. Analyze patterns\n3. Apply strategy

## Tools Used
pandas, numpy

## Examples
```python
from src.skills.data_engineering.missing_value_handler import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Choose strategy based on data type and missingness pattern
