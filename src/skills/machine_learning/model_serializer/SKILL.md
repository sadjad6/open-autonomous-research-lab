---
name: model_serializer
description: Save and load trained models
---

# Model Serializer

## Description
Save and load trained models

## When to Use
After model training for deployment

## Workflow
1. Serialize model\n2. Save to file\n3. Verify load

## Tools Used
joblib

## Examples
```python
from src.skills.machine_learning.model_serializer import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Include preprocessing in saved artifacts
