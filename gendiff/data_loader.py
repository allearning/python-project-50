import json
import yaml


def _convert_bools(dictionary):
    for key, parsed_value in dictionary.items():
        if isinstance(parsed_value, bool):
            dictionary[key] = str(parsed_value).lower()


def load_flat_data(file_path: str) -> dict:
    """Loads flat data fron JSON or YAML into dict

    Args:
        file_path (str): path to file

    Returns:
        dict (Dict): parsed data
    """

    if file_path.lower().endswith('.json'):
        load = json.load
    elif file_path.lower().endswith(('.yml', '.yaml')):
        load = lambda file_: yaml.safe_load(file_)
    else:
        return {}

    with open(file_path) as file:
        data = load(file)
        _convert_bools(data)

    return data
