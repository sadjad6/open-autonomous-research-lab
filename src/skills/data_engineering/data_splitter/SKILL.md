---
name: data_splitter
description: Split data into train/test/validation sets
---

# Data Splitter

## Description
Split data into train/test/validation sets

## When to Use
Before model training

## Workflow
1. Stratify if needed\n2. Split data\n3. Validate split ratios

## Tools Used
sklearn

## Examples
```python
from src.skills.data_engineering.data_splitter import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use stratified splits for imbalanced data
