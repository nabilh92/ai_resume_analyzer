🧠 AI Resume Analyzer

AI Resume Analyzer is a smart tool that helps you evaluate how well your resume matches a given job description — powered by OpenAI GPT models with an offline keyword-based fallback (no API key required).

Built with Python and Streamlit, it’s designed to help job seekers optimize their resumes for specific job roles in seconds.

🚀 Features

✅ PDF Resume Upload — Extracts and analyzes text from your uploaded resume
✅ Job Description Matching — Compares your resume to any pasted job description
✅ AI-Powered Insights — Uses GPT to suggest missing skills, strengths, and improvements
✅ Offline Mode — Falls back to local keyword analysis when no API key is available
✅ Interactive Web Interface — Simple Streamlit UI for fast, visual results
✅ Deployed on Streamlit Cloud (optional)

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/<yourusername>/ai-resume-analyzer.git
cd ai-resume-analyzer

2️⃣ Create a Virtual Environment
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ (Optional) Add OpenAI API Key

Create a file named .env in the project root:

OPENAI_API_KEY=sk-yourapikeyhere

(If you skip this, the app will run in offline mode using keyword matching.)

💻 Running the App

Start the web interface:

streamlit run app.py

Then open the local URL (default: http://localhost:8501)
