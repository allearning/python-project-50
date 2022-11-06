from gendiff.gendiff import compare_dicts
from gendiff.data_loader import load_flat_data


def test_compare_dicts_json():
    answer = 'tests/fixtures/correct1.txt'
    with open(answer) as ans: 
        correct = "".join(ans.readlines())
    path1 = 'tests/fixtures/file1.json'
    path2 = 'tests/fixtures/file2.json'
    dict1 = load_flat_data(path1)
    dict2 = load_flat_data(path2)
    assert compare_dicts(dict1, dict2) == correct


def test_compare_dicts_yaml():
    answer = 'tests/fixtures/correct1.txt'
    with open(answer) as ans: 
        correct = "".join(ans.readlines())
    path1 = 'tests/fixtures/file1.yml'
    path2 = 'tests/fixtures/file2.yml'
    dict1 = load_flat_data(path1)
    dict2 = load_flat_data(path2)
    assert compare_dicts(dict1, dict2) == correct


def test_compare_dicts_onefile():
    answer = 'tests/fixtures/correct2.txt'
    with open(answer) as ans: 
        correct = "".join(ans.readlines())
    path_ = 'tests/fixtures/file1.json'
    dict_ = load_flat_data(path_)
    assert compare_dicts(dict_, dict_) == correct
