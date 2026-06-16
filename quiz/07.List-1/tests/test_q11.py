import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q11 import make_ends

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3], [1, 3]),
    ([1, 2, 3, 4], [1, 4]),
    ([7, 4, 6, 2], [7, 2]),
    ([1, 2, 2, 2, 2, 2, 3], [1, 3]),
    ([7, 4], [7, 4]),
    ([7], [7, 7]),
    ([5, 2, 9], [5, 9]),
    ([2, 3, 4, 1], [2, 1]),
])
def test_make_ends(nums, expected):
    assert make_ends(nums) == expected
