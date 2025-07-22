import sys
import os
import pytest

# srcディレクトリをインポートパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q01 import double_char

@pytest.mark.parametrize("input_str, expected", [
    ('The', 'TThhee'),
    ('AAbb', 'AAAAbbbb'),
    ('Hi-There', 'HHii--TThheerree'),
    ('Word!', 'WWoorrdd!!'),
    ('!!', '!!!!'),
    ('', ''),
    ('a', 'aa'),
    ('.', '..'),
    ('aa', 'aaaa'),
])
def test_double_char(input_str, expected):
    assert double_char(input_str) == expected
