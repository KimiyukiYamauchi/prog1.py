import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q03 import string_bits

@pytest.mark.parametrize("s, expected", [
    ("Hello", "Hlo"),
    ("Hi", "H"),
    ("Heeololeo", "Hello"),
    ("HiHiHi", "HHH"),
    ("", ""),
    ("Greetings", "Getns"),
    ("Chocoate", "Coot"),
    ("pi", "p"),
    ("Hello Kitten", "HloKte"),
    ("hxaxpxpxy", "happy"),
])
def test_string_bits(s, expected):
    assert string_bits(s) == expected
