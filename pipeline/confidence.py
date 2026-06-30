def calculate_field_confidence(provenance):

    confidence = {}

    for field, source in provenance.items():

        if isinstance(source, list):
            count = len(source)
        elif source:
            count = 1
        else:
            count = 0

        score_map = {
            0: 0.0,
            1: 0.75,
            2: 0.90,
            3: 1.00
        }

        confidence[field] = score_map.get(count, 1.0)

    return confidence


def calculate_overall_confidence(field_confidence):

    if not field_confidence:
        return 0.0

    overall = sum(field_confidence.values()) / len(field_confidence)

    return round(overall,2)