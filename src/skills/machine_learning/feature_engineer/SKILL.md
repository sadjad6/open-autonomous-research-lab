---
name: feature_engineer
description: Create new features from existing data
---

# Feature Engineer

## Description
Create new features from existing data

## When to Use
Before model training

## Workflow
1. Analyze features\n2. Create interactions\n3. Validate

## Tools Used
pandas, sklearn

## Examples
```python
from src.skills.machine_learning.feature_engineer import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Test feature impact with ablation
