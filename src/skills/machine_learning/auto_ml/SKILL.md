---
name: auto_ml
description: Automated model selection and tuning
---

# AutoML

## Description
Automated model selection and tuning

## When to Use
For rapid prototyping

## Workflow
1. Define search space\n2. Run trials\n3. Select best

## Tools Used
sklearn

## Examples
```python
from src.skills.machine_learning.auto_ml import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Set time and resource limits
