---
name: linear_regression
description: Train linear regression models
---

# Linear Regression

## Description
Train linear regression models

## When to Use
For continuous target prediction

## Workflow
1. Prepare data\n2. Fit model\n3. Evaluate

## Tools Used
sklearn

## Examples
```python
from src.skills.machine_learning.linear_regression import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Check linearity assumptions
