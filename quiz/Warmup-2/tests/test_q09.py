import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q09 import string_match

@pytest.mark.parametrize("a, b, expected", [
    ("xxcaazz", "xxbaaz", 3),
    ("abc", "abc", 2),
    ("abc", "axc", 0),
    ("hello", "he", 1),
    ("he", "hello", 1),
    ("h", "hello", 0),
    ("", "hello", 0),
    ("aabbccdd", "abbbxxd", 1),
    ("aaxxaaxx", "iaxxai", 3),
    ("iaxxai", "aaxxaaxx", 3),
])
def test_string_match(a, b, expected):
    assert string_match(a, b) == expected
