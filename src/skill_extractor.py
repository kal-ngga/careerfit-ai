import pandas as pd

def load_skill_taxonomy(file_path):
    df = pd.read_csv(file_path)
    skills = df["skill"].dropna().str.lower().tolist()
    return skills

def extract_skills(text, skills):
    found_skills = []

    for skill in skills:
        if skill in text:
            found_skills.append(skill)
    return sorted(list(set(found_skills)))

def compare_skills(resume_skills, job_skills):
    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matched_skills = sorted(list(resume_set.intersection(job_set)))
    missing_skills = sorted(list(job_set.difference(resume_set)))

    if len(job_set) == 0:
        skill_score = 0
    else: skill_score = len(matched_skills) / len(job_set) * 100

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "skill_match_score": round(skill_score, 2)
    }