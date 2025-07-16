import streamlit as st
import PyPDF2
import os
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# Streamlit app setup
st.set_page_config(page_title="AI Resume Critiquer", page_icon="📄", layout="centered")
st.title("📄 AI Resume Critiquer")
st.markdown("Upload your resume below 👇")

# File upload and input
uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you're targeting")
analyze = st.button("Analyze Resume")

# Extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"
    return text

# Extract text from file
def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(uploaded_file)
    elif uploaded_file.type == "text/plain":
        return uploaded_file.read().decode("utf-8")
    else:
        return ""

# Resume analysis
if analyze and uploaded_file and job_role:
    try:
        resume_text = extract_text_from_file(uploaded_file)

        if not resume_text.strip():
            st.error("❌ Could not extract text from the uploaded file.")
        else:
            with st.spinner("🤖 Analyzing your resume with AI..."):
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that reviews resumes."},
                        {"role": "user", "content": f"My resume:\n{resume_text}\n\nThe job role I'm targeting is: {job_role}.\nGive me feedback on how well my resume fits and suggestions to improve it."}
                    ]
                )
                feedback = response['choices'][0]['message']['content']
                st.success("✅ Resume Analysis Complete")
                st.markdown("### 💬 Feedback:")
                st.write(feedback)

    except Exception as e:
        st.error(f"⚠️ An error occurred: {str(e)}")
