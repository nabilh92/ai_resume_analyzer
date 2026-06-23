import streamlit as st
from analyzer.extractor import extract_text_from_pdf
from analyzer.analyzer import analyze_resume

st.set_page_config(page_title="AI Resume Analyzer", page_icon="🧠", layout="centered")

st.title("🧠 AI Resume Analyzer")
st.caption("Analyze how well your resume matches a job description — powered by AI with offline fallback.")

# Upload resume
resume_file = st.file_uploader("📄 Upload your resume (PDF only)", type=["pdf"])

# Job description
job_description = st.text_area("🧾 Paste the job description here")

# Action button
if st.button("🔍 Analyze Resume"):
    if not resume_file:
        st.warning("Please upload your resume first.")
        st.stop()
    if not job_description.strip():
        st.warning("Please enter a job description.")
        st.stop()

    # Save uploaded file temporarily
    with open("temp_resume.pdf", "wb") as f:
        f.write(resume_file.read())

    # Extract and analyze
    with st.spinner("Analyzing your resume..."):
        resume_text = extract_text_from_pdf("temp_resume.pdf")
        result = analyze_resume(resume_text, job_description)

    # Display results
    st.subheader("📊 Analysis Results")

    if "error" in result:
        st.error("Error: " + result["error"])
    else:
        st.metric(label="Match Score", value=f"{result.get('match_score', 0)}%")
        st.write("**Analysis Mode:**", "AI" if result.get("mode") == "ai" else "Local (Offline)")
        st.write("---")
        st.write("### ✅ Strengths")
        st.write(", ".join(result.get("strengths", [])) or "None found.")

        st.write("### ❌ Missing Skills")
        st.write(", ".join(result.get("missing_skills", [])) or "None found.")

        st.write("### 💡 Suggestions")
        for s in result.get("suggestions", []):
            st.write(f"- {s}")

st.markdown("---")
st.caption("Built using Python, Streamlit, and GPT-4o-mini.")