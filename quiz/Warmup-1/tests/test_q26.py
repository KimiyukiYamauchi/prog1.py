import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q26 import in3050

@pytest.mark.parametrize("a, b, expected", [
    (30, 31, True),
    (30, 41, False),
    (40, 50, True),
    (40, 51, False),
    (39, 50, False),
    (50, 39, False),
    (40, 39, True),
    (49, 48, True),
    (50, 40, True),
    (50, 51, False),
    (35, 36, True),
    (35, 45, False),
    (30, 30, True),
    (40, 40, True),
    (50, 50, True),
    (30, 50, False),
    (40, 30, True),
])
def test_in3050(a, b, expected):
    assert in3050(a, b) == expected
