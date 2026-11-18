
import re


# Technical Skills Dictionary
skills = [
    "python", "java", "javascript", "c++", "c#",
    "sql", "html", "css", "react", "angular",
    "node.js", "flask", "django", "fastapi",
    "machine learning", "deep learning",
    "artificial intelligence",
    "natural language processing",
    "data science", "data analysis",
    "pandas", "numpy", "matplotlib",
    "scikit-learn", "tensorflow", "pytorch",
    "excel", "power bi", "tableau",
    "git", "github", "docker", "aws", "azure",
    "mysql", "mongodb",
    "communication", "leadership", "problem solving"
]


# Sample Job Description
job_description = """
We are looking for a Python Developer.

The candidate should have knowledge of Python,
SQL, Flask, Machine Learning, Data Analysis,
Pandas, NumPy, Git and Problem Solving.

Knowledge of HTML and CSS is also preferred.
"""


# Function to extract skills from job description
def extract_job_skills(description):

    required_skills = []

    for skill in skills:

        # Match complete words or phrases
        pattern = r'(?<!\w)' + re.escape(skill) + r'(?!\w)'

        if re.search(pattern, description, re.IGNORECASE):

            required_skills.append(skill)

    return required_skills


# Run only when this file is executed directly
if __name__ == "__main__":

    job_skills = extract_job_skills(job_description)

    print("\n--- Job Description ---")
    print(job_description)

    print("\n--- Required Skills ---")
    print(job_skills)

    print("\nTotal Required Skills:", len(job_skills))
