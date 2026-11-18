
# AI-Powered Career & Skill Gap Analyzer

## Project Overview

The AI-Powered Career & Skill Gap Analyzer is a web-based application that analyzes a user's resume and compares their skills with the requirements of a specific job description.

It identifies matched skills, missing skills, calculates a skill match percentage, and provides learning recommendations to help users improve their skills.

## Features

- Resume Upload (PDF format)
- Resume Text Extraction
- Automatic Skill Extraction
- Custom Job Description Input
- Matched Skills Identification
- Missing Skills Identification
- Skill Match Percentage Calculation
- Personalized Learning Recommendations
- Interactive Web Interface

## Technologies Used

- Python
- Flask
- Pandas
- Regular Expressions (Regex)
- PyMuPDF
- HTML
- CSS

## Project Structure

```text
Career_Skill_Gap_Analyzer/
│
├── dataset/
│   ├── Resume.csv
│   ├── cleaned_resume.csv
│   └── resume_skills.csv
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── css/
│       └── style.css
│
├── uploads/
│
├── app.py
├── data_analysis.py
├── skill_extraction.py
├── job_description.py
├── skill_gap_analysis.py
├── recommendations.py
├── resume_parser.py
├── requirements.txt
└── README.md
```


## How It Works

1. The user uploads their resume in PDF format.
2. The user enters a Job Description.
3. PyMuPDF extracts text from the uploaded resume.
4. The system extracts skills from the resume using keyword matching and regular expressions.
5. Required skills are extracted from the Job Description.
6. The system compares resume skills with required skills.
7. It identifies matched skills and missing skills.
8. A match percentage is calculated based on the matched required skills.
9. Learning recommendations are displayed for missing skills.
10. The results are shown on a dashboard.


## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd Career_Skill_Gap_Analyzer
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
python app.py
```

### 7. Open in Browser

```text
http://127.0.0.1:5000
```

## Dataset

The project uses the Resume Dataset from Kaggle for resume analysis and skill extraction.

Dataset Source:

https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset

## Future Scope

- Expand the skill database.
- Improve skill extraction accuracy.
- Add support for more job roles.
- Integrate advanced NLP techniques.

## Author

Anshika Kumari

B.Tech - Computer Science and Engineering (AIML)
