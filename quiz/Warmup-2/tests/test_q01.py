import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.iniがない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q01 import string_times

@pytest.mark.parametrize("s, n, expected", [
    ("Hi", 2, "HiHi"),
    ("Hi", 3, "HiHiHi"),
    ("Hi", 1, "Hi"),
    ("Hi", 0, ""),
    ("Hi", 5, "HiHiHiHiHi"),
    ("Oh Boy!", 2, "Oh Boy!Oh Boy!"),
    ("x", 4, "xxxx"),
    ("", 4, ""),
    ("code", 2, "codecode"),
    ("code", 3, "codecodecode"),
])
def test_string_times(s, n, expected):
    assert string_times(s, n) == expected
