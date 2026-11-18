
import pymupdf

from skill_extraction import extract_skills
from job_description import extract_job_skills


def analyze_resume(pdf_path, job_description_text):

    # Open uploaded PDF and extract text
    resume_text = ""

    with pymupdf.open(pdf_path) as document:
        for page in document:
            resume_text += page.get_text()

    # Extract skills from resume
    resume_skills = extract_skills(resume_text)

    # Extract required skills from job description
    required_skills = extract_job_skills(job_description_text)

    # Find matched skills
    matched_skills = [
        skill for skill in required_skills
        if skill in resume_skills
    ]

    # Find missing skills
    missing_skills = [
        skill for skill in required_skills
        if skill not in resume_skills
    ]

    # Calculate match percentage
    if len(required_skills) > 0:
        match_percentage = (
            len(matched_skills) / len(required_skills)
        ) * 100
    else:
        match_percentage = 0

    # Return analysis results
    return {
        "resume_text": resume_text,
        "resume_skills": resume_skills,
        "required_skills": required_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_percentage": round(match_percentage, 2)
    }
