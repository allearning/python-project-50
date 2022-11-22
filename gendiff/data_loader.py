import json

import yaml


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

    return data
