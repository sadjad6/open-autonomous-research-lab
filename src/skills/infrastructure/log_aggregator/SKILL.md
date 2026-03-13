---
name: log_aggregator
description: Aggregate and search through logs
---

# Log Aggregator

## Description
Aggregate and search through logs

## When to Use
When debugging or monitoring

## Workflow
1. Collect logs\n2. Parse\n3. Index\n4. Search

## Tools Used
structlog

## Examples
```python
from src.skills.infrastructure.log_aggregator import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use structured logging format
