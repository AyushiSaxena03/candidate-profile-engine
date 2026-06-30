from pipeline.extractor import (
    extract_resume,
    extract_linkedin,
    extract_form
)

from pipeline.normalizer import normalize_candidate

from pipeline.merger import merge_candidates

from pipeline.confidence import (
    calculate_field_confidence,
    calculate_overall_confidence
)

from pipeline.validator import validate_candidate

from pipeline.projector import project_output


def run_pipeline():

    # Extract
    resume = normalize_candidate(
        extract_resume(),
        "resume"
    )

    linkedin = normalize_candidate(
        extract_linkedin(),
        "linkedin"
    )

    form = normalize_candidate(
        extract_form(),
        "form"
    )

    # Merge
    merged_candidate, provenance = merge_candidates([
        resume,
        linkedin,
        form
    ])

    # Confidence
    field_confidence = calculate_field_confidence(
        provenance
    )

    overall_confidence = calculate_overall_confidence(
        field_confidence
    )

    # Validation
    is_valid = validate_candidate(
        merged_candidate
    )

    if not is_valid:
        print("Validation Failed")
        return

    # Default Output
    default_output = project_output(
        merged_candidate,
        field_confidence,
        provenance,
        "config/default_config.json"
    )

    # Custom Output
    custom_output = project_output(
        merged_candidate,
        field_confidence,
        provenance,
        "config/custom_config.json"
    )

    print("\n========== DEFAULT OUTPUT ==========\n")

    print(default_output)

    print("\n========== CUSTOM OUTPUT ==========\n")

    print(custom_output)

    print("\nOverall Confidence :", overall_confidence)


if __name__ == "__main__":

    run_pipeline()