import os
from pathlib import Path

from dotenv import load_dotenv
from crewai import Crew, Process

from app.agents.jobmatch_agents import (
    create_resume_analyst_agent,
    create_job_description_analyst_agent,
    create_match_scoring_agent,
)
from app.tasks.jobmatch_tasks import (
    create_resume_analysis_task,
    create_job_description_analysis_task,
    create_match_scoring_task,
)


def read_file(file_path: str) -> str:
    """
    Reads text content from a file.
    """
    return Path(file_path).read_text(encoding="utf-8")


def save_report(report_text: str, output_path: str) -> None:
    """
    Saves the CrewAI output into a markdown report file.
    """
    Path(output_path).write_text(str(report_text), encoding="utf-8")


def main():
    """
    Runs the first version of Agentic JobMatch AI.
    """

    # Load environment variables from .env
    load_dotenv(dotenv_path=".env")

    # Use a cheaper OpenAI model for development
    os.environ.setdefault("OPENAI_MODEL_NAME", "gpt-4o-mini")

    resume_text = read_file("data/sample_resume.txt")
    job_description_text = read_file("data/sample_job_description.txt")

    resume_analyst_agent = create_resume_analyst_agent()
    jd_analyst_agent = create_job_description_analyst_agent()
    match_scoring_agent = create_match_scoring_agent()

    resume_analysis_task = create_resume_analysis_task(
        resume_text=resume_text,
        resume_analyst_agent=resume_analyst_agent,
    )

    jd_analysis_task = create_job_description_analysis_task(
        job_description_text=job_description_text,
        jd_analyst_agent=jd_analyst_agent,
    )

    match_scoring_task = create_match_scoring_task(
    resume_analysis_task=resume_analysis_task,
    jd_analysis_task=jd_analysis_task,
    match_scoring_agent=match_scoring_agent,
)
    crew = Crew(
    agents=[
        resume_analyst_agent,
        jd_analyst_agent,
        match_scoring_agent,
    ],
    tasks=[
        resume_analysis_task,
        jd_analysis_task,
        match_scoring_task,
    ],
    process=Process.sequential,
    verbose=True,
)
    print("\nStarting Agentic JobMatch AI...\n")

    result = crew.kickoff()

    output_file = "outputs/job_match_score_report.md"
    save_report(result, output_file)

    print("\nCrewAI run completed.")
    print(f"Report saved to: {output_file}")


if __name__ == "__main__":
    main()