# Candidate Profile Engine

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)  

A configurable Candidate Profile Engine that extracts, normalizes, merges, validates, and projects candidate information from multiple heterogeneous data sources into a single canonical profile.

This project was developed as part of the **Eightfold AI Engineering Internship Assignment**.

---

## Project Overview

Candidate information often exists across multiple sources such as resumes, LinkedIn profiles, and application forms. These sources contain overlapping information with different field names, formats, and levels of completeness.

The Candidate Profile Engine solves this problem by creating a single standardized candidate profile through a modular data processing pipeline.

---

## Features

- Extract candidate information from multiple sources
  - Resume
  - LinkedIn
  - Application Form

- Normalize data
  - Phone numbers (E.164 format)
  - Skills (Canonical names)

- Convert all sources into a Canonical Candidate Schema

- Merge multiple profiles into one unified candidate profile

- Track provenance (which source contributed each field)

- Calculate field-level and overall confidence scores

- Validate output using JSON Schema

- Generate configurable outputs using runtime configuration
  - Field selection
  - Field renaming
  - Include/Exclude confidence
  - Include/Exclude provenance
  - Missing value handling

- Unit tests using pytest

---

## Project Architecture

```
                  Resume JSON
                        │
                  LinkedIn JSON
                        │
                    Form JSON
                        │
                        ▼
                  Extractor Module
                        │
                        ▼
                 Normalizer Module
                        │
                        ▼
                    Merger Module
                        │
          ┌─────────────┴─────────────┐
          ▼                           ▼
    Provenance                  Confidence
          │                           │
          └─────────────┬─────────────┘
                        ▼
                 Validator Module
                        │
                        ▼
                 Projector Module
                        │
                        ▼
              Configurable Final Output
```

---

## Folder Structure

```
candidate-profile-engine/

│
├── config/
│   ├── default_config.json
│   └── custom_config.json
│
├── data/
│   ├── resume.json
│   ├── linkedin.json
│   └── form.json
│
├── pipeline/
│   ├── extractor.py
│   ├── normalizer.py
│   ├── merger.py
│   ├── confidence.py
│   ├── validator.py
│   ├── projector.py
│   └── __init__.py
│
├── schema/
│   └── candidate_schema.json
│
├── tests/
│   └── test_pipeline.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Pipeline Flow

### 1. Extraction

Reads candidate data from multiple structured sources.

### 2. Normalization

Converts different formats into a canonical representation.

Examples:

- ML → Machine Learning
- CPP → C++
- 9876543210 → +919876543210

---

### 3. Canonical Mapping

Different field names are mapped into one common schema.

Example

Resume

```
name
phone
```

LinkedIn

```
full_name
mobile
```

Application Form

```
candidate_name
contact
```

↓

Canonical

```
full_name
phone
```

---

### 4. Merge Engine

Combines all normalized records into a single candidate profile.

Merge strategy:

| Field | Strategy |
|--------|----------|
| Name | First non-empty |
| Email | First non-empty |
| Phone | First non-empty |
| Skills | Union |
| Experience | First non-empty |
| Education | First non-empty |
| Headline | First non-empty |

---

### 5. Provenance

Tracks which source contributed each field.

Example

```json
{
  "phone": "resume",
  "headline": "linkedin",
  "skills": [
    "resume",
    "linkedin"
  ]
}
```

---

### 6. Confidence Scoring

Confidence is calculated using the number of contributing sources.

| Sources | Score |
|----------|-------|
| 3 | 1.00 |
| 2 | 0.90 |
| 1 | 0.75 |
| 0 | 0.00 |

Overall confidence is computed as the average field confidence.

---

### 7. Validation

The merged profile is validated against a JSON Schema before projection.

Validation includes:

- Required fields
- Data types
- Email format
- Phone pattern
- URI validation

---

### 8. Configurable Projection

The engine supports runtime configuration.

Example capabilities:

- Select output fields
- Rename fields
- Include/Exclude confidence
- Include/Exclude provenance
- Handle missing values

---

## Technologies Used

- Python 3
- json
- phonenumbers
- jsonschema
- pytest

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run

```bash
python main.py
```

---

## Run Tests

```bash
python -m pytest
```

---

## Sample Output

### Default Output

```json
{
  "full_name": "Ayushi Saxena",
  "primary_email": "ayushi.saxena@gmail.com",
  "phone": "+919876543210",
  "skills": [
    "Python",
    "Machine Learning",
    "C++"
  ],
  "confidence": {
    ...
  },
  "overall_confidence": 0.77,
  "provenance": {
    ...
  }
}

```
<img width="1340" height="387" alt="Screenshot 2026-06-30 212857" src="https://github.com/user-attachments/assets/140718a7-6324-4090-a822-30c8ed902866" />


### Custom Output

```json
{
  "candidate_name": "Ayushi Saxena",
  "email": "ayushi.saxena@gmail.com",
  "skills": [
    "Python",
    "Machine Learning",
    "C++"
  ]
}

```
<img width="1332" height="228" alt="Screenshot 2026-06-30 212935" src="https://github.com/user-attachments/assets/2ea760f1-bbc2-49f5-b3d8-dbb0fac02851" />


---

## Design Principles

This project was designed with the following principles:

- Modular architecture
- Separation of concerns
- Config-driven processing
- Deterministic behavior
- Explainable confidence scoring
- Extensible pipeline
- Clean code
- Reusable components

---

## Future Improvements

- Configurable source priority
- Conflict-aware confidence scoring
- Support for additional candidate sources
- CLI arguments for runtime configuration
- REST API deployment
- Batch processing support

---

## Author

**Ayushi Saxena**

- GitHub: https://github.com/<your-github-username>
- Built as part of the **Eightfold AI Engineering    Internship Assignment**.
