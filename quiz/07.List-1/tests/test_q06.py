import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q06 import rotate_left3

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3], [2, 3, 1]),
    ([5, 11, 9], [11, 9, 5]),
    ([7, 0, 0], [0, 0, 7]),
    ([1, 2, 1], [2, 1, 1]),
    ([0, 0, 1], [0, 1, 0]),
])
def test_rotate_left3(nums, expected):
    assert rotate_left3(nums) == expected
