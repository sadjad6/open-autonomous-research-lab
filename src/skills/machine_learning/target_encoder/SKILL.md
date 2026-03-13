---
name: target_encoder
description: Encode categorical targets for ML
---

# Target Encoder

## Description
Encode categorical targets for ML

## When to Use
When targets are categorical

## Workflow
1. Detect type\n2. Choose encoding\n3. Transform

## Tools Used
sklearn

## Examples
```python
from src.skills.machine_learning.target_encoder import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use ordinal encoding for ordered categories
