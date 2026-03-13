---
name: outlier_detector
description: Detect outliers using statistical methods
---

# Outlier Detector

## Description
Detect outliers using statistical methods

## When to Use
When numeric data may contain anomalies

## Workflow
1. Compute IQR/Z-scores\n2. Flag outliers\n3. Report

## Tools Used
pandas, scipy

## Examples
```python
from src.skills.data_engineering.outlier_detector import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use IQR for skewed data, Z-score for normal
