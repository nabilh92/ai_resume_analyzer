import streamlit as st
from analyzer.extractor import extract_text_from_pdf
from analyzer.analyzer import analyze_resume

st.title("🧠 AI Resume Analyzer")

resume_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
job_description = st.text_area("Paste job description")

if resume_file and job_description and st.button("Analyze"): # when resume is uploaded and job decription text area is populated, Analyze button is enabled.
    with open("temp.pdf", "wb") as f:
        f.write(resume_file.read())

    resume_text = extract_text_from_pdf("temp.pdf")
    st.info("Analyzing resume...")

    result = analyze_resume(resume_text, job_description)
    st.success("Analysis Complete")
    st.json(result)   