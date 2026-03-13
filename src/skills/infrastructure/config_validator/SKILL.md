---
name: config_validator
description: Validate configuration files
---

# Config Validator

## Description
Validate configuration files

## When to Use
At application startup

## Workflow
1. Load config\n2. Validate schema\n3. Report errors

## Tools Used
pydantic

## Examples
```python
from src.skills.infrastructure.config_validator import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Fail fast on invalid config
