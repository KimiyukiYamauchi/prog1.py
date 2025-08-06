import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q07 import first_half

@pytest.mark.parametrize("s, expected", [
    ("WooHoo", "Woo"),
    ("HelloThere", "Hello"),
    ("abcdef", "abc"),
    ("ab", "a"),
    ("", ""),
    ("0123456789", "01234"),
    ("kitten", "kit"),
])
def test_first_half(s, expected):
    assert first_half(s) == expected
