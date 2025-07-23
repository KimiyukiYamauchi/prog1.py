import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q07 import array_front9

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 9, 3, 4], True),
    ([1, 2, 3, 4, 9], False),
    ([1, 2, 3, 4, 5], False),
    ([9, 2, 3], True),
    ([1, 9, 9], True),
    ([1, 2, 3], False),
    ([1, 9], True),
    ([5, 5], False),
    ([2], False),
    ([9], True),
    ([], False),
    ([3, 9, 2, 3, 3], True),
])
def test_array_front9(nums, expected):
    assert array_front9(nums) == expected
