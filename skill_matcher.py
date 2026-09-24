import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


skills = [
    "python",
    "java",
    "c++",
    "c",
    "sql",
    "html",
    "css",
    "javascript",
    "git",
    "github",
    "react",
    "node.js",
    "spring boot",
    "rest api",
    "mongodb",
    "mysql",
    "machine learning",
    "data structures",
    "algorithms",
    "streamlit",
    "scikit-learn"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills:

        if skill in ["c", "c++", "node.js"]:

            pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        else:

            pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):

            found_skills.append(skill)

    return found_skills


def calculate_similarity(resume, job_description):

    documents = [resume, job_description]

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )

    score = similarity[0][0] * 100

    return score


def analyze_resume(resume, job_description):

    resume_skills = extract_skills(resume)

    job_skills = extract_skills(job_description)

    matching_skills = []

    for skill in job_skills:

        if skill in resume_skills:
            matching_skills.append(skill)


    missing_skills = []

    for skill in job_skills:

        if skill not in resume_skills:
            missing_skills.append(skill)


    if len(job_skills) > 0:

        skill_match_percentage = (
            len(matching_skills) / len(job_skills)
        ) * 100

    else:

        skill_match_percentage = 0


    nlp_similarity = calculate_similarity(
        resume,
        job_description
    )


    return (
        resume_skills,
        job_skills,
        matching_skills,
        missing_skills,
        skill_match_percentage,
        nlp_similarity
    )