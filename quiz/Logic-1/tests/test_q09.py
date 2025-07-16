import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q09 import near_ten

@pytest.mark.parametrize("num, expected", [
    (12, True),
    (17, False),
    (19, True),
    (31, True),
    (6, False),
    (10, True),
    (11, True),
    (21, True),
    (22, True),
    (23, False),
    (54, False),
    (155,False),
    (158, True),
    (3, False),
    (1, True),
])
def test_near_ten(num, expected):
    assert near_ten(num) == expected
