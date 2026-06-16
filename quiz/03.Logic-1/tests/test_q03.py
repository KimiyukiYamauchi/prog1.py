import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q03 import squirrel_play

@pytest.mark.parametrize("temp, is_summer, expected", [
    (70, False, True),
    (95, False, False),
    (95, True, True),
    (90, False, True),
    (90, True, True),
    (50, False, False),
    (50, True, False),
    (100, False, False),
    (100, True, True),
    (105, True, False),
    (59, False, False),
    (59, True, False),
    (60, False, True),
])
def test_squirrel_play(temp, is_summer, expected):
    assert squirrel_play(temp, is_summer) == expected
