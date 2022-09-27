"""Module to compute differences between files."""
import json

COMMON_PREFIX = '      '
FIRST_PREFIX = '    - '
SECOND_PREFIX = '    + '


def _convert_bools(dictionary):
    for key, parsed_value in dictionary.items():
        if isinstance(parsed_value, bool):
            dictionary[key] = str(parsed_value).lower()


def generate_diff(file_path1: str, file_path2: str) -> str:
    """Generate difference between two JSON files.

    Args:
        file_path1 (str): path to file1
        file_path2 (str): path to file2

    Returns:
        diffs (str): diff
    """
    with open(file_path1) as file1:
        json1 = json.load(file1)
        _convert_bools(json1)
    with open(file_path2) as file2:
        json2 = json.load(file2)
        _convert_bools(json2)

    diffs = ['{']
    for key in sorted(json1.keys() | json2.keys()):
        value1 = json1.get(key, None)
        value2 = json2.get(key, None)

        if value1 == value2:
            diffs.append(f'{COMMON_PREFIX}{key}: {value1}')
        else:
            if value1:
                diffs.append(f'{FIRST_PREFIX}{key}: {value1}')
            if value2:
                diffs.append(f'{SECOND_PREFIX}{key}: {value2}')
    diffs.append('}')
    return '\n'.join(diffs)
