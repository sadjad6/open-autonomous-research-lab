---
name: clustering_analysis
description: Group data into natural clusters
---

# Clustering Analysis

## Description
Group data into natural clusters

## When to Use
When discovering natural groupings

## Workflow
1. Scale features\n2. Choose k\n3. Fit clusters\n4. Evaluate

## Tools Used
sklearn

## Examples
```python
from src.skills.data_science.clustering_analysis import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Use silhouette score to choose k
