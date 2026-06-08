document.getElementById("uploadForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = new FormData(e.target);

    const response = await fetch("/analyze", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    /* =====================
       BEST ROLE
    ====================== */
    document.getElementById("role").innerText = data.recommended_role;

    /* =====================
       LINKEDIN LINK
    ====================== */
    const linkedin = document.getElementById("linkedinLink");
    linkedin.href = `https://www.linkedin.com/jobs/search/?keywords=${encodeURIComponent(data.recommended_role)}`;

    /* =====================
       EXTRACTED SKILLS
    ====================== */
    const skillsDiv = document.getElementById("skills");
    skillsDiv.innerHTML = "";

    data.skills.forEach(skill => {
        const span = document.createElement("span");
        span.className = "skill-tag";
        span.innerText = skill;
        skillsDiv.appendChild(span);
    });

    /* =====================
       OTHER ROLES (TAG STYLE)
    ====================== */
    const otherRolesDiv = document.getElementById("otherRoles");
    otherRolesDiv.innerHTML = "";

    if (data.other_roles.length === 0) {
        otherRolesDiv.innerText = "—";
    } else {
        data.other_roles.forEach(role => {
            const span = document.createElement("span");
            span.className = "skill-tag other-role";
            span.innerText = role;
            otherRolesDiv.appendChild(span);
        });
    }

    /* =====================
       MISSING SKILLS (TAG STYLE)
    ====================== */
    const missingDiv = document.getElementById("missingSkills");
    missingDiv.innerHTML = "";

    if (data.missing_skills.length === 0) {
        missingDiv.innerText = "No major gaps detected";
    } else {
        data.missing_skills.forEach(skill => {
            const span = document.createElement("span");
            span.className = "skill-tag missing-skill";
            span.innerText = skill;
            missingDiv.appendChild(span);
        });
    }

    /* =====================
       INTERVIEW QUESTIONS
    ====================== */
    const questionsUl = document.getElementById("questions");
    questionsUl.innerHTML = "";

    data.questions.forEach(q => {
        const li = document.createElement("li");
        li.innerText = q;
        questionsUl.appendChild(li);
    });

    /* =====================
       PDF LINK
    ====================== */
    const pdfLink = document.getElementById("pdfLink");
    if (data.pdf) {
        pdfLink.href = `/${data.pdf}`;
        pdfLink.style.display = "inline-block";
    } else {
        pdfLink.style.display = "none";
    }
});
