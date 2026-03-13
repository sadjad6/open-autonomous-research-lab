---
name: distribution_analysis
description: Analyze the statistical distribution of features
---

# Distribution Analysis

## Description
Analyze the statistical distribution of features

## When to Use
When understanding data shape

## Workflow
1. Test normality\n2. Compute moments\n3. Visualize

## Tools Used
scipy, matplotlib

## Examples
```python
from src.skills.data_science.distribution_analysis import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Test assumptions before parametric tests
