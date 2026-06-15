import os
import tempfile

from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from careerfit.api.schemas import AnalyzeTextRequest
from careerfit.engine.matcher import analyze_resume_job_match


router = APIRouter()

SKILL_TAXONOMY_PATH = "data/skill_taxonomy.csv"


@router.get("/")
def root():
    return {
        "message": "CareerFit AI API is running",
        "stage": "Stage 2 - Backend API"
    }


@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "CareerFit AI API is healthy"
    }


@router.post("/analyze-text")
def analyze_text(request: AnalyzeTextRequest):
    if not request.resume_text.strip():
        raise HTTPException(
            status_code=400,
            detail="Resume text cannot be empty."
        )

    if not request.job_description.strip():
        raise HTTPException(
            status_code=400,
            detail="Job description cannot be empty."
        )

    try:
        result = analyze_resume_job_match(
            resume_text=request.resume_text,
            job_description_text=request.job_description,
            skill_taxonomy_path=SKILL_TAXONOMY_PATH
        )

        return result

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Text analysis failed: {str(error)}"
        )


@router.post("/analyze")
async def analyze_resume(
    resume_file: UploadFile = File(...),
    job_description: str = Form(...)
):
    allowed_extensions = [".pdf", ".docx", ".txt"]

    file_name = resume_file.filename or ""
    file_extension = os.path.splitext(file_name.lower())[1]

    if file_extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file format. Please upload PDF, DOCX, or TXT file."
        )

    if not job_description.strip():
        raise HTTPException(
            status_code=400,
            detail="Job description cannot be empty."
        )

    temp_resume_path = None

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as temp_file:
            file_content = await resume_file.read()
            temp_file.write(file_content)
            temp_resume_path = temp_file.name

        result = analyze_resume_job_match(
            resume_path=temp_resume_path,
            job_description_text=job_description,
            skill_taxonomy_path=SKILL_TAXONOMY_PATH
        )

        return result

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Analysis failed: {str(error)}"
        )

    finally:
        if temp_resume_path and os.path.exists(temp_resume_path):
            os.remove(temp_resume_path)
