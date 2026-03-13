---
name: cross_validator
description: Perform k-fold cross-validation
---

# Cross Validator

## Description
Perform k-fold cross-validation

## When to Use
When estimating model generalization

## Workflow
1. Choose k\n2. Split data\n3. Train and evaluate each fold

## Tools Used
sklearn

## Examples
```python
from src.skills.machine_learning.cross_validator import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use stratified folds for classification
