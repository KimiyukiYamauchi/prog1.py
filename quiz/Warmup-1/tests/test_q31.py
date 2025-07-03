import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q31 import every_nth

@pytest.mark.parametrize("s, n, expected", [
    ("Miracle", 2, "Mrce"),
    ("abcdefg", 2, "aceg"),
    ("abcdefg", 3, "adg"),
    ("Chocolate", 3, "Cca"),
    ("Chocolates", 3, "Ccas"),
    ("Chocolates", 4, "Coe"),
    ("Chocolates", 100, "C"),
])
def test_every_nth(s, n, expected):
    assert every_nth(s, n) == expected
