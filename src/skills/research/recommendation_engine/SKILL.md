---
name: recommendation_engine
description: Generate actionable recommendations
---

# Recommendation Engine

## Description
Generate actionable recommendations

## When to Use
When providing guidance from analysis

## Workflow
1. Identify actions\n2. Assess feasibility\n3. Prioritize

## Tools Used
pandas

## Examples
```python
from src.skills.research.recommendation_engine import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Rank by impact and effort
