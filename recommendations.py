
# Learning Recommendations System

recommendations = {

    "python": "Learn Python basics, functions and OOP.",

    "sql": "Learn SQL queries, joins and database management.",

    "flask": "Learn Flask framework and build web applications.",

    "machine learning": "Study ML algorithms and build ML projects.",

    "pandas": "Learn data manipulation using Pandas.",

    "numpy": "Learn arrays and numerical computing using NumPy.",

    "git": "Learn Git commands and version control.",

    "problem solving": "Practice coding problems and logical thinking.",

    "html": "Learn HTML structure and web page creation.",

    "css": "Learn CSS styling and responsive web design.",

    "data analysis": "Learn data cleaning, analysis and visualization."
}


# Function to generate recommendations

def generate_recommendations(missing_skills):

    suggested_learning = {}

    for skill in missing_skills:

        suggestion = recommendations.get(
            skill,
            "Explore learning resources for this skill."
        )

        suggested_learning[skill] = suggestion

    return suggested_learning
