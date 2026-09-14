from crewai import Task


def create_resume_analysis_task(resume_text: str, resume_analyst_agent) -> Task:
    """
    Creates a task for analysing the candidate resume.
    """
    return Task(
        description=(
            "Analyse the following candidate resume carefully.\n\n"
            "Resume:\n"
            f"{resume_text}\n\n"
            "Extract and summarise:\n"
            "1. Candidate's professional background\n"
            "2. Technical skills\n"
            "3. AI/GenAI/Agentic AI skills\n"
            "4. Automation and API experience\n"
            "5. Projects mentioned\n"
            "6. Strengths for AI Automation / GenAI roles\n"
            "7. Possible limitations or missing evidence\n\n"
            "Important rule: Use only the information found in the resume. "
            "Do not invent experience."
        ),
        expected_output=(
            "A structured resume analysis report with sections for background, "
            "technical skills, AI skills, projects, strengths, and limitations."
        ),
        agent=resume_analyst_agent,
    )


def create_job_description_analysis_task(job_description_text: str, jd_analyst_agent) -> Task:
    """
    Creates a task for analysing the job description.
    """
    return Task(
        description=(
            "Analyse the following job description carefully.\n\n"
            "Job Description:\n"
            f"{job_description_text}\n\n"
            "Extract and summarise:\n"
            "1. Role title and role type\n"
            "2. Main responsibilities\n"
            "3. Required technical skills\n"
            "4. Required AI/GenAI/Agentic AI skills\n"
            "5. Required backend/cloud/deployment skills\n"
            "6. Soft skills and stakeholder expectations\n"
            "7. Key hiring signals\n\n"
            "Important rule: Use only the information found in the job description. "
            "Do not invent requirements."
        ),
        expected_output=(
            "A structured job description analysis report with sections for role summary, "
            "responsibilities, required skills, AI skills, backend/cloud skills, soft skills, "
            "and key hiring signals."
        ),
        agent=jd_analyst_agent,
    )


def create_match_scoring_task(
    resume_analysis_task,
    jd_analysis_task,
    match_scoring_agent,
) -> Task:
    """
    Creates a task for comparing the resume analysis against the job description analysis.
    """
    return Task(
        description=(
            "Compare the resume analysis and job description analysis from the previous tasks.\n\n"
            "Your job is to produce a realistic job match report.\n\n"
            "Include:\n"
            "1. Overall match score out of 100\n"
            "2. Match category: Strong Match / Good Match / Partial Match / Weak Match\n"
            "3. Top matching skills\n"
            "4. Missing or weak skills\n"
            "5. Experience gaps\n"
            "6. Project gaps\n"
            "7. Resume improvement suggestions\n"
            "8. Recommendation: Apply now / Apply after improvements / Not suitable yet\n\n"
            "Important rules:\n"
            "- Use only the resume analysis and job description analysis provided in context.\n"
            "- Do not invent candidate experience.\n"
            "- Be honest but constructive.\n"
            "- Explain the reasoning behind the score."
        ),
        expected_output=(
            "A structured job match report with score, category, matching skills, "
            "missing skills, experience gaps, project gaps, resume suggestions, "
            "and final application recommendation."
        ),
        agent=match_scoring_agent,
        context=[
            resume_analysis_task,
            jd_analysis_task,
        ],
    )