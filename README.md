# CareerFit AI

CareerFit AI is an AI-powered resume and job description matching system that analyzes how well a candidate's CV matches a specific job opportunity. The system uses Natural Language Processing (NLP), semantic similarity, and skill extraction to calculate a compatibility score between a resume and a job description.

This project was built as a personal portfolio project to explore the combination of Data Science, Machine Learning, NLP, and Web/API development.

## Project Overview

The main goal of this project is to help job seekers understand how relevant their resume is to a specific internship or job vacancy.

Users can provide:

- A resume or CV
- A job description

The system will analyze both texts and generate:

- Overall match score
- Match category
- Matched skills
- Missing skills
- Score breakdown
- Resume improvement recommendations

## Important Disclaimer

This system does not guarantee whether a candidate will be accepted or rejected by a company.

The generated score represents the compatibility between the resume and the job description based on text similarity, skill matching, and keyword analysis. Hiring decisions may depend on many other factors such as interview performance, portfolio quality, work experience, company requirements, and recruiter judgment.

## Features

- Resume text extraction from TXT, PDF, or DOCX files
- Job description text processing
- General skill extraction using a customizable skill taxonomy
- Alias-based skill matching
- Semantic similarity using Sentence Transformer
- Baseline text similarity using TF-IDF
- CV-job compatibility scoring
- Matched skills and missing skills detection
- Recommendation generation for resume improvement
- Modular Python code structure
- Ready to be integrated with API and web interface in future development

## How It Works

The system follows a simple AI/NLP pipeline:

text Resume / CV     ↓ Text Extraction     ↓ Text Cleaning     ↓ Skill Extraction     ↓ Semantic Similarity Calculation     ↓ Skill Match Calculation     ↓ Final Score Calculation     ↓ Recommendation Generation 

The model compares the resume and job description using two main approaches:

1. Semantic Similarity  
   Measures how similar the meaning of the resume is to the job description using Sentence Transformer embeddings.

2. Skill Matching  
   Detects skills from both the resume and job description using a general skill taxonomy and alias mapping.

The final score is calculated using a weighted scoring system.

Example formula for the simple MVP version:

text Final Score = 60% Semantic Similarity + 40% Skill Match 

For a more advanced version, additional components such as ATS keyword score, core skill match, soft skill match, and domain relevance can be added.

## Model Approach

This project uses a hybrid NLP-based approach.

### 1. Skill-Based Matching

The system uses a skill taxonomy file to detect relevant skills from resumes and job descriptions.

Example:

csv skill,category,domain,priority,aliases seo,technical,marketing,core,"search engine optimization;organic search" content writing,technical,marketing,core,"copywriting;article writing;blog writing" customer service,soft skill,customer support,core,"customer support;client support;customer care" python,technical,data science,core,"python programming;py" 

This allows the system to understand that different terms may refer to the same skill.

For example:

text "copywriting" → content writing "search engine optimization" → SEO "customer care" → customer service "dashboard" → data visualization 

### 2. Semantic Similarity

The system uses Sentence Transformer to convert resume text and job description text into semantic embeddings. These embeddings are then compared using cosine similarity.

This helps the system understand meaning, not only exact keyword matches.

### 3. TF-IDF Baseline

TF-IDF is used as a baseline text similarity method. It helps compare keyword-level similarity between the resume and the job description.

### 4. Recommendation Engine

The recommendation engine generates feedback based on:

- Final match score
- Missing skills
- Missing core requirements
- Detected job domain
- Resume improvement opportunities

## Project Structure

careerfit-ai/
│
├── data/
│   ├── sample_resumes/
│   ├── sample_jobs/
│   └── skill_taxonomy.csv
│
├── src/
│   ├── text_extractor.py
│   ├── preprocessing.py
│   ├── skill_extractor.py
│   ├── similarity_model.py
│   ├── scoring.py
│   └── recommender.py
│
├── main.py
├── requirements.txt
└── README.md

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

text ===== AI Resume Job Match Result ===== Overall Score: 74.25% Category: Medium Match Detected Job Domain: data science  Score Breakdown: - Semantic Similarity: 78.00% - Skill Match Score: 68.00% - TF-IDF Similarity: 61.00% - ATS Keyword Score: 70.00%  Matched Skills: - python - sql - machine learning - pandas - streamlit  Missing Skills: - statistics - power bi - data visualization  Recommendations: - CV is quite relevant, but it can be improved by adding more keywords and relevant achievements. - Add missing skills explicitly if you already have experience with them. - Add measurable project impact such as model accuracy, dataset size, dashboard output, business result, or deployment link. 

## Current Development Stage

This project is currently in Phase 1: AI/ML Model Development.

The current focus is to build the resume-job matching engine before integrating it into a web application.

### Phase 1: AI/ML Engine

- Text extraction
- Text preprocessing
- Skill extraction
- Semantic similarity
- Skill matching
- Final scoring
- Recommendation generation

### Phase 2: API Development

Planned backend API using FastAPI:

- Upload resume
- Submit job description
- Return match score and recommendations as JSON
- Store analysis history

### Phase 3: Web Interface

Planned frontend using React or Next.js:

- Resume upload page
- Job description input form
- Match score dashboard
- Skill gap analysis
- Recommendation section

## Future Improvements

- Add larger and more complete skill taxonomy
- Add support for multiple job domains
- Improve skill extraction with Named Entity Recognition
- Add job link scraping feature
- Add ATS-style keyword analysis
- Add resume section detection
- Add PDF layout-aware parsing
- Add FastAPI backend
- Add React/Next.js frontend
- Add database for analysis history
- Add user authentication
- Add downloadable analysis report

## Learning Goals

This project is designed to strengthen practical skills in:

- Natural Language Processing
- Machine Learning model development
- Semantic similarity
- Text preprocessing
- Feature extraction
- Python project structure
- API integration
- AI product development
- End-to-end Data Science project workflow

## Author

Kalingga Rafif  
Aspiring Data Scientist and Information Systems student.

GitHub: @kal-ngga
