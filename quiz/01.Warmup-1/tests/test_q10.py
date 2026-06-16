import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q10 import missing_char

@pytest.mark.parametrize("s, n, expected", [
    ("kitten", 1, "ktten"),
    ("kitten", 0, "itten"),
    ("kitten", 4, "kittn"),
    ("Hi", 0, "i"),
    ("Hi", 1, "H"),
    ("code", 0, "ode"),
    ("code", 1, "cde"),
    ("code", 2, "coe"),
    ("code", 3, "cod"),
    ("chocolate", 8, "chocolat"),
])
def test_missing_char(s, n, expected):
    assert missing_char(s, n) == expected
