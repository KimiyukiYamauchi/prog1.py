import sys
import os
import pytest

# src ディレクトリをパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q01 import make_bricks

@pytest.mark.parametrize("small, big, goal, expected", [
    (3, 1, 8, True),
    (3, 1, 9, False),
    (3, 2, 10, True),
    (3, 2, 8, True),
    (3, 2, 9, False),
    (6, 1, 11, True),
    (6, 0, 11, False),
    (1, 4, 11, True),
    (0, 3, 10, True),
    (1, 4, 12, False),
    (3, 1, 7, True),
    (1, 1, 7, False),
    (2, 1, 7, True),
    (7, 1, 11, True),
    (7, 1, 8, True),
    (7, 1, 13, False),
    (43, 1, 46, True),
    (40, 1, 46, False),
    (40, 2, 47, True),
    (40, 2, 50, True),
    (40, 2, 52, False),
    (22, 2, 33, False),
    (0, 2, 10, True),
    (1000000, 1000, 1000100, True),
    (2, 1000000, 100003, False),
    (20, 0, 19, True),
    (20, 0, 21, False),
    (20, 4, 51, False),
    (20, 4, 39, True),
])
def test_make_bricks(small, big, goal, expected):
    assert make_bricks(small, big, goal) == expected
