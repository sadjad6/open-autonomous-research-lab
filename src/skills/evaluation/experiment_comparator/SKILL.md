---
name: experiment_comparator
description: Compare multiple experiments side-by-side
---

# Experiment Comparator

## Description
Compare multiple experiments side-by-side

## When to Use
When selecting best experiment

## Workflow
1. Collect experiments\n2. Align metrics\n3. Rank

## Tools Used
pandas

## Examples
```python
from src.skills.evaluation.experiment_comparator import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use statistical tests for comparison
