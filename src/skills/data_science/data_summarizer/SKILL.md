---
name: data_summarizer
description: Generate natural-language data summaries
---

# Data Summarizer

## Description
Generate natural-language data summaries

## When to Use
When presenting data to stakeholders

## Workflow
1. Compute key stats\n2. Identify highlights\n3. Write summary

## Tools Used
pandas

## Examples
```python
from src.skills.data_science.data_summarizer import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Focus on actionable insights
