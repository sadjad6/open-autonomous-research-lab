---
name: box_plot
description: Generate box plot visualizations
---

# Box Plot

## Description
Generate box plot visualizations

## When to Use
When comparing distributions across groups

## Workflow
1. Group data\n2. Configure\n3. Render

## Tools Used
seaborn

## Examples
```python
from src.skills.visualization.box_plot import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Show individual points for small datasets
