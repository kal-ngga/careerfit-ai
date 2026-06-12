from careerfit.engine.text_extractor import extract_text
from careerfit.engine.preprocessing import clean_text, normalize_for_matching
from careerfit.engine.skill_extractor import (
    load_skill_taxonomy,
    extract_skills,
    compare_skills,
    compare_core_skills,
    detect_job_domain,
    calculate_soft_skill_score,
    calculate_domain_relevance_score
)
from careerfit.engine.similarity_model import (
    calculate_tfidf_similarity,
    calculate_semantic_similarity
)
from careerfit.engine.scoring import (
    calculate_ats_keyword_score,
    calculate_final_score,
    get_match_category
)
from careerfit.engine.recommender import generate_recommendations


def analyze_resume_job_match(resume_path, job_description_path, skill_taxonomy_path):
    resume_text = extract_text(resume_path)
    job_text = extract_text(job_description_path)

    clean_resume = clean_text(resume_text)
    clean_job = clean_text(job_text)

    match_resume = normalize_for_matching(resume_text)
    match_job = normalize_for_matching(job_text)

    taxonomy_df = load_skill_taxonomy(skill_taxonomy_path)

    resume_skills = extract_skills(match_resume, taxonomy_df)
    job_skills = extract_skills(match_job, taxonomy_df)

    skill_result = compare_skills(resume_skills, job_skills)
    matched_skills = skill_result["matched_skills"]
    missing_skills = skill_result["missing_skills"]
    overall_skill_score = skill_result["skill_match_score"]

    core_skill_result = compare_core_skills(resume_skills, job_skills)
    matched_core_skills = core_skill_result["matched_core_skills"]
    missing_core_skills = core_skill_result["missing_core_skills"]
    core_skill_score = core_skill_result["core_skill_score"]

    dominant_domain, domain_count = detect_job_domain(job_skills)

    soft_skill_score = calculate_soft_skill_score(resume_skills, job_skills)

    domain_relevance_score = calculate_domain_relevance_score(
        resume_skills=resume_skills,
        dominant_domain=dominant_domain
    )

    tfidf_score = calculate_tfidf_similarity(clean_resume, clean_job)
    semantic_score = calculate_semantic_similarity(clean_resume, clean_job)

    ats_score = calculate_ats_keyword_score(clean_resume, clean_job)

    final_score = calculate_final_score(
        semantic_score=semantic_score,
        overall_skill_score=overall_skill_score,
        core_skill_score=core_skill_score,
        tfidf_score=tfidf_score,
        ats_score=ats_score,
        soft_skill_score=soft_skill_score,
        domain_relevance_score=domain_relevance_score
    )

    category = get_match_category(final_score)

    recommendations = generate_recommendations(
        final_score=final_score,
        missing_skills=missing_skills,
        missing_core_skills=missing_core_skills,
        dominant_domain=dominant_domain
    )

    return {
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
