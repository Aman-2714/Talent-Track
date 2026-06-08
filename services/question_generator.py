import json

QUESTIONS_DB = {
    "Backend Developer": [
        "What is REST API?",
        "Explain Flask architecture",
        "Difference between SQL and NoSQL",
        "What is ORM?",
        "How does authentication work in Flask?",
        "Explain MVC pattern",
        "What is middleware?",
        "How do you handle errors in Flask?",
        "Explain database indexing",
        "What is JWT?"
    ],
    "DevOps Engineer": [
        "What is Docker?",
        "Explain CI/CD pipeline",
        "What is Kubernetes?",
        "Difference between VM and container",
        "What is Linux?",
        "Explain Git workflow",
        "What is load balancing?",
        "What is monitoring?",
        "Explain cloud services",
        "What is infrastructure as code?"
    ],
    "Software Engineer": [
        "Explain OOP concepts",
        "What is Git?",
        "Difference between list and tuple",
        "Explain time complexity",
        "What is debugging?",
        "Explain SDLC",
        "What is unit testing?",
        "Explain recursion",
        "What is API?",
        "Explain exception handling"
    ]
}

def normalize_role(role):
    role = role.lower()
    if "backend" in role:
        return "Backend Developer"
    if "devops" in role:
        return "DevOps Engineer"
    if "software" in role:
        return "Software Engineer"
    return role.title()

def get_questions(role, limit=5):
    normalized_role = normalize_role(role)
    questions = QUESTIONS_DB.get(normalized_role, [])
    return questions[:limit]

def get_all_questions(role):
    normalized_role = normalize_role(role)
    return QUESTIONS_DB.get(normalized_role, [])
