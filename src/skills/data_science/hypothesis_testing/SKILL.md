---
name: hypothesis_testing
description: Formulate and test research hypotheses
---

# Hypothesis Testing

## Description
Formulate and test research hypotheses

## When to Use
When answering specific research questions

## Workflow
1. State H0/H1\n2. Choose test\n3. Compute p-value\n4. Decide

## Tools Used
scipy, statsmodels

## Examples
```python
from src.skills.data_science.hypothesis_testing import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Report effect sizes alongside p-values
