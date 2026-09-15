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


def create_learning_roadmap_task(
    match_scoring_task,
    learning_roadmap_agent,
) -> Task:
    """
    Creates a task for generating a practical learning roadmap from the match report.
    """
    return Task(
        description=(
            "Review the job match scoring report from the previous task.\n\n"
            "Create a practical improvement roadmap for the candidate and for this GitHub project.\n\n"
            "Important context:\n"
            "- The candidate is already building this project using CrewAI.\n"
            "- Do not list CrewAI as a missing skill if it is already shown in the resume or project.\n"
            "- Focus on gaps that improve AI Engineer / GenAI Developer readiness.\n\n"
            "Include:\n"
            "1. Top 5 priority gaps based on the match report\n"
            "2. Evidence for each gap from the previous match report\n"
            "3. What to learn for each gap\n"
            "4. How to improve THIS Agentic JobMatch AI project to prove each skill\n"
            "5. 2-week action plan focused on project delivery\n"
            "6. 30-day action plan focused on production readiness\n"
            "7. Interview preparation topics\n"
            "8. Final advice: Apply now / Apply after improvements / Not suitable yet\n\n"
            "Preferred project improvements should include items such as:\n"
            "- FastAPI backend\n"
            "- Streamlit UI\n"
            "- Docker\n"
            "- Deployment link\n"
            "- Pytest tests\n"
            "- Evaluation checks\n"
            "- Better README and architecture diagram\n\n"
            "Important rules:\n"
            "- Be practical and specific.\n"
            "- Do not suggest certifications unless the job description explicitly asks for certifications.\n"
            "- Do not suggest too many courses.\n"
            "- Do not invent candidate experience.\n"
            "- Do not invent job requirements that are not in the job description.\n"
            "- Do not repeat skills as gaps if they are already demonstrated.\n"
            "- Treat project evidence as more important than certificates.\n"
            "- Focus on building portfolio evidence for AI Automation Engineer, GenAI Application Developer, "
            "LLM Application Engineer, and Agentic AI Developer roles."
        ),
        expected_output=(
            "A structured, project-focused learning roadmap with priority gaps, evidence, "
            "learning actions, improvements to Agentic JobMatch AI, 2-week plan, "
            "30-day production-readiness plan, interview topics, and final advice."
        ),
        agent=learning_roadmap_agent,
        context=[
            match_scoring_task,
        ],
    )

def create_final_report_task(
    resume_analysis_task,
    jd_analysis_task,
    match_scoring_task,
    learning_roadmap_task,
    final_report_agent,
) -> Task:
    """
    Creates a task for generating the final polished job match report.
    """
    return Task(
        description=(
            "Create one polished final job match report using the outputs from the previous tasks.\n\n"
            "The final report should be useful for a candidate reviewing whether to apply for a role.\n\n"
            "Include these sections:\n"
            "1. Executive summary\n"
            "2. Role being analysed\n"
            "3. Overall match score and match category\n"
            "4. Key strengths aligned to the job description\n"
            "5. Main gaps or risks\n"
            "6. Recommended improvements to the resume\n"
            "7. Recommended improvements to the Agentic JobMatch AI GitHub project\n"
            "8. 2-week action plan\n"
            "9. 30-day action plan\n"
            "10. Interview preparation focus areas\n"
            "11. Final recommendation\n\n"
   "Important rules:\n"
"- Do not invent candidate experience.\n"
"- Do not invent job requirements.\n"
"- Do not recommend certifications, education, or qualifications unless the job description explicitly asks for them.\n"
"- Do not recommend Kubernetes unless the job description explicitly asks for Kubernetes.\n"
"- Do not recommend advanced ML training, model training, or transformer model development unless the job description explicitly asks for ML model development.\n"
"- This role is focused on AI automation, GenAI applications, API integrations, agentic workflows, RAG, deployment, reliability, and documentation.\n"
"- Do not describe demonstrated skills as completely missing.\n"
"- If the resume mentions GenAI, CrewAI, LangChain, LangGraph, RAG, DeepEval, or RAGAS, do not say the candidate has no LLM or LLM testing experience. "
"Instead, say they need stronger production-level evidence if applicable.\n"
"- Treat GitHub project evidence as more important than certificates.\n"
"- Recommended GitHub improvements should focus only on FastAPI, Streamlit UI, Docker, cloud deployment, Pytest tests, LLM evaluation checks, README, architecture diagram, and demo link.\n"
"- Resume improvements should focus on measurable project outcomes, deployed project links, API/backend evidence, cloud deployment evidence, and LLM evaluation evidence.\n"
"- Keep the report professional and recruiter-friendly.\n"
"- Avoid generic career advice.\n"
"- Focus on practical portfolio evidence."
        ),
        expected_output=(
            "A polished markdown final report with executive summary, match score, strengths, "
            "gaps, resume improvements, GitHub project improvements, action plans, "
            "interview preparation focus areas, and final recommendation."
        ),
        agent=final_report_agent,
        context=[
            resume_analysis_task,
            jd_analysis_task,
            match_scoring_task,
            learning_roadmap_task,
        ],
    )