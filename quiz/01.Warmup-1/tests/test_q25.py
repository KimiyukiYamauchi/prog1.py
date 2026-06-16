import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q25 import close10

@pytest.mark.parametrize("a, b, expected", [
    (8, 13, 8),
    (13, 8, 8),
    (13, 7, 0),
    (7, 13, 0),
    (9, 13, 9),
    (13, 8, 8),
    (10, 12, 10),
    (11, 10, 10),
    (5, 21, 5),
    (0, 20, 0),
    (10, 10, 0),
])
def test_close10(a, b, expected):
    assert close10(a, b) == expected
