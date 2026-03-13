---
name: ab_test_analyzer
description: Analyze results of A/B experiments
---

# A/B Test Analyzer

## Description
Analyze results of A/B experiments

## When to Use
When comparing control vs treatment

## Workflow
1. Validate data\n2. Run test\n3. Compute confidence interval

## Tools Used
scipy

## Examples
```python
from src.skills.data_science.ab_test_analyzer import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Check sample size for statistical power
