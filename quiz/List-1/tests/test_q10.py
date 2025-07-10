import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q10 import middle_way

@pytest.mark.parametrize("a, b, expected", [
    ([1, 2, 3], [4, 5, 6], [2, 5]),
    ([7, 7, 7], [3, 8, 0], [7, 8]),
    ([5, 2, 9], [1, 4, 5], [2, 4]),
    ([1, 9, 7], [4, 8, 8], [9, 8]),
    ([1, 2, 3], [3, 1, 4], [2, 1]),
    ([1, 2, 3], [4, 1, 1], [2, 1]),
])
def test_middle_way(a, b, expected):
    assert middle_way(a, b) == expected
