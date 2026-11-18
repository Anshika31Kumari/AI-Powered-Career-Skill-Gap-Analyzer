# AI-Powered Career & Skill Gap Analyzer

## Project Overview

The AI-Powered Career & Skill Gap Analyzer is a Python-based web application that helps users identify their skills and understand the skill gaps between their resume and a particular job description.

Users can upload their resume in PDF format and enter a custom Job Description. The system extracts skills, identifies matched and missing skills, calculates a match percentage, and provides learning recommendations.

The application currently uses keyword-based skill extraction and matching with Regular Expressions (Regex).

## Features

- Upload resumes in PDF format.
- Extract resume text using PyMuPDF.
- Extract skills using keyword matching.
- Enter custom Job Descriptions.
- Identify matched skills.
- Identify missing skills.
- Calculate resume match percentage.
- Generate learning recommendations.
- Display results on a web dashboard.

## Technologies Used

- Python
- Flask
- Pandas
- PyMuPDF
- Regular Expressions (Regex)
- HTML
- CSS

## Project Structure

```text
AI-Powered-Career-Skill-Gap-Analyzer/
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── app.py
├── data_analysis.py
├── job_description.py
├── recommendations.py
├── resume_parser.py
├── skill_extraction.py
├── skill_gap_analysis.py
├── requirements.txt
├── .gitignore
└── README.md
```

**Note:** The dataset CSV files and uploaded resumes are not included in this public repository.

## How It Works

1. The user uploads a resume in PDF format.
2. The user enters a Job Description.
3. PyMuPDF extracts text from the uploaded resume.
4. The system extracts skills using keyword matching and Regular Expressions.
5. Required skills are extracted from the Job Description.
6. Resume skills are compared with required skills.
7. Matched and missing skills are identified.
8. A match percentage is calculated.
9. Learning recommendations are generated for missing skills.
10. Results are displayed on the dashboard.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Anshika31Kumari/AI-Powered-Career-Skill-Gap-Analyzer.git
```

### 2. Open the Project Folder

```bash
cd AI-Powered-Career-Skill-Gap-Analyzer
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
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

Visit:

```text
http://127.0.0.1:5000/
```

## Dataset

This project uses the Resume Dataset from Kaggle.

**Dataset Source:** [Kaggle Resume Dataset](https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset)

To run the dataset preprocessing and skill extraction scripts, download the dataset and place `Resume.csv` inside a folder named `dataset` in the project directory.

The dataset is not included in this GitHub repository.

## Future Scope

- Improve skill extraction using Natural Language Processing (NLP).
- Integrate Machine Learning models for advanced analysis.
- Expand the skill database.
- Support additional resume formats.
- Provide more personalized learning resources.

## Author

**Anshika Kumari**

B.Tech – Computer Science and Engineering (AIML)

JIS University, Kolkata
