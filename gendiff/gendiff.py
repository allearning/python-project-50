"""Module to compute differences between files."""

COMMON_PREFIX = '      '
FIRST_PREFIX = '    - '
SECOND_PREFIX = '    + '


def compare_dicts(dict1, dict2):
    diffs = ['{']
    common_keys = dict1.keys() & dict2.keys()
    same_common_keys = set(filter(lambda k: dict1[k] == dict2[k], common_keys))
    keys1 = dict1.keys() - same_common_keys
    keys2 = dict2.keys() - same_common_keys
    all_keys = dict1.keys() | dict2.keys()

    for key in sorted(all_keys):
        if key in keys1:
            diffs.append(f'{FIRST_PREFIX}{key}: {dict1[key]}')
        if key in keys2:
            diffs.append(f'{SECOND_PREFIX}{key}: {dict2[key]}')
        if key in same_common_keys:
            diffs.append(f'{COMMON_PREFIX}{key}: {dict2[key]}')

    diffs.append('}')
    return '\n'.join(diffs)
