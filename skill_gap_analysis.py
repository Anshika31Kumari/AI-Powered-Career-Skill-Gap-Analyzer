import pandas as pd
import ast

from recommendations import generate_recommendations
from job_description import job_description, extract_job_skills

# Load resume skills dataset
df = pd.read_csv("dataset/resume_skills.csv")

# Convert skills into Python lists
df["extracted_skills"] = df["extracted_skills"].apply(ast.literal_eval)

# Extract required skills from job description
required_skills = extract_job_skills(job_description)


# Function for skill gap analysis
def analyze_skill_gap(resume_id):

    # Find resume using ID
    selected_resume = df[df["ID"] == resume_id]

    if selected_resume.empty:
        print("Resume ID not found!")
        return

    # Get candidate skills
    candidate_skills = selected_resume.iloc[0]["extracted_skills"]

    # Compare skills
    matched_skills = [
        skill for skill in required_skills
        if skill in candidate_skills
    ]

    missing_skills = [
        skill for skill in required_skills
        if skill not in candidate_skills
    ]

    # Calculate percentage
    match_percentage = (
        len(matched_skills) / len(required_skills)
    ) * 100

    # Display report
    print("\n--- SKILL GAP ANALYSIS REPORT ---")
    print("Resume ID:", resume_id)
    print("Candidate Skills:", candidate_skills)
    print("Matched Skills:", matched_skills)
    print("Missing Skills:", missing_skills)
    print("Match Percentage:", round(match_percentage, 2), "%")

# Generate learning recommendations
    generate_recommendations(missing_skills)

# Test with a resume ID
analyze_skill_gap(16852973)