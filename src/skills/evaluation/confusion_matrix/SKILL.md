---
name: confusion_matrix
description: Generate confusion matrices
---

# Confusion Matrix

## Description
Generate confusion matrices

## When to Use
After classification predictions

## Workflow
1. Generate matrix\n2. Normalize\n3. Visualize

## Tools Used
sklearn, seaborn

## Examples
```python
from src.skills.evaluation.confusion_matrix import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Show both raw and normalized
