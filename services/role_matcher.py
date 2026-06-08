print("ROLE MATCHER FILE LOADED")

def match_roles(extracted_skills):
    extracted = set(skill.lower() for skill in extracted_skills)

    ROLE_SKILLS = {
        "Frontend Developer": {
            "html", "css", "javascript", "react"
        },
        "Backend Developer": {
            "python", "flask", "django", "sql", "api", "database"
        },
        "Full Stack Developer": {
            "html", "css", "javascript",
            "python", "flask", "sql"
        }
    }

    results = []

    for role, required_skills in ROLE_SKILLS.items():
        print("\n--- CHECKING ROLE:", role)

        required = set(required_skills)

        matched = extracted.intersection(required)
        missing = required - extracted

        print("MATCHED:", matched)
        print("MISSING:", missing)

        if len(matched) == 0:
            continue

        results.append({
            "role": role,
            "matched_skills": sorted(matched),
            "missing_skills": sorted(missing),
            "score": len(matched)
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    print("\nFINAL RESULTS:", results)
    return results
