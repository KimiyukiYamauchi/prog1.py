import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q18 import in1020

@pytest.mark.parametrize("a, b, expected", [
    (12, 99, True),
    (21, 12, True),
    (8, 99, False),
    (99, 10, True),
    (20, 20, True),
    (21, 21, False),
    (9, 9, False),
])
def test_in1020(a, b, expected):
    assert in1020(a, b) == expected
