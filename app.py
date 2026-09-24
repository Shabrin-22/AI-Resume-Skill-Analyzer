import streamlit as st
from skill_matcher import analyze_resume


st.set_page_config(
    page_title="AI Resume Skill Analyzer",
    page_icon="📄",
    layout="wide"
)


st.title("📄 AI Resume Skill Analyzer")

st.write(
    "Analyze how well a resume matches a job description "
    "using skill matching and NLP-based text similarity."
)

st.divider()


# Resume and job description input

col1, col2 = st.columns(2)


with col1:

    st.subheader("📑 Resume")

    resume = st.text_area(
        "Paste your resume below",
        height=300,
        placeholder="Paste your resume text here..."
    )


with col2:

    st.subheader("💼 Job Description")

    job_description = st.text_area(
        "Paste the job description below",
        height=300,
        placeholder="Paste the job description here..."
    )


st.divider()


# Analyze resume

if st.button("🔍 Analyze Resume", use_container_width=True):

    if resume.strip() == "" or job_description.strip() == "":
        st.warning(
            "Please enter both your resume and the job description."
        )

    else:

        (
            resume_skills,
            job_skills,
            matching_skills,
            missing_skills,
            skill_match_percentage,
            nlp_similarity
        ) = analyze_resume(
            resume,
            job_description
        )

        st.success("Resume analysis completed!")


        # Scores

        st.subheader("📊 Analysis Results")

        score1, score2 = st.columns(2)


        with score1:

            st.metric(
                "Skill Match",
                f"{skill_match_percentage:.2f}%"
            )


        with score2:

            st.metric(
                "NLP Similarity",
                f"{nlp_similarity:.2f}%"
            )


        st.divider()


        # Skill results

        result1, result2 = st.columns(2)


        with result1:

            st.subheader("✅ Matching Skills")

            if len(matching_skills) > 0:

                for skill in matching_skills:
                    st.write("✅", skill)

            else:

                st.write("No matching skills found.")


        with result2:

            st.subheader("❌ Missing Skills")

            if len(missing_skills) > 0:

                for skill in missing_skills:
                    st.write("❌", skill)

            else:

                st.write("No missing skills found.")


        st.divider()


        st.caption(
            "AI Resume Skill Analyzer | "
            "Python • NLP • Scikit-learn • Streamlit"
        )