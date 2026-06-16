import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q03 import make_tags

@pytest.mark.parametrize("tag, word, expected", [
    ("i", "Yay", "<i>Yay</i>"),
    ("i", "Hello", "<i>Hello</i>"),
    ("cite", "Yay", "<cite>Yay</cite>"),
    ("address", "here", "<address>here</address>"),
    ("body", "Heart", "<body>Heart</body>"),
    ("i", "i", "<i>i</i>"),
    ("i", "", "<i></i>"),
])
def test_make_tags(tag, word, expected):
    assert make_tags(tag, word) == expected
