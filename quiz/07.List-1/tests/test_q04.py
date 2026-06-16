import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q04 import common_end

@pytest.mark.parametrize("a, b, expected", [
    ([1, 2, 3], [7, 3], True),
    ([1, 2, 3], [7, 3, 2], False),
    ([1, 2, 3], [1, 3], True),
    ([1, 2, 3], [1], True),
    ([1, 2, 3], [2], False),
])
def test_common_end(a, b, expected):
    assert common_end(a, b) == expected
