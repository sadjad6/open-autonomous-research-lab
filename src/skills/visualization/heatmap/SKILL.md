---
name: heatmap
description: Generate heatmap visualizations
---

# Heatmap

## Description
Generate heatmap visualizations

## When to Use
When showing correlation or frequency matrices

## Workflow
1. Prepare matrix\n2. Choose colormap\n3. Render

## Tools Used
seaborn

## Examples
```python
from src.skills.visualization.heatmap import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Annotate cells with values
