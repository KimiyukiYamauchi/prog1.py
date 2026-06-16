import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q29 import last_digit

@pytest.mark.parametrize("a, b, expected", [
    (7, 17, True),
    (6, 17, False),
    (3, 113, True),
    (114, 113, False),
    (114, 4, True),
    (10, 0, True),
    (11, 0, False),
    (0, 0, True),
    (1, 11, True),
    (2, 12, True),
    (3, 23, True),
    (4, 14, True),
    (5, 15, True),
    (6, 16, True),
    (7, 17, True),
    (8, 18, True),
    (9, 19, True),
])
def test_last_digit(a, b, expected):
    assert last_digit(a, b) == expected
 
