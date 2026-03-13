---
name: model_selector
description: Compare and select the best model
---

# Model Selector

## Description
Compare and select the best model

## When to Use
After training multiple candidates

## Workflow
1. Collect results\n2. Compare metrics\n3. Select best

## Tools Used
sklearn

## Examples
```python
from src.skills.machine_learning.model_selector import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Consider both accuracy and complexity
