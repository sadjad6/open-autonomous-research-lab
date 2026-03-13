---
name: xgboost_trainer
description: Train XGBoost models
---

# XGBoost Trainer

## Description
Train XGBoost models

## When to Use
For competitive ML performance

## Workflow
1. Prepare DMatrix\n2. Set params\n3. Train\n4. Evaluate

## Tools Used
xgboost

## Examples
```python
from src.skills.machine_learning.xgboost_trainer import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use GPU training for large datasets
