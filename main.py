import streamlit as st
import tempfile
import os
from streamlit_option_menu import option_menu
from resume_text_extraction import get_pdf_text
from ATS_score_predictor import ats_predictor
from streamlit_extras.let_it_rain import rain
from resume_section_extractor import extract_education, extract_projects, extract_experience, extract_skills, \
    extract_contact_info
from resume_creator import create_resume_pdf
from ATS_content_creation import generate_ats_skills, generate_ats_projects, generate_ats_experience
from background_image import set_background
import hydralit_components as hc
st.set_page_config(layout="wide", page_title="JobFIT Crafter: Enhance your resume")


if 'resume_text' not in st.session_state:
    st.session_state.resume_text = None

if 'ats_results' not in st.session_state:
    st.session_state.ats_results = None

if 'new_resume_path' not in st.session_state:
    st.session_state.new_resume_path = None

if 'job_description_text' not in st.session_state:
    st.session_state.job_description_text = None

if 'selected_tab' not in st.session_state:
    st.session_state.selected_tab = 'Home'

with st.sidebar:
    selected_tab = option_menu("Menu",
                            ["Home", "Upload", "ATS Analysis", "Optimized Resume", "Contact"],
                                icons=['house-heart-fill', 'cloud-upload', "graph-up-arrow", 'box-arrow-down',
                                       'person-lines-fill'],
                                menu_icon="cast", default_index=0,)

if selected_tab != st.session_state.selected_tab:
    st.session_state.selected_tab = selected_tab
    if st.session_state.selected_tab == 'Home':
        st.session_state.clear()
        st.rerun()

if st.session_state['selected_tab'] == 'Home':
    set_background("./helper_images/jobcrafter image.jpg")
    st.markdown("""
                    <h1 
                    style='font-family: Georgia, serif; text-align: center;'>
                    JobFIT Crafter: Enhance Your Resume for Every Job Application
                    </h1>
                """,
                unsafe_allow_html=True)
    st.write(
        """
        Welcome to JobFIT Crafter! We solve the problem of low ATS scores when applying for jobs. Our platform
         analyzes your resume against job descriptions, highlights areas to improve, and helps you create a better
          version. See your ATS score rise instantly and increase your chances of getting shortlisted!
        """)
    st.markdown("""
        <style>
            .features-title {
                font-size: 2em;
                color: #4A90E2;
                font-weight: bold;
                margin-bottom: 10px;
            }
            .features-list {
                font-size: 1.2em;
                line-height: 1.6;
            }
            .feature-item {
                background-color: #f5f5f5;
                border-radius: 8px;
                padding: 10px;
                margin: 5px 0;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }
        </style>
        <div class="features-title">🌟 Key Features 🌟</div>
        <div class="features-list">
            <div class="feature-item">📄 Seamless Upload: Effortlessly upload your resume and job description in just a few clicks.</div>
            <div class="feature-item">🔍 In-Depth ATS Analysis: Receive a comprehensive analysis of your resume tailored to specific job requirements.</div>
            <div class="feature-item">✍️ Optimize and Download: Modify your resume with expert insights and download a polished, ATS-friendly version.</div>
        </div>
    """, unsafe_allow_html=True)


elif st.session_state['selected_tab'] == "Upload":
    st.title("Upload Your Resume and Job Description")

    pdf_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)
    st.session_state.job_description_text = st.text_area("Enter Job Description Text", height=300)

    if st.button("Analyze Resume") and pdf_files and st.session_state.job_description_text:
        resume_text = get_pdf_text(pdf_files)
        st.session_state.resume_text = resume_text
        loader_placeholder = st.empty()

        with hc.HyLoader('This will take around 20 seconds to analyze your resume...',hc.Loaders.standard_loaders,index=[2,2,2,2]):
                ats_results = ats_predictor(resume_text, st.session_state.job_description_text)
                st.session_state.ats_results = ats_results


        st.markdown(
            """
            <div style="
                background-color: #f0f0f0;
                padding: 20px;
                border-radius: 15px;
                box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
                text-align: center;
                font-family: 'Helvetica', sans-serif;
                font-size: 24px;
                color: #333;
                ">
                <p><strong>Resume and Job Description Uploaded!</strong></p>
                <p>Proceed to the <em>'ATS Analysis'</em> page to view detailed results.</p>
            </div>
            """,
            unsafe_allow_html=True
        )


