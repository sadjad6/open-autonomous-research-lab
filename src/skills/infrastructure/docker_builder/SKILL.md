---
name: docker_builder
description: Build Docker images for deployment
---

# Docker Builder

## Description
Build Docker images for deployment

## When to Use
When containerizing the application

## Workflow
1. Write Dockerfile\n2. Build image\n3. Test

## Tools Used
docker

## Examples
```python
from src.skills.infrastructure.docker_builder import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use multi-stage builds
