---
name: lightgbm_trainer
description: Train LightGBM models
---

# LightGBM Trainer

## Description
Train LightGBM models

## When to Use
For fast training on large datasets

## Workflow
1. Prepare data\n2. Set params\n3. Train\n4. Evaluate

## Tools Used
lightgbm

## Examples
```python
from src.skills.machine_learning.lightgbm_trainer import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use categorical feature support
