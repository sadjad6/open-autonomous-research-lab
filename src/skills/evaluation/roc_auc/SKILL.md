---
name: roc_auc
description: Compute ROC curves and AUC scores
---

# ROC-AUC Evaluator

## Description
Compute ROC curves and AUC scores

## When to Use
For binary classification evaluation

## Workflow
1. Compute probabilities\n2. Plot ROC\n3. Compute AUC

## Tools Used
sklearn

## Examples
```python
from src.skills.evaluation.roc_auc import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use probability calibration first
