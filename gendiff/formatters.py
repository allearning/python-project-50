COMMON_PREFIX = '    '
FIRST_PREFIX = '  - '
SECOND_PREFIX = '  + '
# States
ADDED = 0
REMOVED = 1
SAME = 2
MODIFIED = 3


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
    if state == ADDED:
        return print_key(key, dif['value2'], SECOND_PREFIX, level)
    if state == REMOVED:
        return print_key(key, dif['value1'], FIRST_PREFIX, level)
    if state == SAME:
        return print_key(key, dif['value1'], COMMON_PREFIX, level)
    if state == MODIFIED:
        return print_key(key, dif['value1'], FIRST_PREFIX, level) + \
            print_key(key, dif['value2'], SECOND_PREFIX, level)


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
