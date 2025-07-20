import sys
import os
import pytest

# src ディレクトリをパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q04 import no_teen_sum

@pytest.mark.parametrize("a, b, c, expected", [
    (1, 2, 3, 6),
    (2, 13, 1, 3),
    (2, 1, 14, 3),
    (2, 1, 15, 18),
    (2, 1, 16, 19),
    (2, 1, 17, 3),
    (17, 1, 2, 3),
    (2, 15, 2, 19),
    (16, 17, 18, 16),
    (17, 18, 19, 0),
    (15, 16, 1, 32),
    (15, 19, 16, 31),
    (5, 17, 18, 5),
    (17, 18, 16, 16),
    (17, 19, 18, 0),
])
def test_no_teen_sum(a, b, c, expected):
    assert no_teen_sum(a, b, c) == expected
