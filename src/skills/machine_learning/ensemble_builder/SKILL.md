---
name: ensemble_builder
description: Build model ensembles (voting, stacking)
---

# Ensemble Builder

## Description
Build model ensembles (voting, stacking)

## When to Use
When combining model strengths

## Workflow
1. Select base models\n2. Choose strategy\n3. Build ensemble

## Tools Used
sklearn

## Examples
```python
from src.skills.machine_learning.ensemble_builder import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use diverse models for better ensembles
