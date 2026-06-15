# CareerFit AI

CareerFit AI is an AI-powered resume and job description matching project. It compares a resume with a target job description, calculates a compatibility score, identifies matched and missing skills, detects the dominant job domain, and generates resume improvement recommendations.

The project currently includes two ways to use the matcher:

- A Python matching engine that can be run locally from sample files.
- A FastAPI backend with text-based and file-upload analysis endpoints.

## Disclaimer

CareerFit AI does not predict whether a candidate will be accepted or rejected by a company. The score is only an estimate based on text similarity, skill matching, keyword coverage, and domain relevance. Real hiring decisions can depend on interviews, portfolio quality, work experience, recruiter judgment, company needs, and many other factors.

## Features

- Extract resume text from TXT, PDF, and DOCX files.
- Analyze resume text directly through the API.
- Process job description text.
- Load a skill taxonomy from CSV.
- Detect skills using skill names and aliases.
- Compare matched, missing, core, and soft skills.
- Detect the dominant job domain from job skills.
- Calculate semantic similarity with Sentence Transformers.
- Calculate TF-IDF similarity as a keyword baseline.
- Calculate ATS-style keyword coverage.
- Generate score breakdown and resume recommendations.
- Serve the matcher through FastAPI.

## How It Works

CareerFit AI uses a hybrid NLP pipeline:

```text
Resume / CV
    |
    v
Text extraction or direct text input
    |
    v
Text cleaning and matching normalization
    |
    v
Skill extraction from taxonomy
    |
    v
Semantic similarity + TF-IDF similarity
    |
    v
Skill, core skill, soft skill, ATS keyword, and domain scoring
    |
    v
Final score, match category, missing skills, and recommendations
```

The current final score combines several signals:

```text
Final Score =
  35% Semantic Similarity
+ 25% Core Skill Match
+ 15% Overall Skill Match
+ 10% Domain Relevance
+ 10% ATS Keyword Score
+  5% Soft Skill Match
```

The score is categorized as:

- `High Match`: score >= 75
- `Medium Match`: score >= 50
- `Low Match`: score < 50

## Project Structure

```text
careerfit-ai/
├── data/
│   ├── resume.txt
│   ├── job_description.txt
│   └── skill_taxonomy.csv
├── examples/
│   └── run_engine.py
├── src/
│   └── careerfit/
│       ├── api/
│       │   ├── app.py
│       │   ├── routes.py
│       │   └── schemas.py
│       └── engine/
│           ├── matcher.py
│           ├── preprocessing.py
│           ├── recommender.py
│           ├── scoring.py
│           ├── similarity_model.py
│           ├── skill_extractor.py
│           └── text_extractor.py
├── main.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pandas
- NumPy
- Scikit-learn
- Sentence Transformers
- PDFPlumber
- python-docx
- TF-IDF
- Cosine similarity

## Installation

Clone the repository and enter the project directory:

```bash
git clone https://github.com/kal-ngga/careerfit-ai.git
cd careerfit-ai
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

For package-style imports from the `src/` layout, install the project in editable mode:

```bash
pip install -e .
```

## Run the Matching Engine

The default local runner reads these sample files:

- `data/resume.txt`
- `data/job_description.txt`
- `data/skill_taxonomy.csv`

Run:

```bash
python main.py
```

You can also run the example script:

```bash
python examples/run_engine.py
```

Example result fields:

```text
overall_score
category
dominant_domain
score_breakdown
resume_skills
job_skills
matched_skills
missing_skills
matched_core_skills
missing_core_skills
recommendations
```

## Run the API

Start the FastAPI server:

```bash
uvicorn careerfit.api.app:app --reload
```

If the package is not installed in editable mode, run with `PYTHONPATH`:

```bash
PYTHONPATH=src uvicorn careerfit.api.app:app --reload
```

Open the interactive API docs:

```text
http://127.0.0.1:8000/docs
```

Available endpoints:

```text
GET  /
GET  /health
POST /analyze-text
POST /analyze
```

### Analyze Text

Use `POST /analyze-text` when both resume and job description are already plain text.

Example request:

```bash
curl -X POST "http://127.0.0.1:8000/analyze-text" \
  -H "Content-Type: application/json" \
  -d '{
    "resume_text": "Python developer with SQL, data analysis, and dashboard experience.",
    "job_description": "We need a data analyst intern with Python, SQL, statistics, and dashboard skills."
  }'
```

### Analyze Uploaded Resume

Use `POST /analyze` when uploading a resume file. Supported resume formats are `.pdf`, `.docx`, and `.txt`.

Example request:

```bash
curl -X POST "http://127.0.0.1:8000/analyze" \
  -F "resume_file=@data/resume.txt" \
  -F "job_description=$(cat data/job_description.txt)"
```

## Skill Taxonomy

The matcher depends on `data/skill_taxonomy.csv`. The CSV must contain these columns:

```text
skill,category,domain,priority,aliases
```

Example:

```csv
skill,category,domain,priority,aliases
python,technical,data science,core,python programming;py
seo,technical,marketing,core,search engine optimization;organic search
communication,soft skill,general,supporting,presentation;public speaking
```

Aliases help the matcher connect different terms to the same skill. For example, `search engine optimization` can be matched as `seo`.

## API Response

The API returns a JSON object similar to the engine output:

```json
{
  "overall_score": 74.25,
  "category": "Medium Match",
  "dominant_domain": "data science",
  "domain_count": {
    "data science": 6
  },
  "score_breakdown": {
    "semantic_similarity_score": 80.0,
    "tfidf_similarity_score": 55.0,
    "overall_skill_score": 70.0,
    "core_skill_score": 75.0,
    "ats_keyword_score": 60.0,
    "soft_skill_score": 50.0,
    "domain_relevance_score": 80.0
  },
  "matched_skills": ["python", "sql"],
  "missing_skills": ["statistics"],
  "matched_core_skills": ["python"],
  "missing_core_skills": ["statistics"],
  "recommendations": []
}
```

Actual values depend on the resume, job description, taxonomy, and model output.

## Development Roadmap

- Improve skill taxonomy coverage across job domains.
- Improve extraction accuracy for multi-word skills and aliases.
- Add stronger ATS keyword scoring.
- Add resume section detection.
- Add tests for engine and API behavior.
- Add a frontend interface for uploading resumes and viewing analysis results.
- Add downloadable reports.

## Author

Kalingga Rafif

GitHub: [@kal-ngga](https://github.com/kal-ngga)
