import json
import re

def extract_skills(text):
    with open("data/skills.json") as f:
        skills = json.load(f)

    text = text.lower()

    extracted = set()

    for skill in skills:
        skill_l = skill.lower()

        # allow plural & partial match
        pattern = r"\b" + re.escape(skill_l) + r"s?\b"
        if re.search(pattern, text):
            extracted.add(skill_l)

    return sorted(extracted)
