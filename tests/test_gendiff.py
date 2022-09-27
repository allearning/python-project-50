from gendiff import __version__
from gendiff.gendiff import generate_diff


def test_version():
    assert __version__ == '0.1.0'


def test_generate_diff():
    correct = \
        """{
    - follow: false
      host: hexlet.io
    - proxy: 123.234.53.22
    - timeout: 50
    + timeout: 20
    + verbose: true
}"""
    path1 = 'tests/data/file1.json'
    path2 = 'tests/data/file2.json'
    assert generate_diff(path1, path2) == correct


def test_generate_diff_onefile():
    correct = \
        """{
      follow: false
      host: hexlet.io
      proxy: 123.234.53.22
      timeout: 50
}"""
    path = 'tests/data/file1.json'
    assert generate_diff(path, path) == correct
