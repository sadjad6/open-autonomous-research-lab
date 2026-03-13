---
name: insight_extractor
description: Extract key insights from analysis results
---

# Insight Extractor

## Description
Extract key insights from analysis results

## When to Use
After data analysis

## Workflow
1. Review results\n2. Identify patterns\n3. Summarize

## Tools Used
pandas

## Examples
```python
from src.skills.research.insight_extractor import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Prioritize actionable insights
