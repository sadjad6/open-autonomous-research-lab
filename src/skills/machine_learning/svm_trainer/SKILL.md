---
name: svm_trainer
description: Train support vector machine models
---

# SVM Trainer

## Description
Train support vector machine models

## When to Use
For high-dimensional classification

## Workflow
1. Scale features\n2. Choose kernel\n3. Fit\n4. Evaluate

## Tools Used
sklearn

## Examples
```python
from src.skills.machine_learning.svm_trainer import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Always scale features for SVM
