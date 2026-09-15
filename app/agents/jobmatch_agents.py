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


def create_learning_roadmap_agent() -> Agent:
    """
    Creates an agent responsible for generating a practical learning roadmap.
    """
    return Agent(
        role="Learning Roadmap Agent",
        goal=(
            "Create a practical learning and project improvement roadmap based on "
            "the candidate's job match score, missing skills, and experience gaps."
        ),
        backstory=(
            "You are an experienced AI career coach and GenAI engineering mentor. "
            "You help candidates move into AI Automation Engineer, GenAI Application Developer, "
            "LLM Application Engineer, and Agentic AI Developer roles. "
            "You convert skill gaps into practical learning actions, GitHub project improvements, "
            "and interview preparation steps."
        ),
        verbose=True,
        allow_delegation=False,
    )

def create_final_report_agent() -> Agent:
    """
    Creates an agent responsible for producing the final polished report.
    """
    return Agent(
        role="Final Report Agent",
        goal=(
            "Create a polished final job match report that combines resume analysis, "
            "job description analysis, match scoring, and learning roadmap into one clear output."
        ),
        backstory=(
            "You are a senior AI career consultant and technical report writer. "
            "You create clear, recruiter-friendly reports for candidates applying to "
            "AI Automation Engineer, GenAI Application Developer, LLM Application Engineer, "
            "and Agentic AI Developer roles. "
            "You make reports professional, practical, evidence-based, and easy to read."
        ),
        verbose=True,
        allow_delegation=False,
    )