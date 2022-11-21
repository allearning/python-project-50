from gendiff.gendiff import generate_diff
from gendiff.formatters import stylish
from gendiff.data_loader import load_data


def test_compare_dicts_json():
    answer = 'tests/fixtures/correct1.txt'
    with open(answer) as ans: 
        correct = "".join(ans.readlines())
    path1 = 'tests/fixtures/file1_flat.json'
    path2 = 'tests/fixtures/file2_flat.json'
    dict1 = load_data(path1)
    dict2 = load_data(path2)
    diffs = generate_diff(dict1, dict2)
    assert stylish(diffs) == correct


def test_compare_dicts_yaml():
    answer = 'tests/fixtures/correct1.txt'
    with open(answer) as ans: 
        correct = "".join(ans.readlines())
    path1 = 'tests/fixtures/file1_flat.yml'
    path2 = 'tests/fixtures/file2_flat.yml'
    dict1 = load_data(path1)
    dict2 = load_data(path2)
    diffs = generate_diff(dict1, dict2)
    assert stylish(diffs) == correct


def test_compare_dicts_onefile():
    answer = 'tests/fixtures/correct2.txt'
    with open(answer) as ans: 
        correct = "".join(ans.readlines())
    path_ = 'tests/fixtures/file1_flat.json'
    dict_ = load_data(path_)
    diffs = generate_diff(dict_, dict_)
    assert stylish(diffs) == correct
