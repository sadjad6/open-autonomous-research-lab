---
name: model_drift_detector
description: Detect data or concept drift
---

# Model Drift Detector

## Description
Detect data or concept drift

## When to Use
When monitoring model performance

## Workflow
1. Compare distributions\n2. Test drift\n3. Alert

## Tools Used
scipy

## Examples
```python
from src.skills.evaluation.model_drift_detector import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Monitor feature-level drift
