# CareerFit AI

CareerFit AI is the backend and AI engine for the CareerFit project. This repository handles resume text extraction, resume-job matching analysis, skill extraction, scoring logic, and API processing.

This project is connected with the frontend repository:

```text
https://github.com/kal-ngga/careerfit-web
```

The frontend provides the user interface, while this repository provides the AI engine and FastAPI backend.

## Overview

CareerFit AI helps analyze how well a resume matches a job description. It processes resume files, extracts text and skills, compares them with job requirements, and returns a structured compatibility analysis.

The system can generate:

- Overall resume-job match score
- Match category
- Detected job domain
- Score breakdown
- Matched skills
- Missing skills
- Missing core skills
- Improvement recommendations

## Related Repository

Frontend repository:

```text
https://github.com/kal-ngga/careerfit-web
```

Use `careerfit-web` if you want to run the web interface.

Use this repository, `careerfit-ai`, if you want to run the AI engine and backend API.

## Tech Stack

This backend is built with:

- Python
- FastAPI
- Uvicorn
- Pandas
- NumPy
- Scikit-learn
- Sentence Transformers
- PDFPlumber
- PyMuPDF
- Pytesseract
- Python DOCX

## Main Features

- Resume text extraction
- PDF, DOCX, and TXT file support
- OCR fallback for image-based PDF resumes
- Job description processing
- Skill extraction using taxonomy
- Skill alias matching
- Resume-job semantic similarity
- TF-IDF similarity
- ATS keyword score
- Domain detection
- Final match score calculation
- Recommendation generation
- FastAPI endpoint for frontend integration

## Project Structure

```text
careerfit-ai/
├── data/
│   ├── resume.txt
│   ├── job_description.txt
│   └── skill_taxonomy.csv
│
├── examples/
│   └── run_engine.py
│
├── src/
│   └── careerfit/
│       ├── engine/
│       │   ├── text_extractor.py
│       │   ├── preprocessing.py
│       │   ├── skill_extractor.py
│       │   ├── similarity_model.py
│       │   ├── scoring.py
│       │   ├── recommender.py
│       │   └── matcher.py
│       │
│       └── api/
│           ├── app.py
│           ├── routes.py
│           └── schemas.py
│
├── main.py
├── requirements.txt
├── pyproject.toml
└── README.md
```

## How It Works

```text
Resume File / Resume Text
        ↓
Text Extraction
        ↓
Text Cleaning
        ↓
Skill Extraction
        ↓
Semantic Similarity
        ↓
Skill Matching
        ↓
Score Calculation
        ↓
Recommendation Generation
        ↓
API Response
```

## Matching Logic

CareerFit AI combines several scoring components:

- Semantic similarity score
- TF-IDF similarity score
- Overall skill match score
- Core skill match score
- ATS keyword score
- Soft skill match score
- Domain relevance score

The final score is calculated using a weighted scoring approach. The result is categorized into match levels such as Low Match, Medium Match, or High Match.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/kal-ngga/careerfit-ai.git
cd careerfit-ai
```

### 2. Create Virtual Environment

For macOS, use `python3`:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
```

### 4. Install Tesseract for OCR

This project supports OCR fallback for image-based PDF resumes. On macOS, install Tesseract using Homebrew:

```bash
brew install tesseract
```

Check installation:

```bash
tesseract --version
```

## Running the AI Engine Only

To test the matching engine without running the API:

```bash
PYTHONPATH=src python examples/run_engine.py
```

This will analyze the sample files from the `data/` folder:

```text
data/resume.txt
data/job_description.txt
data/skill_taxonomy.csv
```

If the package has been installed correctly with `pip install -e .`, you can also run:

```bash
python examples/run_engine.py
```

## Running the API Server

Run the FastAPI backend:

```bash
PYTHONPATH=src python -m uvicorn careerfit.api.app:app --reload
```

The API will run on:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### Health Check

```text
GET /health
```

Used to check whether the backend is running.

### Analyze Resume File

```text
POST /analyze
```

Request type:

```text
multipart/form-data
```

Form fields:

| Field | Type | Required | Description |
|---|---|---|---|
| resume_file | File | Yes | Resume file uploaded by user |
| job_description | Text | Yes | Job description text |

Supported file formats:

- PDF
- DOCX
- TXT

### Analyze Text Only

```text
POST /analyze-text
```

Request body:

```json
{
  "resume_text": "string",
  "job_description": "string"
}
```

This endpoint is useful for testing without file upload.

## Example API Response

```json
{
  "overall_score": 64.77,
  "category": "Medium Match",
  "dominant_domain": "marketing",
  "domain_count": {
    "marketing": 12,
    "general": 6
  },
  "score_breakdown": {
    "semantic_similarity_score": 50.33,
    "tfidf_similarity_score": 31.21,
    "overall_skill_score": 70.0,
    "core_skill_score": 87.5,
    "ats_keyword_score": 53.33,
    "soft_skill_score": 100.0,
    "domain_relevance_score": 44.44
  },
  "matched_skills": [
    "campaign management",
    "communication",
    "content writing",
    "market research",
    "social media marketing"
  ],
  "missing_skills": [
    "google ads",
    "meta ads",
    "seo"
  ],
  "missing_core_skills": [
    "seo"
  ],
  "recommendations": [
    "CV kamu cukup relevan, tetapi masih bisa ditingkatkan.",
    "Core requirement yang belum terlihat di CV kamu: seo.",
    "Requirement tambahan yang belum terlihat: google ads, meta ads."
  ]
}
```

## Running with the Frontend

This backend is designed to be used with the CareerFit Web frontend.

### 1. Run Backend

```bash
cd careerfit-ai
source .venv/bin/activate
PYTHONPATH=src python -m uvicorn careerfit.api.app:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

### 2. Clone and Run Frontend

Open a new terminal:

```bash
git clone https://github.com/kal-ngga/careerfit-web.git
cd careerfit-web
npm install
cp .env.example .env
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

Make sure the frontend `.env` file contains:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

## Environment Notes

If Python cannot find the `careerfit` package, run commands with:

```bash
PYTHONPATH=src
```

Example:

```bash
PYTHONPATH=src python -m uvicorn careerfit.api.app:app --reload
```

If you want to avoid using `PYTHONPATH=src`, install the project as an editable package:

```bash
python -m pip install -e .
```

## Development Notes

This repository focuses on:

- AI engine development
- Resume parsing
- Skill matching
- Scoring logic
- Recommendation logic
- FastAPI backend

The frontend UI is handled in:

```text
https://github.com/kal-ngga/careerfit-web
```

## Roadmap

Planned improvements:

- Improve skill taxonomy coverage
- Add better OCR preprocessing
- Add resume section detection
- Improve ATS keyword scoring
- Add downloadable report generation
- Add job URL extraction
- Add resume improvement suggestions
- Add model evaluation scripts
- Prepare backend deployment

## Disclaimer

CareerFit AI provides a resume-job compatibility analysis based on text extraction, skill matching, and NLP similarity. The result is intended to help users improve their resume and is not a guarantee of job acceptance or rejection.
