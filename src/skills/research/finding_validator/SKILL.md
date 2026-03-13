---
name: finding_validator
description: Validate research findings
---

# Finding Validator

## Description
Validate research findings

## When to Use
When verifying analysis results

## Workflow
1. Cross-check data\n2. Validate stats\n3. Confirm conclusions

## Tools Used
scipy

## Examples
```python
from src.skills.research.finding_validator import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use multiple validation methods
