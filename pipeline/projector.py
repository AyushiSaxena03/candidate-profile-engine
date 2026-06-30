import json

def get_nested_value(data, path):
    value = data

    for key in path.split("."):
        if not isinstance(value, dict):
            return None
        value = value.get(key)

    return value
def project_output(
    candidate,
    confidence,
    provenance,
    config_path
):

    with open(config_path, "r") as file:
        config = json.load(file)

    output = {}

    for field in config["fields"]:

        output_name = field["path"]

        source_name = field["from"]

        value = get_nested_value(candidate, source_name)

        if value in ("", None, [], {}):

            if config["on_missing"] == "omit":
                continue

            output[output_name] = None

        else:

            output[output_name] = value

    if config["include_confidence"]:

        output["confidence"] = confidence
        output["overall_confidence"] = round(
        sum(confidence.values())/len(confidence),
        2
    )

    if config["include_provenance"]:

        output["provenance"] = provenance

    return output