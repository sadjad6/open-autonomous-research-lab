---
name: cache_manager
description: Manage caching of computed results
---

# Cache Manager

## Description
Manage caching of computed results

## When to Use
When optimizing repeated computations

## Workflow
1. Define cache key\n2. Store result\n3. Invalidate when needed

## Tools Used
functools

## Examples
```python
from src.skills.infrastructure.cache_manager import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Set TTL for cache entries
