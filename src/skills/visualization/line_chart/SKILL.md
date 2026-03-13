---
name: line_chart
description: Generate line chart visualizations
---

# Line Chart

## Description
Generate line chart visualizations

## When to Use
When showing trends over time

## Workflow
1. Prepare data\n2. Configure axes\n3. Render

## Tools Used
matplotlib

## Examples
```python
from src.skills.visualization.line_chart import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use markers for discrete data points
