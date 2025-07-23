import sys
import os
import pytest

# src ディレクトリをパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q06 import has22

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 2], True),
    ([1, 2, 1, 2], False),
    ([2, 1, 2], False),
    ([2, 2, 1, 2], True),
    ([1, 3, 2], False),
    ([1, 3, 2, 2], True),
    ([2, 3, 2, 2], True),
    ([4, 2, 4, 2, 2, 5], True),
    ([1, 2], False),
    ([2, 2], True),
    ([2], False),
    ([], False),
    ([3, 3, 2, 2], True),
    ([5, 2, 5, 2], False),
])
def test_has22(nums, expected):
    assert has22(nums) == expected
