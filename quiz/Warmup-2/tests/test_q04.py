import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q04 import string_splosion

@pytest.mark.parametrize("s, expected", [
    ("Code", "CCoCodCode"),
    ("abc", "aababc"),
    ("ab", "aab"),
    ("x", "x"),
    ("fade", "ffafadfade"),
    ("There", "TThTheTherThere"),
    ("Kitten", "KKiKitKittKitteKitten"),
    ("Bye", "BByBye"),
    ("Good", "GGoGooGood"),
    ("Bad", "BBaBad"),
])
def test_string_splosion(s, expected):
    assert string_splosion(s) == expected
