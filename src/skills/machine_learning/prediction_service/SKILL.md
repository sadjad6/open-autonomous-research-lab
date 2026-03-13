---
name: prediction_service
description: Generate predictions from trained models
---

# Prediction Service

## Description
Generate predictions from trained models

## When to Use
When making predictions on new data

## Workflow
1. Load model\n2. Validate input\n3. Predict\n4. Format output

## Tools Used
sklearn

## Examples
```python
from src.skills.machine_learning.prediction_service import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Validate input schema before prediction
