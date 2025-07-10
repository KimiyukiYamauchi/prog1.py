import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q08 import max_end3

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3], [3, 3, 3]),
    ([11, 5, 9], [11, 11, 11]),
    ([2, 11, 3], [3, 3, 3]),
    ([11, 3, 3], [11, 11, 11]),
    ([3, 11, 11], [11, 11, 11]),
    ([2, 2, 2], [2, 2, 2]),
    ([2, 11, 2], [2, 2, 2]),
    ([0, 0, 1], [1, 1, 1]),
])
def test_max_end3(nums, expected):
    assert max_end3(nums) == expected
