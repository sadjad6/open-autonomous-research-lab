---
name: pie_chart
description: Generate pie chart visualizations
---

# Pie Chart

## Description
Generate pie chart visualizations

## When to Use
When showing proportions of a whole

## Workflow
1. Compute shares\n2. Configure\n3. Render

## Tools Used
matplotlib

## Examples
```python
from src.skills.visualization.pie_chart import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Limit to 6-7 slices maximum
