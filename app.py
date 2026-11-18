
from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from resume_parser import analyze_resume
from recommendations import generate_recommendations

app = Flask(__name__)


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Resume Upload Route
@app.route("/analyze", methods=["POST"])
def analyze():

    # Receive uploaded PDF file
    uploaded_file = request.files.get("resume")

    # Check if file is selected
    if uploaded_file is None or uploaded_file.filename == "":
        return "Please select a resume!"

    # Check PDF extension
    if not uploaded_file.filename.lower().endswith(".pdf"):
        return "Only PDF files are allowed!"

    # Secure filename
    filename = secure_filename(uploaded_file.filename)

    if not filename:
        return "Invalid file name!"

    # Receive Job Description from user
    job_description_text = request.form.get("job_description", "").strip()

    # Check if Job Description is provided
    if not job_description_text:
        return "Please enter a Job Description!"

    # Create uploads folder if it does not exist
    os.makedirs("uploads", exist_ok=True)

    # Define file path
    file_path = os.path.join("uploads", filename)

    # Save uploaded PDF
    uploaded_file.save(file_path)

    # Analyze uploaded resume using custom Job Description
    results = analyze_resume(file_path, job_description_text)

    # Generate learning recommendations
    learning_recommendations = generate_recommendations(
        results["missing_skills"]
    )

    # Display analysis results using result.html
    return render_template(
        "result.html",
        resume_skills=results["resume_skills"],
        matched_skills=results["matched_skills"],
        missing_skills=results["missing_skills"],
        match_percentage=results["match_percentage"],
        learning_recommendations=learning_recommendations
    )


# Run Flask Application
if __name__ == "__main__":
    app.run(debug=True)
