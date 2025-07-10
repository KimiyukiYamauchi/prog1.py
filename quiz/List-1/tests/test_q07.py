import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q07 import reverse3

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3], [3, 2, 1]),
    ([5, 11, 9], [9, 11, 5]),
    ([7, 0, 0], [0, 0, 7]),
    ([2, 1, 2], [2, 1, 2]),
    ([1, 2, 1], [1, 2, 1]),
    ([2, 11, 3], [3, 11, 2]),
    ([0, 6, 5], [5, 6, 0]),
    ([7, 2, 3], [3, 2, 7]),
])
def test_reverse3(nums, expected):
    assert reverse3(nums) == expected
