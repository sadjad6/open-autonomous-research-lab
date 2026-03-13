---
name: excel_loader
description: Load Excel files into DataFrames
---

# Excel Loader

## Description
Load Excel files into DataFrames

## When to Use
When ingesting spreadsheet data

## Workflow
1. Read Excel file\n2. Select sheet\n3. Return DataFrame

## Tools Used
pandas, openpyxl

## Examples
```python
from src.skills.data_engineering.excel_loader import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Specify sheet name and header row
