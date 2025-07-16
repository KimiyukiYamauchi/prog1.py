import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q07 import love6

@pytest.mark.parametrize("a, b, expected", [
    (6, 4, True),
    (4, 5, False),
    (1, 5, True),
    (1, 6, True),
    (1, 8, False),
    (1, 7, True),
    (7, 5, True),
    (8, 2, True),
    (6, 6, True),
    (-6, 2, False),
    (-4, -10, True),
    (-7, 1, False),
    (7, -1, True),
    (6, 12, True),
    (-2, -4, False),
    (7, 1, True),
    (0, 9, False),
    (8, 3, False),
    (3, 3, True),
    (3, 4, False),
])
def test_love6(a, b, expected):
    assert love6(a, b) == expected
