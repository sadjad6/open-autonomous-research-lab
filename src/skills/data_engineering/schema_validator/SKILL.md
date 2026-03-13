---
name: schema_validator
description: Validate data against expected schema
---

# Schema Validator

## Description
Validate data against expected schema

## When to Use
After loading data or before processing

## Workflow
1. Define schema\n2. Validate types\n3. Check constraints

## Tools Used
pydantic, pandas

## Examples
```python
from src.skills.data_engineering.schema_validator import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Define schemas as code for reproducibility
