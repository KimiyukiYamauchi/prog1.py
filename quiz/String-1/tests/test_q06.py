import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q06 import first_two

@pytest.mark.parametrize("s, expected", [
    ("Hello", "He"),
    ("abcdefg", "ab"),
    ("ab", "ab"),
    ("a", "a"),
    ("", ""),
    ("Kitten", "Ki"),
    ("hi", "hi"),
    ("hiya", "hi"),
])
def test_first_two(s, expected):
    assert first_two(s) == expected
