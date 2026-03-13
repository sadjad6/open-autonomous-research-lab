---
name: fairness_checker
description: Check model fairness across groups
---

# Fairness Checker

## Description
Check model fairness across groups

## When to Use
Before deploying models

## Workflow
1. Define groups\n2. Compute disparity\n3. Report

## Tools Used
sklearn

## Examples
```python
from src.skills.evaluation.fairness_checker import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Check multiple fairness metrics
