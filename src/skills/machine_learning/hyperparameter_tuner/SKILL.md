---
name: hyperparameter_tuner
description: Optimize model hyperparameters
---

# Hyperparameter Tuner

## Description
Optimize model hyperparameters

## When to Use
After initial model training

## Workflow
1. Define search space\n2. Choose strategy\n3. Search\n4. Validate

## Tools Used
sklearn

## Examples
```python
from src.skills.machine_learning.hyperparameter_tuner import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use random search before grid search
