import sys
import os
import pytest

# src ディレクトリをインポートパスに追加（pytest.iniがない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q11 import front_back

@pytest.mark.parametrize("s, expected", [
    ("code", "eodc"),
    ("a", "a"),
    ("ab", "ba"),
    ("abc", "cba"),
    ("", ""),
    ("Chocolate", "ehocolatC"),
    ("aavJ", "Java"),
    ("hello", "oellh"),
])
def test_front_back(s, expected):
    assert front_back(s) == expected
