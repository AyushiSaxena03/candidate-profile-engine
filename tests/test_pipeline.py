from pipeline.normalizer import (
    normalize_phone,
    normalize_skills
)

from pipeline.validator import validate_candidate

from pipeline.projector import project_output


def test_phone():

    assert normalize_phone("9876543210") == "+919876543210"


def test_skills():

    skills = normalize_skills([
        "ML",
        "Python",
        "machine learning",
        "CPP"
    ])

    assert skills == [
        "Machine Learning",
        "Python",
        "C++"
    ]


def test_validator():

    candidate = {

        "full_name": "Ayushi",

        "primary_email": "abc@gmail.com",

        "phone": "+919876543210",

        "headline": "",

        "skills": [],

        "experience": [],

        "education": [],

        "location": {},

        "links": {}

    }

    assert validate_candidate(candidate) == True


def test_projector():

    candidate = {

        "full_name": "Ayushi",

        "primary_email": "abc@gmail.com",

        "phone": "+919876543210",

        "skills": []

    }

    confidence = {}

    provenance = {}

    output = project_output(

        candidate,

        confidence,

        provenance,

        "config/custom_config.json"

    )

    assert output["candidate_name"] == "Ayushi"