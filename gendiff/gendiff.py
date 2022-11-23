"""Module to compute differences between files."""
from gendiff.data_loader import load_data
from gendiff.formatters import get_formatter, ADDED, REMOVED, SAME, MODIFIED


def find_state(key, dict1: dict, dict2: dict):
    value1 = dict1.get(key, None)
    value2 = dict2.get(key, None)

    if key not in dict1:
        return ADDED
    if key not in dict2:
        return REMOVED
    if value1 == value2:
        return SAME
    return MODIFIED


def compare_dicts(dict1: dict, dict2: dict) -> dict:
    """Recursively generates difference bettween dic1 and dict2.

    Args:
        dict1 (dict): dictionary in state 1
        dict2 (dict): dictionary in state 1

    Returns:
        dict: {'key': {'state', 'value1', value2', children'}}
    """
    diffs = {}

    for key in dict1.keys() | dict2.keys():
        diffs[key] = {
            'state': find_state(key, dict1, dict2),
            'value1': dict1.get(key, None),
            'value2': dict2.get(key, None),
        }

        if diffs[key]['state'] == MODIFIED:
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                diffs[key]['children'] = compare_dicts(dict1[key], dict2[key])

    return diffs


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = load_data(file_path1)
    data2 = load_data(file_path2)
    formatter = get_formatter(format_name)
    diffs = compare_dicts(data1, data2)
    return formatter(diffs)
