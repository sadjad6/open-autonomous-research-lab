---
name: feature_importance
description: Rank features by predictive importance
---

# Feature Importance

## Description
Rank features by predictive importance

## When to Use
When selecting features for modeling

## Workflow
1. Train model\n2. Extract importances\n3. Rank and filter

## Tools Used
sklearn

## Examples
```python
from src.skills.data_science.feature_importance import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use permutation importance for unbiased results
