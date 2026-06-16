import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q11 import left2

@pytest.mark.parametrize("s, expected", [
    ("Hello", "lloHe"),
    ("java", "vaja"),
    ("Hi", "Hi"),
    ("code", "deco"),
    ("cat", "tca"),
    ("12345", "34512"),
    ("Chocolate", "ocolateCh"),
    ("bricks", "icksbr"),
])
def test_left2(s, expected):
    assert left2(s) == expected
