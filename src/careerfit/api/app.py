from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from careerfit.api.routes import router

app = FastAPI(
    title="CareerFit AI API",
    description="API for resume and job description matching using NLP and semantic similarity.",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)