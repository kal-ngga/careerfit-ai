from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer, util

def calculate_tfidf_similarity(resume_text, job_text):
    documents = [resume_text, job_text]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    similarity = float(similarity_matrix[0][0])

    return round(similarity * 100, 2)

def calculate_semantic_similarity(resume_text, job_text):
    model = SentenceTransformer("all-MiniLM-L6-v2")

    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    job_embedding = model.encode(job_text, convert_to_tensor=True)

    similarity = util.cos_sim(resume_embedding, job_embedding).item()

    return round(similarity * 100, 2)