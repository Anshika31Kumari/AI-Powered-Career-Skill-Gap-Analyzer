
import pandas as pd

# Load dataset
df = pd.read_csv("dataset/Resume.csv")

# 1. Display first 5 rows
print("\n--- First 5 Records ---")
print(df.head())

# 2. Dataset shape
print("\n--- Dataset Shape ---")
print(df.shape)

# 3. Column names
print("\n--- Column Names ---")
print(df.columns.tolist())

# 4. Dataset information
print("\n--- Dataset Information ---")
df.info()

# 5. Missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# 6. Duplicate records
print("\n--- Duplicate Records ---")
print(df.duplicated().sum())

# 7. Job categories
print("\n--- Job Categories ---")
print(df["Category"].value_counts())

# 8. Total unique categories
print("\n--- Total Categories ---")
print(df["Category"].nunique())


# Display one complete resume sample (first 1000 characters)

print("\n--- Resume Text Sample ---")

sample_resume = df["Resume_str"].iloc[0]

print(sample_resume[:1000])

# Check resume text length

print("\n--- Resume Text Length ---")

print("Characters:", len(sample_resume))


import re

# Function to clean resume text
def clean_text(text):

    # Convert text into lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text


# Apply cleaning to resume text
df["cleaned_resume"] = df["Resume_str"].apply(clean_text)


# Display original and cleaned resume
print("\n--- Original Resume ---")
print(df["Resume_str"].iloc[0][:500])

print("\n--- Cleaned Resume ---")
print(df["cleaned_resume"].iloc[0][:500])

# Count words in each cleaned resume
df["word_count"] = df["cleaned_resume"].apply(lambda x: len(x.split()))

# Display word count
print("\n--- Resume Word Count ---")
print(df["word_count"].head())

# Average word count
print("\n--- Average Resume Word Count ---")
print(df["word_count"].mean())

# Shortest and longest resume
print("\n--- Minimum Word Count ---")
print(df["word_count"].min())

print("\n--- Maximum Word Count ---")
print(df["word_count"].max())


# Check empty resumes
print("\n--- Empty Resumes ---")
empty_resumes = df[df["word_count"] == 0]

print("Number of empty resumes:", len(empty_resumes))

# Display empty resume details
print(empty_resumes[["ID", "Category", "word_count"]])

# Remove empty resumes
df = df[df["word_count"] > 0].copy()

# Reset index
df.reset_index(drop=True)

# Check updated dataset
print("\n--- Dataset After Removing Empty Resumes ---")
print("New Dataset Shape:", df.shape)

# Save cleaned dataset
df.reset_index(drop=True, inplace=False).to_csv(
    "dataset/cleaned_resume.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")