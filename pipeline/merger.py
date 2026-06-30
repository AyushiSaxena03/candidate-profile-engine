"""
merger.py

Merges multiple normalized candidate records into one canonical profile.
"""

FIELD_RULES = {
    "full_name": "first",
    "primary_email": "first",
    "phone": "first",
    "headline": "first",
    "skills": "union",
    "experience": "first",
    "education": "first"
}


def first_non_empty(values):
    """
    Returns the first non-empty value from a list.
    """
    for value in values:
        if value not in ("", None, [], {}):
            return value
    return ""
    

def merge_union(values):
    """
    Merge lists while removing duplicates and preserving order.
    """

    merged = []
    seen = set()

    for value in values:

        if not isinstance(value, list):
            continue

        for item in value:

            if item not in seen:
                seen.add(item)
                merged.append(item)

    return merged


def merge_location(records):
    """
    Merge nested location object.
    """

    location = {
        "city": "",
        "region": "",
        "country": ""
    }

    for key in location.keys():

        for record in records:

            if "location" in record:

                value = record["location"].get(key)

                if value not in ("", None):
                    location[key] = value
                    break

    return location


def merge_links(records):
    """
    Merge nested links object.
    """

    links = {
        "linkedin": "",
        "github": "",
        "portfolio": "",
        "other": []
    }

    for key in links.keys():

        if key == "other":
            continue

        for record in records:

            if "links" in record:

                value = record["links"].get(key)

                if value not in ("", None):
                    links[key] = value
                    break

    other_links = []

    for record in records:

        if "links" in record:

            for item in record["links"].get("other", []):

                if item not in other_links:
                    other_links.append(item)

    links["other"] = other_links

    return links


def merge_candidates(records):
    """
    Main merger function.
    """

    merged = {}
    provenance = {}

    for field, rule in FIELD_RULES.items():

        values = [record.get(field) for record in records]

        if rule == "first":
            selected = first_non_empty(values)

            merged[field] = selected
            source_names = [
               "resume",
               "linkedin",
               "form"
            ]

            for index, value in enumerate(values):

                if value == selected:

                    provenance[field] = source_names[index]

                    break

        elif rule == "union":
            merged[field] = merge_union(values)
            provenance[field]=[
                source_names[i]
                for i,value in enumerate(values)
                if value
            ]

    merged["location"] = merge_location(records)

    merged["links"] = merge_links(records)

    return merged, provenance