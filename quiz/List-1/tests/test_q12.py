import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q12 import has23

@pytest.mark.parametrize("nums, expected", [
    ([2, 5], True),
    ([4, 3], True),
    ([4, 5], False),
    ([2, 2], True),
    ([3, 2], True),
    ([3, 3], True),
    ([7, 7], False),
    ([3, 9], True),
    ([9, 5], False),
])
def test_has23(nums, expected):
    assert has23(nums) == expected
