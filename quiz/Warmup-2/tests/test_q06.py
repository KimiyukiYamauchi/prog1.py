import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q06 import array_count9

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 9], 1),
    ([1, 9, 9], 2),
    ([1, 9, 9, 3, 9], 3),
    ([1, 2, 3], 0),
    ([], 0),
    ([4, 2, 4, 3, 1], 0),
    ([9, 2, 4, 3, 1], 1),
])
def test_array_count9(nums, expected):
    assert array_count9(nums) == expected
