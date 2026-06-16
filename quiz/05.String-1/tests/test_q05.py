import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q05 import extra_end

@pytest.mark.parametrize("s, expected", [
    ("Hello", "lololo"),
    ("ab", "ababab"),
    ("Hi", "HiHiHi"),
    ("Candy", "dydydy"),
    ("Code", "dedede"),
])
def test_extra_end(s, expected):
    assert extra_end(s) == expected
