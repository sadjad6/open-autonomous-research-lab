---
name: data_versioner
description: Version control datasets
---

# Data Versioner

## Description
Version control datasets

## When to Use
When tracking dataset changes

## Workflow
1. Hash dataset\n2. Store version\n3. Log metadata

## Tools Used
hashlib

## Examples
```python
from src.skills.infrastructure.data_versioner import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Track schema changes separately
