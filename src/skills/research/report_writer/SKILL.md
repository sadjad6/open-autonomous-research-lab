---
name: report_writer
description: Generate structured research reports
---

# Report Writer

## Description
Generate structured research reports

## When to Use
After analysis is complete

## Workflow
1. Outline sections\n2. Write content\n3. Format

## Tools Used
jinja2

## Examples
```python
from src.skills.research.report_writer import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Follow IMRaD structure
