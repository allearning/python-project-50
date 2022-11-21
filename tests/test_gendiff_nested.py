from gendiff.gendiff import generate_diff
from gendiff.formatters import stylish
from gendiff.data_loader import load_data


def test_stylish_json():
    answer = 'tests/fixtures/correct3.txt'
    with open(answer) as ans: 
        correct = "".join(ans.readlines())
    path1 = 'tests/fixtures/file1.json'
    path2 = 'tests/fixtures/file2.json'
    dict1 = load_data(path1)
    dict2 = load_data(path2)
    diffs = generate_diff(dict1, dict2)
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
    diffs = generate_diff(dict1, dict2)
    assert stylish(diffs) == correct


def test_generate_diffs_onefile_json():
    answer = 'tests/fixtures/correct4.txt'
    with open(answer) as ans: 
        correct = "".join(ans.readlines())
    path_ = 'tests/fixtures/file1.json'
    dict_ = load_data(path_)
    diffs = generate_diff(dict_, dict_)
    assert stylish(diffs) == correct


def test_generate_diffs_onefile_yaml():
    answer = 'tests/fixtures/correct4.txt'
    with open(answer) as ans: 
        correct = "".join(ans.readlines())
    path_ = 'tests/fixtures/file1.yml'
    dict_ = load_data(path_)
    diffs = generate_diff(dict_, dict_)
    assert stylish(diffs) == correct