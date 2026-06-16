import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q20 import lone_teen

@pytest.mark.parametrize("a, b, expected", [
    (13, 99, True),
    (21, 19, True),
    (13, 13, False),
    (14, 20, True),
    (20, 15, True),
    (16, 17, False),
    (16, 9, True),
    (16, 18, False),
    (13, 19, False),
    (13, 20, True),
    (6, 18, True),
    (99, 13, True),
    (99, 99, False),
])
def test_lone_teen(a, b, expected):
    assert lone_teen(a, b) == expected
