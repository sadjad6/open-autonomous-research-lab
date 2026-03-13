---
name: interactive_plot
description: Generate interactive Plotly visualizations
---

# Interactive Plot

## Description
Generate interactive Plotly visualizations

## When to Use
When users need to explore data

## Workflow
1. Prepare data\n2. Build figure\n3. Add interactivity

## Tools Used
plotly

## Examples
```python
from src.skills.visualization.interactive_plot import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Add tooltips for context
