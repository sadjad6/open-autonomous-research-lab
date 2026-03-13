---
name: summary_generator
description: Generate executive summaries
---

# Summary Generator

## Description
Generate executive summaries

## When to Use
When creating reports for stakeholders

## Workflow
1. Identify key points\n2. Prioritize\n3. Write summary

## Tools Used
jinja2

## Examples
```python
from src.skills.research.summary_generator import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Keep under 1 page
