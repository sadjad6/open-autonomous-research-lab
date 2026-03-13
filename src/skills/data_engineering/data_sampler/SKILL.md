---
name: data_sampler
description: Create representative data samples
---

# Data Sampler

## Description
Create representative data samples

## When to Use
When working with very large datasets

## Workflow
1. Choose strategy\n2. Sample data\n3. Validate distribution

## Tools Used
pandas

## Examples
```python
from src.skills.data_engineering.data_sampler import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Maintain class distribution in samples
