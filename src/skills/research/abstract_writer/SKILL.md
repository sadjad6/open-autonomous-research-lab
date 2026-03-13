---
name: abstract_writer
description: Generate research abstracts
---

# Abstract Writer

## Description
Generate research abstracts

## When to Use
When creating report summaries

## Workflow
1. Summarize objective\n2. Key findings\n3. Conclusions

## Tools Used
jinja2

## Examples
```python
from src.skills.research.abstract_writer import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Follow structured abstract format
