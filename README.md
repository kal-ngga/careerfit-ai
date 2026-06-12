# CareerFit AI

CareerFit AI is an AI-powered resume and job description matching engine that analyzes how well a CV matches a specific job opportunity.

This project uses Natural Language Processing, semantic similarity, and skill matching to calculate a CV-job compatibility score. The goal is to help job seekers understand their resume relevance before applying to internships or jobs.

## Project Description

CareerFit AI compares two main inputs:

- Resume / CV
- Job description

Then the system generates:

- Overall match score
- Match category
- Matched skills
- Missing skills
- Score breakdown
- Resume improvement recommendations

This project is currently focused on building the AI/ML matching engine. The API and web interface will be developed in the next stage.

## Important Disclaimer

This system does not guarantee whether a candidate will be accepted or rejected by a company.

The score only represents the compatibility between a resume and a job description based on text similarity, skill matching, and keyword analysis. Real hiring decisions may depend on interviews, portfolio quality, work experience, recruiter judgment, and company requirements.

## Features

- Extract text from resume files
- Process job description text
- Extract skills from resume and job description
- Support general skill taxonomy with aliases
- Calculate semantic similarity using Sentence Transformer
- Calculate baseline similarity using TF-IDF
- Detect matched and missing skills
- Generate CV improvement recommendations
- Modular Python project structure

## How It Works

The system follows this pipeline:

text Resume / CV     ↓ Text Extraction     ↓ Text Cleaning     ↓ Skill Extraction     ↓ Semantic Similarity     ↓ Skill Matching     ↓ Final Score     ↓ Recommendations 

The matching score is calculated using a combination of semantic similarity and skill matching.

Simple scoring formula:

text Final Score = 60% Semantic Similarity + 40% Skill Match 

The formula can be improved later by adding ATS keyword score, core skill matching, soft skill matching, and domain relevance.

## Model Approach

CareerFit AI uses a hybrid NLP approach.

### Semantic Similarity

The system uses Sentence Transformer to compare the meaning of the resume and job description. This helps the model understand context, not only exact words.

### Skill Matching

The system uses a skill taxonomy to detect skills from both resume and job description.

Example:

csv skill,category,domain,priority,aliases seo,technical,marketing,core,"search engine optimization;organic search" content writing,technical,marketing,core,"copywriting;article writing" python,technical,data science,core,"python programming;py" 

With aliases, the system can understand that:

text copywriting → content writing search engine optimization → seo dashboard → data visualization customer care → customer service 

### TF-IDF Baseline

TF-IDF is used as a baseline method to compare keyword similarity between the resume and job description.

## Project Structure

- data/  
  Contains sample resumes, sample job descriptions, and skill taxonomy.

- src/  
  Contains the main AI/ML logic, including text extraction, preprocessing, skill extraction, similarity model, scoring, and recommendation.

- main.py  
  Main file to run the resume-job matching engine.

- requirements.txt  
  List of Python libraries required for this project.

- README.md  
  Project documentation.

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Sentence Transformers
- PDFPlumber
- python-docx
- TF-IDF
- Cosine Similarity
- NLP Text Processing

## Installation

Clone this repository:

bash git clone https://github.com/kal-ngga/careerfit-ai.git cd careerfit-ai 

Create and activate a virtual environment:

bash python -m venv .venv source .venv/bin/activate 

Install dependencies:

bash pip install -r requirements.txt 

## Usage

Prepare your files:

text data/sample_resumes/resume.txt data/sample_jobs/job_description.txt data/skill_taxonomy.csv 

Run the program:

bash python main.py 

Example output:

text ===== AI Resume Job Match Result ===== Overall Score: 74.25% Category: Medium Match  Matched Skills: - python - sql - machine learning - pandas  Missing Skills: - statistics - power bi - data visualization  Recommendations: - Your CV is quite relevant, but it can still be improved. - Add missing skills explicitly if you already have experience with them. - Add measurable project impact such as model accuracy, dataset size, dashboard output, or deployment link. 

## Development Roadmap

This project is planned in three main stages:

### Stage 1 — AI/ML Matching Engine

Build the core resume-job matching model using NLP, semantic similarity, skill extraction, scoring, and recommendation logic.

Current repository status: Stage 1 in progress.

### Stage 2 — Backend API

Extend the matching engine into an API service using FastAPI so it can receive resume and job description inputs and return analysis results as JSON.

### Stage 3 — Web Interface

Build a web interface where users can upload their CV, paste a job description, and view the match score, missing skills, and recommendations.

The web interface may be developed as a separate frontend project or as an extension of this repository.

## Future Improvements

- Add larger general skill taxonomy
- Improve skill extraction accuracy
- Add ATS keyword scoring
- Add resume section detection
- Add job domain detection
- Add FastAPI backend
- Add React or Next.js web interface
- Add analysis history
- Add downloadable report

## Learning Goals

This project is designed to improve practical skills in:

- Natural Language Processing
- Machine Learning
- Text preprocessing
- Semantic similarity
- Feature extraction
- Python project structure
- AI product development
- API and web integration

## Author

Kalingga Rafif  
Aspiring Data Scientist and Information Systems student.

GitHub: @kal-ngga
