import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q05 import last2

@pytest.mark.parametrize("s, expected", [
    ("hixxhi", 1),
    ("xaxxaxaxx", 1),
    ("axxxaaxx", 2),
    ("xxxxaxxxaxx", 3),
    ("xaxaxaxx", 0),
    ("xxxx", 2),
    ("13121312", 1),
    ("1312131312", 0),
    ("171717171", 2),
    ("hi", 0),
    ("h", 0),
    ("", 0),
])
def test_last2(s, expected):
    assert last2(s) == expected
