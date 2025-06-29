import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.iniがない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q06 import makes10

@pytest.mark.parametrize("a, b, expected", [
    (9, 10, True),
    (9, 9, False),
    (1, 9, True),
    (10, 1, True),
    (10, 10, True),
    (8, 2, True),
    (8, 3, False),
    (10, 42, True),
    (12, -2, True),
])
def test_makes10(a, b, expected):
    assert makes10(a, b) == expected
