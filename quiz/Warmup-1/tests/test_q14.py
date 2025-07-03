import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.iniがない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q14 import or35

@pytest.mark.parametrize("n, expected", [
    (3, True),
    (10, True),
    (8, False),
    (15, True),
    (5, True),
    (9, True),
    (4, False),
    (7, False),
    (6, True),
    (17, False),
    (18, True),
    (29, False),
    (20, True),
    (21, True),
    (22, False),
    (45, True),
    (99, True),
    (100, True),
    (101, False),
    (121, False),
    (122, False),
    (123, True),
])
def test_or35(n, expected):
    assert or35(n) == expected
