---
name: gradient_boosting
description: Train gradient boosting models
---

# Gradient Boosting

## Description
Train gradient boosting models

## When to Use
For high-accuracy predictions

## Workflow
1. Prepare data\n2. Configure\n3. Fit\n4. Evaluate

## Tools Used
sklearn

## Examples
```python
from src.skills.machine_learning.gradient_boosting import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use early stopping to prevent overfitting
