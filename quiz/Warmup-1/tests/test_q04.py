import sys
import os
import pytest

# src ディレクトリをインポートパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q04 import diff21

@pytest.mark.parametrize("n, expected", [
    (19, 2),
    (10, 11),
    (21, 0),
    (22, 2),
    (25, 8),
    (30, 18),
    (0, 21),
    (1, 20),
    (2, 19),
    (-1, 22),
    (-2, 23),
    (50, 58),
])
def test_diff21(n, expected):
    assert diff21(n) == expected
