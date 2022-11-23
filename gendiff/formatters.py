import json

COMMON_PREFIX = '    '
FIRST_PREFIX = '  - '
SECOND_PREFIX = '  + '
# States
ADDED = 'ADDED'
REMOVED = 'REMOVED'
SAME = 'SAME'
MODIFIED = 'MODIFIED'


def get_formatter(name: str):
    formatters = {
        'stylish': stylish,
        'plain': plain,
        'json': json_formatter
    }
    return formatters[name]


def get_converted(value):
    mapping = {
        None: 'null',
        False: 'false',
        True: 'true',
    }
    if isinstance(value, dict):
        return value
    return mapping.get(value, value)


def print_key(key: str, value_of_key, prefix: str, level=0) -> 'list[str]':
    """Prints key, where key can be single value or dict

    Args:
        key (str): key name
        value_of_key (_type_): value of key
        prefix (str): prefix to print
        level (int, optional): offset level. Defaults to 0.

    Returns:
        list[str]: _description_
    """
    strings = []
    offset = ' ' * 4 * level
    value_of_key = get_converted(value_of_key)
    if isinstance(value_of_key, dict):
        strings.append(f'{offset}{prefix}{key}: {{')
        for k, v in value_of_key.items():
            strings.extend(print_key(k, v, COMMON_PREFIX, level + 1))
        strings.append(f'{offset}{COMMON_PREFIX}}}')
    else:
        strings.append(f'{offset}{prefix}{key}: {value_of_key}')
    return strings


def simple_state_print(dif, level, key):
    state = dif['state']
    value1 = dif['value1']
    value2 = dif['value2']
    if state == ADDED:
        return print_key(key, value2, SECOND_PREFIX, level)
    if state == REMOVED:
        return print_key(key, value1, FIRST_PREFIX, level)
    if state == SAME:
        return print_key(key, value1, COMMON_PREFIX, level)
    if state == MODIFIED:
        return print_key(key, value1, FIRST_PREFIX, level) + \
            print_key(key, value2, SECOND_PREFIX, level)


def print_dif(dif_list: dict, level=0):
    strings = []
    offset = ' ' * 4 * level

    for key in sorted(dif_list.keys()):
        state = dif_list[key]['state']
        children = dif_list[key].get('children', None)
        if state == MODIFIED and children:
            strings.append(f'{offset}{COMMON_PREFIX}{key}: {{')
            strings.extend(
                print_dif(children, level + 1)
            )
            strings.append(f'{offset}{COMMON_PREFIX}}}')
        else:
            strings.extend(simple_state_print(dif_list[key], level, key))
    return strings


def stylish(dif_list: dict):
    strings = ['{'] + print_dif(dif_list, level=0) + ['}']
    return '\n'.join(strings)


def get_value_or_complex(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    return get_converted(value)


def simple_state_plain_print(dif, key, prefix=''):
    state = dif['state']
    value1 = get_value_or_complex(dif['value1'])
    value2 = get_value_or_complex(dif['value2'])
    if state == ADDED:
        return f"Property '{prefix}{key}' was added with value: {value2}"
    if state == REMOVED:
        return f"Property '{prefix}{key}' was removed"
    if state == MODIFIED:
        return \
            f"Property '{prefix}{key}' was updated. From {value1} to {value2}"


def plain_strings(dif_list: dict, prefix=''):
    strings = []
    not_same_keys = set(
        filter(lambda k: dif_list[k]['state'] != SAME, dif_list.keys())
    )
    for key in sorted(not_same_keys):
        state = dif_list[key]['state']
        children = dif_list[key].get('children', None)
        if state == MODIFIED and children:
            strings.extend(plain_strings(children, f'{prefix}{key}.'))
        else:
            strings.append(
                simple_state_plain_print(dif_list[key], key, prefix),
            )
    return strings


def plain(dif_list: dict):
    strings = plain_strings(dif_list)
    return '\n'.join(strings)


def json_formatter(dif_list: dict):
    return json.dumps(dif_list, sort_keys=True)
