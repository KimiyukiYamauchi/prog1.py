import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q08 import without_end

@pytest.mark.parametrize("s, expected", [
    ("Hello", "ell"),
    ("java", "av"),
    ("coding", "odin"),
    ("code", "od"),
    ("ab", ""),
    ("Chocolate!", "hocolate"),
    ("kitten", "itte"),
    ("woohoo", "ooho"),
])
def test_without_end(s, expected):
    assert without_end(s) == expected
