"""Module to compute differences between files."""

# States
ADDED = 0
REMOVED = 1
SAME = 2
MODIFIED = 3


def find_state(key, dict1: dict, dict2: dict):
    value1 = dict1.get(key, None)
    value2 = dict2.get(key, None)

    if value1 is None:
        return ADDED
    if value2 is None:
        return REMOVED
    if value1 == value2:
        return SAME
    return MODIFIED


def generate_diff(dict1: dict, dict2: dict) -> dict:
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
                diffs[key]['children'] = generate_diff(dict1[key], dict2[key])

    return diffs
