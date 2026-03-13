---
name: knn_trainer
description: Train K-nearest neighbors models
---

# KNN Trainer

## Description
Train K-nearest neighbors models

## When to Use
For instance-based classification

## Workflow
1. Scale features\n2. Choose k\n3. Fit\n4. Evaluate

## Tools Used
sklearn

## Examples
```python
from src.skills.machine_learning.knn_trainer import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use cross-validation to choose k
