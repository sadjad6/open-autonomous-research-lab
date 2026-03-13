---
name: model_comparator
description: Compare models side-by-side on metrics
---

# Model Comparator

## Description
Compare models side-by-side on metrics

## When to Use
When choosing between model candidates

## Workflow
1. Collect models\n2. Evaluate each\n3. Create comparison table

## Tools Used
sklearn, pandas

## Examples
```python
from src.skills.machine_learning.model_comparator import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use same test set for fair comparison
