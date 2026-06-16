import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q05 import sorta_sum

@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 7),
    (9, 4, 20),
    (10, 11, 21),
    (12, -3, 9),
    (-3, 12, 9),
    (4, 5, 9),
    (4, 6, 20),
    (14, 7, 21),
    (14, 6, 20),
])
def test_sorta_sum(a, b, expected):
    assert sorta_sum(a, b) == expected
