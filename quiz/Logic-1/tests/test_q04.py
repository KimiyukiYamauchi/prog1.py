import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q04 import caught_speeding

@pytest.mark.parametrize("speed, is_birthday, expected", [
    (60, False, 0),
    (65, False, 1),
    (65, True, 0),
    (80, False, 1),
    (85, False, 2),
    (85, True, 1),
    (70, False, 1),
    (75, False, 1),
    (75, True, 0),
    (40, False, 0),
    (40, True, 0),
    (90, False, 2),
])
def test_caught_speeding(speed, is_birthday, expected):
    assert caught_speeding(speed, is_birthday) == expected
