from careerfit.engine.matcher import analyze_resume_job_match

def print_result(result):
    print("\n===== AI Resume Job Match Result =====")
    print(f"Overall Score: {result['overall_score']}%")
    print(f"Category: {result['category']}")
    print(f"Detected Job Domain: {result['dominant_domain']}")

    print("\nScore Breakdown:")
    breakdown = result["score_breakdown"]
    print(f"- Semantic Similarity: {breakdown['semantic_similarity_score']}%")
    print(f"- TF-IDF Similarity: {breakdown['tfidf_similarity_score']}%")
    print(f"- Overall Skill Score: {breakdown['overall_skill_score']}%")
    print(f"- Core Skill Score: {breakdown['core_skill_score']}%")
    print(f"- ATS Keyword Score: {breakdown['ats_keyword_score']}%")
    print(f"- Soft Skill Score: {breakdown['soft_skill_score']}%")
    print(f"- Domain Relevance Score: {breakdown['domain_relevance_score']}%")

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
    result = analyze_resume_job_match(
        resume_path="data/resume.txt",
        job_description_path="data/job_description.txt",
        skill_taxonomy_path="data/skill_taxonomy.csv"
    )

    print_result(result)