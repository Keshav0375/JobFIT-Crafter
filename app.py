import streamlit as st
import tempfile
import os
from resume_text_extraction import get_pdf_text
from ATS_score_predictor import ats_predictor
from resume_section_extractor import extract_education, extract_projects, extract_experience, extract_skills, extract_contact_info
from resume_creator import create_resume_pdf
from ATS_content_creation import generate_ats_skills, generate_ats_projects, generate_ats_experience

st.set_page_config(layout="wide", page_title="JobFIT Crafter: Enhance your resume")
pdf_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)
job_description_text = st.text_area("Enter Job Description Text(Make sure Job description should be relevant based on your job profile)", height=300)

if pdf_files and job_description_text:
    resume_text = get_pdf_text(pdf_files)

    st.success("Resume Found")

    with st.spinner("Extracting Information...."):
        ats = ats_predictor(resume_text, job_description_text)
        score = ats["score"]
        keywords = ats["keyword_insights"]
        missing = ats["missing_skills"]
        ranking = ats["resume_ranking"]
        flagging = ats["flagging_issues"]
        st.success(score)
        st.success(keywords)
        st.success(missing)
        st.success(ranking)
        st.success(flagging)

        contact = extract_contact_info(resume_text)
        st.success("Contact Info Found")

        education = extract_education(resume_text)
        st.success("Education Found")

        projects = extract_projects(resume_text)
        st.success("Projects Found")

        experience = extract_experience(resume_text)
        st.success("Experience Found")

        skills = extract_skills(resume_text)
        st.success("Skills Found")

    with st.spinner("Making your Resume strong...."):
        ats_skills = generate_ats_skills(skills, job_description_text, ats)
        st.success("Modified Skills")
        ats_experience = generate_ats_experience(experience, job_description_text, ats)
        st.success("Modified experience")
        ats_projects = generate_ats_projects(projects, job_description_text, ats)
        st.success("Modified projects")

        data = {
            "name": contact["name"],
            "phone": contact["contact_number"],
            "email": contact["email"],
            "linkedin": contact["linkedin_url"],
            "github": contact["github_url"],
            "educations": education["educations"],
            "skills": ats_skills["skills"],
            "projects": ats_projects["projects"],
            "experiences": ats_experience["experiences"]
        }

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_pdf_path = temp_file.name
            create_resume_pdf(data, temp_pdf_path)

        new_resume_text = get_pdf_text([temp_pdf_path])

    with st.spinner("Re-analyzing the updated resume..."):
        new_ats = ats_predictor(new_resume_text, job_description_text)
        new_score = new_ats["score"]
        new_keywords = new_ats["keyword_insights"]
        new_missing = new_ats["missing_skills"]
        new_ranking = new_ats["resume_ranking"]
        new_flagging = new_ats["flagging_issues"]

        st.success(f"New ATS Score: {new_score}")
        st.success(f"New Keywords: {new_keywords}")
        st.success(f"New Missing Skills: {new_missing}")
        st.success(f"New Resume Ranking: {new_ranking}")
        st.success(f"New Flagging Issues: {new_flagging}")

        with open(temp_pdf_path, "rb") as file:
            btn = st.download_button(
                label="Download Resume PDF",
                data=file,
                file_name="updated_resume.pdf",
                mime="application/pdf"
            )
        os.remove(temp_pdf_path)

