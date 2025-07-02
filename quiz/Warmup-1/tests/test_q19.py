import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q19 import has_teen

@pytest.mark.parametrize("a, b, c, expected", [
    (13, 20, 10, True),
    (20, 19, 10, True),
    (20, 10, 13, True),
    (1, 20, 12, False),
    (19, 20, 12, True),
    (12, 20, 19, True),
    (12, 9, 20, False),
    (12, 18, 20, True),
    (14, 2, 20, True),
    (4, 2, 20, False),
    (11, 22, 22, False),
])
def test_has_teen(a, b, c, expected):
    assert has_teen(a, b, c) == expected
