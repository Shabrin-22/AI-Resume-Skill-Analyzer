# AI Resume Skill Analyzer

An NLP-based application that analyzes a resume against a job description and identifies matching and missing technical skills.

## Features

- Extracts technical skills from resume and job description
- Identifies matching skills
- Identifies missing skills
- Calculates skill match percentage
- Calculates NLP-based text similarity
- Provides an interactive Streamlit interface

## Technologies Used

- Python
- Streamlit
- Scikit-learn
- NLP
- TF-IDF
- Cosine Similarity
- Regular Expressions

## How It Works

1. User enters their resume text.
2. User enters a job description.
3. The application extracts technical skills from both texts.
4. It compares the skills and identifies matching and missing skills.
5. TF-IDF converts the resume and job description into numerical vectors.
6. Cosine similarity measures the textual similarity between them.
7. The results are displayed through the Streamlit interface.

## Example Output

The application displays:

- Skill Match Percentage
- NLP Similarity Percentage
- Matching Skills
- Missing Skills

## Installation

Clone the repository:

```bash
git clone https://github.com/Shabrin-22/AI-Resume-Skill-Analyzer.git