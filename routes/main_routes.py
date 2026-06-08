from flask import Blueprint, render_template, request, jsonify
import os

from services.resume_parser import read_resume
from services.skill_extractor import extract_skills
from services.role_matcher import match_roles
from services.question_generator import get_questions, get_all_questions
from services.pdf_generator import generate_question_pdf

main_bp = Blueprint("main", __name__)
UPLOAD_FOLDER = "uploads"

@main_bp.route("/")
def home():
    return render_template("index.html")

@main_bp.route("/analyze", methods=["POST"])
def analyze():
    file = request.files.get("resume")

    if not file:
        return jsonify({"error": "No resume uploaded"}), 400

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    text = read_resume(path)
    skills = extract_skills(text)

    role_results = match_roles(skills)

    if not role_results:
        return jsonify({
            "skills": skills,
            "recommended_role": None,
            "other_roles": [],
            "missing_skills": [],
            "questions": [],
            "pdf": None
        })

    top_role = role_results[0]

    preview_questions = get_questions(top_role["role"], limit=5)
    all_questions = get_all_questions(top_role["role"])
    pdf_path = generate_question_pdf(top_role["role"], all_questions)

    return jsonify({
        "skills": skills,
        "recommended_role": top_role["role"],
        "other_roles": [r["role"] for r in role_results[1:]],
        "missing_skills": top_role["missing_skills"],
        "questions": preview_questions,
        "pdf": pdf_path
    })