from typing import Dict, List, Any
from pydantic import BaseModel

class AnalyzeTextRequest(BaseModel):
    resume_text: str
    job_description: str

class ScoreBreakdown(BaseModel):
    semantic_similarity_score: float
    tfidf_similarity_score: float
    overall_skill_score: float
    core_skill_score: float
    ats_keyword_score: float
    soft_skill_score: float
    domain_relevance_score: float

class AnalyzeResponse(BaseModel):
    overall_score: float
    category: str
    dominant_domain: str
    domain_count: Dict[str, int]
    score_breakdown: ScoreBreakdown
    resume_skills: List[Dict[str, Any]]
    job_skills: List[Dict[str, Any]]
    matched_skills: List[str]
    missing_skills: List[str]
    matched_core_skills: List[str]
    missing_core_skills: List[str]
    recommendations: List[str]

class HealthResponse(BaseModel):
    status: str
    message: str
