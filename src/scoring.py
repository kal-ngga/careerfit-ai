from collections import Counter

def calculate_ats_keyword_score(resume_text, job_text):
    job_words = job_text.split()
    resume_words = resume_text.split()

    job_word_counts = Counter(job_words)
    important_words = []

    for word, count in job_word_counts.items():
        if len(word) > 3:
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

def calculate_final_score(semantic_score, skill_score, tfidf_score, ats_score):
    final_score = (
        semantic_score * 0.45 +
        skill_score * 0.30 +
        tfidf_score * 0.15 +
        ats_score * 0.10
    )

    return round(final_score, 2)

def get_match_category(final_score):
    if final_score >= 75:
        return "High Match"
    elif final_score >= 50:
        return "Medium Match"
    else:
        return "Low Match"