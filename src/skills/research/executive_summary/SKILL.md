---
name: executive_summary
description: Write executive summaries from analysis
---

# Executive Summary Writer

## Description
Write executive summaries from analysis

## When to Use
When reporting to leadership

## Workflow
1. Identify decisions\n2. Summarize findings\n3. State actions

## Tools Used
jinja2

## Examples
```python
from src.skills.research.executive_summary import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Keep under 2 pages
