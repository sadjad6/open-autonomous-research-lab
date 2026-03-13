---
name: json_loader
description: Load JSON files into DataFrames
---

# JSON Loader

## Description
Load JSON files into DataFrames

## When to Use
When ingesting JSON data

## Workflow
1. Read file\n2. Parse JSON\n3. Normalize nested structures

## Tools Used
pandas, json

## Examples
```python
from src.skills.data_engineering.json_loader import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Handle nested JSON with json_normalize
