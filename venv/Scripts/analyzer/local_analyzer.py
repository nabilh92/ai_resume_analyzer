import re
from collections import Counter

def extract_keywords(text):
    #Extract alphanumeric keywords from text (no stopwords).
    text = text.lower()
    words = re.findall(r"\b[a-z]{3,}\b", text)
    return words

def local_resume_analysis(resume_text, job_description):
    #Compare keywords and compute a basic match score.
    resume_words = extract_keywords(resume_text)
    job_words = extract_keywords(job_description)

    resume_counts = Counter(resume_words)
    job_counts = Counter(job_words)

    # Determine overlap
    overlap = set(resume_words) & set(job_words)
    missing = set(job_words) - set(resume_words)

    # Calculate simple score: ratio of overlap to total unique job keywords
    if len(job_words) == 0:
        match_score = 0
    else:
        match_score = round((len(overlap) / len(set(job_words))) * 100, 2)

    strengths = list(overlap)
    missing_skills = list(missing)

    suggestions = []
    if missing_skills:
        suggestions.append("Add missing keywords: " + ", ".join(list(missing_skills)[:5]))
    if match_score < 70:
        suggestions.append("Tailor resume keywords closer to the job description.")
    else:
        suggestions.append("Resume is well-aligned with the job requirements.")

    return {
        "match_score": match_score,
        "missing_skills": missing_skills,
        "strengths": strengths,
        "suggestions": suggestions,
        "mode": "local"
    }