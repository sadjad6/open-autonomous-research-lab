---
name: resource_monitor
description: Monitor CPU, memory, and disk usage
---

# Resource Monitor

## Description
Monitor CPU, memory, and disk usage

## When to Use
When tracking system health

## Workflow
1. Collect metrics\n2. Check thresholds\n3. Alert

## Tools Used
psutil

## Examples
```python
from src.skills.infrastructure.resource_monitor import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Set up alerts for critical resources
