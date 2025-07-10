import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q09 import sum2

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3], 3),
    ([1, 1], 2),
    ([1, 1, 1, 1], 2),
    ([1, 2], 3),
    ([1], 1),
    ([], 0),
    ([4, 5, 6], 9),
    ([4], 4),
])
def test_sum2(nums, expected):
    assert sum2(nums) == expected
