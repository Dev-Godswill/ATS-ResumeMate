import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
import pyttsx3  # For text-to-speech functionality
from dotenv import load_dotenv

# Load all the environment variables
load_dotenv()

# Configure Google Generative AI (Gemini)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize text-to-speech engine
tts_engine = pyttsx3.init()

## Gemini Pro Response
def get_gemini_response(input):
    """
    Sends the input to the Gemini model and returns the response.
    """
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    """
    Extracts text from a PDF file and returns it as a string.
    """
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += str(page.extract_text())
    return text

# Summarize the resume content
def summarize_resume(text):
    """
    Summarizes the resume text using the Gemini AI model.
    """
    prompt = f"Summarize this resume: {text}"
    return get_gemini_response(prompt)

# Extract strengths from the resume
def extract_strengths(text):
    """
    Extracts strengths from the resume text using the Gemini AI model.
    """
    prompt = f"Based on this resume, list the candidate's strengths: {text}"
    return get_gemini_response(prompt)

# Extract weaknesses from the resume
def extract_weaknesses(text):
    """
    Extracts weaknesses from the resume text using the Gemini AI model.
    """
    prompt = f"Based on this resume, list the candidate's weaknesses: {text}"
    return get_gemini_response(prompt)

# Recommend job roles
def recommend_job_roles(text):
    """
    Recommends job roles based on the resume using the Gemini AI model.
    """
    prompt = f"Based on this resume, recommend suitable job roles: {text}"
    return get_gemini_response(prompt)

# Provide final thoughts on the resume
def final_thoughts_on_cv(text, jd):
    """
    Provides final critique and insights on whether the candidate should apply for the job.
    """
    prompt = f"""
    Based on this resume:
    {text}
    
    And this job description:
    {jd}
    
    Should the candidate apply for this role? Please provide final thoughts on how the candidate can improve their CV to match this role better. 
    Highlight what changes could give the candidate an upper edge and a higher percentage match for the job.
    """
    return get_gemini_response(prompt)

# New functionality: Suggest improvements in the CV
def suggest_cv_improvements(text):
    """
    Suggest specific improvements within the CV.
    """
    prompt = f"Suggest specific areas of improvement in the following resume: {text}"
    return get_gemini_response(prompt)

# New functionality: Text-to-Speech
def speak_text(text):
    """
    Uses text-to-speech to read the given text aloud.
    """
    tts_engine.say(text)
    tts_engine.runAndWait()

# ---- Main Streamlit App ----

# Sidebar Navigation
st.sidebar.title("📋 ResumeMate Dashboard")
st.sidebar.write("Navigate through the sections below:")
page = st.sidebar.radio(
    "Select a page:",
    ("Home", "Analyze Resume"),
)

# ---- Home Page ----
if page == "Home":
    st.title("🚀 Welcome to ResumeMate!")
    st.write("""
        ### Your friendly AI-powered resume analyzer 💼🔍
        ResumeMate helps you improve your resume by analyzing it against job descriptions, identifying strengths, weaknesses, and recommending suitable job roles.
    """)
    
    st.subheader("About ResumeMate:")
    st.markdown("""
    - **🔍 ATS-Style Resume Evaluation**: Compare your resume with job descriptions to see how well it matches.
    - **💡 Resume Summarizer**: Get a concise summary of your resume.
    - **💪 Strengths Identification**: Discover the strong points in your resume.
    - **⚠️ Weaknesses Identification**: Uncover the areas that could be improved.
    - **📊 Job Role Recommendations**: Get job role suggestions based on your resume's content.
    """)
    
    st.subheader("📬 Get in Touch")
    st.markdown("""
    - **Email**: [your_email@example.com](mailto:your_email@example.com)
    - **LinkedIn**: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)
    - **GitHub**: [github.com/yourprofile](https://github.com/yourprofile)
    """)
    
    # Contact Us Section
    with st.expander("📧 Contact Us"):
        st.write("For queries, please fill out the form below:")
        contact_email = st.text_input("Your Email Address:")
        query = st.text_area("Your Query:")
        if st.button("Send Information"):
            if contact_email and query:
                st.success("Thank you! We have received your query and will get back to you soon.")
            else:
                st.error("Please provide both an email address and your query.")

    # Footer
    st.markdown(
        """
        <div style="text-align: right;">
            Designed by: <strong>[Your Name]</strong>
        </div>
        """, unsafe_allow_html=True
    )

# ---- Analyze Resume Page ----
elif page == "Analyze Resume":
    st.title("🔍 Analyze Your Resume with ResumeMate")

    # Job description input
    jd = st.text_area("Paste the Job Description", help="Enter the job description for the position you're applying to.")

    # Resume upload
    uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload your resume in PDF format.")

    if uploaded_file is not None:
        # Extract text from the uploaded resume
        resume_text = input_pdf_text(uploaded_file)
        
        # Define the input prompt for job matching
        input_prompt = """
        Compare this resume:
        {text}
        
        With the following job description:
        {jd}
        
        List the percentage match and identify any missing or weak areas in the resume for the role.
        """
        
        # Buttons for features with Emojis
        if st.button("📝 Summarize the Resume"):
            summary = summarize_resume(resume_text)
            st.subheader("Resume Summary:")
            st.write(summary)
            # Speak the summary aloud (disabled to avoid runtime error)
            # speak_text(summary)
        
        if st.button("💪 Strengths"):
            strengths = extract_strengths(resume_text)
            st.subheader("Strengths:")
            st.write(strengths)
        
        if st.button("⚠️ Weaknesses"):
            weaknesses = extract_weaknesses(resume_text)
            st.subheader("Weaknesses:")
            st.write(weaknesses)
        
        if st.button("📊 Job Percentage Match"):
            if jd:  # Check if a job description is provided
                input_data = input_prompt.format(text=resume_text, jd=jd)
                response = get_gemini_response(input_data)
                st.subheader("Job Percentage Match and Missing Keywords:")
                st.write(response)
            else:
                st.error("Please enter a job description before running the job match analysis.")
        
        if st.button("📋 Recommended Job Roles"):
            roles = recommend_job_roles(resume_text)
            st.subheader("Recommended Job Roles:")
            st.write(roles)

        # Use session state to track if "Final Thoughts" was clicked
        if st.button("📝 Final Thoughts"):
            if jd:
                # Store in session state that the "Final Thoughts" button was clicked
                st.session_state.final_thoughts_clicked = True
                final_insights = final_thoughts_on_cv(resume_text, jd)
                st.subheader("Final Thoughts:")
                st.write(final_insights)
            else:
                st.error("Please provide a job description for final thoughts.")

        # Check if final thoughts button was clicked and show additional options
        if st.session_state.get('final_thoughts_clicked', False):
            if st.button("📍 Suggest CV Improvements"):
                improvements = suggest_cv_improvements(resume_text)
                st.subheader("Suggested Improvements:")
                st.write(improvements)
            
            if st.button("🚀 I'll Improve It Myself"):
                st.success("Thank you! I am here to help at any time.")

    else:
        st.write("Please upload a resume to use the features.")

    # Footer on the second page
    st.markdown(
        """
        <div style="text-align: right;">
            Designed by: <strong>[Your Name]</strong>
        </div>
        """, unsafe_allow_html=True
    )