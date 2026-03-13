---
name: dependency_manager
description: Manage project dependencies
---

# Dependency Manager

## Description
Manage project dependencies

## When to Use
When adding or updating packages

## Workflow
1. Check compatibility\n2. Update lock\n3. Verify

## Tools Used
uv

## Examples
```python
from src.skills.infrastructure.dependency_manager import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use lockfiles for reproducibility
