---
name: scatter_plot
description: Generate scatter plot visualizations
---

# Scatter Plot

## Description
Generate scatter plot visualizations

## When to Use
When exploring variable relationships

## Workflow
1. Prepare data\n2. Configure\n3. Add regression line

## Tools Used
matplotlib, seaborn

## Examples
```python
from src.skills.visualization.scatter_plot import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use color for additional dimensions
