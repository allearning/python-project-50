from gendiff.gendiff import generate_diff


def test_generate_diff():
    answer = 'tests/fixtures/correct1.txt'
    with open(answer) as ans: 
        correct = "".join(ans.readlines())
    path1 = 'tests/fixtures/file1.json'
    path2 = 'tests/fixtures/file2.json'
    assert generate_diff(path1, path2) == correct


def test_generate_diff_onefile():
    answer = 'tests/fixtures/correct2.txt'
    with open(answer) as ans: 
        correct = "".join(ans.readlines())
    path = 'tests/fixtures/file1.json'
    assert generate_diff(path, path) == correct