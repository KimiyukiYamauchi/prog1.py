import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q10 import non_start

@pytest.mark.parametrize("a, b, expected", [
    ("Hello", "There", "ellohere"),
    ("java", "code", "avaode"),
    ("shotl", "java", "hotlava"),
    ("ab", "xy", "by"),
    ("ab", "x", "b"),
    ("x", "ac", "c"),
    ("a", "x", ""),
    ("Kit", "kat", "itat"),
    ("mart", "dart", "artart"),
])
def test_non_start(a, b, expected):
    assert non_start(a, b) == expected
