---
name: research_planner
description: Plan research investigations
---

# Research Planner

## Description
Plan research investigations

## When to Use
At the start of new research

## Workflow
1. Define questions\n2. Plan methods\n3. Estimate resources

## Tools Used
pandas

## Examples
```python
from src.skills.research.research_planner import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Start with clear hypotheses
