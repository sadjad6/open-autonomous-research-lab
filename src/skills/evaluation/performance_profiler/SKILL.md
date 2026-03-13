---
name: performance_profiler
description: Profile model inference performance
---

# Performance Profiler

## Description
Profile model inference performance

## When to Use
Before deployment

## Workflow
1. Measure latency\n2. Measure throughput\n3. Profile memory

## Tools Used
pandas

## Examples
```python
from src.skills.evaluation.performance_profiler import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Test with realistic data volumes
