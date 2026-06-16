import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q05 import sum3

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3], 6),
    ([5, 11, 2], 18),
    ([7, 0, 0], 7),
    ([1, 2, 1], 4),
    ([1, 1, 1], 3),
    ([2, 7, 2], 11),
])
def test_sum3(nums, expected):
    assert sum3(nums) == expected
