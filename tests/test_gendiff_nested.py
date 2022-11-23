import json
from gendiff.gendiff import compare_dicts, generate_diff
from gendiff.formatters import json_formatter, stylish, plain
from gendiff.data_loader import load_data


def test_stylish_json():
    answer = 'tests/fixtures/correct3.txt'
    with open(answer) as ans:
        correct = "".join(ans.readlines())
    path1 = 'tests/fixtures/file1.json'
    path2 = 'tests/fixtures/file2.json'
    dict1 = load_data(path1)
    dict2 = load_data(path2)
    diffs = compare_dicts(dict1, dict2)
    assert stylish(diffs) == correct


def test_json_yaml1():
    path1 = 'tests/fixtures/file1.json'
    path2 = 'tests/fixtures/file1.yml'
    dict1 = load_data(path1)
    dict2 = load_data(path2)
    assert dict1 == dict2


def test_json_yaml2():
    path1 = 'tests/fixtures/file2.json'
    path2 = 'tests/fixtures/file2.yml'
    dict1 = load_data(path1)
    dict2 = load_data(path2)
    assert dict1 == dict2


def test_generate_diffs_yaml():
    answer = 'tests/fixtures/correct3.txt'
    with open(answer) as ans:
        correct = "".join(ans.readlines())
    path1 = 'tests/fixtures/file1.yml'
    path2 = 'tests/fixtures/file2.yml'
    dict1 = load_data(path1)
    dict2 = load_data(path2)
    diffs = compare_dicts(dict1, dict2)
    assert stylish(diffs) == correct


def test_generate_diffs_onefile_json():
    answer = 'tests/fixtures/correct4.txt'
    with open(answer) as ans:
        correct = "".join(ans.readlines())
    path_ = 'tests/fixtures/file1.json'
    dict_ = load_data(path_)
    diffs = compare_dicts(dict_, dict_)
    assert stylish(diffs) == correct


def test_generate_diffs_onefile_yaml():
    answer = 'tests/fixtures/correct4.txt'
    with open(answer) as ans:
        correct = "".join(ans.readlines())
    path_ = 'tests/fixtures/file1.yml'
    dict_ = load_data(path_)
    diffs = compare_dicts(dict_, dict_)
    assert stylish(diffs) == correct


def test_plain_json():
    answer = 'tests/fixtures/correct_plain.txt'
    with open(answer) as ans:
        correct = "".join(ans.readlines())
    path1 = 'tests/fixtures/file1.json'
    path2 = 'tests/fixtures/file2.json'
    dict1 = load_data(path1)
    dict2 = load_data(path2)
    diffs = compare_dicts(dict1, dict2)
    answer = plain(diffs)
    assert answer == correct


def test_gendiff_plain():
    answer = 'tests/fixtures/correct_plain.txt'
    with open(answer) as ans:
        correct = "".join(ans.readlines())
    path1 = 'tests/fixtures/file1.json'
    path2 = 'tests/fixtures/file2.json'
    diffs = generate_diff(path1, path2, 'plain')
    assert diffs == correct


def test_gendiff_stylish():
    answer = 'tests/fixtures/correct3.txt'
    with open(answer) as ans:
        correct = "".join(ans.readlines())
    path1 = 'tests/fixtures/file1.json'
    path2 = 'tests/fixtures/file2.json'
    diffs = generate_diff(path1, path2, 'stylish')
    assert diffs == correct


def test_json_json():
    path1 = 'tests/fixtures/file1.json'
    path2 = 'tests/fixtures/file2.json'
    dict1 = load_data(path1)
    dict2 = load_data(path2)
    diffs = compare_dicts(dict1, dict2)
    answer = json_formatter(diffs)
    reload = json.loads(answer)
    assert reload == diffs
