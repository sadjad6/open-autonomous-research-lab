---
name: job_scheduler
description: Schedule and manage background jobs
---

# Job Scheduler

## Description
Schedule and manage background jobs

## When to Use
When running periodic tasks

## Workflow
1. Define schedule\n2. Register job\n3. Monitor

## Tools Used
asyncio

## Examples
```python
from src.skills.infrastructure.job_scheduler import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use cron-style scheduling
