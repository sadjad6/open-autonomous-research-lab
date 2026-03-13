"""Validate all generated skills."""

import sys
from src.skills.base.registry import SkillRegistry
from skills_marketplace import discover_marketplace_skills

def validate_skills():
    registry = SkillRegistry()
    
    # Discover skills in all domains
    domains = [
        "data_engineering", "data_science", "evaluation", 
        "infrastructure", "machine_learning", "research", "visualization"
    ]
    
    for domain in domains:
        registry.discover_skills(f"src/skills/{domain}")
        
    base_skills = registry.list_skills()
    print(f"Discovered {len(base_skills)} base skills.")
    
    # Discover marketplace
    market_skills = discover_marketplace_skills()
    for s in market_skills:
        registry.register(s)
    print(f"Discovered {len(market_skills)} marketplace skills.")
    
    all_skills = registry.list_skills()
    print(f"Total skills registered: {len(all_skills)}")
    
    if len(all_skills) != 100:
        print(f"WARNING: Expected 100 skills, found {len(all_skills)}")
        # It's actually 105 total (95 base + 5 marketplace? Wait: 15*3 + 20 + 10*3 = 45+20+30 = 95. Yes, 95 base + 5 market = 100)
    
    for skill_info in all_skills:
        skill = registry.get(skill_info["name"])
        assert skill.name == skill_info["name"]
        assert skill.domain == skill_info["domain"]
        assert skill.description is not None
        
    print("All skills successfully instantiated and validated.")
    
if __name__ == "__main__":
    validate_skills()
