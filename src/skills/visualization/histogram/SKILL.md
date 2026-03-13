---
name: histogram
description: Generate histogram visualizations
---

# Histogram

## Description
Generate histogram visualizations

## When to Use
When analyzing distributions

## Workflow
1. Choose bins\n2. Configure\n3. Render

## Tools Used
matplotlib

## Examples
```python
from src.skills.visualization.histogram import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use Freedman-Diaconis rule for bin count
