# CareerFit AI

CareerFit AI is a Python-based resume and job description matcher. It analyzes how well a CV fits a target role by combining semantic similarity, TF-IDF similarity, skill matching, ATS keyword coverage, and recommendation generation.

## Features

- Extracts text from `.txt`, `.pdf`, and `.docx` files.
- Cleans and normalizes resume and job description text.
- Detects skills using a CSV-based skill taxonomy.
- Compares resume skills against job description requirements.
- Calculates semantic similarity using `sentence-transformers`.
- Calculates TF-IDF similarity using `scikit-learn`.
- Calculates ATS-style keyword coverage.
- Produces an overall match score, match category, missing skills, and improvement recommendations.

## Project Structure

```text
careerfit-ai/
├── data/
│   ├── job_description.txt
│   ├── resume.txt
│   └── skill_taxonomy.csv
├── src/
│   ├── preprocessing.py
│   ├── recommender.py
│   ├── scoring.py
│   ├── similarity_model.py
│   ├── skill_extractor.py
│   └── text_extractor.py
├── main.py
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10 or newer
- pip

## Installation

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

By default, the app reads these files:

- `data/resume.txt`
- `data/job_description.txt`
- `data/skill_taxonomy.csv`

Run the analyzer:

```bash
python main.py
```

Example output includes:

- Overall score
- Match category
- Semantic similarity score
- TF-IDF similarity score
- Skill match score
- ATS keyword score
- Matched skills
- Missing skills
- Recommendations

## Custom Data

To analyze another CV or job description, replace the default files in `data/` or update these paths in `main.py`:

```python
resume_path = "data/resume.txt"
job_description_path = "data/job_description.txt"
skill_taxonomy_path = "data/skill_taxonomy.csv"
```

Supported resume/job description formats are `.txt`, `.pdf`, and `.docx`.

## Scoring Formula

The final score is calculated with this weighting:

```text
final_score = semantic_similarity * 45%
            + skill_match * 30%
            + tfidf_similarity * 15%
            + ats_keyword_score * 10%
```

Match categories:

- `High Match`: score >= 75
- `Medium Match`: score >= 50
- `Low Match`: score < 50

## Notes

The semantic similarity model uses `all-MiniLM-L6-v2`. On the first run, `sentence-transformers` may download the model if it is not already cached locally.
