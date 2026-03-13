---
name: env_setup
description: Set up Python environments
---

# Environment Setup

## Description
Set up Python environments

## When to Use
At project start

## Workflow
1. Create venv\n2. Install deps\n3. Verify

## Tools Used
uv

## Examples
```python
from src.skills.infrastructure.env_setup import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Pin dependency versions
