import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.iniがない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q15 import front22

@pytest.mark.parametrize("s, expected", [
    ("kitten", "kikittenki"),
    ("Ha", "HaHaHa"),
    ("abc", "ababcab"),
    ("ab", "ababab"),
    ("a", "aaa"),
    ("", ""),
    ("Logic", "LoLogicLo"),
])
def test_front22(s, expected):
    assert front22(s) == expected
