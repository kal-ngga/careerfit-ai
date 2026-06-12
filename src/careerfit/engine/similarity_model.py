from functools import lru_cache

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer, util

@lru_cache(maxsize=1)
def get_sentence_model():
    """
    Load sentence transformer once.
    This prevents reloading model every time analysis runs.
    """
    return SentenceTransformer("all-MiniLM-L6-v2")

def calculate_tfidf_similarity(resume_text, job_text):
    """
    Baseline keyword-based similarity using TF-IDF.
    """
    documents = [resume_text, job_text]
    if not resume_text.strip() or not job_text.strip():
        return 0

    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(documents)
    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    similarity = float(similarity_matrix[0][0])

    return round(similarity * 100, 2)

def calculate_semantic_similarity(resume_text, job_text):
    """
    Semantic similarity using Sentence Transformer.
    """
    if not resume_text.strip() or not job_text.strip():
        return 0

    model = get_sentence_model()
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    job_embedding = model.encode(job_text, convert_to_tensor=True)

    similarity = util.cos_sim(resume_embedding, job_embedding).item()

    return round(similarity * 100, 2)