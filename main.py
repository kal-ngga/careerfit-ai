from careerfit.engine.matcher import analyze_resume_job_match

def print_result(result):
    print("\n===== AI Resume Job Match Result =====")
    print(f"Overall Score: {result['overall_score']}%")
    print(f"Category: {result['category']}")
    print(f"Detected Job Domain: {result['dominant_domain']}")

    print("\nScore Breakdown:")
    for score_name, score_value in result["score_breakdown"].items():
        label = score_name.replace("_", " ").title()
        print(f"- {label}: {score_value}%")

    print("\nMatched Skills:")
    for skill in result["matched_skills"]:
        print(f"- {skill}")

    print("\nMissing Skills:")
    for skill in result["missing_skills"]:
        print(f"- {skill}")

    print("\nMatched Core Skills:")
    for skill in result["matched_core_skills"]:
        print(f"- {skill}")

    print("\nMissing Core Skills:")
    for skill in result["missing_core_skills"]:
        print(f"- {skill}")

    print("\nRecommendations:")
    for recommendation in result["recommendations"]:
        print(f"- {recommendation}")


if __name__ == "__main__":
    match_result = analyze_resume_job_match(
        resume_path="data/CV_Kalingga.pdf",
        job_description_path="data/job_description.txt",
        skill_taxonomy_path="data/skill_taxonomy.csv"
    )

    print_result(match_result)
