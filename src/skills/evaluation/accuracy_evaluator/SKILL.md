---
name: accuracy_evaluator
description: Compute classification accuracy metrics
---

# Accuracy Evaluator

## Description
Compute classification accuracy metrics

## When to Use
After model training

## Workflow
1. Generate predictions\n2. Compute accuracy\n3. Report

## Tools Used
sklearn

## Examples
```python
from src.skills.evaluation.accuracy_evaluator import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Report confidence intervals
