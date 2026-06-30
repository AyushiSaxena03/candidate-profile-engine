import json


def load_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def extract_resume():
    return load_json("data/resume.json")


def extract_linkedin():
    return load_json("data/linkedin.json")


def extract_form():
    return load_json("data/form.json")