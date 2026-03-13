---
name: methodology_writer
description: Write methodology sections for reports
---

# Methodology Writer

## Description
Write methodology sections for reports

## When to Use
When documenting analysis methods

## Workflow
1. Describe approach\n2. List tools\n3. Document parameters

## Tools Used
jinja2

## Examples
```python
from src.skills.research.methodology_writer import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Include reproducibility information
