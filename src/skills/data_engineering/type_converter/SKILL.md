---
name: type_converter
description: Convert column data types
---

# Type Converter

## Description
Convert column data types

## When to Use
When columns have incorrect dtypes

## Workflow
1. Detect current types\n2. Infer correct types\n3. Convert

## Tools Used
pandas

## Examples
```python
from src.skills.data_engineering.type_converter import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Handle conversion errors gracefully
