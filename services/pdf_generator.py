from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
import uuid

def generate_question_pdf(top_role, questions):
    pdf_dir = os.path.join("static", "pdfs")
    os.makedirs(pdf_dir, exist_ok=True)

    filename = f"interview_questions_{uuid.uuid4().hex}.pdf"
    file_path = os.path.join(pdf_dir, filename)

    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    y = height - 50
    c.setFont("Helvetica-Bold", 16)

    # 🔥 FIX: top_role is a STRING
    c.drawString(50, y, f"Interview Questions for {top_role}")
    y -= 40

    c.setFont("Helvetica", 12)

    for i, q in enumerate(questions, start=1):
        if y < 80:
            c.showPage()
            c.setFont("Helvetica", 12)
            y = height - 50

        c.drawString(50, y, f"{i}. {q}")
        y -= 25

    c.save()
    return file_path

