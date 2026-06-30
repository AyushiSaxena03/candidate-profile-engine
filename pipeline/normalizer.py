import phonenumbers
SKILL_MAPPING = {
    "ml": "Machine Learning",
    "machine learning": "Machine Learning",
    "python": "Python",
    "c++": "C++",
    "cpp": "C++",
    "javascript": "JavaScript"
}


def normalize_skills(skills):
    normalized = []

    for skill in skills:
        key = skill.strip().lower()

        canonical_skill = SKILL_MAPPING.get(key, skill)

        if canonical_skill not in normalized:
            normalized.append(canonical_skill)

    return normalized

def normalize_phone(phone):
    try:
        parsed_number = phonenumbers.parse(phone, "IN")

        if phonenumbers.is_valid_number(parsed_number):
            return phonenumbers.format_number(
                parsed_number,
                phonenumbers.PhoneNumberFormat.E164
            )

        return None

    except:
        return None

def normalize_candidate(candidate, source):

    normalized = {}

    if source == "resume":

        normalized["full_name"] = candidate.get("name", "")

        normalized["primary_email"] = candidate.get("email", "")

        normalized["phone"] = normalize_phone(
            candidate.get("phone", "")
        )

        normalized["skills"] = normalize_skills(
            candidate.get("skills", [])
        )

        normalized["experience"] = candidate.get("experience", [])

        normalized["education"] = candidate.get("education", [])

        normalized["headline"] = ""
    elif source == "linkedin":
        normalized["full_name"] = candidate.get("full_name", "")

        normalized["primary_email"] = candidate.get("email", "")

        normalized["phone"] = normalize_phone(
            candidate.get("mobile", "")
        )

        normalized["skills"] = normalize_skills(
            candidate.get("skills", [])
        )

        normalized["headline"] = candidate.get("headline", "")

        normalized["experience"] = []

        normalized["education"] = []

        normalized["links"] = {
            "linkedin": candidate.get("linkedin", ""),
            "github": candidate.get("github", ""),
            "portfolio": "",
            "other": []
        }
    elif source == "form":

        normalized["full_name"] = candidate.get("candidate_name", "")

        normalized["primary_email"] = candidate.get("primary_email", "")

        normalized["phone"] = normalize_phone(
            candidate.get("contact", "")
        )

        normalized["skills"] = []

        normalized["experience"] = []

        normalized["education"] = []

        normalized["headline"] = ""

        normalized["location"] = {
            "city": candidate.get("city", ""),
            "region": "",
            "country": candidate.get("country", "")
        }

        normalized["links"] = {
            "linkedin": "",
            "github": "",
            "portfolio": "",
            "other": []
        }

    return normalized