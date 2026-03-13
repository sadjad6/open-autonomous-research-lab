---
name: health_checker
description: Check system and service health
---

# Health Checker

## Description
Check system and service health

## When to Use
For monitoring and alerting

## Workflow
1. Check services\n2. Verify connectivity\n3. Report status

## Tools Used
httpx

## Examples
```python
from src.skills.infrastructure.health_checker import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Include dependency health checks
