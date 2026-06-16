import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q02 import same_first_last

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3], False),
    ([1, 2, 3, 1], True),
    ([1, 2, 1], True),
    ([7], True),
    ([], False),
    ([1, 2, 3, 4, 5, 1], True),
    ([1, 2, 3, 4, 5, 13], False),
    ([13, 2, 3, 4, 5, 13], True),
    ([7, 7], True),
])
def test_same_first_last(nums, expected):
    assert same_first_last(nums) == expected
