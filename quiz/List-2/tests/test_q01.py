import sys
import os
import pytest

# src ディレクトリをパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q01 import count_evens

@pytest.mark.parametrize("nums, expected", [
    ([2, 1, 2, 3, 4], 3),
    ([2, 2, 0], 3),
    ([1, 3, 5], 0),
    ([], 0),
    ([11, 9, 0, 1], 1),
    ([2, 11, 9, 0], 2),
    ([2], 1),
    ([2, 5, 12], 2),
])
def test_count_evens(nums, expected):
    assert count_evens(nums) == expected
