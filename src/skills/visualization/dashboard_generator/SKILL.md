---
name: dashboard_generator
description: Generate multi-panel dashboards
---

# Dashboard Generator

## Description
Generate multi-panel dashboards

## When to Use
When presenting multiple metrics

## Workflow
1. Select panels\n2. Layout\n3. Render

## Tools Used
plotly

## Examples
```python
from src.skills.visualization.dashboard_generator import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use consistent color scheme
