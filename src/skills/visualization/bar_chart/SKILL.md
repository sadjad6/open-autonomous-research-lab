---
name: bar_chart
description: Generate bar chart visualizations
---

# Bar Chart

## Description
Generate bar chart visualizations

## When to Use
When comparing categories

## Workflow
1. Prepare data\n2. Configure chart\n3. Render

## Tools Used
matplotlib, seaborn

## Examples
```python
from src.skills.visualization.bar_chart import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Sort bars by value for readability
