import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q22 import mix_start

@pytest.mark.parametrize("s, expected", [
    ("mix snacks", True),
    ("pix snacks", True),
    ("piz snacks", False),
    ("nix", True),
    ("ni", False),
    ("n", False),
    ("", False),
])
def test_mix_start(s, expected):
    assert mix_start(s) == expected
