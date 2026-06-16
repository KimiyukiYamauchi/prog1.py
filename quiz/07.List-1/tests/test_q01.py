import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q01 import first_last6

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 6], True),
    ([6, 1, 2, 3], True),
    ([13, 6, 1, 2, 3], False),
    ([13, 6, 1, 2, 6], True),
    ([3, 2, 1], False),
    ([6, 1], True),
    ([3, 6], True),
    ([6], True),
    ([3], False),
    ([5, 6], True),
    ([5, 5], False),
    ([1, 2, 3, 4, 6], True),
    ([1, 2, 3, 4], False),
])
def test_first_last6(nums, expected):
    assert first_last6(nums) == expected
