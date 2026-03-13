---
name: dimensionality_reduction
description: Reduce feature space using PCA or t-SNE
---

# Dimensionality Reduction

## Description
Reduce feature space using PCA or t-SNE

## When to Use
When dealing with high-dimensional data

## Workflow
1. Scale data\n2. Choose method\n3. Transform\n4. Visualize

## Tools Used
sklearn

## Examples
```python
from src.skills.data_science.dimensionality_reduction import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Standardize features before PCA
