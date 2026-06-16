import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q09 import combo_string

@pytest.mark.parametrize("a, b, expected", [
    ("Hello", "hi", "hiHellohi"),
    ("hi", "Hello", "hiHellohi"),
    ("aaa", "b", "baaab"),
    ("b", "aaa", "baaab"),
    ("aaa", "", "aaa"),
    ("", "bb", "bb"),
    ("aaa", "1234", "aaa1234aaa"),
    ("aaa", "bb", "bbaaabb"),
    ("a", "bb", "abba"),
    ("bb", "a", "abba"),
    ("xyz", "ab", "abxyzab"),
])
def test_combo_string(a, b, expected):
    assert combo_string(a, b) == expected
