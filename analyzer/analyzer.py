from openai import OpenAI
import os
import json
import re
from dotenv import load_dotenv
from .local_analyzer import local_resume_analysis

load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None

def analyze_resume(resume_text, job_description):

    if client: # Use AI if API Key is available
        try:
            prompt =f"""
            You are a professional career advisor.
            Compare the following RESUME and JOB DESCRIPTION.
            - Identify top keywords
            - List missing skills or keywords.
            - Suggest specific improvements or rewrites.
            - Give an overall match score (0-100%).

            RESUME:
            {resume_text}

            JOB DESCRIPTION:
            {job_description}

            Respond in this JSON format:
            {{
                "match_score": number,
                "missing_skills": [list of strings],
                "strengths": [list of strings],
                "suggestions": [list of strings]
            }}
            """

            response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            )

            # Extract raw model output
            raw_output = response.choices[0].message.content.strip()

            # ✅ Remove Markdown code fences (```json ... ```)
            clean_output = re.sub(r"```(?:json)?", "", raw_output).strip()

            # ✅ Parse JSON safely
            try:
                result = json.loads(clean_output)
                result["mode"] = "ai"
            except json.JSONDecodeError:
                print("⚠️ Could not parse model output as JSON. Here's the raw text:")
                print(raw_output)
                result = {"error": "Invalid JSON format returned by model"}

            return result
        
        except Exception as e:
            print(f"⚠️ AI Analysis failed: {e}\nFalling back to local keyword analysis...")
            return local_resume_analysis(resume_text, job_description)
        
    else: #uses local fallback to check 
        print("⚙️ No OpenAI API key found. Using local keyword analyzer.")
        return local_resume_analysis(resume_text, job_description)