import sys
import os
import pytest

# src ディレクトリをパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q05 import sum67

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 2], 5),
    ([1, 2, 2, 6, 99, 99, 7], 5),
    ([1, 1, 6, 7, 2], 4),
    ([1, 6, 2, 2, 7, 1, 6, 99, 99, 7], 2),
    ([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7], 2),
    ([2, 7, 6, 2, 6, 2, 7], 18),
    ([2, 7, 6, 2, 6, 2, 7], 9),
    ([1, 6, 7, 7], 8),
    ([6, 7, 1, 6, 7, 7], 8),
    ([6, 8, 1, 6, 7], 0),
    ([], 0),
    ([6, 7, 11], 11),
    ([11, 6, 7, 11], 22),
    ([2, 6, 7, 7], 11),
])
def test_sum67(nums, expected):
    assert sum67(nums) == expected
