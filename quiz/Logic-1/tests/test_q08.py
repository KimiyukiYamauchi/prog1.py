import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q08 import in1to10

@pytest.mark.parametrize("n, outside_mode, expected", [
    (5, False, True),
    (11, False, False),
    (11, True, True),
    (10, False, True),
    (10, True, True),
    (9, False, True),
    (9, True, False),
    (1, True, True),
    (0, False, False),
    (0, True, True),
    (-1, False, False),
    (-1, True, True),
    (99, False, False),
    (-99, True, True),
])
def test_in1to10(n, outside_mode, expected):
    assert in1to10(n, outside_mode) == expected
