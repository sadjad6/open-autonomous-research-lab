---
name: cohort_analysis
description: Analyze behavior across user cohorts
---

# Cohort Analysis

## Description
Analyze behavior across user cohorts

## When to Use
When studying retention or lifecycle

## Workflow
1. Define cohorts\n2. Compute metrics\n3. Compare

## Tools Used
pandas

## Examples
```python
from src.skills.data_science.cohort_analysis import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use time-based cohorts for retention
