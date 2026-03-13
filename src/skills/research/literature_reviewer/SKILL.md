---
name: literature_reviewer
description: Conduct systematic literature reviews
---

# Literature Reviewer

## Description
Conduct systematic literature reviews

## When to Use
When surveying existing research

## Workflow
1. Define scope\n2. Search\n3. Analyze\n4. Summarize

## Tools Used
httpx

## Examples
```python
from src.skills.research.literature_reviewer import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use PRISMA guidelines
