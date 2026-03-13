---
name: paper_searcher
description: Search for relevant academic papers
---

# Paper Searcher

## Description
Search for relevant academic papers

## When to Use
When conducting literature review

## Workflow
1. Define keywords\n2. Search databases\n3. Rank results

## Tools Used
httpx

## Examples
```python
from src.skills.research.paper_searcher import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use multiple search sources
