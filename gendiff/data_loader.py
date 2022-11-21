import json

import yaml


def _convert_values(dictionary):
    for key, parsed_value in dictionary.items():
        if isinstance(parsed_value, bool):
            dictionary[key] = str(parsed_value).lower()
        elif parsed_value is None:
            dictionary[key] = 'null'
        elif isinstance(parsed_value, dict):
            _convert_values(parsed_value)


def get_loader(file_path: str):
    if file_path.lower().endswith('.json'):
        return json.load
    elif file_path.lower().endswith(('.yml', '.yaml')):
        return lambda file_: yaml.safe_load(file_)
    raise ValueError("Wrong type of file")


def load_data(file_path: str) -> dict:
    """Loads flat data fron JSON or YAML into dict

    Args:
        file_path (str): path to file

    Returns:
        dict (Dict): parsed data
    """

    load = get_loader(file_path)

    with open(file_path) as file:
        data = load(file)
        _convert_values(data)

    return data
