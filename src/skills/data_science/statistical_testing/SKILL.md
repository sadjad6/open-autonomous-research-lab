---
name: statistical_testing
description: Perform hypothesis tests (t-test, chi-square, etc.)
---

# Statistical Testing

## Description
Perform hypothesis tests (t-test, chi-square, etc.)

## When to Use
When validating hypotheses statistically

## Workflow
1. Choose test\n2. Check assumptions\n3. Run test\n4. Interpret

## Tools Used
scipy

## Examples
```python
from src.skills.data_science.statistical_testing import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Always check test assumptions first
