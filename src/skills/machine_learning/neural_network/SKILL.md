---
name: neural_network
description: Train neural network models
---

# Neural Network

## Description
Train neural network models

## When to Use
For complex non-linear patterns

## Workflow
1. Design architecture\n2. Compile\n3. Train\n4. Evaluate

## Tools Used
sklearn

## Examples
```python
from src.skills.machine_learning.neural_network import Skill

skill = Skill()
result = await skill.run(SkillInput(data={"key": "value"}))
```

## Best Practices
Start simple, add complexity as needed
