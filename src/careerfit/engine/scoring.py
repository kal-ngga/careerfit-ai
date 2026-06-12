from collections import Counter
BASIC_STOPWORDS = {
    "the", "and", "for", "with", "you", "your", "are", "our", "will", "this",
    "that", "have", "has", "from", "into", "who", "can", "able", "work",
    "team", "role", "job", "position", "candidate", "experience", "skills",
    "skill", "required", "requirements", "responsibilities", "responsibility",
    "looking", "knowledge", "basic", "good", "plus", "using", "use", "ability",
    "strong", "excellent", "understanding", "company", "intern", "internship"
}

def calculate_ats_keyword_score(resume_text, job_text):
    """
    Simple ATS-style keyword score.
    It checks how many important words from job description appear in resume.
    """
    if not resume_text.strip() or not job_text.strip():
        return 0

    job_words = job_text.split()
    resume_words = set(resume_text.split())
    job_word_counts = Counter(job_words)

    important_words = []
    for word, count in job_word_counts.items():
        if len(word) > 3 and word not in BASIC_STOPWORDS:
            important_words.append(word)

    important_words = list(set(important_words))

    if len(important_words) == 0:
        return 0

    matched_keywords = []

    for word in important_words:
        if word in resume_words:
            matched_keywords.append(word)

    ats_score = len(matched_keywords) / len(important_words) * 100

    return round(ats_score, 2)


def calculate_final_score(
    semantic_score,
    overall_skill_score,
    core_skill_score,
    tfidf_score,
    ats_score,
    soft_skill_score,
    domain_relevance_score
):
    """
    General scoring formula for many job domains.

    35% semantic similarity
    25% core skill match
    15% overall skill match
    10% domain relevance
    10% ATS keyword score
    5% soft skill match
    """
    final_score = (
        semantic_score * 0.35 +
        core_skill_score * 0.25 +
        overall_skill_score * 0.15 +
        domain_relevance_score * 0.10 +
        ats_score * 0.10 +
        soft_skill_score * 0.05
    )

    return round(final_score, 2)


def get_match_category(final_score):
    if final_score >= 75:
        return "High Match"
    elif final_score >= 50:
        return "Medium Match"
    else:
        return "Low Match"