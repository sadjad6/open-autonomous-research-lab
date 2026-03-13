---
name: cross_val_scorer
description: Score models using cross-validation
---

# Cross-Validation Scorer

## Description
Score models using cross-validation

## When to Use
When estimating generalization

## Workflow
1. Define scoring\n2. Run CV\n3. Aggregate scores

## Tools Used
sklearn

## Examples
```python
from src.skills.evaluation.cross_val_scorer import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Report mean and standard deviation
