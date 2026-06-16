import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q17 import icy_hot

@pytest.mark.parametrize("temp1, temp2, expected", [
    (120, -1, True),
    (-1, 120, True),
    (2, 120, False),
    (-1, 100, False),
    (-2, -2, False),
    (120, 120, False),
])
def test_icy_hot(temp1, temp2, expected):
    assert icy_hot(temp1, temp2) == expected
