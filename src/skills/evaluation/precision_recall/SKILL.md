---
name: precision_recall
description: Compute precision and recall metrics
---

# Precision-Recall Evaluator

## Description
Compute precision and recall metrics

## When to Use
For classification evaluation

## Workflow
1. Compute precision\n2. Compute recall\n3. Compute F1

## Tools Used
sklearn

## Examples
```python
from src.skills.evaluation.precision_recall import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use macro/micro averaging for multi-class
