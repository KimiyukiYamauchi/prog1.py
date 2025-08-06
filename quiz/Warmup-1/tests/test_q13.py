import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q13 import back_around

@pytest.mark.parametrize("s, expected", [
    ("cat", "tcatt"),
    ("Hello", "oHelloo"),
    ("a", "aaa"),
    ("abc", "cabcc"),
    ("read", "dreadd"),
    ("boo", "obooo"),
])
def test_back_around(s, expected):
    assert back_around(s) == expected
