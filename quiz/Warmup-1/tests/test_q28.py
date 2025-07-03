import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q28 import string_e

@pytest.mark.parametrize("s, expected", [
    ("Hello", True),
    ("Heello", False),
    ("Heelle", True),
    ("Heelele", False),
    ("Hll", False),
    ("e", True),
    ("", False),
])
def test_string_e(s, expected):
    assert string_e(s) == expected
