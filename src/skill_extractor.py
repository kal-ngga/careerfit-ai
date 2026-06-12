import re
import pandas as pd


def load_skill_taxonomy(file_path):
    """
    Load general skill taxonomy from CSV.

    Required columns:
    - skill
    - category
    - domain
    - priority
    - aliases
    """
    df = pd.read_csv(file_path)
    required_columns = {"skill", "category", "domain", "priority", "aliases"}
    missing_columns = required_columns.difference(df.columns)
    if missing_columns:
        raise ValueError(f"Missing columns in skill taxonomy: {missing_columns}")
    for column in required_columns:
        df[column] = df[column].fillna("").astype(str).str.lower().str.strip()

    return df


def build_search_terms(skill, aliases):
    """
    Combine main skill name and aliases.
    """
    terms = [skill]
    if aliases:
        alias_list = aliases.split(";")

        for alias in alias_list:
            alias = alias.strip()
            if alias:
                terms.append(alias)
    # Sort by length desc so longer phrases checked first
    terms = sorted(list(set(terms)), key=len, reverse=True)

    return terms

def phrase_exists(text, phrase):
    """
    Check phrase existence using safer regex boundary.
    Works for words and multi-word phrases.
    """
    phrase = re.escape(phrase)
    pattern = r"(?<![a-zA-Z0-9])" + phrase + r"(?![a-zA-Z0-9])"

    return re.search(pattern, text) is not None

def extract_skills(text, taxonomy_df):
    """
    Extract skills using skill name + aliases.
    Returns list of dictionaries:
    {
        skill,
        category,
        domain,
        priority,
        matched_term
    }
    """
    found_skills = []
    for _, row in taxonomy_df.iterrows():
        skill = row["skill"]
        category = row["category"]
        domain = row["domain"]
        priority = row["priority"]
        aliases = row["aliases"]

        terms = build_search_terms(skill, aliases)

        for term in terms:
            if phrase_exists(text, term):
                found_skills.append({
                    "skill": skill,
                    "category": category,
                    "domain": domain,
                    "priority": priority,
                    "matched_term": term
                })
                break

    # Remove duplicates by skill
    unique_skills = {}

    for item in found_skills:
        unique_skills[item["skill"]] = item

    return list(unique_skills.values())

def get_skill_names(skill_items):
    return sorted([item["skill"] for item in skill_items])

def compare_skills(resume_skills, job_skills):
    """
    Compare resume skills and job skills.
    """
    resume_skill_names = {item["skill"] for item in resume_skills}
    job_skill_names = {item["skill"] for item in job_skills}

    matched_skills = sorted(list(resume_skill_names.intersection(job_skill_names)))
    missing_skills = sorted(list(job_skill_names.difference(resume_skill_names)))

    if len(job_skill_names) == 0:
        skill_score = 0
    else:
        skill_score = len(matched_skills) / len(job_skill_names) * 100

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "skill_match_score": round(skill_score, 2)
    }

def compare_core_skills(resume_skills, job_skills):
    """
    Compare only core skills from job description.
    Core skills are more important than supporting/optional skills.
    """
    resume_skill_names = {item["skill"] for item in resume_skills}

    job_core_skills = {
        item["skill"]
        for item in job_skills
        if item["priority"] == "core"
    }

    if len(job_core_skills) == 0:
        return {
            "matched_core_skills": [],
            "missing_core_skills": [],
            "core_skill_score": 0
        }

    matched_core_skills = sorted(list(resume_skill_names.intersection(job_core_skills)))
    missing_core_skills = sorted(list(job_core_skills.difference(resume_skill_names)))

    core_skill_score = len(matched_core_skills) / len(job_core_skills) * 100

    return {
        "matched_core_skills": matched_core_skills,
        "missing_core_skills": missing_core_skills,
        "core_skill_score": round(core_skill_score, 2)
    }


def calculate_soft_skill_score(resume_skills, job_skills):
    """
    Calculate soft skill matching score.
    """
    resume_soft_skills = {
        item["skill"]
        for item in resume_skills
        if item["category"] == "soft skill"
    }

    job_soft_skills = {
        item["skill"]
        for item in job_skills
        if item["category"] == "soft skill"
    }

    if len(job_soft_skills) == 0:
        return 0

    matched_soft_skills = resume_soft_skills.intersection(job_soft_skills)
    score = len(matched_soft_skills) / len(job_soft_skills) * 100

    return round(score, 2)


def detect_job_domain(job_skills):
    """
    Detect dominant job domain based on extracted job skills.
    General domain is ignored unless no other domain exists.
    """
    domain_count = {}

    for item in job_skills:
        domain = item["domain"]

        if domain not in domain_count:
            domain_count[domain] = 0

        # Core skill gives stronger domain signal
        if item["priority"] == "core":
            domain_count[domain] += 2
        else:
            domain_count[domain] += 1

    if not domain_count:
        return "general", {}

    # Prefer non-general domain when possible
    non_general_domains = {
        domain: count
        for domain, count in domain_count.items()
        if domain != "general"
    }

    if non_general_domains:
        sorted_domains = sorted(
            non_general_domains.items(),
            key=lambda item: item[1],
            reverse=True
        )
    else:
        sorted_domains = sorted(
            domain_count.items(),
            key=lambda item: item[1],
            reverse=True
        )

    dominant_domain = sorted_domains[0][0]

    return dominant_domain, domain_count


def calculate_domain_relevance_score(resume_skills, dominant_domain):
    """
    Calculate whether resume has skills related to detected job domain.
    """
    if dominant_domain == "general":
        return 0

    resume_domain_skills = [
        item for item in resume_skills
        if item["domain"] == dominant_domain
    ]

    if len(resume_skills) == 0:
        return 0

    score = len(resume_domain_skills) / len(resume_skills) * 100

    return round(score, 2)