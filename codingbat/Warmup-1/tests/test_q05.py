import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q05 import parrot_trouble

@pytest.mark.parametrize("talking, hour, expected", [
    (True, 6, True),
    (True, 7, False),
    (False, 6, False),
    (True, 21, True),
    (False, 21, False),
    (False, 20, False),
    (True, 23, True),
    (False, 23, False),
    (True, 20, False),
    (False, 12, False),
])
def test_parrot_trouble(talking, hour, expected):
    assert parrot_trouble(talking, hour) == expected
