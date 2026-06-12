from src.text_extractor import extract_text
from src.preprocessing import clean_text, normalize_for_matching
from src.skill_extractor import (
    load_skill_taxonomy,
    extract_skills,
    compare_skills,
    compare_core_skills,
    detect_job_domain,
    calculate_soft_skill_score,
    calculate_domain_relevance_score
)
from src.similarity_model import calculate_tfidf_similarity, calculate_semantic_similarity
from src.scoring import calculate_ats_keyword_score, calculate_final_score, get_match_category
from src.recommender import generate_recommendations


def analyze_resume_job_match(resume_path, job_description_path, skill_taxonomy_path):
    # 1. Extract text
    resume_text = extract_text(resume_path)
    job_text = extract_text(job_description_path)

    # 2. Clean text for models
    clean_resume = clean_text(resume_text)
    clean_job = clean_text(job_text)

    # 3. Normalize text for skill matching
    match_resume = normalize_for_matching(resume_text)
    match_job = normalize_for_matching(job_text)

    # 4. Load general skill taxonomy
    taxonomy_df = load_skill_taxonomy(skill_taxonomy_path)

    # 5. Extract skills
    resume_skills = extract_skills(match_resume, taxonomy_df)
    job_skills = extract_skills(match_job, taxonomy_df)

    # 6. Compare all skills
    skill_result = compare_skills(resume_skills, job_skills)

    matched_skills = skill_result["matched_skills"]
    missing_skills = skill_result["missing_skills"]
    overall_skill_score = skill_result["skill_match_score"]

    # 7. Compare core skills
    core_skill_result = compare_core_skills(resume_skills, job_skills)

    matched_core_skills = core_skill_result["matched_core_skills"]
    missing_core_skills = core_skill_result["missing_core_skills"]
    core_skill_score = core_skill_result["core_skill_score"]

    # 8. Detect job domain
    dominant_domain, domain_count = detect_job_domain(job_skills)

    # 9. Additional scores
    soft_skill_score = calculate_soft_skill_score(resume_skills, job_skills)
    domain_relevance_score = calculate_domain_relevance_score(
        resume_skills=resume_skills,
        dominant_domain=dominant_domain
    )

    # 10. Text similarity scores
    tfidf_score = calculate_tfidf_similarity(clean_resume, clean_job)
    semantic_score = calculate_semantic_similarity(clean_resume, clean_job)

    # 11. ATS keyword score
    ats_score = calculate_ats_keyword_score(clean_resume, clean_job)

    # 12. Final score
    final_score = calculate_final_score(
        semantic_score=semantic_score,
        overall_skill_score=overall_skill_score,
        core_skill_score=core_skill_score,
        tfidf_score=tfidf_score,
        ats_score=ats_score,
        soft_skill_score=soft_skill_score,
        domain_relevance_score=domain_relevance_score
    )

    # 13. Category
    category = get_match_category(final_score)

    # 14. Recommendations
    recommendations = generate_recommendations(
        final_score=final_score,
        missing_skills=missing_skills,
        missing_core_skills=missing_core_skills,
        dominant_domain=dominant_domain
    )

    result = {
        "overall_score": final_score,
        "category": category,
        "dominant_domain": dominant_domain,
        "domain_count": domain_count,

        "score_breakdown": {
            "semantic_similarity_score": semantic_score,
            "tfidf_similarity_score": tfidf_score,
            "overall_skill_score": overall_skill_score,
            "core_skill_score": core_skill_score,
            "ats_keyword_score": ats_score,
            "soft_skill_score": soft_skill_score,
            "domain_relevance_score": domain_relevance_score
        },

        "resume_skills": resume_skills,
        "job_skills": job_skills,

        "matched_skills": matched_skills,
        "missing_skills": missing_skills,

        "matched_core_skills": matched_core_skills,
        "missing_core_skills": missing_core_skills,

        "recommendations": recommendations
    }

    return result


def print_result(result):
    print("\n===== AI Resume Job Match Result =====")
    print(f"Overall Score: {result['overall_score']}%")
    print(f"Category: {result['category']}")
    print(f"Detected Job Domain: {result['dominant_domain']}")

    print("\nDomain Count:")
    for domain, count in result["domain_count"].items():
        print(f"- {domain}: {count}")

    print("\nScore Breakdown:")
    breakdown = result["score_breakdown"]
    print(f"- Semantic Similarity: {breakdown['semantic_similarity_score']}%")
    print(f"- TF-IDF Similarity: {breakdown['tfidf_similarity_score']}%")
    print(f"- Overall Skill Score: {breakdown['overall_skill_score']}%")
    print(f"- Core Skill Score: {breakdown['core_skill_score']}%")
    print(f"- ATS Keyword Score: {breakdown['ats_keyword_score']}%")
    print(f"- Soft Skill Score: {breakdown['soft_skill_score']}%")
    print(f"- Domain Relevance Score: {breakdown['domain_relevance_score']}%")

    print("\nResume Skills Detected:")
    for item in result["resume_skills"]:
        print(
            f"- {item['skill']} "
            f"({item['domain']} / {item['category']} / {item['priority']}) "
            f"[matched: {item['matched_term']}]"
        )

    print("\nJob Skills Detected:")
    for item in result["job_skills"]:
        print(
            f"- {item['skill']} "
            f"({item['domain']} / {item['category']} / {item['priority']}) "
            f"[matched: {item['matched_term']}]"
        )

    print("\nMatched Core Skills:")
    for skill in result["matched_core_skills"]:
        print(f"- {skill}")

    print("\nMissing Core Skills:")
    for skill in result["missing_core_skills"]:
        print(f"- {skill}")

    print("\nMatched Skills:")
    for skill in result["matched_skills"]:
        print(f"- {skill}")

    print("\nMissing Skills:")
    for skill in result["missing_skills"]:
        print(f"- {skill}")

    print("\nRecommendations:")
    for recommendation in result["recommendations"]:
        print(f"- {recommendation}")


if __name__ == "__main__":
    resume_path = "data/resume.txt"
    job_description_path = "data/job_description.txt"
    skill_taxonomy_path = "data/skill_taxonomy.csv"

    result = analyze_resume_job_match(
        resume_path=resume_path,
        job_description_path=job_description_path,
        skill_taxonomy_path=skill_taxonomy_path
    )

    print_result(result)