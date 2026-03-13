---
name: results_formatter
description: Format analysis results for presentation
---

# Results Formatter

## Description
Format analysis results for presentation

## When to Use
When preparing results for reports

## Workflow
1. Select key results\n2. Format tables\n3. Create figures

## Tools Used
pandas, matplotlib

## Examples
```python
from src.skills.research.results_formatter import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use consistent number formatting
