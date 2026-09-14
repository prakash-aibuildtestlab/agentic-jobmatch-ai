from crewai import Agent


def create_resume_analyst_agent() -> Agent:
    """
    Creates an agent responsible for analysing the candidate resume.
    """
    return Agent(
        role="Resume Analyst Agent",
        goal=(
            "Analyse the candidate resume and extract key skills, experience, "
            "projects, tools, strengths, and potential limitations."
        ),
        backstory=(
            "You are an experienced technical recruiter and AI career analyst. "
            "You carefully review resumes for AI Automation Engineer, GenAI Application Developer, "
            "LLM Application Engineer, and Agentic AI Developer roles. "
            "You focus only on evidence found in the resume and avoid inventing experience."
        ),
        verbose=True,
        allow_delegation=False,
    )


def create_job_description_analyst_agent() -> Agent:
    """
    Creates an agent responsible for analysing the job description.
    """
    return Agent(
        role="Job Description Analyst Agent",
        goal=(
            "Analyse the job description and extract required skills, responsibilities, "
            "technical tools, experience expectations, and key hiring signals."
        ),
        backstory=(
            "You are an AI recruitment analyst who understands modern AI Engineer, "
            "GenAI Developer, AI Automation Engineer, and Agentic AI roles. "
            "You identify the most important technical and business requirements from job descriptions."
        ),
        verbose=True,
        allow_delegation=False,
    )

def create_match_scoring_agent() -> Agent:
    """
    Creates an agent responsible for comparing the resume against the job description.
    """
    return Agent(
        role="Match Scoring Agent",
        goal=(
            "Compare the candidate resume analysis against the job description analysis "
            "and calculate a realistic job match score with clear reasoning."
        ),
        backstory=(
            "You are a senior AI career advisor and technical hiring analyst. "
            "You understand AI Automation Engineer, GenAI Application Developer, "
            "LLM Application Engineer, and Agentic AI Developer roles. "
            "You compare candidates fairly using evidence from the resume and job description. "
            "You do not exaggerate, and you clearly separate strong matches from skill gaps."
        ),
        verbose=True,
        allow_delegation=False,
    )