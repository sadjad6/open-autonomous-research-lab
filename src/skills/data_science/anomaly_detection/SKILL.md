---
name: anomaly_detection
description: Detect anomalous observations in data
---

# Anomaly Detection

## Description
Detect anomalous observations in data

## When to Use
When finding unusual patterns or fraud

## Workflow
1. Choose method\n2. Fit detector\n3. Score observations

## Tools Used
sklearn

## Examples
```python
from src.skills.data_science.anomaly_detection import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Combine multiple methods for robustness
