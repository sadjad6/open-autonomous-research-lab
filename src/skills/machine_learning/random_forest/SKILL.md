---
name: random_forest
description: Train random forest ensemble models
---

# Random Forest

## Description
Train random forest ensemble models

## When to Use
For robust classification or regression

## Workflow
1. Prepare data\n2. Set hyperparams\n3. Fit\n4. Evaluate

## Tools Used
sklearn

## Examples
```python
from src.skills.machine_learning.random_forest import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Tune n_estimators and max_depth
