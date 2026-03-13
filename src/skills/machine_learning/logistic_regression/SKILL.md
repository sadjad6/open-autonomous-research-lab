---
name: logistic_regression
description: Train logistic regression classifiers
---

# Logistic Regression

## Description
Train logistic regression classifiers

## When to Use
For binary/multi-class classification

## Workflow
1. Prepare data\n2. Scale features\n3. Fit\n4. Evaluate

## Tools Used
sklearn

## Examples
```python
from src.skills.machine_learning.logistic_regression import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Regularize to prevent overfitting
