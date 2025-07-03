import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q24 import int_max

@pytest.mark.parametrize("a, b, c, expected", [
    (1, 2, 3, 3),
    (1, 3, 2, 3),
    (3, 2, 1, 3),
    (9, 3, 3, 9),
    (3, 9, 3, 9),
    (3, 3, 9, 9),
    (8, 2, 3, 8),
    (-3, -1, -2, -1),
    (6, 2, 5, 6),
    (5, 6, 2, 6),
    (5, 2, 6, 6),
])
def test_int_max(a, b, c, expected):
    assert int_max(a, b, c) == expected