elif st.session_state['selected_tab'] == "ATS Analysis":
    st.title("ATS Analysis Results")

    if st.session_state.ats_results and st.session_state.resume_text:
        score = st.session_state.ats_results["score"]
        keywords = st.session_state.ats_results["keyword_insights"]
        missing = st.session_state.ats_results["missing_skills"]
        ranking = st.session_state.ats_results["resume_ranking"]
        flagging = st.session_state.ats_results["flagging_issues"]

        card_style = """
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Lobster&family=Open+Sans:wght@400;700&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Lobster&family=Merriweather:wght@300;400&display=swap');
    
            .card {
                padding: 20px;
                margin: 10px 0;
                border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
                font-family: 'Merriweather', serif;
            }
            .green-card {
                background-color: #e6f9e6;
                color: #2e7d32;
            }
            .red-card {
                background-color: #fbeae5;
                color: #d32f2f;
            }
            .card-title {
                font-family: 'Lobster', cursive;
                font-weight: bold;
                font-size: 24px;
                margin-bottom: 10px;
            }
            .card-content {
                font-size: 18px;
            }
            </style>
            """

        st.markdown(card_style, unsafe_allow_html=True)

        ats_score = st.session_state.ats_results["score"]
        st.markdown(f"""
            <div class="card green-card">
                <div class="card-title">ATS Score</div>
                <div class="card-content">Your ATS Score is: {ats_score}</div>
            </div>
            """, unsafe_allow_html=True)

        keywords = st.session_state.ats_results["keyword_insights"]
        st.markdown(f"""
            <div class="card green-card">
                <div class="card-title">Keywords Insights</div>
                <div class="card-content">{keywords}</div>
            </div>
            """, unsafe_allow_html=True)

        missing_skills = ', '.join(st.session_state.ats_results["missing_skills"])
        st.markdown(f"""
            <div class="card red-card">
                <div class="card-title">Missing Skills</div>
                <div class="card-content">{missing_skills}</div>
            </div>
            """, unsafe_allow_html=True)

        ranking = st.session_state.ats_results["resume_ranking"]
        st.markdown(f"""
            <div class="card green-card">
                <div class="card-title">Your Resume Ranking</div>
                <div class="card-content">{ranking}</div>
            </div>
            """, unsafe_allow_html=True)

        flagging = st.session_state.ats_results["flagging_issues"]
        st.markdown(f"""
            <div class="card green-card">
                <div class="card-title">Flagging Issues</div>
                <div class="card-content">{flagging}</div>
            </div>
            """, unsafe_allow_html=True)

    else:
        st.error("Please upload your resume and job description first on the 'Upload Resume' page.")

elif st.session_state['selected_tab'] == "Optimized Resume":
    st.title("Your Optimized Resume")

    if st.session_state.ats_results and st.session_state.resume_text:
        if st.session_state.new_resume_path is None:
            with hc.HyLoader('This will take around 2-4 minutes to analyze and create a new optimized resume...',hc.Loaders.standard_loaders,index=[2,2,2,2]):
                resume_text = st.session_state.resume_text
                ats = st.session_state.ats_results

                contact = extract_contact_info(resume_text)
                education = extract_education(resume_text)
                projects = extract_projects(resume_text)
                experience = extract_experience(resume_text)
                skills = extract_skills(resume_text)

                ats_skills = generate_ats_skills(skills, st.session_state.job_description_text, ats)
                ats_experience = generate_ats_experience(experience, st.session_state.job_description_text, ats)
                ats_projects = generate_ats_projects(projects, st.session_state.job_description_text, ats)

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
                    st.session_state.new_resume_path = temp_pdf_path

            new_resume_text = get_pdf_text([st.session_state.new_resume_path])
            new_ats = ats_predictor(new_resume_text, st.session_state.job_description_text)
            st.session_state.new_ats = new_ats

            if st.session_state.new_ats and st.session_state.new_resume_path:
                prev_ats = st.session_state.ats_results["score"]
                st.markdown(
                    f"""
                        <div style="display: flex; justify-content: center; align-items: center; padding: 20px;">
                            <div style="background-color: #f0f0f0; border-radius: 10px; padding: 20px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); width: 1200px; text-align: center;">
                                <h2 style="color: #2E86C1; font-family: 'Arial';">Improvised ATS Score</h2>
                                <div style="font-size: 24px; font-weight: bold; color: #1ABC9C;">
                                    {prev_ats} <span style="color: #7F8C8D;">→</span> {new_ats["score"]}
                                </div>
                                <p style="color: #555; font-family: 'Arial';">
                                    Congratulations! Your resume has been optimized with an improved ATS score.
                                </p>
                            </div>
                        </div>
                        """, unsafe_allow_html=True
                )
                rain(emoji="🎉", font_size=100, falling_speed=60, animation_length="infinite")
                with open(st.session_state.new_resume_path, "rb") as file:
                    st.download_button(
                        label="Download Optimized Resume PDF",
                        data=file,
                        file_name="optimized_resume.pdf",
                        mime="application/pdf"
                    )
                if st.session_state.new_resume_path:
                    os.remove(st.session_state.new_resume_path)

    else:
        st.error("Please upload your resume and perform the ATS analysis before downloading.")


elif st.session_state['selected_tab'] == "Contact":
    st.markdown(
        """
        <style>
        .contact-container {
            background-color: #f9f9f9;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
            text-align: center;
            font-family: 'Helvetica', sans-serif;
        }
        .contact-container h1 {
            font-size: 36px;
            color: #333;
        }
        .contact-container p {
            font-size: 18px;
            color: #555;
        }
        .contact-container a {
            color: #0073b1; /* LinkedIn blue */
            text-decoration: none;
            font-weight: bold;
        }
        .contact-container a:hover {
            color: #005582;
        }
        .emoji {
            font-size: 24px;
        }
        </style>

        <div class="contact-container">
            <h1>Contact Us 😄</h1>
            <p>Have a question, a comment, or just want to say hi?</p>
            <p class="emoji">📧 <strong>For inquiries:</strong> Feel free to reach out to us at: 
            <a href="mailto:keshavk5655@gmail.com">keshavk5655@gmail.com</a>
            <br><br><br>🔗 <strong>Recruiter Alert:</strong> If you’re looking to hire me, 
            <a href="https://www.linkedin.com/in/keshav-kumar-arri/" target="_blank">connect with me on LinkedIn</a> and let's chat professionally 😉! <br>
            (But if you're here just to say I’m awesome, use the email above!)
            <br> <br><br>Sorry, no contact numbers! I believe in the magic of emails and LinkedIn – 
            let's keep it digital ✌️!<br>Made with love and a dash of humor, just for you. Thank you for using JobFIT Crafter! 💼✨</p>
        </div>
        """, unsafe_allow_html=True
    )

st.sidebar.markdown("---")
st.sidebar.write("Thank you for using JobFIT Crafter created by Keshav!")
