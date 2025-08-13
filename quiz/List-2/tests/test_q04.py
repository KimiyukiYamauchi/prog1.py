import sys
import os
import pytest

# src ディレクトリをパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q04 import sum13

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 2, 1], 6),
    ([1, 1], 2),
    ([1, 2, 2, 1, 13], 6),
    ([1, 2, 13, 2, 1, 13], 4),
    ([13, 1, 2, 13, 2, 1, 13], 3),
    ([], 0),
    ([13], 0),
    ([13, 13], 0),
    ([13, 0], 0),
    ([13, 1, 13], 0),
    ([13, 1, 2, 13], 2),
    ([5, 7, 2], 14),
    ([5, 13, 2], 5),
    ([0], 0),
    ([13, 0], 0),
])
def test_sum13(nums, expected):
    assert sum13(nums) == expected
