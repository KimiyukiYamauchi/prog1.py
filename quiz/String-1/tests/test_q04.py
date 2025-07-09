import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q04 import make_out_word

@pytest.mark.parametrize("out, word, expected", [
    ("<<>>", "Yay", "<<Yay>>"),
    ("<<>>", "WooHoo", "<<WooHoo>>"),
    ("[[]]", "word", "[[word]]"),
    ("HHoo", "Hello", "HHHellooo"),
    ("abyz", "YAY", "abYAYyz"),
])
def test_make_out_word(out, word, expected):
    assert make_out_word(out, word) == expected
