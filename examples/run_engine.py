from careerfit.engine.matcher import analyze_resume_job_match

if __name__ == "__main__":
    result = analyze_resume_job_match(
        resume_path="data/resume.txt",
        job_description_path="data/job_description.txt",
        skill_taxonomy_path="data/skill_taxonomy.csv"
    )

    print(result)