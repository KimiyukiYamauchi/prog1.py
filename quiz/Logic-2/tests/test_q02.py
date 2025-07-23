import sys
import os
import pytest

# src ディレクトリをパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q02 import lone_sum

@pytest.mark.parametrize("a, b, c, expected", [
    (1, 2, 3, 6),
    (3, 2, 3, 2),
    (3, 3, 3, 0),
    (9, 2, 2, 9),
    (2, 2, 9, 9),
    (2, 9, 2, 9),
    (2, 9, 3, 14),
    (4, 2, 3, 9),
    (1, 3, 1, 3),
])
def test_lone_sum(a, b, c, expected):
    assert lone_sum(a, b, c) == expected
