import sys
import os
import pytest

# src ディレクトリをパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q03 import lucky_sum

@pytest.mark.parametrize("a, b, c, expected", [
    (1, 2, 3, 6),
    (1, 2, 13, 3),
    (1, 13, 3, 1),
    (1, 13, 13, 1),
    (6, 5, 2, 13),
    (13, 2, 3, 0),
    (13, 2, 13, 0),
    (13, 13, 2, 0),
    (9, 4, 13, 13),
    (8, 13, 2, 8),
    (7, 2, 1, 10),
    (3, 3, 13, 6),
])
def test_lucky_sum(a, b, c, expected):
    assert lucky_sum(a, b, c) == expected
