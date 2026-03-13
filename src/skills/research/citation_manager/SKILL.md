---
name: citation_manager
description: Manage and format research citations
---

# Citation Manager

## Description
Manage and format research citations

## When to Use
When referencing external sources

## Workflow
1. Collect sources\n2. Format citations\n3. Build bibliography

## Tools Used
jinja2

## Examples
```python
from src.skills.research.citation_manager import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use consistent citation format
