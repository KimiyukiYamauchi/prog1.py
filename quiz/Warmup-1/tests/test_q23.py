import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q23 import start_oz

@pytest.mark.parametrize("s, expected", [
    ("ozymandias", "oz"),
    ("bzoo", "z"),
    ("oxx", "o"),
    ("oz", "oz"),
    ("ounce", "o"),
    ("o", "o"),
    ("abc", ""),
    ("", ""),
    ("zoo", ""),
    ("aztec", "z"),
    ("zzzz", "z"),
    ("oznic", "oz"),
])
def test_start_oz(s, expected):
    assert start_oz(s) == expected
