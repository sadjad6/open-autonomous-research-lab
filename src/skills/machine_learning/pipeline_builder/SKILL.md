---
name: pipeline_builder
description: Build sklearn preprocessing pipelines
---

# Pipeline Builder

## Description
Build sklearn preprocessing pipelines

## When to Use
When standardizing ML workflows

## Workflow
1. Define steps\n2. Build pipeline\n3. Validate

## Tools Used
sklearn

## Examples
```python
from src.skills.machine_learning.pipeline_builder import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Include preprocessing in the pipeline
