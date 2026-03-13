---
name: knowledge_synthesizer
description: Synthesize knowledge from multiple sources
---

# Knowledge Synthesizer

## Description
Synthesize knowledge from multiple sources

## When to Use
When combining findings

## Workflow
1. Collect sources\n2. Identify themes\n3. Synthesize

## Tools Used
pandas

## Examples
```python
from src.skills.research.knowledge_synthesizer import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use structured frameworks for synthesis
