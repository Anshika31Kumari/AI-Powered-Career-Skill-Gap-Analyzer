
import pandas as pd
import re
from collections import Counter


# Technical Skills Dictionary
skills = [
    "python",
    "java",
    "javascript",
    "c++",
    "c#",
    "sql",
    "html",
    "css",
    "react",
    "angular",
    "node.js",
    "flask",
    "django",
    "fastapi",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "natural language processing",
    "data science",
    "data analysis",
    "pandas",
    "numpy",
    "matplotlib",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "excel",
    "power bi",
    "tableau",
    "git",
    "github",
    "docker",
    "aws",
    "azure",
    "mysql",
    "mongodb",
    "communication",
    "leadership",
    "problem solving"
]


# Function to extract skills from resume
def extract_skills(resume):

    extracted_skills = []

    for skill in skills:

        # Match complete words or phrases
        pattern = r'(?<!\w)' + re.escape(skill) + r'(?!\w)'

        if re.search(pattern, str(resume), re.IGNORECASE):
            extracted_skills.append(skill)

    return extracted_skills


# Dataset analysis function
def analyze_dataset():

    # Load cleaned dataset
    df = pd.read_csv("dataset/cleaned_resume.csv")

    print("Total Skills Available:", len(skills))

    print("\n--- Available Skills ---")
    for skill in skills:
        print(skill)

    # Extract skills from every resume
    df["extracted_skills"] = df["cleaned_resume"].apply(extract_skills)

    # Display first 5 resumes
    print("\n--- Extracted Skills from First 5 Resumes ---")

    for index, row in df.head(5).iterrows():

        print("\nResume ID:", row["ID"])
        print("Job Category:", row["Category"])
        print("Extracted Skills:", row["extracted_skills"])

    # Count total extracted skills
    print("\n--- Total Skills Found ---")

    total_skills = df["extracted_skills"].apply(len).sum()

    print("Total Skill Occurrences:", total_skills)

    # Count skill frequency
    all_skills = []

    for resume_skills in df["extracted_skills"]:
        all_skills.extend(resume_skills)

    skill_counts = Counter(all_skills)

    # Top 10 skills
    print("\n--- Top 10 Most Common Skills ---")

    for skill, count in skill_counts.most_common(10):
        print(f"{skill}: {count}")

    # Least common skills
    print("\n--- Least Common Skills ---")

    for skill, count in skill_counts.most_common()[-10:]:
        print(f"{skill}: {count}")

    # Save extracted skills
    df.to_csv(
        "dataset/resume_skills.csv",
        index=False
    )

    print("\nExtracted skills saved successfully!")
    print("File: dataset/resume_skills.csv")


# Run dataset analysis only when this file is executed directly
if __name__ == "__main__":
    analyze_dataset()
