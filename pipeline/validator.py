from jsonschema import Draft7Validator, FormatChecker
import json


def validate_candidate(candidate):

    with open("schema/candidate_schema.json") as f:
        schema=json.load(f)

    validator = Draft7Validator(
        schema,
        format_checker=FormatChecker()
    )

    errors=list(
        validator.iter_errors(candidate)
    )

    if errors:

        print("\nValidation Errors")

        for error in errors:
            print("-",error.message)

        return False

    return True