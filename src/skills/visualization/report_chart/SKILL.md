---
name: report_chart
description: Generate publication-quality charts
---

# Report Chart

## Description
Generate publication-quality charts

## When to Use
When including charts in reports

## Workflow
1. Style chart\n2. Add labels\n3. Export high-DPI

## Tools Used
matplotlib

## Examples
```python
from src.skills.visualization.report_chart import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use consistent typography
