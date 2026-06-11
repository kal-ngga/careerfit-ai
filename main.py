from src.text_extractor import extract_text
from src.preprocessing import clean_text
from src.skill_extractor import load_skill_taxonomy, extract_skills, compare_skills
from src.similarity_model import calculate_tfidf_similarity, calculate_semantic_similarity
from src.scoring import calculate_ats_keyword_score, calculate_final_score, get_match_category
from src.recommender import generate_recommendations


def analyze_resume_job_match(resume_path, job_description_path, skill_taxonomy_path):
    # 1. Extract text
    resume_text = extract_text(resume_path)
    job_text = extract_text(job_description_path)

    # 2. Clean text
    clean_resume = clean_text(resume_text)
    clean_job = clean_text(job_text)

    # 3. Load skill taxonomy
    skills = load_skill_taxonomy(skill_taxonomy_path)

    # 4. Extract skills
    resume_skills = extract_skills(clean_resume, skills)
    job_skills = extract_skills(clean_job, skills)

    # 5. Compare skills
    skill_result = compare_skills(resume_skills, job_skills)

    matched_skills = skill_result["matched_skills"]
    missing_skills = skill_result["missing_skills"]
    skill_score = skill_result["skill_match_score"]

    # 6. Calculate similarities
    tfidf_score = calculate_tfidf_similarity(clean_resume, clean_job)
    semantic_score = calculate_semantic_similarity(clean_resume, clean_job)

    # 7. Calculate ATS keyword score
    ats_score = calculate_ats_keyword_score(clean_resume, clean_job)

    # 8. Calculate final score
    final_score = calculate_final_score(
        semantic_score=semantic_score,
        skill_score=skill_score,
        tfidf_score=tfidf_score,
        ats_score=ats_score
    )

    # 9. Get category
    category = get_match_category(final_score)

    # 10. Generate recommendations
    recommendations = generate_recommendations(final_score, missing_skills)

    result = {
        "overall_score": final_score,
        "category": category,
        "semantic_similarity_score": semantic_score,
        "tfidf_similarity_score": tfidf_score,
        "skill_match_score": skill_score,
        "ats_keyword_score": ats_score,
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "recommendations": recommendations
    }

    return result


if __name__ == "__main__":
    resume_path = "data/resume.txt"
    job_description_path = "data/job_description.txt"
    skill_taxonomy_path = "data/skill_taxonomy.csv"

    result = analyze_resume_job_match(
        resume_path,
        job_description_path,
        skill_taxonomy_path
    )

    print("\n===== AI Resume Job Match Result =====")
    print(f"Overall Score: {result['overall_score']}%")
    print(f"Category: {result['category']}")

    print("\nScore Breakdown:")
    print(f"- Semantic Similarity: {result['semantic_similarity_score']}%")
    print(f"- TF-IDF Similarity: {result['tfidf_similarity_score']}%")
    print(f"- Skill Match Score: {result['skill_match_score']}%")
    print(f"- ATS Keyword Score: {result['ats_keyword_score']}%")

    print("\nMatched Skills:")
    for skill in result["matched_skills"]:
        print(f"- {skill}")

    print("\nMissing Skills:")
    for skill in result["missing_skills"]:
        print(f"- {skill}")

    print("\nRecommendations:")
    for recommendation in result["recommendations"]:
        print(f"- {recommendation}")